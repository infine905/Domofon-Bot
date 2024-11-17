from .callbacks import RouterCallback
from .register import RouterReg, sendContactFromUser


from aiogram import Router


RouterMain = Router()

RouterMain.include_routers(
    RouterCallback,
    RouterReg,
)