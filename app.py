import streamlit as st
import pandas as pd


# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="European Banking Churn Analytics",
    page_icon="🏦",
    layout="wide"
)


# ==========================================
# 2. LOAD DATASET
# ==========================================

df = pd.read_csv("European_Bank_Final_Analysis.csv")


# ==========================================
# 3. SIDEBAR FILTERS
# ==========================================

st.sidebar.header("🔍 Customer Filters")


# Geography Filter
geography_options = ["All"] + sorted(
    df["Geography"].dropna().unique().tolist()
)

selected_geography = st.sidebar.selectbox(
    "🌍 Select Geography",
    geography_options
)


# Gender Filter
gender_options = ["All"] + sorted(
    df["Gender"].dropna().unique().tolist()
)

selected_gender = st.sidebar.selectbox(
    "👤 Select Gender",
    gender_options
)


# Age Group Filter
age_options = ["All"] + [
    "<30",
    "30-45",
    "46-60",
    "60+"
]

selected_age = st.sidebar.selectbox(
    "🎂 Select Age Group",
    age_options
)


# Tenure Group Filter
tenure_options = ["All"] + [
    "New",
    "Mid-term",
    "Long-term"
]

selected_tenure = st.sidebar.selectbox(
    "🕐 Select Tenure Group",
    tenure_options
)


# Customer Value Filter
value_options = ["All"] + sorted(
    df["CustomerValueSegment"].dropna().unique().tolist()
)

selected_value = st.sidebar.selectbox(
    "💎 Customer Value Segment",
    value_options
)


# ==========================================
# 4. APPLY FILTERS
# ==========================================

filtered_df = df.copy()


# Geography Filter
if selected_geography != "All":
    filtered_df = filtered_df[
        filtered_df["Geography"] == selected_geography
    ]


# Gender Filter
if selected_gender != "All":
    filtered_df = filtered_df[
        filtered_df["Gender"] == selected_gender
    ]


# Age Group Filter
if selected_age != "All":
    filtered_df = filtered_df[
        filtered_df["AgeGroup"] == selected_age
    ]


# Tenure Group Filter
if selected_tenure != "All":
    filtered_df = filtered_df[
        filtered_df["TenureGroup"] == selected_tenure
    ]


# Customer Value Filter
if selected_value != "All":
    filtered_df = filtered_df[
        filtered_df["CustomerValueSegment"] == selected_value
    ]


# ==========================================
# 5. CALCULATE FILTERED KPIs
# ==========================================

total_customers = len(filtered_df)

churned_customers = filtered_df["Exited"].sum()


# Overall Churn Rate
if total_customers > 0:
    overall_churn_rate = (
        filtered_df["Exited"].mean() * 100
    )
else:
    overall_churn_rate = 0


# High-Value Customer Churn Rate
high_value_df = filtered_df[
    filtered_df["CustomerValueSegment"] == "High Value"
]


if len(high_value_df) > 0:
    high_value_churn_rate = (
        high_value_df["Exited"].mean() * 100
    )
else:
    high_value_churn_rate = 0


# ==========================================
# 6. DASHBOARD TITLE
# ==========================================

st.title("🏦 European Banking Customer Churn Analytics")

st.write(
    "Customer Segmentation & Churn Pattern Analytics in European Banking"
)

st.divider()


# ==========================================
# 7. KPI CARDS
# ==========================================

st.subheader("📊 Key Performance Indicators")


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        label="👥 Total Customers",
        value=f"{total_customers:,}"
    )


with col2:
    st.metric(
        label="🚪 Churned Customers",
        value=f"{churned_customers:,}"
    )


with col3:
    st.metric(
        label="📉 Overall Churn Rate",
        value=f"{overall_churn_rate:.2f}%"
    )


with col4:
    st.metric(
        label="💎 High-Value Churn Rate",
        value=f"{high_value_churn_rate:.2f}%"
    )


st.divider()


# ==========================================
# 8. FILTERED DATASET
# ==========================================

st.subheader("📋 Filtered Customer Dataset")


st.write(
    f"Showing {len(filtered_df):,} customers"
)


st.dataframe(
    filtered_df,
    use_container_width=True
)