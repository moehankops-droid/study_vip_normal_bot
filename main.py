import asyncio
import logging
import sqlite3
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

TOKEN = "9059876499:AAE0cPC0nDRxOYqkwDf49ftNPgm2aIzwUAM"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

# ----------------- DATABASE SETUP -----------------
def init_db():
    conn = sqlite3.connect("zombie_game.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            user_id INTEGER PRIMARY KEY,
            hp INTEGER,
            food INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def get_player(user_id):
    conn = sqlite3.connect("zombie_game.db")
    cursor = conn.cursor()
    cursor.execute("SELECT hp, food FROM players WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    if not row:
        cursor.execute("INSERT INTO players (user_id, hp, food) VALUES (?, ?, ?)", (user_id, 100, 50))
        conn.commit()
        hp, food = 100, 50
    else:
        hp, food = row
    conn.close()
    return hp, food

def update_player(user_id, hp, food):
    conn = sqlite3.connect("zombie_game.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE players SET hp = ?, food = ? WHERE user_id = ?", (hp, food, user_id))
    conn.commit()
    conn.close()

# ----------------- KEYBOARDS -----------------
def get_game_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔍 ရိက္ခာရှာမည် (Scavenge)", callback_data="scavenge")],
            [InlineKeyboardButton(text="💤 အနားယူမည် (Rest)", callback_data="rest")],
            [InlineKeyboardButton(text="📊 အခြေအနေစစ်ဆေးမည် (Status)", callback_data="status")]
        ]
    )

def get_restart_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔄 အစကပြန်စမည် (Restart)", callback_data="restart")]
        ]
    )

# ----------------- HANDLERS -----------------
@dp.message(Command("start"))
async def cmd_start(message: Message):
    user_id = message.from_user.id
    update_player(user_id, 100, 50)
    
    welcome_text = (
        "🧟‍♂️ **Zombie Survival RPG သို့ ကြိုဆိုပါတယ်!** 🧟‍♂️\n\n"
        "မြို့တစ်စခန်းလုံး ဇိုဘီတွေ ၀ိုင်းနေပါပြီ။ သင် အသက်ရှင်နိုင်မလား?\n"
        "သင့်ရဲ့ HP နဲ့ Food ကို ထိန်းချုပ်ပြီး ရှင်သန်အောင် ကြိုးစားပါ။"
    )
    await message.answer(welcome_text, reply_markup=get_game_keyboard(), parse_mode="Markdown")

@dp.callback_query(F.data == "restart")
async def process_restart(callback: CallbackQuery):
    user_id = callback.from_user.id
    update_player(user_id, 100, 50)
    
    text = "🧟‍♂️ **Zombie Survival RPG (ပြန်လည်စတင်သည်)** 🧟‍♂️\n\nရှင်သန်ရန်အတွက် မီနူးမှ ရွေးချယ်ပါ။"
    await callback.message.edit_text(text, reply_markup=get_game_keyboard(), parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "scavenge")
async def process_scavenge(callback: CallbackQuery):
    user_id = callback.from_user.id
    hp, food = get_player(user_id)
    
    food += 10
    hp -= 25
    
    if hp <= 0:
        update_player(user_id, 0, food)
        text = "💀 **Game Over!**\n\nရိက္ခာထွက်ရှာရင်း ဇိုဘီအုပ်စုနဲ့ တိုးပြီး ပြင်းထန်တဲ့ ဒဏ်ရာတွေနဲ့ သေဆုံးသွားပါပြီ..."
        await callback.message.edit_text(text, reply_markup=get_restart_keyboard(), parse_mode="Markdown")
        await callback.answer()
        return

    update_player(user_id, hp, food)
    text = (
        "🔍 **ရိက္ခာရှာဖွေခြင်း:**\n"
        "သင့်မှာ စားစရာအနည်းငယ် ရလိုက်ပါတယ်၊ ဒါပေမဲ့ ဇိုဘီနဲ့ တိုက်ပွဲဖြစ်လို့ ထိခိုက်ဒဏ်ရာ ရသွားပါတယ်။\n\n"
        f"❤️ HP: {hp}/100\n"
        f"🍞 Food: {food}"
    )
    await callback.message.edit_text(text, reply_markup=get_game_keyboard(), parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "rest")
async def process_rest(callback: CallbackQuery):
    user_id = callback.from_user.id
    hp, food = get_player(user_id)
    
    if food <= 0:
        text = (
            "⚠️ **သတိပေးချက်:**\n"
            "သင့်မှာ ရိက္ခာလုံးဝ မရှိတော့ပါ! အနားယူရန် ရိက္ခာလိုပါသည်။ ကျေးဇူးပြု၍ ရိက္ခာ အမြန်ရှာပါ။\n\n"
            f"❤️ HP: {hp}/100\n"
            f"🍞 Food: 0"
        )
        await callback.message.edit_text(text, reply_markup=get_game_keyboard(), parse_mode="Markdown")
        await callback.answer()
        return

    hp = min(100, hp + 20)
    food = max(0, food - 10)
    update_player(user_id, hp, food)
    
    text = (
        "💤 **အနားယူခြင်း:**\n"
        "လုံခြုံတဲ့နေရာမှာ အနားယူလိုက်လို့ HP ပြန်တက်လာပါတယ်၊ ဒါပေမဲ့ ရိက္ခာအနည်းငယ် စားသုံးလိုက်ရပါတယ်။\n\n"
        f"❤️ HP: {hp}/100\n"
        f"🍞 Food: {food}"
    )
    await callback.message.edit_text(text, reply_markup=get_game_keyboard(), parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "status")
async def process_status(callback: CallbackQuery):
    user_id = callback.from_user.id
    hp, food = get_player(user_id)
    
    text = f"📊 **သင့်ရဲ့ လက်ရှိအခြေအနေ:**\n\n❤️ HP: {hp}/100\n🍞 Food: {food}"
    await callback.message.edit_text(text, reply_markup=get_game_keyboard(), parse_mode="Markdown")
    await callback.answer()

async def main():
    init_db()  # Bot စစချင်း Database တည်ဆောက်ရန်
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
