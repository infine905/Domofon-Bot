from aiogram import Bot
from utils import Database

async def webhookHandler(tenant_id, domofon_id, bot:Bot):
    chat_id=Database().GetOne(data='tg_id', table_name='Users', find_param='tenant_id', find_value=tenant_id)
    
    await bot.send_message(chat_id=chat_id, text='Вам позвонили')