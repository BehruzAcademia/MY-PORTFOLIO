from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from config import PORTFOLIO
from keyboards import asosiy_menyu, ortga_tugma

router = Router()


# ==========================================
# /start KOMANDASI
# ==========================================
@router.message(CommandStart())
async def start(message: Message):
    xabar = (
        f"Assalomu alaykum, {message.from_user.first_name}! 👋\n\n"
        f"Men *{PORTFOLIO['ism_familiya']}* ning shaxsiy portfolio botiman.\n"
        f"Quyidagi tugmalar orqali men haqimda ma'lumot olishingiz mumkin! 👇"
    )
    try:
        await message.answer_photo(
            photo=PORTFOLIO["rasm_url"],
            caption=xabar,
            parse_mode="Markdown",
            reply_markup=asosiy_menyu()
        )
    except Exception:
        await message.answer(
            text=xabar,
            parse_mode="Markdown",
            reply_markup=asosiy_menyu()
        )


# ==========================================
# 🔙 BOSH MENYU
# ==========================================
@router.callback_query(F.data == "bosh_menu")
async def bosh_menu(callback: CallbackQuery):
    xabar = (
        f"*{PORTFOLIO['ism_familiya']}* ning shaxsiy portfolio boti\n\n"
        f"Quyidagi tugmalardan birini tanlang 👇"
    )
    await callback.message.edit_text(
        text=xabar,
        parse_mode="Markdown",
        reply_markup=asosiy_menyu()
    )


# ==========================================
# 👤 MEN HAQIMDA
# ==========================================
@router.callback_query(F.data == "men_haqimda")
async def men_haqimda(callback: CallbackQuery):
    matn = (
        "👤 *Men haqimda*\n"
        "─────────────────\n"
        f"📛 *Ism Familiya:* {PORTFOLIO['ism_familiya']}\n"
        f"🎂 *Yosh:* {PORTFOLIO['yosh']}\n\n"
        f"📝 *Qisqacha:*\n{PORTFOLIO['haqida']}"
    )
    await callback.message.edit_text(
        text=matn,
        parse_mode="Markdown",
        reply_markup=ortga_tugma()
    )


# ==========================================
# 🎓 TA'LIMIM
# ==========================================
@router.callback_query(F.data == "talimim")
async def talimim(callback: CallbackQuery):
    matn = (
        "🎓 *Ta'limim*\n"
        "─────────────────\n"
        f"🏫 *O'quv muassasasi:*\n{PORTFOLIO['maktab']}\n\n"
        f"📚 *Yo'nalish:*\n{PORTFOLIO['yunalish']}"
    )
    await callback.message.edit_text(
        text=matn,
        parse_mode="Markdown",
        reply_markup=ortga_tugma()
    )


# ==========================================
# 💻 KO'NIKMALARIM
# ==========================================
@router.callback_query(F.data == "konikmalar")
async def konikmalar(callback: CallbackQuery):
    dasturlash = "\n".join([f"  ▪️ {til}" for til in PORTFOLIO["dasturlash_tillari"]])
    texnologiyalar = "\n".join([f"  ▪️ {tex}" for tex in PORTFOLIO["texnologiyalar"]])

    matn = (
        "💻 *Ko'nikmalarim*\n"
        "─────────────────\n"
        f"🖥 *Dasturlash tillari:*\n{dasturlash}\n\n"
        f"⚙️ *Texnologiyalar:*\n{texnologiyalar}"
    )
    await callback.message.edit_text(
        text=matn,
        parse_mode="Markdown",
        reply_markup=ortga_tugma()
    )


# ==========================================
# 📞 ALOQA
# ==========================================
@router.callback_query(F.data == "aloqa")
async def aloqa(callback: CallbackQuery):
    matn = (
        "📞 *Aloqa*\n"
        "─────────────────\n"
        f"📱 *Telefon:* {PORTFOLIO['telefon']}\n"
        f"✈️ *Telegram:* {PORTFOLIO['telegram']}"
    )
    await callback.message.edit_text(
        text=matn,
        parse_mode="Markdown",
        reply_markup=ortga_tugma()
    )


# ==========================================
# 📍 MANZIL
# ==========================================
@router.callback_query(F.data == "manzil")
async def manzil(callback: CallbackQuery):
    matn = (
        "📍 *Manzil*\n"
        "─────────────────\n"
        f"🌆 *Shahar:* {PORTFOLIO['shahar']}\n"
        f"🏠 *Tuman:* {PORTFOLIO['manzil']}"
    )
    await callback.message.edit_text(
        text=matn,
        parse_mode="Markdown",
        reply_markup=ortga_tugma()
    )
