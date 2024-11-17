from .callbacks import RouterCallback
from .register import RouterReg
from .profile import getProfile
from aiogram import Router


RouterMain = Router()

RouterMain.include_routers(
    RouterCallback,
    RouterReg,
)