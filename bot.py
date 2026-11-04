import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Your Bot Token
API_TOKEN = '8437112340:AAEgXfvJ07jeBnGCtTsZgG69zHLCDBaOjRI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# AI Quiz pool
QUIZ_POOL = [
    {
        "q": "Correct the sentence: 'He go to school every day.'",
        "ans": ["goes"],
        "hint": "Simple Present Tense တွင် Subject က He ဖြစ်ပါက Verb မှာ s/es ထည့်ရပါမည်။"
    },
    {
        "q": "Correct the sentence: 'They plays football on Sundays.'",
        "ans": ["play"],
        "hint": "Subject က They (plural) ဖြစ်၍ Verb အရင်း (V1) သာ သုံးရပါမည်။"
    },
    {
        "q": "Fill in the blank: 'She ___ English yesterday.' (study)",
        "ans": ["studied"],
        "hint": "yesterday ပါရှိသောကြောင့် Simple Past Tense (V2) ကို အသုံးပြုပါ။"
    },
    {
        "q": "Fill in the blank: 'I ___ a letter now.' (write)",
        "ans": ["am writing"],
        "hint": "now ပါရှိသောကြောင့် Present Continuous Tense ကို သုံးပါ။"
    }
]

# Start Command & Main Menu Library Keyboard
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("📚 အပိုင်း (၁) - အခြေခံ ဝါကျတည်ဆောက်ခြင်း ကျင့်စဉ်", callback_data="lib_1"),
        InlineKeyboardButton("📚 အပိုင်း (၂) - ပစ္စုပ္ပန်ကာလ ကျင့်စဉ်များ", callback_data="lib_2"),
        InlineKeyboardButton("📚 အပိုင်း (၃) - အတိတ်ကာလ ကျင့်စဉ်များ", callback_data="lib_3"),
        InlineKeyboardButton("📚 အပိုင်း (၄) - အနာဂတ်ကာလ ကျင့်စဉ်များ", callback_data="lib_4"),
        InlineKeyboardButton("📚 အပိုင်း (၅) - အဆင့်မြင့် ဝါကျဆက်စပ်ခြင်း ကျင့်စဉ်", callback_data="lib_5"),
        InlineKeyboardButton("📚 အပိုင်း (၆) - အလုံးစုံ စစ်ဆေးသည့် နောက်ဆုံးကျင့်စဉ်", callback_data="lib_6"),
        InlineKeyboardButton("📊 ကိုယ်ပိုင် အဆင့်နှင့် Profile (Rank)", callback_data="profile"),
        InlineKeyboardButton("🎯 AI ကျင့်စဉ်နှင့် တိုက်ရိုက်ယှဉ်ပြိုင်ရန် (Quiz Battle)", callback_data="quiz_start")
    )
    
    welcome_text = (
        "🏯 မင်္ဂလာပါ စစ်သည်တော် MOHE။\n"
        "အင်္ဂလိပ်စာ ကျင့်စဉ်စာကြည့်တိုက် (Library Mode) မှ ကြိုဆိုပါတယ်။\n\n"
        "လေ့လာလိုသော အပိုင်း (သို့မဟုတ်) ကျင့်စဉ်ကို ရွေးချယ်ပါ!"
    )
    await message.answer(welcome_text, reply_markup=keyboard)

# Callback Handler for Library Sections (with internal sub-levels & martial art styles)
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('lib_'))
async def process_library(callback_query: types.CallbackQuery):
    code = callback_query.data.split('_')[1]
    
    details = {
        "1": (
            "📚 **အပိုင်း (၁) - အခြေခံ ဝါကျတည်ဆောက်ခြင်း ကျင့်စဉ်**\n\n"
            "• **အဓိက အချက်များ:** S + V, S + V + O, S + V + C\n"
            "• **အတွင်းပိုင်း ကျင့်စဉ်ခွဲများ:**\n"
            "  - 🥋 *အစပြု လက်သီးချက် (Basic S+V)*\n"
            "  - 🥋 *ကံဆောင် တိုက်ကွက် (Object Focus)*"
        ),
        "2": (
            "📚 **အပိုင်း (၂) - ပစ္စုပ္ပန်ကာလ ကျင့်စဉ်များ**\n\n"
            "• **အတွင်းပိုင်း ကျင့်စဉ်ခွဲများ:**\n"
            "  - 🔥 *ရိုးရှင်းသော ပစ္စုပ္ပန် တိုက်ကွက် (Simple Present Style)*\n"
            "  - ⚡ *လက်ရှိဖြစ်ဆဲ လှုပ်ရှားမှု (Continuous Style)*"
        ),
        "3": (
            "📚 **အပိုင်း (၃) - အတိတ်ကာလ ကျင့်စဉ်များ**\n\n"
            "• **အတွင်းပိုင်း ကျင့်စဉ်ခွဲများ:**\n"
            "  - 🛡️ *အတိတ်ကို ပြန်ပြောင်းကြည့်ခြင်း (Simple Past Style)*\n"
            "  - 🌪️ *အတိတ်တွင် ဖြစ်ပျက်ဆဲ စက်ကွင်း (Past Continuous)*"
        ),
        "4": (
            "📚 **အပိုင်း (၄) - အနာဂတ်ကာလ ကျင့်စဉ်များ**\n\n"
            "• **အတွင်းပိုင်း ကျင့်စဉ်ခွဲများ:**\n"
            "  - ⚔️ *အနာဂတ် ခရီးစတင်ခြင်း (Future Simple)*\n"
            "  - 🎯 *ကြိုတင်ကြံစည်မှု တိုက်ကွက် (Future Plans)*"
        ),
        "5": (
            "📚 **အပိုင်း (၅) - အဆင့်မြင့် ဝါကျဆက်စပ်ခြင်း ကျင့်စဉ်**\n\n"
            "• **အတွင်းပိုင်း ကျင့်စဉ်ခွဲများ:**\n"
            "  - 👑 *တက်ကြွ/ခံ동ါ တိုက်ကွက် (Active & Passive)*\n"
            "  - 🐉 *ကြိုးမျှားခွင် ဆက်စပ်ကွက် (Relative Clauses)*"
        ),
        "6": (
            "📚 **အပိုင်း (၆) - အလုံးစုံ စစ်ဆေးသည့် နောက်ဆုံးကျင့်စဉ်**\n\n"
            "• **အတွင်းပိုင်း ကျင့်စဉ်ခွဲများ:**\n"
            "  - 🏆 *ဂရင်းမာစတာ နောက်ဆုံးစိန်ခေါ်ပွဲ (Grand Master Trial)*"
        )
    }
    
    text = details.get(code, "ကျင့်စဉ် အချက်အလက်များ...")
    
    action_kb = InlineKeyboardMarkup(row_width=1)
    action_kb.add(
        InlineKeyboardButton("🎯 ဤအပိုင်းအတွက် AI Quiz ဆက်ဖြေမည်", callback_data="quiz_start"),
        InlineKeyboardButton("⬅️ ပင်မစာကြည့်တိုက်သို့ ပြန်ရန်", callback_data="back_home")
    )
    
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text, reply_markup=action_kb, parse_mode="Markdown")

# Profile / Rank Handler
@dp.callback_query_handler(lambda c: c.data == 'profile')
async def show_profile(callback_query: types.CallbackQuery):
    profile_text = (
        "📊 **စစ်သည်တော် Profile & Rank**\n\n"
        "• အမည်: MOHE\n"
        "• လက်ရှိအဆင့်: 🥋 အခြေခံ ကျင့်စဉ် တည်ဆောက်သူ\n"
        "• ရရှိထားသော အမှတ်: 200 XP\n"
        "• AI Battle အနိုင်ရနှုန်း: 90%\n"
        "• လေ့လာပြီးစီးမှု: အပိုင်း (၁) မှ အစပြုနေဆဲ"
    )
    back_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ ပင်မစာကြည့်တိုက်သို့ ပြန်ရန်", callback_data="back_home"))
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, profile_text, reply_markup=back_kb, parse_mode="Markdown")

# AI Training Quiz Battle Mode Start
@dp.callback_query_handler(lambda c: c.data == 'quiz_start')
async def start_ai_quiz(callback_query: types.CallbackQuery):
    current_q = random.choice(QUIZ_POOL)
    
    quiz_text = (
        "🤖 **AI ကျင့်စဉ်နှင့် တိုက်ရိုက်ယှဉ်ပြိုင်ရန် (Quiz Battle)**\n\n"
        f"⚔️ **စိန်ခေါ်မှု မေးခွန်း:**\n{current_q['q']}\n\n"
        "💡 *အရိပ်အမြွက်:* သင့်ရဲ့ အဖြေကို ချတ်ဘောက်စ်ထဲမှာ တိုက်ရိုက် ရေးပို့ပေးပါ (ဥပမာ - မှန်ကန်သော စာသား)။ AI Bot က တိုက်ခိုက်မှုကို စစ်ဆေးပေးပါမယ်!"
    )
    back_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ ပင်မစာကြည့်တိုက်သို့ ပြန်ရန်", callback_data="back_home"))
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, quiz_text, reply_markup=back_kb, parse_mode="Markdown")

# Message handler for Quiz Answer checking against AI
@dp.message_handler(lambda message: message.text and not message.text.startswith('/'))
async def check_quiz_answer(message: types.Message):
    user_answer = message.text.strip().lower()
    
    is_correct = any(ans in user_answer for ans in ["goes", "play", "studied", "am writing", "go", "correct", "မှန်"])
    
    if is_correct:
        reply_text = (
            "✨ **တိုက်ခိုက်မှု အောင်မြင်သည်! AI Bot ကို အနိုင်ယူလိုက်ပြီ 🔥**\n"
            "• ရရှိသော အမှတ်: +50 XP\n"
            "• စုစုပေါင်းအမှတ်: 250 pts\n\n"
            "ဆက်လက်လေ့ကျင့်ရန် /start ကို နှိပ်ပါ။"
        )
    else:
        reply_text = (
            "❌ **တိုက်ခိုက်မှု လွဲချော်သွားသည်! AI Bot က တိုက်ခိုက်လိုက်သည် 🛡️**\n"
            "သင်၏အဖြေမှာ အနည်းငယ် မှားယွင်းနေပါသည်။ ထပ်မံကြိုးစားကြည့်ပါဦး သူငယ်ချင်း။"
        )
    
    await message.answer(reply_text, parse_mode="Markdown")

# Back to Home Callback
@dp.callback_query_handler(lambda c: c.data == 'back_home')
async def back_home(callback_query: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("📚 အပိုင်း (၁) - အခြေခံ ဝါကျတည်ဆောက်ခြင်း ကျင့်စဉ်", callback_data="lib_1"),
        InlineKeyboardButton("📚 အပိုင်း (၂) - ပစ္စုပ္ပန်ကာလ ကျင့်စဉ်များ", callback_data="lib_2"),
        InlineKeyboardButton("📚 အပိုင်း (၃) - အတိတ်ကာလ ကျင့်စဉ်များ", callback_data="lib_3"),
        InlineKeyboardButton("📚 အပိုင်း (၄) - အနာဂတ်ကာလ ကျင့်စဉ်များ", callback_data="lib_4"),
        InlineKeyboardButton("📚 အပိုင်း (၅) - အဆင့်မြင့် ဝါကျဆက်စပ်ခြင်း ကျင့်စဉ်", callback_data="lib_5"),
        InlineKeyboardButton("📚 အပိုင်း (၆) - အလုံးစုံ စစ်ဆေးသည့် နောက်ဆုံးကျင့်စဉ်", callback_data="lib_6"),
        InlineKeyboardButton("📊 ကိုယ်ပိုင် အဆင့်နှင့် Profile (Rank)", callback_data="profile"),
        InlineKeyboardButton("🎯 AI ကျင့်စဉ်နှင့် တိုက်ရိုက်ယှဉ်ပြိုင်ရန် (Quiz Battle)", callback_data="quiz_start")
    )
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "🏯 ပင်မ စာကြည့်တိုက်သို့ ပြန်ရောက်ပါပြီ စစ်သည်တော် MOHE။", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

