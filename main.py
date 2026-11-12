import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

# Bot Token ကို ထည့်ပါ
TOKEN = "9059876499:AAE0cPC0nDRxOYqkwDf49ftNPgm2aIzwUAM"

# Game States တွေ သတ်မှတ်ခြင်း
class GameStates(StatesGroup):
    playing = State()

# Player ရဲ့ အချက်အလက်များ သိမ်းဆည်းရန် (HP နှင့် ရိက္ခာ)
player_stats = {}

dp = Dispatcher()

# /start Command ဖြင့် ဂိမ်းစတင်ရန်
@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    player_stats[user_id] = {"hp": 100, "food": 50}
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏃‍♂️ မြို့ထဲသို့ ဝင်မည်", callback_data="go_city")],
        [InlineKeyboardButton(text="🌲 တောဘက်သို့ ရှောင်မည်", callback_data="go_forest")]
    ])
    
    await message.answer(
        f"ဟေး {html.bold(message.from_user.first_name)}၊ ဇိုဘီကပ်ဘေးကြီး စတင်နေပြီ!\n\n"
        f"❤️ အသက် (HP): 100 | 🥫 ရိက္ခာ: 50\n\n"
        f"မင်း ပထမဆုံး ဘယ်လို ဆုံးဖြတ်မလဲ?",
        reply_markup=keyboard
    )
    await state.set_state(GameStates.playing)

# မြို့ထဲသွားမည့် ဆုံးဖြတ်ချက်
@dp.callback_query(F.data == "go_city", GameStates.playing)
async def process_city(callback: Message):
    user_id = callback.from_user.id
    player_stats[user_id]["food"] += 20
    player_stats[user_id]["hp"] -= 30
    
    hp = player_stats[user_id]["hp"]
    food = player_stats[user_id]["food"]
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔫 လက်နက်တိုက်သို့ သွားမည်", callback_data="go_armory")],
        [InlineKeyboardButton(text="🏠 အိမ်တွင် ပုန်းခိုမည်", callback_data="go_hide")]
    ])
    
    await callback.message.edit_text(
        f"🏙️ မင်း မြို့ထဲက စားသောက်ဆိုင်ကို ဝင်ရှာတာ ရိက္ခာတွေ တွေ့လိုက်ရပေမဲ့ ဇိုဘီနဲ့ တိုးလို့ ဒဏ်ရာရသွားတယ်!\n\n"
        f"❤️ အသက် (HP): {hp} | 🥫 ရိಕ္ခာ: {food}\n\n"
        f"ဆက်ပြီး ဘာလုပ်မလဲ?",
        reply_markup=keyboard
    )
    await callback.answer()

# တောဘက်သွားမည့် ဆုံးဖြတ်ချက်
@dp.callback_query(F.data == "go_forest", GameStates.playing)
async def process_forest(callback: Message):
    user_id = callback.from_user.id
    player_stats[user_id]["food"] -= 15
    
    hp = player_stats[user_id]["hp"]
    food = player_stats[user_id]["food"]
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⛺ စခန်းချ အနားယူမည်", callback_data="rest_camp")],
        [InlineKeyboardButton(text="🔍 ရိက္ခာထွက်ရှာမည်", callback_data="search_food")]
    ])
    
    await callback.message.edit_text(
        f"🌲 တောထဲကို ရှောင်လာတာ လုံခြုံပေမဲ့ စားစရာရှားပါးလို့ ရိက္ခာ လျော့သွားတယ်...\n\n"
        f"❤️ အသက် (HP): {hp} | 🥫 ရိက္ခာ: {food}\n\n"
        f"ဆက်ပြီး ဘာလုပ်မလဲ?",
        reply_markup=keyboard
    )
    await callback.answer()

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    
