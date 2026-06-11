import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# ==========================================
# SHAXSIY MA'LUMOTLAR - O'ZGARTIRING!
# ==========================================
PORTFOLIO = {
    "ism_familiya": "Nazarov Behruz`",
    "yosh": 18,
    "haqida": "Men dasturlashni yaxshi ko'raman. Python va web dasturlash bilan shug'ullanaman.",

    "maktab": "79-maktab",
    "yunalish": "Dasturiy ta'minot muhandisligi",

    "dasturlash_tillari": ["Python", "JavaScript", "HTML/CSS"],
    "texnologiyalar": ["Aiogram", "Django", "Git"],

    "telefon": "+998 99 123 77 74",
    "telegram": "username qo'yilmagan",

    "shahar": "Surxondaryo viloyati",
    "manzil": "Denov tumani",

    # O'z rasm URL manzilini qo'ying
    "rasm_url": "nazarov.png"
}
