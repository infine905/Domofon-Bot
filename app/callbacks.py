from aiogram import Router
from aiogram.types import CallbackQuery

RouterCallback = Router()

@RouterCallback.callback_query()
async def callbackHandler(call:CallbackQuery):
    data = call.data.split('_')
    
    action = data[0]
    
    if action == 'logout':
        #кикнуть дауна 
        return
    
    #тут action не может быть равен ничему кроме "get"
        
    get_data = data[1]
    
    if get_data == 'apartment':
        apartment = getApartment()
        
        
        for i in apartment:
            apartment_id = A