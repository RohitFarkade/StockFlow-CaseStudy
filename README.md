
# 📦 Inventory Management Backend – Case Study

This repository contains my solution to the **Backend Engineering Intern Case Study** provided by **Bynry**.

The goal of this project is to demonstrate backend design thinking, API development, data modeling, and handling real-world business constraints such as multi-warehouse inventory, company-level isolation, and low-stock alerts.

---

## 📄 Case Study Reference


## [Case Study](https://github.com/RohitFarkade/StockFlow-CaseStudy/blob/5427b99e011d346eaf5cc8fb66541e7fc33f56f5/Rohit_Farkade-Case%20Study%20-%20Backend%20Engineering%20intern.pdf) 
---

## 🧠 Key Objectives

* Design scalable backend APIs
* Model real-world inventory systems
* Handle multi-company and multi-warehouse scenarios
* Implement business rules like low-stock alerts
* Demonstrate clean architecture and readable code

---

## 🏗️ Project Structure

```
.
├── main.py                 # FastAPI application and routes
├── fake_db.py              # In-memory data layer (mock database)
├── models.py               # Pydantic request models
├── README.md               # Project documentation
└── Rohit_Farkade-Case Study - Backend Engineering intern.pdf
```

---

## ⚙️ Tech Stack

* **Python 3.10+**
* **FastAPI** – API framework
* **Pydantic** – Request validation
* **In-memory data store** (simulated DB)
* **Uvicorn** – ASGI server

> ⚠️ Note: This is a conceptual backend solution.
> No real database is used to keep focus on architecture and logic.

---

## 🧩 Core Features

### ✅ Product Management

* Products belong to a **company**
* SKU uniqueness enforced **per company**
* Each product has:

  * price
  * low stock threshold
  * inventory per warehouse

---

### ✅ Inventory Management

* Products can exist in multiple warehouses
* Each warehouse tracks quantity separately
* Inventory is isolated per company

---

### ✅ Low Stock Alert System

* Checks all warehouses of a company
* Filters products with:

  * recent sales activity
  * quantity below defined threshold
* Calculates estimated **days until stock-out**
* Attaches supplier information

---

## 🚀 API Endpoints

### 1️⃣ Create Product

**POST** `/products`

```json
{
  "name": "Widget A",
  "sku": "WID-001",
  "price": 99.99,
  "company_id": 1,
  "warehouse_id": 1,
  "initial_quantity": 20
}
```

**Response**

```json
{
  "message": "Product created successfully",
  "product": {
    "id": 1,
    "name": "Widget A",
    "sku": "WID-001",
    "price": 99.99,
    "company_id": 1,
    "low_stock_threshold": 10
  }
}
```

---

### 2️⃣ Get Low Stock Alerts

**GET** `/companies/{company_id}/alerts/low-stock`

**Response**

```json
{
  "alerts": [
    {
      "product_id": 1,
      "product_name": "Widget A",
      "sku": "WID-001",
      "warehouse_id": 1,
      "warehouse_name": "Main Warehouse",
      "current_stock": 5,
      "threshold": 10,
      "days_until_stockout": 12,
      "supplier": {
        "id": 1,
        "name": "Supplier Corp",
        "contact_email": "orders@supplier.com"
      }
    }
  ],
  "total_alerts": 1
}
```

---

## 🧠 Design Decisions & Assumptions

### ✔ Multi-Tenancy

* Each product belongs to exactly one company.
* All reads are scoped by `company_id`.

### ✔ Inventory Model

* Inventory is maintained per `(product, warehouse)` combination.
* Supports multiple warehouses per company.

### ✔ Business Rules

* SKU uniqueness enforced per company.
* Low stock threshold stored at product level.
* Alerts generated only for products with recent sales activity.

### ✔ Simplifications

* In-memory data store used instead of database.
* Sales data is mocked for demonstration.
* Authentication/authorization is out of scope.

---

## ▶️ How to Run

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

Open browser:

```
http://127.0.0.1:8000/docs
```

---