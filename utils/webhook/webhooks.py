from pydantic import BaseModel
from fastapi import FastAPI, Query
from hypercorn.asyncio import serve
from hypercorn.config import Config

from .handler_webhook import webhookHandler

fastapi_app = FastAPI()

# Модель данных для POST запросов
class RequestModel(BaseModel):
    tenant_id: int
    domofon_id: int
    apartment_id: int
    
class ReturnModel(BaseModel):
    status: str
    message: str
    
# Обработка GET запроса
@fastapi_app.get("/call_domofon/")
async def handle_get(
    tenant_id: int = Query(..., description="ID жильца"),
    domofon_id: int = Query(..., description="ID домофона"),
    apartment_id: int = Query(..., description="ID квартиры")
):
    result, message = await webhookHandler(tenant_id=tenant_id, domofon_id=domofon_id, apartment_id=apartment_id)   
    return {
        "status": "success" if result else "error",
        "message": message
    }


# Обработка POST запроса
@fastapi_app.post("/call_domofon/")
async def handle_post(data: RequestModel) -> ReturnModel:
    result, message = await webhookHandler(tenant_id=data.tenant_id, domofon_id=data.domofon_id, apartment_id=data.apartment_id)   
    return {
        "status": "success" if result else "error",
        "message": message
    }


def fastapi_main():
    config = Config()
    config.bind = ["0.0.0.0:4123"] 
    return serve(fastapi_app, config)

if __name__ == "__main__":
    fastapi_main()
