# Banking BI Dashboard - Streamlit App
# Perfect for Canadia Bank BI Manager portfolio

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Page config
st.set_page_config(page_title="Banking BI Dashboard", layout="wide")
st.title("🏦 Banking BI Management Dashboard")
st.markdown("**End-to-End BI Portfolio for Canadia Bank**")

# ------------------- CONFIG -------------------
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'postgres',
    'user': 'postgres',
    'password': 'P@ssw0rd'  # Change for production
}

SCHEMA = 'banking_bi_demo'

@st.cache_resource
 def get_engine():
    encoded_pw = quote_plus(DB_CONFIG['password'])
    return create_engine(
        f"postgresql+psycopg2://{DB_CONFIG['user']}:{encoded_pw}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )

engine = get_engine()

# Sidebar
st.sidebar.header("Filters & Controls")
show_raw = st.sidebar.checkbox("Show Raw Data Tables", value=False)

# Load data with fallback
try:
    with engine.connect() as conn:
        customers = pd.read_sql(f"SELECT * FROM {SCHEMA}.customers", conn)
        transactions = pd.read_sql(f"SELECT * FROM {SCHEMA}.transactions", conn)
        branches = pd.read_sql(f"SELECT * FROM {SCHEMA}.branches", conn)
    st.success("✅ Connected to PostgreSQL Banking BI Demo")
except Exception as e:
    st.warning("⚠️ Database connection failed. Using local CSV fallback.")
    try:
        customers = pd.read_csv('raw_data/customer_data.csv')
        transactions = pd.read_csv('raw_data/transaction_data.csv')
        branches = pd.read_csv('raw_data/bank_data.csv')
    except:
        st.error("No data source available. Please run the ETL pipeline first!")
        st.stop()

# KPIs Row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Customers", f"{len(customers):,}")
with col2:
    st.metric("Total Transactions", f"{len(transactions):,}")
with col3:
    total_vol = transactions.get('Transaction_Amount', pd.Series([0])).sum()
    st.metric("Total Volume", f"${total_vol:,.0f}")
with col4:
    avg_age = customers.get('Age', pd.Series([0])).mean()
    st.metric("Avg Customer Age", f"{avg_age:.1f}")

# Main Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📊 Customer Overview", "💰 Transaction Analysis", "🏬 Branch Performance", "🔮 Risk Insights"])

with tab1:
    st.subheader("Customer Segmentation by Region")
    if 'Region' in customers.columns:
        fig_region = px.pie(customers, names='Region', title='Distribution by Region')
        st.plotly_chart(fig_region, use_container_width=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        if 'Age' in customers.columns:
            fig_age = px.histogram(customers, x='Age', color='Customer_Type' if 'Customer_Type' in customers.columns else None, title='Age Distribution')
            st.plotly_chart(fig_age, use_container_width=True)
    with col_b:
        st.dataframe(customers.describe(), use_container_width=True)

with tab2:
    st.subheader("Transaction Trends & Insights")
    if 'Transaction_Date' in transactions.columns:
        transactions['date'] = pd.to_datetime(transactions['Transaction_Date'], errors='coerce')
        daily = transactions.groupby(transactions['date'].dt.date)['Transaction_Amount'].sum().reset_index()
        fig_trend = px.line(daily, x='date', y='Transaction_Amount', title='Daily Transaction Volume')
        st.plotly_chart(fig_trend, use_container_width=True)
    
    st.subheader("Top 10 Transactions")
    st.dataframe(transactions.nlargest(10, 'Transaction_Amount' if 'Transaction_Amount' in transactions.columns else transactions.columns[0]))

with tab3:
    st.subheader("Branch / Bank Performance")
    st.dataframe(branches, use_container_width=True)
    if 'Branch_Name' in branches.columns or 'Bank_Name' in branches.columns:
        st.bar_chart(branches.set_index(branches.columns[0]))

with tab4:
    st.subheader("Predictive Credit Risk")
    st.info("🔗 This tab can be extended with your XGBoost model from Project2_Predictive_Credit_Risk.ipynb")
    st.markdown("**Demo Idea**: Upload customer features → Get risk score")

if show_raw:
    st.subheader("Raw Data Preview")
    st.dataframe(customers.head(100))
    st.dataframe(transactions.head(100))

st.caption(f"📅 Dashboard last refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Powered by PostgreSQL + Streamlit")
