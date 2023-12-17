from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="Telefon raqam jo'natish",
                                                      request_contact=True)
                                   ]
                               ])