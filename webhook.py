import asyncio
from pydantic import BaseModel
from fastapi import FastAPI, Query
from hypercorn.asyncio import serve
from hypercorn.config import Config

fastapi_app = FastAPI()

# Модель данных для POST запросов
class RequestModel(BaseModel):
    tenant_id: int
    domofon_id: int
    apartment_id: int
    
class ReturnModel(BaseModel):
    status: str
    
# Обработка GET запроса
@fastapi_app.get("/call_domofon/")
async def handle_get(
    tenant_id: int = Query(..., description="ID жильца"),
    domofon_id: int = Query(..., description="ID домофона"),
    apartment_id: int = Query(..., description="ID квартиры")
):
    return {
        "status": "success",
    }

# Обработка POST запроса
@fastapi_app.post("/call_domofon/")
async def handle_post(data: RequestModel) -> ReturnModel:
    return {
        "status": "success",
    }

def main():
    config = Config()
    config.bind = ["0.0.0.0:4123"] 
    asyncio.run(serve(fastapi_app, config))

if __name__ == "__main__":
    main()
