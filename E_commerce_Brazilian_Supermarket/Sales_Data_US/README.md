# 📦 Sales Data US — Data Engineering Project

A project that showcases the core principles of data engineering using US car sales data. From raw Excel ingestion to normalized schema design, this project covers data modeling, pipeline design, and querying best practices.

---

## 📌 Introduction & Goals

This project aims to simulate a real-world data engineering workflow using a sales dataset containing used vehicle transaction records across the US.

- **Data Source**: Used vehicle sales data with attributes such as vehicle specs, seller info, price, and sale date.
- **Goal**: Build a clean, normalized database schema (in 3NF), and prepare it for querying and analytics.
- **Tools Used**: 
  - `pandas` for data wrangling
  - `MySQL` for relational schema
  - SQL Workbench for ERD visualization
- **Deliverables**:
  - Normalized schema for product, customer, and sales order
  - ERD (Entity Relationship Diagram)
  - Clean, queryable tables with referential integrity

---

## 📁 Contents

- [📊 The Data Set](#the-data-set)
- [🛠️ Used Tools](#used-tools)
- [⚙️ Pipeline Summary](#pipeline-summary)
- [🧱 Entity-Relationship Diagram (ERD)](#entity-relationship-diagram)
- [🎯 Conclusion](#conclusion)
- [🔗 Connect with Me](#connect-with-me)

---

## 📊 The Data Set

The dataset contains historical information on supermarket sales, including:

- 

📝 **Reason for Selection**:
- Rich in categorical and numeric fields
- Great candidate for normalization
- Reflects real-world business use cases like inventory systems and dealer analysis

---

## 🛠️ Used Tools

| Purpose      | Tool        | Why It Was Used                          |
|--------------|-------------|------------------------------------------|
| Data cleaning| `pandas`    | Parsing, splitting, and deduplicating    |
| Data storage | `MySQL`     | Enforcing relational integrity (3NF)     |
| Modeling     | MySQL Workbench | To visualize schema and ERD             |

---

## ⚙️ Pipeline Summary

1. **Load & Clean** raw data with Python (`pandas`)
2. **Split** full name fields, normalize categories
3. **Create Database** and define 3NF schema
4. **Insert Cleaned Data** into MySQL
5. **Model Relationships** via foreign keys

---

## 🧱 Entity-Relationship Diagram

The ERD below shows the three core tables in the final relational schema:

### 🔹 CUSTOMER  
- `customer_id`, `name`, `segment`, `state`, `region`, etc.

### 🔹 PRODUCT  
- `product_id`, `product_name`, `category`, `sub_category`

### 🔹 SALES_ORDER  
- `order_id`, `order_date`, `ship_date`, `customer_id`, `product_id`, etc.

🖼️ ![ERD]()

---

## 🎯 Conclusion

This project solidified core concepts of:
- 3NF normalization
- Relational schema design
- Foreign key enforcement
- Handling messy real-world data

✅ **Key takeaway**: Good data starts with **good structure**. Building reliable pipelines begins with mastering foundational skills like modeling, validation, and transformation.# 🛒 Supermarket Sales — Data Engineering Project

A project that demonstrates data engineering principles using a supermarket sales dataset. This project focuses on data ingestion, normalization, relational modeling, and ERD visualization to support analytics-ready pipelines.

---

## 📌 Introduction & Goals

This project simulates the lifecycle of preparing structured sales data for a supermarket business. The dataset includes detailed transaction records like product purchases, customer segments, payment modes, and returns.

- **Data Source**: Supermarket sales records across regions with fields like customer info, product details, and financial metrics.
- **Goal**: Design a normalized relational database (3NF) to enable efficient querying and reporting.
- **Tools Used**: 
  - `pandas` for cleaning and prep
  - `MySQL` for data modeling and storage
  - SQL Workbench for ERD generation
- **Deliverables**:
  - 3NF schema across product, customer, and order dimensions
  - Entity Relationship Diagram (ERD)
  - Populated MySQL tables ready for queries

---

## 📁 Contents

- [🛍️ The Data Set](#the-data-set)
- [🧰 Tools Used](#tools-used)
- [⚙️ Pipeline Overview](#pipeline-overview)
- [🧱 Entity-Relationship Diagram (ERD)](#entity-relationship-diagram)
- [📌 Conclusion](#conclusion)
- [🔗 Connect](#connect)

---

## 🛍️ The Data Set

This dataset contains transaction-level data with the following attributes:

- Transaction metadata: `Order ID`, `Order Date`, `Ship Date`, `Ship Mode`
- Customer details: `Customer ID`, `Customer Name`, `Segment`, `Country`, `City`, `State`, `Region`
- Product info: `Product ID`, `Category`, `Sub-Category`, `Product Name`
- Financials: `Sales`, `Profit`, `Quantity`, `Returns`, `Payment Mode`

📝 **Why This Data?**
- Clean blend of categorical and numeric fields
- Realistic structure for retail transaction modeling
- Suited for OLAP/BI workloads

---

## 🧰 Tools Used

| Task           | Tool           | Purpose                              |
|----------------|----------------|--------------------------------------|
| Data Prep      | `pandas`       | Clean, split, and deduplicate fields |
| Data Storage   | `MySQL`        | Host relational schema with 3NF      |
| Modeling/ERD   | MySQL Workbench| Visual schema validation             |

---

## ⚙️ Pipeline Overview

1. Load raw Excel/CSV data
2. Clean and split compound columns (e.g. names)
3. Normalize into 3NF (`Customer`, `Product`, `Orders`)
4. Establish foreign keys for integrity
5. Generate ERD to validate relationships

---

## 🧱 Entity-Relationship Diagram

This ERD models 3 key entities with proper referential design:

### 🧍 CUSTOMER  
- `customer_id`, `name`, `segment`, `state`, `region`, etc.

### 📦 PRODUCT  
- `product_id`, `product_name`, `category`, `sub_category`

### 🧾 SALES_ORDER  
- `order_id`, `order_date`, `ship_date`, `sales`, `profit`, `returns`, etc.

🖼️ ![ERD](./assets_files/Sales_data)

---

## 📌 Conclusion

This supermarket sales project covered:

- Building relational models from semi-structured data
- Applying 3NF normalization
- Designing customer-product-order relationships
- Preparing datasets for BI and analytics use cases

✅ **Key Learning**: Strong foundational modeling enables clean, scalable data pipelines.

---

---

## 🔗 Connect With Me

Let’s connect!  
🔹 [LinkedIn](http://www.linkedin.com/in/kabirat-adeniyi-2899a0245)  
🔹 GitHub: [@Kadeniyi23](https://github.com/Kadeniyi23)
