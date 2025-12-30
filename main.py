from fastapi import FastAPI, HTTPException
from models import ProductCreate
import fake_db

app = FastAPI(title="Inventory Management API")


@app.post("/products")
def create_product(data: ProductCreate):

    company = fake_db.get_company(data.company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    existing = fake_db.get_product_by_sku_and_company(data.sku, data.company_id)
    if existing:
        raise HTTPException(status_code=409, detail="SKU already exists for this company")

    product = {
        "id": len(fake_db.products) + 1,
        "name": data.name,
        "sku": data.sku,
        "price": data.price,
        "company_id": data.company_id,
        "low_stock_threshold": 10
    }

    fake_db.add_product(product)

    inventory = {
        "product_id": product["id"],
        "warehouse_id": data.warehouse_id,
        "quantity": data.initial_quantity
    }

    fake_db.add_inventory(inventory)

    return {
        "message": "Product created successfully",
        "product": product
    }


@app.get("/companies/{company_id}/alerts/low-stock")
def get_low_stock_alerts(company_id: int):

    company = fake_db.get_company(company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    alerts = []

    warehouses = fake_db.get_warehouses_by_company(company_id)

    for warehouse in warehouses:
        inventory_items = fake_db.get_inventory_by_warehouse(warehouse["id"])

        for item in inventory_items:
            product = fake_db.get_product(item["product_id"])

            if not product or product["company_id"] != company_id:
                continue

            recent_sales = fake_db.get_recent_sales(
                product_id=product["id"],
                warehouse_id=warehouse["id"]
            )

            if recent_sales <= 0:
                continue

            if item["quantity"] < product["low_stock_threshold"]:
                supplier = fake_db.get_supplier_for_product(product["id"])

                avg_daily_sales = recent_sales / 30
                days_until_stockout = (
                    int(item["quantity"] / avg_daily_sales)
                    if avg_daily_sales > 0 else None
                )

                alerts.append({
                    "product_id": product["id"],
                    "product_name": product["name"],
                    "sku": product["sku"],
                    "warehouse_id": warehouse["id"],
                    "warehouse_name": warehouse["name"],
                    "current_stock": item["quantity"],
                    "threshold": product["low_stock_threshold"],
                    "days_until_stockout": days_until_stockout,
                    "supplier": supplier
                })

    return {
        "alerts": alerts,
        "total_alerts": len(alerts)
    }
