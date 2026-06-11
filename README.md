# Banking BI Management Portfolio

**End-to-End Business Intelligence & Data Analytics Projects** for Banking / Fintech  
**Target Role**: Business Intelligence and Data Analysis Manager | Canadia Bank (Phnom Penh)

---

## 📋 Project Overview

This repository demonstrates practical **BI, Data Engineering, and Analytics** capabilities using real-world banking datasets. It covers the full data lifecycle:

- **Data Ingestion & ETL** with governance
- **Data Warehouse** modeling (star schema ready)
- **BI Dashboards & Visualization** ← **NEW: Interactive Streamlit App**
- **Predictive Analytics** (Credit / Investment Risk)

Built to showcase production-grade skills relevant to core banking systems, CBC compliance, and data-driven decision making in the Cambodian banking sector.

---

## 🛠️ Tech Stack

- **Python** – Pandas, SQLAlchemy, Scikit-learn, XGBoost, **Streamlit**
- **Database** – PostgreSQL (with schema, views, logging)
- **Visualization** – Plotly, Streamlit, Jupyter Notebooks
- **Tools** – Docker-ready, Logging, Data Quality Reports
- **Methodology** – Star Schema, SCD concepts, ETL best practices

---

## 📁 Projects

### 1. Automated ETL Pipeline + Data Governance (`notebooks/etl_pipeline.py`)
- Loads and cleans three banking datasets
- Comprehensive data quality checks and reporting
- Loads into PostgreSQL (`banking_bi_demo` schema)
- Production features: Logging, error handling, chunked inserts

### 2. Banking BI Dashboard (`streamlit_dashboard.py` + `notebooks/Project1_Banking_BI_Dashboard.ipynb`)
- **Interactive Streamlit web app** connected to PostgreSQL
- Customer segmentation, transaction trends, branch performance, KPIs
- Real-time filters and visualizations

### 3. Predictive Credit Risk Modeling (`notebooks/Project2_Predictive_Credit_Risk.ipynb`)
- Machine Learning models for credit risk prediction

---

## 🚀 How to Run

### Prerequisites
- Python 3.9+
- PostgreSQL database
- Raw data files in `raw_data/` folder (Kaggle link below)

### 1. Run ETL
```bash
git clone https://github.com/vivord/Banking-BI-Management-Portfolio.git
cd Banking-BI-Management-Portfolio
pip install pandas sqlalchemy psycopg2-binary
python notebooks/etl_pipeline.py
```

### 2. Launch Streamlit Dashboard
```bash
pip install streamlit plotly
streamlit run streamlit_dashboard.py
```

Open http://localhost:8501 in your browser.

### Docker Support (Coming Soon)

---

## 🎯 Relevance to Cambodian Banking

- Mirrors core banking operations
- Regulatory-ready data governance
- **Live interactive dashboards** for stakeholder reporting

---

## 📈 Future Enhancements
- Full Docker + CI/CD
- SCD Type 2
- CBC template integration
- SHAP explainability in Streamlit

---

**Made with ❤️ for advancing BI capabilities in Cambodian financial institutions.**

[View Live Demo](https://github.com/vivord/Banking-BI-Management-Portfolio) (run locally)
