from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from loader import dp, db
from keyboards.default.req_contact import contact
from filters.chat_filtr import IsPrivate, IsBotUser
from states.state import User

@dp.message_handler(IsBotUser(), IsPrivate(), CommandStart(), state="*")
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\nBotdan foydalanish uchun telefon raqmingizni jo'nating.", reply_markup=contact)
    await User.Tel.set()

@dp.message_handler(content_types='contact', state=User.Tel)
async def bot_start(message: types.Message, state:FSMContext):
    tel = message.contact.phone_number
    if not [tel.startswith('+998'), tel.startswith('998')]:
        await message.answer("O'zbekiston telefon raqamidan foydalaning!")
        return
    name = message.from_user.full_name
    tg_id = message.from_user.id
    db.add_user(tg_id, tel[-9:], name)
    await message.answer("Siz ro'yxatdan o'tdiz. Endi /start ni qaytadan bosing.", reply_markup=ReplyKeyboardRemove())
    await state.finish()