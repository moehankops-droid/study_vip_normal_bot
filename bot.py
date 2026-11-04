import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Your Bot Token
API_TOKEN = '8437112340:AAEgXfvJ07jeBnGCtTsZgG69zHLCDBaOjRI'


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Start Command & Main Menu Keyboard
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("🥋 Level 1 (🌱 Novice)", callback_data="level_1"),
        InlineKeyboardButton("🌿 Level 2 (🌿 Beginner)", callback_data="level_2"),
        InlineKeyboardButton("🔥 Level 3 (🌿 Inter)", callback_data="level_3"),
        InlineKeyboardButton("🛡️ Level 4 (⚡ Adv)", callback_data="level_4"),
        InlineKeyboardButton("⚡ Level 5 (🌟 Master)", callback_data="level_5"),
        InlineKeyboardButton("👑 Level 6 (🏆 G-Master)", callback_data="level_6"),
        InlineKeyboardButton("📊 My Rank & Leaderboard", callback_data="rank"),
        InlineKeyboardButton("🎯 Training Quiz (AI Battle)", callback_data="quiz")
    )
    
    welcome_text = (
        "🏯 မင်္ဂလာပါ စစ်သည်တော် MOHE!\n"
        "အင်္ဂလိပ်စာ သိုင်းကျင့်စဉ် (Study RPG Bot) မှ ကြိုဆိုပါတယ်။\n\n"
        "လေ့ကျင့်လိုသော Level သို့မဟုတ် မိုက်ခလုတ်များကို နှိပ်ပြီး စတင်လိုက်ပါ!"
    )
    await message.answer(welcome_text, reply_markup=keyboard)

# Callback Handler for Levels and Quiz
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('level_'))
async def process_levels(callback_query: types.CallbackQuery):
    code = callback_query.data.split('_')[1]
    
    details = {
        "1": "🌱 **Level 1: အခြေခံဆုံး အုတ်မြစ် (Novice Stage)**\n\n1. **Basic Patterns:** S+V, S+V+O, S+V+C\n2. **Simple Present Tense:** Subject + V1 (s/es)\n   • *I play chess every day.*\n3. **Simple Past Tense:** Subject + V2\n   • *I studied English yesterday.*\n4. **Simple Future Tense:** Subject + will + V1\n   • *I will code tomorrow.*",
        "2": "🌿 **Level 2: စတင်ရှင်သန်ခြင်း (Beginner Stage)**\n\n1. **Present Continuous Tense:** Subject + is/am/are + V-ing\n   • *I am coding a Python bot right now.*\n2. **Past Continuous Tense:** Subject + was/were + V-ing\n   • *She was studying English yesterday evening.*",
        "3": "🌿 **Level 3: အလယ်အလတ် ကျင့်စဉ် (Intermediate)**\n\n1. **Present Perfect Tense:** Subject + has/have + V3\n   • *I have finished my homework.*\n2. **Past Perfect Tense:** Subject + had + V3\n   • *He had left before I arrived.*",
        "4": "⚡ **Level 4: အဆင့်မြင့် တိုက်ခိုက်ရေး (Advanced)**\n\n1. **Active & Passive Voice:**\n   • *Active: He writes a letter.*\n   • *Passive: A letter is written by him.*\n2. **Relative Clauses:** Who, Which, That အသုံးများ။",
        "5": "🌟 **Level 5: မာစတာ အဆင့် (Master Stage)**\n\n1. **Conditionals (If-clauses):** Type 1, Type 2, Type 3\n2. **Reported Speech:** တိုက်ရိုက်စကားနှင့် သွယ်ဝိုက်စကား ပြောဆိုပုံများ။",
        "6": "🏆 **Level 6: ဂရင်းမာစတာ (Grand Master)**\n\n1. **Essay Composition & Advanced Grammar**\n2. **AI Battle & Complex Quizzes:** အင်္ဂလိပ်စာ တစ်ခုလုံးကို ကျွမ်းကျင်ပိုင်နိုင်စွာ စိန်ခေါ်ရမည့် အဆင့်။"
    }
    
    text = details.get(code, "လေ့ကျင့်ခန်း အချက်အလက်များ...")
    
    back_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ ပင်မမီနူးသို့ ပြန်ရန်", callback_data="back_home"))
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text, reply_markup=back_kb, parse_mode="Markdown")

# AI Training Quiz Battle Mode
@dp.callback_query_handler(lambda c: c.data == 'quiz')
async def start_ai_quiz(callback_query: types.CallbackQuery):
    quiz_text = (
        "🤖 **AI Bot Training Quiz (Battle Mode)**\n\n"
        "စိန်ခေါ်မှု မေးခွန်း:\n"
        "*Correct the sentence:* 'He go to school every day.'\n\n"
        "သင့်ရဲ့ အဖြေကို ချတ်ဘောက်စ်ထဲမှာ စာသားနဲ့ ရေးပို့ပေးပါ (ဥပမာ - He goes...)။ AI Bot က မှန်/မမှန် ချက်ချင်း စစ်ဆေးပေးပါမယ်!"
    )
    back_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ ပင်မမီနူးသို့ ပြန်ရန်", callback_data="back_home"))
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, quiz_text, reply_markup=back_kb, parse_mode="Markdown")

# Back to Home Callback
@dp.callback_query_handler(lambda c: c.data == 'back_home')
async def back_home(callback_query: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("🥋 Level 1 (🌱 Novice)", callback_data="level_1"),
        InlineKeyboardButton("🌿 Level 2 (🌿 Beginner)", callback_data="level_2"),
        InlineKeyboardButton("🔥 Level 3 (🌿 Inter)", callback_data="level_3"),
        InlineKeyboardButton("🛡️ Level 4 (⚡ Adv)", callback_data="level_4"),
        InlineKeyboardButton("⚡ Level 5 (🌟 Master)", callback_data="level_5"),
        InlineKeyboardButton("👑 Level 6 (🏆 G-Master)", callback_data="level_6"),
        InlineKeyboardButton("📊 My Rank & Leaderboard", callback_data="rank"),
        InlineKeyboardButton("🎯 Training Quiz (AI Battle)", callback_data="quiz")
    )
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "🏯 ပင်မ မီနူးသို့ ပြန်ရောက်ပါပြီ စစ်သည်တော် MOHE။", reply_markup=keyboard)

# Rank Handler
@dp.callback_query_handler(lambda c: c.data == 'rank')
async def show_rank(callback_query: types.CallbackQuery):
    rank_text = "📊 **My Rank & Leaderboard**\n\n• စစ်သည်တော်: MOHE\n• လက်ရှိအဆင့်: Level 1 (Novice)\n• ရရှိထားသော အမှတ်: 120 XP\n• AI Battle 勝率: 85%"
    back_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ ပင်မမီနူးသို့ ပြန်ရန်", callback_data="back_home"))
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, rank_text, reply_markup=back_kb, parse_mode="Markdown")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
