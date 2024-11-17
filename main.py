from config.config import dp, bot
import asyncio 
from hypercorn.asyncio import serve
from hypercorn.config import Config
from time import strftime 

import app
from utils import set_command, fastapi_app

async def bot_main():
    dp.include_routers(
        app.RouterMain
    )

    await set_command(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)

async def fastapi_main():
    config = Config()
    config.bind = ["0.0.0.0:4123"] 
    await serve(fastapi_app, config)

async def main():
    await asyncio.gather(bot_main(), fastapi_main())


if __name__ == '__main__':
    now_time = strftime("%H:%M")
    
    print(f'FastApi and Bot started at {now_time}')
    asyncio.run(main())
