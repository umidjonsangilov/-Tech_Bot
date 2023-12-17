from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from loader import dp, db
from filters.chat_filtr import IsPrivate
from states.state import User
from keyboards.inline.order import category

@dp.message_handler(IsPrivate(), CommandStart(), state="*")
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\nNima buyurtma qilasiz?",reply_markup=category)
