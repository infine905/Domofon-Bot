from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

RouterHandler = Router()


@RouterHandler.message(Command('get_doorphone'))
async def getDoorphone(message:Message):
    




# @RouterHandler.message(Command('start'))
# async def aboba(message:Message):
#     inl_kb = [
#         [InlineKeyboardButton(text='1', callback_data='123')],
#         [InlineKeyboardButton(text='2', callback_data='123')],
#         [InlineKeyboardButton(text='3', callback_data='123')]
#     ]
#     Inl = InlineKeyboardMarkup(inline_keyboard=inl_kb)

#     await message.answer(text='1', reply_markup=Inl)


# @RouterHandler.message(Command('test'))
# async def aboba(message:Message):

#     rep_kb = [
#         [KeyboardButton(text='1')],
#         [KeyboardButton(text='2')],
#         [KeyboardButton(text='3')]
#     ]
#     Rep = ReplyKeyboardMarkup(keyboard=rep_kb)

#     await message.answer(text='2', reply_markup=Rep)
