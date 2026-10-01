# E-Commerce Customer Segmentation and Prediction

## Project Overview

This project focuses on analyzing e-commerce customer purchasing behavior and grouping customers into different segments based on their purchase history.

The project uses **RFM Analysis (Recency, Frequency, Monetary)** to create customer-level features. K-Means Clustering is then used to identify different customer groups. A Random Forest Classifier is also used to predict whether a customer is a high-value customer based on their purchasing behavior.

The project also includes an interactive **Streamlit dashboard** for exploring customer segments and making high-value customer predictions.

---

## Objectives

- Analyze customer purchasing behavior.
- Clean and preprocess the e-commerce transaction dataset.
- Calculate Recency, Frequency and Monetary values for customers.
- Segment customers using K-Means Clustering.
- Identify different customer groups based on purchasing patterns.
- Predict high-value customers using Random Forest.
- Create an interactive Streamlit dashboard.
- Generate useful insights that can help with customer retention and targeted marketing.

---

## Dataset

The project uses an Online Retail e-commerce dataset containing more than **540,000 transaction records**.

The dataset contains the following main columns:

- `InvoiceNo`
- `StockCode`
- `Description`
- `Quantity`
- `InvoiceDate`
- `UnitPrice`
- `CustomerID`
- `Country`

After cleaning the data, the project contains approximately:

- **541,909** original transaction records
- **392,692** valid transaction records
- **4,338** unique customers

---

## Data Preprocessing

The following preprocessing steps were performed:

1. Removed duplicate records.
2. Removed transactions with missing `CustomerID`.
3. Converted `InvoiceDate` into datetime format.
4. Removed invalid transactions with negative or zero quantity.
5. Removed invalid transactions with negative or zero unit price.
6. Created a `TotalPrice` column.

The total price was calculated as:

```text
TotalPrice = Quantity × UnitPrice
