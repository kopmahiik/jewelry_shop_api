from fastapi import FastAPI

from app.api.routes.products import router as products_router

app = FastAPI()
app.include_router(products_router)


@app.get("/")
async def root():
    return {"message": "Ping"}
