from aiogram.fsm.state import StatesGroup, State

class FSM_change(StatesGroup):
    CHANGE_TEXT = State()
    CHANGE_PHOTO = State()
