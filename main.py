from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

router = Router()

# အခန်း (၁) ရွေးချယ်လိုက်သည့်အခါ
@router.callback_query(F.data == "room_1")
async def room_one_chosen(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🗄️ ဗီရိုကို ရှာမည်", callback_data="search_wardrobe")],
            [InlineKeyboardButton(text="🪟 ပြတင်းပေါက်မှ ထွက်မည်", callback_data="escape_window")]
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
    
