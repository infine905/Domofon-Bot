import requests
from io import BytesIO
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from asyncio import run

# Укажите ваш токен Telegram-бота
TOKEN = '7999931936:AAHrP6nu4ehudlRtuTlN5XlvIiHweLhLGYI'
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда для получения фото и отправки
@dp.message(Command('send_photo'))
async def send_photo(message: types.Message):
    # Укажите ссылку на изображение
    photo_url = 'https://cctv-streamer-11.profintel.ru/snapshot/image.jpg?st=PRvo6xXATEFbEMFOksW4EQ&e=1732032242&id=43'

    try:
        # Скачиваем фото
        response = requests.get(photo_url)
        response.raise_for_status()  # Проверяем на ошибки

        with open(f'temp/temp_photo134233.jpg', 'wb') as f:
            f.write(response.content)
            await bot.send_photo(chat_id=message.chat.id, photo=f)
            
    except Exception as e:
        await message.reply(f'Ошибка: {e}')
        
async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    print(f'Bot started')
    run(main())

