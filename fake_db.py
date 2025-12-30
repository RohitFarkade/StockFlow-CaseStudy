products = []
inventories = []

warehouses = [
    {"id": 1, "name": "Main Warehouse"},
    {"id": 2, "name": "Secondary Warehouse"}
]

companies = [
    {"id": 1, "name": "Demo Company"}
]

suppliers = [
    {"id": 1, "name": "Supplier Corp", "contact_email": "orders@supplier.com"}
]

# ----------------------
# Product helpers
# ----------------------

def get_product_by_sku_and_company(sku, company_id):
    return next(
        (p for p in products if p["sku"] == sku and p["company_id"] == company_id),
        None
    )

def get_product(product_id):
    return next((p for p in products if p["id"] == product_id), None)

def add_product(product):
    products.append(product)

# ----------------------
# Inventory helpers
# ----------------------

def add_inventory(inventory):
    inventories.append(inventory)

def get_inventory_by_warehouse(warehouse_id):
    return [i for i in inventories if i["warehouse_id"] == warehouse_id]

# ----------------------
# Company / Warehouse
# ----------------------

def get_company(company_id):
    return next((c for c in companies if c["id"] == company_id), None)

def get_warehouses_by_company(company_id):
    # simplified assumption
    return warehouses if company_id == 1 else []

# ----------------------
# Sales & Supplier Logic
# ----------------------

def get_recent_sales(product_id, warehouse_id, days=30):
    return 15  # simulated data

def get_supplier_for_product(product_id):
    return suppliers[0]
