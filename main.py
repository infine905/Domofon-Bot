
import app

import app
from config.config import dp, bot
from asyncio import run
from time import strftime 
from utils import set_command


async def main():
    dp.include_routers(
        app.RouterMain
    )

    await set_command(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':      
    now_time = strftime("%H:%M")
    print(f'Bot started at {now_time}')
    run(main()) 
