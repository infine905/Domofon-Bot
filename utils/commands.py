from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_command(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начать'
        ),
        BotCommand(
            command='get_doorphone',
            description='Получить список '
        ),
    ]   
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())
