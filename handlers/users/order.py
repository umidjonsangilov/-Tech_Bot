from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Text
from loader import dp, db
from filters.chat_filtr import IsPrivate
from states.state import User, Order
from keyboards.inline.order import product, order_pr

@dp.callback_query_handler(IsPrivate(), Text(startswith="C_"),state="*")
async def category_sel(call: types.CallbackQuery, state:FSMContext):
    category = call.data.lower().split("_")[1]
    data = db.order_data(category)
    food = call.message.reply_markup.inline_keyboard[0]
    for f in food:
        if f["callback_data"]==call.data:
            product_cat = f['text'].lower()
            await state.update_data({"product":product_cat})
            await call.message.edit_text(f"Qanady {product_cat} tanlaysiz",reply_markup=product(data))

@dp.callback_query_handler(IsPrivate(), Text(startswith="P_"),state="*")
async def product_sel(call: types.CallbackQuery, state:FSMContext):
    id = call.data.split('_')[1]
    product = db.product(id)
    data = await state.get_data()
    product_cat = data.get("product")
    text = (f"<b>{product_cat.capitalize()}:</b> {product[2]}\n<b>Tavsif:</b> {product[3]}\n"
            f"<b>Narxi:</b> {product[5]}")
    await call.message.answer_photo(photo=product[4],caption=text,reply_markup=order_pr(id))
    await call.message.delete()

@dp.callback_query_handler(IsPrivate(), Text(startswith="O_"),state="*")
async def placing_an_order(call: types.CallbackQuery, state:FSMContext):
    product_id = call.data.split('_')[1]
    await state.update_data({"product_id":product_id})
    await call.message.answer("miqdorini kiriting")
    await call.message.delete()
    await Order.Amount.set()

@dp.message_handler(content_types="text",state=Order.Amount)
async def bot_start(message: types.Message, state:FSMContext):
    user_id = message.from_user.id
    amount = message.text
    if not amount.isdigit():
        await message.answer("Miqdorni sonda kirgizing!")
        return
    data = await state.get_data()
    product_id = data.get("product_id")
    db.add_order(product_id,user_id,amount)
    await message.answer("Buyurtna qabul qilindi.")