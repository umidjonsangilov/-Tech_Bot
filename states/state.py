from aiogram.dispatcher.filters.state import StatesGroup, State

class User(StatesGroup):
    Tel=State()

class Order(StatesGroup):
    Amount=State()
