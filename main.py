import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# Telegram Bot Token ကို ဤနေရာတွင် ထည့်ပါ
TOKEN = "9059876499:AAE0cPC0nDRxOYqkwDf49ftNPgm2aIzwUAM"

# Logging ကို စတင်ရန်
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ကစားသမားများ၏ အချက်အလက်များကို သိမ်းဆည်းရန် Dictionary
user_data = {}

# ပင်မ မီနူး ခလုတ်များ
def get_game_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔍 ရိက္ခာရှာမည် (Scavenge)", callback_data="scavenge")],
            [InlineKeyboardButton(text="💤 အနားယူမည် (Rest)", callback_data="rest")],
            [InlineKeyboardButton(text="📊 အခြေအနေစစ်ဆေးမည် (Status)", callback_data="status")]
        ]
    )
    return keyboard

@dp.message(Command("start"))
async def cmd_start(message: Message):
    user_id = message.from_user.id
    # ကစားသမား အသစ်စတင်လျှင် HP နှင့် Food ကို သတ်မှတ်ပေးမည်
    user_data[user_id] = {"hp": 100, "food": 50}
    
    welcome_text = (
        "🧟‍♂️ **Zombie Survival RPG သို့ ကြိုဆိုပါတယ်!** 🧟‍♂️\n\n"
        "မြို့တစ်စခန်းလုံး ဇိုဘီတွေ ၀ိုင်းနေပါပြီ။ သင် အသက်ဆက်ရှင်နိုင်မလား?\n"
        "သင့်ရဲ့ HP နဲ့ Food ကို ထိန်းချုပ်ပြီး ရှင်သန်အောင် ကြိုးစားပါ။"
    )
    await message.answer(welcome_text, reply_markup=get_game_keyboard(), parse_mode="Markdown")

@dp.callback_query(F.data == "scavenge")
async def process_scavenge(callback: Message):
    user_id = callback.from_user.id
    if user_id not in user_data:
        user_data[user_id] = {"hp": 100, "food": 50}
    
    # ရိက္ခာရှာဖွေရာတွင် အစားအစာရနိုင်သလို ဇိုဘီနှင့်တွေ့ပြီး HP လျော့နိုင်သည်
    user_data[user_id]["food"] += 10
    user_data[user_id]["hp"] -= 15
    
    hp = user_data[user_id]["hp"]
    food = user_data[user_id]["food"]
    
    text = (
        "🔍 **ရိက္ခာရှာဖွေခြင်း:**\n"
        "သင့်မှာ စားစရာအနည်းငယ် ရလိုက်ပါတယ်၊ ဒါပေမဲ့ ဇိုဘီနဲ့ တိုက်ပွဲဖြစ်လို့ ထိခိုက်ဒဏ်ရာ ရသွားပါတယ်။\n\n"
        f"❤️ HP: {hp}/100\n"
        f"🍞 Food: {food}"
    )
    await callback.message.edit_text(text, reply_markup=get_game_keyboard(), parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "rest")
async def process_rest(callback: Message):
    user_id = callback.from_user.id
    if user_id not in user_data:
        user_data[user_id] = {"hp": 100, "food": 50}
    
    # အနားယူပါက HP ပြန်တက်မည်၊ Food လျော့မည်
    user_data[user_id]["hp"] = min(100, user_data[user_id]["hp"] + 20)
    user_data[user_id]["food"] = max(0, user_data[user_id]["food"] - 10)
    
    hp = user_data[user_id]["hp"]
    food = user_data[user_id]["food"]
    
    text = (
        "💤 **အနားယူခြင်း:**\n"
        "လုံခြုံတဲ့နေရာမှာ အနားယူလိုက်လို့ HP ပြန်တက်လာပါတယ်၊ ဒါပေမဲ့ ရိက္ခာအနည်းငယ် စားသုံးလိုက်ရပါတယ်။\n\n"
        f"❤️ HP: {hp}/100\n"
        f"🍞 Food: {food}"
    )
    await callback.message.edit_text(text, reply_markup=get_game_keyboard(), parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "status")
async def process_status(callback: Message):
    user_id = callback.from_user.id
    if user_id not in user_data:
        user_data[user_id] = {"hp": 100, "food": 50}
    
    hp = user_data[user_id]["hp"]
    food = user_data[user_id]["food"]
    
    text = (
        "📊 **သင့်ရဲ့ လက်ရှိအခြေအနေ:**\n\n"
        f"❤️ HP: {hp}/100\n"
        f"🍞 Food: {food}"
    )
    await callback.message.edit_text(text, reply_markup=get_game_keyboard(), parse_mode="Markdown")
    await callback.answer()

async def main():
    # Bot ကို စတင် Run မည့် Polling ပုံစံ
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

