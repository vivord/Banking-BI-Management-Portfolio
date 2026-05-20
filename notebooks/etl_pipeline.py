# ================================================
# PROJECT 3: AUTOMATED ETL PIPELINE + GOVERNANCE
# For Canadia Bank BI Manager Role
# ================================================

import pandas as pd
import logging
from pathlib import Path
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
from datetime import datetime
import os

# ------------------- CONFIGURATION -------------------
DB_CONFIG = {
    'host':     'localhost',
    'port':     5432,
    'database': 'postgres',
    'user':     'postgres',
    'password': 'P@ssw0rd'   # ← CHANGE THIS ONLY
}

SCHEMA_NAME = 'banking_bi_demo'

DATA_FOLDER = Path("raw_data")                     # Your 3 CSVs must be here
LOG_FOLDER = Path("logs")
LOG_FOLDER.mkdir(exist_ok=True)

# CSV filenames (use exact names from your download)
FILES = {
    'customers':    'customer_data.csv',
    'transactions': 'transaction_data.csv',
    'branches':     'bank_data.csv',
}

# ------------------- LOGGING SETUP -------------------
logging.basicConfig(
    filename=LOG_FOLDER / f"etl_log_{datetime.now().strftime('%Y-%m-%d')}.log",
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(message)s'
)
logger = logging.getLogger(__name__)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(console)

# ------------------- CONNECTION -------------------
encoded_password = quote_plus(DB_CONFIG['password'])
engine = create_engine(
    f"postgresql+psycopg2://{DB_CONFIG['user']}:{encoded_password}@"
    f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}",
    echo=False
)

def set_schema():
    with engine.connect() as conn:
        conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA_NAME};"))
        conn.execute(text(f"SET search_path TO {SCHEMA_NAME};"))
        conn.commit()
    logger.info(f"Schema '{SCHEMA_NAME}' ready.")

# ------------------- DATA QUALITY CHECKS -------------------
def run_data_quality_checks(df: pd.DataFrame, table_name: str) -> pd.DataFrame:
    checks = {
        'total_rows': len(df),
        'duplicate_rows': df.duplicated().sum(),
        'null_percentage': (df.isnull().sum() / len(df) * 100).to_dict(),
        'min_transaction_amount': df['Transaction_Amount'].min() if 'Transaction_Amount' in df.columns else None,
        'max_transaction_amount': df['Transaction_Amount'].max() if 'Transaction_Amount' in df.columns else None,
    }
    report = pd.DataFrame([checks])
    report.to_csv(f"data_quality_report_{table_name}.csv", index=False)
    logger.info(f"Data quality checks completed for {table_name}")
    return report

# ------------------- LOAD & CLEAN FUNCTION -------------------
def load_and_transform(file_path: Path, table_name: str):
    logger.info(f"ETL started for {file_path.name} → {table_name}")
    
    df = pd.read_csv(file_path)
    
    # Basic cleaning (same as Project 1)
    df = df.drop_duplicates()
    for col in df.columns:
        if 'date' in col.lower():
            df[col] = pd.to_datetime(df[col], errors='coerce')
        elif any(k in col.lower() for k in ['amount', 'balance', 'profit', 'revenue', 'investment', 'age']):
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Data quality
    quality_report = run_data_quality_checks(df, table_name)
    
    # Load to PostgreSQL (replace for demo; use 'append' in production)
    df.to_sql(
        name=table_name,
        con=engine,
        schema=SCHEMA_NAME,
        if_exists='replace',
        index=False,
        chunksize=10000,
        method='multi'
    )
    
    logger.info(f"✅ Successfully loaded {len(df):,} rows into {SCHEMA_NAME}.{table_name}")
    return df

# ------------------- MAIN ETL PIPELINE -------------------
def main():
    logger.info("=== STARTING FULL ETL PIPELINE ===")
    set_schema()
    
    for key, filename in FILES.items():
        file_path = DATA_FOLDER / filename
        if not file_path.exists():
            logger.error(f"File missing: {file_path}")
            continue
        
        table_name = key
        load_and_transform(file_path, table_name)
    
    # Optional: Create simple star-schema views (for advanced governance)
    logger.info("Creating star-schema views for BI...")
    with engine.connect() as conn:
        conn.execute(text(f"""
            CREATE OR REPLACE VIEW {SCHEMA_NAME}.fact_transactions AS
            SELECT * FROM {SCHEMA_NAME}.transactions;
        """))
        conn.commit()
    
    logger.info("🎉 ETL Pipeline completed successfully!")
    logger.info("Data Governance artifacts generated.")

if __name__ == "__main__":
    main()