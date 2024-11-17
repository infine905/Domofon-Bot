from aiogram import Bot
from utils import Database

from config import bot

async def webhookHandler(tenant_id:int, domofon_id:int, apartment_id:int) -> bool:
    chat_id = Database().GetOne(data='tg_id', table_name='Users', find_param='tenant_id', find_value=int(tenant_id))
    await bot.send_message(chat_id=int(chat_id), text='Вам позвонили')