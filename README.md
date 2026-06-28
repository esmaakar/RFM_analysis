# Customer Segmentation & RFM Analysis (FLO Dataset)

##  Project Overview

This project focuses on customer segmentation using **RFM (Recency, Frequency, Monetary) analysis** on an e-commerce dataset from FLO. The goal is to identify different customer groups based on their purchasing behavior and generate actionable insights for targeted marketing strategies.

---

##  Objectives

- Perform exploratory data analysis (EDA)
- Create new meaningful features from raw transaction data
- Apply RFM analysis to segment customers
- Define customer personas using rule-based segmentation
- Identify target customer groups for marketing campaigns
- Export customer IDs for specific marketing actions

---

##  Dataset

The dataset contains customer transaction history including:

- Online and offline order counts
- Online and offline total spending
- Order channels
- Customer category interests
- Order dates and customer identifiers

---

##  Steps Performed

### 1. Data Preprocessing
- Checked missing values and data types
- Converted date columns to datetime format
- Created new features:
  - `order_num_total`
  - `customer_value_total`

---

### 2. Exploratory Data Analysis
- Aggregated data by order channel
- Identified top customers by:
  - Total spending
  - Total order count

---

### 3. RFM Analysis
- Calculated:
  - **Recency**: Time since last purchase
  - **Frequency**: Total number of purchases
  - **Monetary**: Total spending
- Created RFM scores using quantiles

---

### 4. Customer Segmentation
Customers were segmented using rule-based mapping:

- champions
- loyal_customers
- potential_loyalists
- new_customers
- promising
- need_attention
- about_to_sleep
- at_risk
- cant_loose
- hibernating

---

### 5. Target Customer Selection

Two main target groups were created:

####  Female Loyal Customers
- Segment: `loyal_customers`
- Interested in: Women's categories
- Output: `yeni_marka_hedef_müşteri_id.csv`

####  Discount Target Group
- Segments: `new_customers`, `cant_loose`
- Interested in: Men's and Kids categories
- Output: `indirim_hedef_müşteri_ids.csv`

---

## Output Files

- `yeni_marka_hedef_müşteri_id.csv` → High-value female loyal customers
- `indirim_hedef_müşteri_ids.csv` → Customers targeted for discount campaigns

---

## Technologies Used

- Python
- Pandas
- NumPy
- Datetime
- RFM Analysis techniques

---

##  Key Insights

- Customer segmentation enables more efficient marketing strategies
- Loyal customers generate a significant portion of revenue
- New and at-risk customers require different engagement strategies
- Category-based filtering helps refine campaign targeting

---

##  Future Improvements

- Add visualization dashboard (Power BI / Tableau)
- Integrate machine learning clustering (KMeans)
- Automate segmentation pipeline
- Build customer lifetime value prediction model

---


