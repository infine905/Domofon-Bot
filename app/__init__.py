from .handler import RouterHandler
from .register import RouterReg


from aiogram import Router


RouterMain = Router()

RouterMain.include_routers(
    RouterHandler,
    RouterReg
)