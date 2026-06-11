from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def asosiy_menyu() -> InlineKeyboardMarkup:
    tugmalar = [
        [InlineKeyboardButton(text="👤 Men haqimda", callback_data="men_haqimda")],
        [InlineKeyboardButton(text="🎓 Ta'limim", callback_data="talimim")],
        [InlineKeyboardButton(text="💻 Ko'nikmalarim", callback_data="konikmalar")],
        [InlineKeyboardButton(text="📞 Aloqa", callback_data="aloqa")],
        [InlineKeyboardButton(text="📍 Manzil", callback_data="manzil")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=tugmalar)


def ortga_tugma() -> InlineKeyboardMarkup:
    tugmalar = [
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="bosh_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=tugmalar)
