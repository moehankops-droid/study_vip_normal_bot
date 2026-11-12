import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# Bot Token ထည့်ပေးထားပြီးပါပြီ
TOKEN = "8437112340:AAEgXfvJ07jeBnGCtTsZgG69zHLCDBaOjRI"

router = Router()

# /start နှိပ်လိုက်သောအခါ ပေါ်လာမည့် Zombie ဇာတ်လမ်း အစ
@router.message(Command("start"))
async def cmd_start(message: Message):
    game_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🚪 အခန်း (၁) သို့ ဝင်မည်", callback_data="room_1")],
            [InlineKeyboardButton(text="🎒 အိတ်ထဲတွင် ဘာပါလဲ စစ်မည်", callback_data="check_bag")],
            [InlineKeyboardButton(text="🏃‍♂️ ထွက်ပြေးမည်", callback_data="run_away")]
        ]
    )
    await message.answer(
        "🧟‍♂️ **Zombie Apocalypse** ဇာတ်လမ်းမှ ကြိုဆိုပါတယ်။\n\n"
        "သင် ဘာလုပ်မလဲ? အောက်ပါတို့မှ တစ်ခုခုကို ရွေးချယ်ပါ -",
        reply_markup=game_keyboard
    )

# အခန်း (၁) ရွေးချယ်သည့်အခါ
@router.callback_query(F.data == "room_1")
async def room_one_chosen(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🗄️ ဗီရိုကို ရှာမည်", callback_data="search_wardrobe")],
            [InlineKeyboardButton(text="🪟 ပြတင်းပေါက်မှ ထွက်မည်", callback_data="escape_window")],
            [InlineKeyboardButton(text="🔙 ပင်မမီနူးသို့ ပြန်ရန်", callback_data="back_to_start")]
        ]
    )
    await callback.message.edit_text(
        "🚪 သင်ဟာ မှောင်မည်းနေတဲ့ အခန်းတစ်ခန်းထဲကို ဝင်လာခဲ့ပါတယ်။ အပြင်မှာ ဇာတ်ကောင်တွေရဲ့ အသံတွေ ကြားနေရတယ်။\n\n"
        "ဘာဆက်လုပ်မလဲ?",
        reply_markup=keyboard
    )
    await callback.answer()

# အိတ်စစ်ဆေးသည့်အခါ
@router.callback_query(F.data == "check_bag")
async def check_bag_chosen(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔙 ပင်မမီနူးသို့ ပြန်ရန်", callback_data="back_to_start")]
        ]
    )
    await callback.message.edit_text(
        "🎒 သင့်အိတ်ထဲမှာ ရေဘူးတစ်ဘူးနဲ့ ဓားမြှောင်ငယ် တစ်လက် ပါလာပါတယ်။",
        reply_markup=keyboard
    )
    await callback.answer()

# ထွက်ပြေးမည့်အခါ
@router.callback_query(F.data == "run_away")
async def run_away_chosen(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔄 အစကနေ ပြန်စမည်", callback_data="back_to_start")]
        ]
    )
    await callback.message.edit_text(
        "🏃‍♂️ သင် အပြင်ကို ထွက်ပြေးဖို့ ကြိုးစားပေမဲ့ ဇာတ်လမ်းက ချက်ချင်းဆိုသလို အဆုံးသတ်သွားခဲ့ပါပြီ (Game Over)!",
        reply_markup=keyboard
    )
    await callback.answer()

# ပင်မမီနူးသို့ ပြန်ရန်
@router.callback_query(F.data == "back_to_start")
async def back_to_start(callback: CallbackQuery):
    game_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🚪 အခန်း (၁) သို့ ဝင်မည်", callback_data="room_1")],
            [InlineKeyboardButton(text="🎒 အိတ်ထဲတွင် ဘာပါလဲ စစ်မည်", callback_data="check_bag")],
            [InlineKeyboardButton(text="🏃‍♂️ ထွက်ပြေးမည်", callback_data="run_away")]
        ]
    )
    await callback.message.edit_text(
        "🧟‍♂️ **Zombie Apocalypse** ဇာတ်လမ်းမှ ကြိုဆိုပါတယ်။\n\n"
        "သင် ဘာလုပ်မလဲ? အောက်ပါတို့မှ တစ်ခုခုကို ရွေးချယ်ပါ -",
        reply_markup=game_keyboard
    )
    await callback.answer()

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    
