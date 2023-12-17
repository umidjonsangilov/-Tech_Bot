from aiogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM

category = IKM(inline_keyboard=[
    [
        IKB(text="Ichimlik",callback_data="C_DRINK"),
        IKB(text="Taom",callback_data="C_FOOD")
    ]
])

def product(data):
    product = IKM(row_width=2)
    for d in data:
        product.insert(IKB(text=f"{d[0]}",callback_data=f"P_{d[1]}"))
    return product

def order_pr(data):
    return IKM(inline_keyboard=[[IKB(text=f"Buyurtma qilish",callback_data=f"O_{data}")]])