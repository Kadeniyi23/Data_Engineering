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

The dataset contains historical information on vehicle sales, including:

- Vehicle features: `make`, `model`, `trim`, `transmission`, etc.
- Sale metadata: `sellingprice`, `saledate`, `mmr`
- Customer and transaction details like `state`, `odometer`, and `condition`

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

🖼️ ![ERD](./Screenshot%202025-06-03%20153343.jpg)

---

## 🎯 Conclusion

This project solidified core concepts of:
- 3NF normalization
- Relational schema design
- Foreign key enforcement
- Handling messy real-world data

✅ **Key takeaway**: Good data starts with **good structure**. Building reliable pipelines begins with mastering foundational skills like modeling, validation, and transformation.

---

## 🔗 Connect With Me

Let’s connect!  
🔹 [LinkedIn](https://www.linkedin.com/in/your-profile)  
🔹 GitHub: [@Kadeniyi23](https://github.com/Kadeniyi23)