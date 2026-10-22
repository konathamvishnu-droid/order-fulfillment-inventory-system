from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.products import router as products_router
from app.api.stock_movements import router as stock_movements_router


app = FastAPI(
    title="Order Fulfillment Inventory Platform",
    version="1.0.0",
)


app.include_router(auth_router)
app.include_router(products_router)
app.include_router(stock_movements_router)


@app.get("/")
def root():
    return {
        "message": "Order Fulfillment Inventory Platform API is running"
    }