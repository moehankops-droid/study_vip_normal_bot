import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '8437112340:AAEgXfvJ07jeBnGCtTsZgG69zHLCDBaOjRI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Store simple user state to track if user is playing quiz
USER_QUIZ_STATE = {}

QUIZ_POOL = [
    {"q": "Correct: 'He go to school every day.'", "ans": ["goes"], "hint": "Subject က He ဖြစ်၍ V1 မှာ s/es ထည့်ပါ။"},
    {"q": "Correct: 'They plays football.'", "ans": ["play"], "hint": "Subject က plural ဖြစ်၍ V1 သာသုံးပါ။"},
    {"q": "Fill: 'She ___ English yesterday.' (study)", "ans": ["studied"], "hint": "Past tense (V2) သုံးပါ။"},
    {"q": "Fill: 'I ___ a letter now.' (write)", "ans": ["am writing"], "hint": "Present continuous သုံးပါ။"},
    {"q": "Correct: 'She will goes tomorrow.'", "ans": ["go"], "hint": "will နောက်တွင် V1 သာလိုက်ရပါမည်။"}
]

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    USER_QUIZ_STATE.pop(message.from_user.id, None)
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("🌱 အဆင့် (၁) - အခြေခံ အုတ်မြစ် ကျင့်စဉ်များ (အပိုင်း ၁-၈)", callback_data="tier_1"),
        InlineKeyboardButton("🌿 အဆင့် (၂) - တိုက်ခိုက်ရေး ကာလများ (အပိုင်း ၉-၁၇)", callback_data="tier_2"),
        InlineKeyboardButton("🔥 အဆင့် (၃) - အဆင့်မြင့် သိုင်းကွက်များ (အပိုင်း ၁၈-၂၅)", callback_data="tier_3"),
        InlineKeyboardButton("👑 အဆင့် (၄) - ဂရင်းမာစတာ စိန်ခေါ်ပွဲ (အပိုင်း ၂၆-၃၀)", callback_data="tier_4"),
        InlineKeyboardButton("📊 စစ်သည်တော် Profile & Rank", callback_data="profile"),
        InlineKeyboardButton("🎯 AI Quiz Battle (တိုက်ရိုက်ယှဉ်ပြိုင်ရန်)", callback_data="quiz_start")
    )
    
    welcome_text = (
        "🏯 မင်္ဂလာပါ စစ်သည်တော် MOHE။\n"
        "အင်္ဂလိပ်စာ ကျင့်စဉ်စာကြည့်တိုက်မှ ကြိုဆိုပါတယ်။\n\n"
        "လေ့လာလိုသော အဆင့်အလိုက် ကဏ္ဍကို ရွေးချယ်ပါ!"
    )
    await message.answer(welcome_text, reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'tier_1')
async def show_tier_1(callback_query: types.CallbackQuery):
    await callback_query.answer()
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("အပိုင်း (၁) - အက္ခရာ", callback_data="lib_1"),
        InlineKeyboardButton("အပိုင်း (၂) - နာမ်", callback_data="lib_2"),
        InlineKeyboardButton("အပိုင်း (၃) - စားနာမ်", callback_data="lib_3"),
        InlineKeyboardButton("အပိုင်း (၄) - ကြိယာ", callback_data="lib_4"),
        InlineKeyboardButton("အပိုင်း (၅) - ဝိဘတ်", callback_data="lib_5"),
        InlineKeyboardButton("အပိုင်း (၆) - အထူးပြု", callback_data="lib_6"),
        InlineKeyboardButton("အပိုင်း (၇) - ကြိယာဝိဘတ်", callback_data="lib_7"),
        InlineKeyboardButton("အပိုင်း (၈) - ဝါကျဆက်", callback_data="lib_8"),
        InlineKeyboardButton("⬅️ ပင်မမီနူးသို့", callback_data="back_home")
    )
    await bot.send_message(callback_query.from_user.id, "🌱 **အဆင့် (၁) - အခြေခံ အုတ်မြစ် ကျင့်စဉ်များ**", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'tier_2')
async def show_tier_2(callback_query: types.CallbackQuery):
    await callback_query.answer()
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("အပိုင်း (၉) - S+V+O", callback_data="lib_9"),
        InlineKeyboardButton("အပိုင်း (၁၀) - Simple Pres", callback_data="lib_10"),
        InlineKeyboardButton("အပိုင်း (၁၁) - Pres Cont", callback_data="lib_11"),
        InlineKeyboardButton("အပိုင်း (၁၂) - Pres Perf", callback_data="lib_12"),
        InlineKeyboardButton("အပိုင်း (၁၃) - Simple Past", callback_data="lib_13"),
        InlineKeyboardButton("အပိုင်း (၁၄) - Past Cont", callback_data="lib_14"),
        InlineKeyboardButton("အပိုင်း (၁၅) - Past Perf", callback_data="lib_15"),
        InlineKeyboardButton("အပိုင်း (၁၆) - Simple Fut", callback_data="lib_16"),
        InlineKeyboardButton("အပိုင်း (၁၇) - Fut Cont", callback_data="lib_17"),
        InlineKeyboardButton("⬅️ ပင်မမီနူးသို့", callback_data="back_home")
    )
    await bot.send_message(callback_query.from_user.id, "🌿 **အဆင့် (၂) - တိုက်ခိုက်ရေး ကာလများ**", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'tier_3')
async def show_tier_3(callback_query: types.CallbackQuery):
    await callback_query.answer()
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("အပိုင်း (၁၈) - Active/Pass 1", callback_data="lib_18"),
        InlineKeyboardButton("အပိုင်း (၁၉) - Active/Pass 2", callback_data="lib_19"),
        InlineKeyboardButton("အပိုင်း (၂၀) - Direct Speech", callback_data="lib_20"),
        InlineKeyboardButton("အပိုင်း (၂၁) - Relative Clause", callback_data="lib_21"),
        InlineKeyboardButton("အပိုင်း (၂၂) - Conditionals", callback_data="lib_22"),
        InlineKeyboardButton("အပိုင်း (၂၃) - Question Tags", callback_data="lib_23"),
        InlineKeyboardButton("အပိုင်း (၂၄) - Comparison", callback_data="lib_24"),
        InlineKeyboardButton("အပိုင်း (၂၅) - Modal Verbs", callback_data="lib_25"),
        InlineKeyboardButton("⬅️ ပင်မမီနူးသို့", callback_data="back_home")
    )
    await bot.send_message(callback_query.from_user.id, "🔥 **အဆင့် (၃) - အဆင့်မြင့် သိုင်းကွက်များ**", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'tier_4')
async def show_tier_4(callback_query: types.CallbackQuery):
    await callback_query.answer()
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("အပိုင်း (၂၆) - Gerunds", callback_data="lib_26"),
        InlineKeyboardButton("အပိုင်း (၂၇) - Vocabulary", callback_data="lib_27"),
        InlineKeyboardButton("အပိုင်း (၂၈) - Essay Patterns", callback_data="lib_28"),
        InlineKeyboardButton("အပိုင်း (၂၉) - Paragraph", callback_data="lib_29"),
        InlineKeyboardButton("အပိုင်း (၃၀) - Final Exam", callback_data="lib_30"),
        InlineKeyboardButton("⬅️ ပင်မမီနူးသို့", callback_data="back_home")
    )
    await bot.send_message(callback_query.from_user.id, "👑 **အဆင့် (၄) - ဂရင်းမာစတာ စိန်ခေါ်ပွဲ**", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('lib_'))
async def process_library(callback_query: types.CallbackQuery):
    await callback_query.answer()
    code = callback_query.data.split('_')[1]
    text = f"📚 **ကျင့်စဉ် အပိုင်း ({code})**\n\n• ဤကျင့်စဉ်တွင် သက်ဆိုင်ရာ လေ့လာရန်အချက်များနှင့် အစွမ်းထက် တိုက်ကွက်များ ပါဝင်ပါသည်။"
    
    action_kb = InlineKeyboardMarkup(row_width=2)
    action_kb.add(
        InlineKeyboardButton("🎯 AI Quiz ဆက်ဖြေမည်", callback_data="quiz_start"),
        InlineKeyboardButton("⬅️ ပင်မမီနူးသို့", callback_data="back_home")
    )
    await bot.send_message(callback_query.from_user.id, text, reply_markup=action_kb, parse_mode="Markdown")

@dp.callback_query_handler(lambda c: c.data == 'profile')
async def show_profile(callback_query: types.CallbackQuery):
    await callback_query.answer()
    profile_text = (
        "📊 **စစ်သည်တော် Profile & Rank**\n\n"
        "• အမည်: MOHE\n"
        "• လက်ရှိအဆင့်: 👑 အဆင့်မြင့် ဂရင်းမာစတာ လေ့လာသူ\n"
        "• ရရှိထားသော အမှတ်: 350 XP\n"
        "• AI Battle အနိုင်ရနှုန်း: 95%"
    )
    back_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ ပင်မမီနူးသို့ ပြန်ရန်", callback_data="back_home"))
    await bot.send_message(callback_query.from_user.id, profile_text, reply_markup=back_kb, parse_mode="Markdown")

@dp.callback_query_handler(lambda c: c.data == 'quiz_start')
async def start_ai_quiz(callback_query: types.CallbackQuery):
    await callback_query.answer()
    user_id = callback_query.from_user.id
    USER_QUIZ_STATE[user_id] = True  # Mark user as active in quiz mode
    
    current_q = random.choice(QUIZ_POOL)
    quiz_text = (
        "🤖 **AI ကျင့်စဉ်နှင့် တိုက်ရိုက်ယှဉ်ပြိုင်ရန် (Quiz Battle)**\n\n"
        f"⚔️ **စိန်ခေါ်မှု မေးခွန်း:**\n{current_q['q']}\n\n"
        "💡 *အရိပ်အမြွက်:* သင့်ရဲ့ အဖြေကို ချတ်ဘောက်စ်ထဲမှာ တိုက်ရိုက် ရေးပို့ပေးပါ!"
    )
    back_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ ပင်မမီနူးသို့ ပြန်ရန်", callback_data="back_home"))
    await bot.send_message(callback_query.from_user.id, quiz_text, reply_markup=back_kb, parse_mode="Markdown")

@dp.message_handler(lambda message: message.text and not message.text.startswith('/'))
async def check_quiz_answer(message: types.Message):
    user_id = message.from_user.id
    
    # Check if user actually initiated a quiz battle
    if USER_QUIZ_STATE.get(user_id):
        user_answer = message.text.strip().lower()
        is_correct = any(ans in user_answer for ans in ["goes", "play", "studied", "correct", "မှန်", "go", "am writing"])
        
        if is_correct:
            reply_text = "✨ **တိုက်ခိုက်မှု အောင်မြင်သည်! AI Bot ကို အနိုင်ယူလိုက်ပြီ 🔥 (+50 XP)**\n\nထပ်မံယှဉ်ပြိုင်ရန် /start ကို နှိပ်ပါ သို့မဟုတ် မီနူးသို့ သွားပါ။"
        else:
            reply_text = "❌ **တိုက်ခိုက်မှု လွဲချော်သွားသည်! AI Bot က တိုက်ခိုက်လိုက်သည် 🛡️**\n\nထပ်မံကြိုးစားကြည့်ပါဦး သူငယ်ချင်း။"
        
        USER_QUIZ_STATE.pop(user_id, None)
        await message.answer(reply_text, parse_mode="Markdown")

@dp.callback_query_handler(lambda c: c.data == 'back_home')
async def back_home(callback_query: types.CallbackQuery):
    await callback_query.answer()
    USER_QUIZ_STATE.pop(callback_query.from_user.id, None)
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("🌱 အဆင့် (၁) - အခြေခံ အုတ်မြစ် ကျင့်စဉ်များ (အပိုင်း ၁-၈)", callback_data="tier_1"),
        InlineKeyboardButton("🌿 အဆင့် (၂) - တိုက်ခိုက်ရေး ကာလများ (အပိုင်း ၉-၁၇)", callback_data="tier_2"),
        InlineKeyboardButton("🔥 အဆင့် (၃) - အဆင့်မြင့် သိုင်းကွက်များ (အပိုင်း ၁၈-၂၅)", callback_data="tier_3"),
        InlineKeyboardButton("👑 အဆင့် (၄) - ဂရင်းမာစတာ စိန်ခေါ်ပွဲ (အပိုင်း ၂၆-၃၀)", callback_data="tier_4"),
        InlineKeyboardButton("📊 စစ်သည်တော် Profile & Rank", callback_data="profile"),
        InlineKeyboardButton("🎯 AI Quiz Battle (တိုက်ရိုက်ယှဉ်ပြိုင်ရန်)", callback_data="quiz_start")
    )
    await bot.send_message(callback_query.from_user.id, "🏯 ပင်မ မီနူးသို့ ပြန်ရောက်ပါပြီ စစ်သည်တော် MOHE။", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
