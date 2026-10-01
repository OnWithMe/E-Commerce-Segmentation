import streamlit as st
import pandas as pd

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(
    page_title="E-commerce Customer Analysis",
    page_icon="🛍️",
    layout="wide"
)

# -----------------------------
# Load data
# -----------------------------
raw_data = pd.read_csv("data.csv", encoding="cp1252")
customers = pd.read_csv("customer_segments.csv")

# Same cleaning used in the ML project
clean_data = raw_data.drop_duplicates()
clean_data = clean_data.dropna(subset=["CustomerID"])
clean_data = clean_data[
    (clean_data["Quantity"] > 0) &
    (clean_data["UnitPrice"] > 0)
]

# -----------------------------
# Title
# -----------------------------
st.title("🛍️ E-commerce Customer Segmentation")
st.write(
    "Analysis of customer purchasing behaviour using RFM analysis "
    "and K-Means clustering."
)

# -----------------------------
# Main metrics
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Original Transactions",
    f"{len(raw_data):,}"
)

col2.metric(
    "Valid Transactions",
    f"{len(clean_data):,}"
)

col3.metric(
    "Unique Customers",
    f"{customers['CustomerID'].nunique():,}"
)

col4.metric(
    "Total Revenue",
    f"£{customers['Monetary'].sum():,.0f}"
)

# -----------------------------
# Customer statistics
# -----------------------------
st.header("Customer Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Spend",
    f"£{customers['Monetary'].mean():,.2f}"
)

col2.metric(
    "Average Orders",
    f"{customers['Frequency'].mean():.1f}"
)

col3.metric(
    "Average Recency",
    f"{customers['Recency'].mean():.1f} days"
)

# -----------------------------
# Cluster chart
# -----------------------------
st.header("Customer Segments")

cluster_count = (
    customers["Cluster"]
    .value_counts()
    .sort_index()
)

st.bar_chart(cluster_count)

# -----------------------------
# Cluster filter
# -----------------------------
selected = st.selectbox(
    "Choose a customer cluster",
    ["All"] + sorted(customers["Cluster"].unique().tolist())
)

if selected == "All":
    filtered = customers
else:
    filtered = customers[
        customers["Cluster"] == selected
    ]

# -----------------------------
# RFM summary
# -----------------------------
st.subheader("RFM Summary")

rfm_summary = filtered[
    ["Recency", "Frequency", "Monetary"]
].mean().round(2)

st.dataframe(
    rfm_summary,
    use_container_width=True
)

# -----------------------------
# Customer table
# -----------------------------
st.subheader("Customer Details")

st.dataframe(
    filtered[
        [
            "CustomerID",
            "Recency",
            "Frequency",
            "Monetary",
            "Cluster",
            "HighValue"
        ]
    ],
    use_container_width=True
)