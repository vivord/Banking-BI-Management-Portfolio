# Banking BI Management Portfolio

**End-to-End Business Intelligence & Data Analytics Projects** for Banking / Fintech  
**Target Role**: Business Intelligence and Data Analysis Manager | Canadia Bank (Phnom Penh)

---

## 📋 Project Overview

This repository demonstrates practical **BI, Data Engineering, and Analytics** capabilities using real-world banking datasets. It covers the full data lifecycle:

- **Data Ingestion & ETL** with governance
- **Data Warehouse** modeling (star schema ready)
- **BI Dashboards & Visualization**
- **Predictive Analytics** (Credit / Investment Risk)

Built to showcase production-grade skills relevant to core banking systems, CBC compliance, and data-driven decision making in the Cambodian banking sector.

---

## 🛠️ Tech Stack

- **Python** – Pandas, SQLAlchemy, Scikit-learn, XGBoost
- **Database** – PostgreSQL (with schema, views, logging)
- **Visualization** – Jupyter Notebooks, Matplotlib / Seaborn / Plotly (expandable to Streamlit / Power BI)
- **Tools** – Docker-ready, Logging, Data Quality Reports
- **Methodology** – Star Schema, SCD concepts, ETL best practices

---

## 📁 Projects

### 1. Automated ETL Pipeline + Data Governance (`notebooks/etl_pipeline.py`)
- Loads and cleans three banking datasets (`customer_data.csv`, `transaction_data.csv`, `bank_data.csv`)
- Comprehensive data quality checks and reporting
- Loads into PostgreSQL (`banking_bi_demo` schema)
- Production features: Logging, error handling, chunked inserts, star-schema views
- Ready for scheduling (Airflow / cron) and integration with core banking systems

### 2. Banking BI Dashboard (`notebooks/Project1_Banking_BI_Dashboard.ipynb`)
- Exploratory Data Analysis (EDA)
- Key performance metrics: Customer segmentation, branch performance, transaction trends
- Interactive visualizations for business stakeholders

### 3. Predictive Credit Risk Modeling (`notebooks/Project2_Predictive_Credit_Risk.ipynb`)
- Machine Learning models for credit/investment risk prediction
- Feature engineering, model training & evaluation
- Business insights tailored to emerging market lending (Cambodia context)

---

## 🚀 How to Run

### Prerequisites
- Python 3.9+
- PostgreSQL database
- Raw data files in `raw_data/` folder (download from [Kaggle](https://www.kaggle.com/datasets/yogeshtekawade/banking-and-customer-transaction-data))

### Setup
```bash
# 1. Clone repo
git clone https://github.com/vivord/Banking-BI-Management-Portfolio.git
cd Banking-BI-Management-Portfolio

# 2. Install dependencies
pip install pandas sqlalchemy psycopg2-binary matplotlib seaborn plotly

# 3. Update database config in etl_pipeline.py
# 4. Run ETL
python notebooks/etl_pipeline.py
```

### Docker Support (Coming Soon)
Docker Compose setup for PostgreSQL + pgAdmin will be added.

---

## 🎯 Relevance to Canadia Bank / Cambodian Banking

- **Core Banking Alignment**: Mirrors daily operations (batch processing, reporting, data quality)
- **Regulatory Readiness**: Data validation, audit-ready logging, governance features (similar to CBC uploads)
- **Business Impact**: Risk modeling, customer analytics, and dashboards support data-driven decisions
- **Scalability**: Clean architecture, logging, and modular design for enterprise use

---

## 📈 Future Enhancements (Portfolio Roadmap)

- Streamlit / Power BI interactive dashboard
- Full Docker + CI/CD pipeline
- SCD Type 2 implementation for history tracking
- Integration with CBC data templates
- Advanced ML (SHAP explainability, deployment)

---

## 📄 License
MIT License – Feel free to explore and adapt.

---

**Made with ❤️ for advancing BI capabilities in Cambodian financial institutions.**
