from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties


TOKEN_API = '7999931936:AAHrP6nu4ehudlRtuTlN5XlvIiHweLhLGYI'

bot = Bot(TOKEN_API, default=DefaultBotProperties(parse_mode='MarkdownV2'))
dp = Dispatcher()

api_key = 'SecretToken'
url = "https://domo-dev.profintel.ru/tg-bot/check-tenant"

db_name = 'database'