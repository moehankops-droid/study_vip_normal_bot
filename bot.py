import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Your Bot Token
API_TOKEN = '8437112340:AAEgXfvJ07jeBnGCtTsZgG69zHLCDBaOjRI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

QUIZ_POOL = [
    {"q": "Correct: 'He go to school every day.'", "ans": ["goes"], "hint": "Subject က He ဖြစ်၍ V1 မှာ s/es ထည့်ပါ။"},
    {"q": "Correct: 'They plays football.'", "ans": ["play"], "hint": "Subject က plural ဖြစ်၍ V1 သာသုံးပါ။"},
    {"q": "Fill: 'She ___ English yesterday.' (study)", "ans": ["studied"], "hint": "Past tense (V2) သုံးပါ။"},
    {"q": "Fill: 'I ___ a letter now.' (write)", "ans": ["am writing"], "hint": "Present continuous သုံးပါ။"},
    {"q": "Correct: 'She will goes tomorrow.'", "ans": ["go"], "hint": "will နောက်တွင် V1 သာလိုက်ရပါမည်။"}
]

# Start Command & Main Menu (Tiered Library Grid Layout)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        # Tier 1: Novice
        InlineKeyboardButton("🌱 အပိုင်း (၁) - အက္ခရာနှင့် အသံထွက်", callback_data="lib_1"),
        InlineKeyboardButton("🌱 အပိုင်း (၂) - နာမ် (Nouns) ကျင့်စဉ်", callback_data="lib_2"),
        InlineKeyboardButton("🌱 အပိုင်း (၃) - စားနာမ် (Pronouns)", callback_data="lib_3"),
        InlineKeyboardButton("🌱 အပိုင်း (၄) - ကြိယာ (Verbs) အခြေခံ", callback_data="lib_4"),
        InlineKeyboardButton("🌱 အပိုင်း (၅) - ဝိဘတ် (Prepositions)", callback_data="lib_5"),
        InlineKeyboardButton("🌱 အပိုင်း (၆) - အထူးပြုစကားလုံး (Adjectives)", callback_data="lib_6"),
        InlineKeyboardButton("🌱 အပိုင်း (၇) - ကြိယာဝိဘတ် (Adverbs)", callback_data="lib_7"),
        InlineKeyboardButton("🌱 အပိုင်း (၈) - ဝါကျဆက် (Conjunctions)", callback_data="lib_8"),
        
        # Tier 2: Intermediate
        InlineKeyboardButton("🌿 အပိုင်း (၉) - S + V + O တည်ဆောက်ကွက်", callback_data="lib_9"),
        InlineKeyboardButton("🌿 အပိုင်း (၁၀) - Simple Present Tense", callback_data="lib_10"),
        InlineKeyboardButton("🌿 အပိုင်း (၁၁) - Present Continuous", callback_data="lib_11"),
        InlineKeyboardButton("🌿 အပိုင်း (၁၂) - Present Perfect", callback_data="lib_12"),
        InlineKeyboardButton("🌿 အပိုင်း (၁၃) - Simple Past Tense", callback_data="lib_13"),
        InlineKeyboardButton("🌿 အပိုင်း (၁၄) - Past Continuous", callback_data="lib_14"),
        InlineKeyboardButton("🌿 အပိုင်း (၁၅) - Past Perfect", callback_data="lib_15"),
        InlineKeyboardButton("🌿 အပိုင်း (၁၆) - Simple Future Tense", callback_data="lib_16"),
        InlineKeyboardButton("🌿 အပိုင်း (၁၇) - Future Continuous", callback_data="lib_17"),
        
        # Tier 3: Advanced
        InlineKeyboardButton("🔥 အပိုင်း (၁၈) - Active & Passive (၁)", callback_data="lib_18"),
        InlineKeyboardButton("🔥 အပိုင်း (၁၉) - Active & Passive (၂)", callback_data="lib_19"),
        InlineKeyboardButton("🔥 အပိုင်း (၂၀) - Direct & Indirect Speech", callback_data="lib_20"),
        InlineKeyboardButton("🔥 အပိုင်း (၂၁) - Relative Clauses", callback_data="lib_21"),
        InlineKeyboardButton("🔥 အပိုင်း (၂၂) - Conditionals (If-clauses)", callback_data="lib_22"),
        InlineKeyboardButton("🔥 အပိုင်း (၂၃) - Question Tags", callback_data="lib_23"),
        InlineKeyboardButton("🔥 အပိုင်း (၂၄) - Degrees of Comparison", callback_data="lib_24"),
        InlineKeyboardButton("🔥 အပိုင်း (၂၅) - Modal Verbs", callback_data="lib_25"),
        
        # Tier 4: Grand Master
        InlineKeyboardButton("👑 အပိုင်း (၂၆) - Gerunds & Infinitives", callback_data="lib_26"),
        InlineKeyboardButton("👑 အပိုင်း (၂၇) - Vocabulary & Synonyms", callback_data="lib_27"),
        InlineKeyboardButton("👑 အပိုင်း (၂၈) - Essay Writing Patterns", callback_data="lib_28"),
        InlineKeyboardButton("👑 အပိုင်း (၂၉) - Paragraph Construction", callback_data="lib_29"),
        InlineKeyboardButton("👑 အပိုင်း (၃၀) - Grand Master Final Exam", callback_data="lib_30"),
        
        # Utilities
        InlineKeyboardButton("📊 Profile & Rank", callback_data="profile"),
        InlineKeyboardButton("🎯 AI Quiz Battle", callback_data="quiz_start")
    )
    
    welcome_text = (
        "🏯 မင်္ဂလာပါ စစ်သည်တော် MOHE။\n"
        "အင်္ဂလိပ်စာ ကျင့်စဉ်စာကြည့်တိုက် (Tiered Library 30+ Modules) မှ ကြိုဆိုပါတယ်။\n\n"
        "🌱 အခြေခံမှ 👑 အဆင့်မြင့် ဂရင်းမာစတာအထိ လေ့လာလိုသော ကျင့်စဉ်များကို ရွေးချယ်ပါ!"
    )
    await message.answer(welcome_text, reply_markup=keyboard)

# Callback Handler for Library Sections
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('lib_'))
async def process_library(callback_query: types.CallbackQuery):
    code = callback_query.data.split('_')[1]
    num = int(code)
    
    # Define tier names based on module number
    if num <= 8:
        tier = "🌱 အဆင့် (၁) - အခြေခံ အုတ်မြစ်"
    elif num <= 17:
        tier = "🌿 အဆင့် (၂) - တိုက်ခိုက်ရေး ကာလများ"
    elif num <= 25:
        tier = "🔥 အဆင့် (၃) - အဆင့်မြင့် သိုင်းကွက်များ"
    else:
        tier = "👑 အဆင့် (၄) - ဂရင်းမာစတာ စိန်ခေါ်ပွဲ"
        
    text = (
        f"📚 **ကျင့်စဉ် အပိုင်း ({code})**\n"
        f"• **အဆင့်သတ်မှတ်ချက်:** {tier}\n\n"
        "• ဤကျင့်စဉ်တွင် သက်ဆိုင်ရာ လေ့လာရန်အချက်များနှင့် အစွမ်းထက် တိုက်ကွက်များ ပါဝင်ပါသည်။ တိုက်ရိုက် လေ့ကျင့်ရန် အောက်ပါ ခလုတ်ကို နှိပ်ပါ။"
    )
    
    action_kb = InlineKeyboardMarkup(row_width=2)
    action_kb.add(
        InlineKeyboardButton("🎯 AI Quiz ဆက်ဖြေမည်", callback_data="quiz_start"),
        InlineKeyboardButton("⬅️ ပင်မမီနူးသို့", callback_data="back_home")
    )
    
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text, reply_markup=action_kb, parse_mode="Markdown")

# Profile / Rank Handler
@dp.callback_query_handler(lambda c: c.data == 'profile')
async def show_profile(callback_query: types.CallbackQuery):
    profile_text = (
        "📊 **စစ်သည်တော် Profile & Rank**\n\n"
        "• အမည်: MOHE\n"
        "• လက်ရှိအဆင့်: 👑 အဆင့်မြင့် ဂရင်းမာစတာ လေ့လာသူ\n"
        "• ရရှိထားသော အမှတ်: 350 XP\n"
        "• AI Battle အနိုင်ရနှုန်း: 95%"
    )
    back_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ ပင်မမီနူးသို့ ပြန်ရန်", callback_data="back_home"))
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, profile_text, reply_markup=back_kb, parse_mode="Markdown")

# AI Training Quiz Battle Mode Start
@dp.callback_query_handler(lambda c: c.data == 'quiz_start')
async def start_ai_quiz(callback_query: types.CallbackQuery):
    current_q = random.choice(QUIZ_POOL)
    quiz_text = (
        "🤖 **AI ကျင့်စဉ်နှင့် တိုက်ရိုက်ယှဉ်ပြိုင်ရန် (Quiz Battle)**\n\n"
        f"⚔️ **စိန်ခေါ်မှု မေးခွန်း:**\n{current_q['q']}\n\n"
        "💡 *အရိပ်အမြွက်:* သင့်ရဲ့ အဖြေကို ချတ်ဘောက်စ်ထဲမှာ တိုက်ရိုက် ရေးပို့ပေးပါ!"
    )
    back_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ ပင်မမီနူးသို့ ပြန်ရန်", callback_data="back_home"))
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, quiz_text, reply_markup=back_kb, parse_mode="Markdown")

# Message handler for Quiz Answer checking against AI
@dp.message_handler(lambda message: message.text and not message.text.startswith('/'))
async def check_quiz_answer(message: types.Message):
    user_answer = message.text.strip().lower()
    is_correct = any(ans in user_answer for ans in ["goes", "play", "studied", "correct", "မှန်", "go"])
    
    if is_correct:
        reply_text = "✨ **တိုက်ခိုက်မှု အောင်မြင်သည်! AI Bot ကို အနိုင်ယူလိုက်ပြီ 🔥 (+50 XP)**"
    else:
        reply_text = "❌ **တိုက်ခိုက်မှု လွဲချော်သွားသည်! AI Bot က တိုက်ခိုက်လိုက်သည် 🛡️**"
    
    await message.answer(reply_text, parse_mode="Markdown")

# Back to Home Callback
@dp.callback_query_handler(lambda c: c.data == 'back_home')
async def back_home(callback_query: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("🌱 အပိုင်း (၁) - အက္ခရာနှင့် အသံထွက်", callback_data="lib_1"),
        InlineKeyboardButton("🌱 အပိုင်း (၂) - နာမ် (Nouns) ကျင့်စဉ်", callback_data="lib_2"),
        InlineKeyboardButton("🌱 အပိုင်း (၃) - စားနာမ် (Pronouns)", callback_data="lib_3"),
        InlineKeyboardButton("🌱 အပိုင်း (၄) - ကြိယာ (Verbs) အခြေခံ", callback_data="lib_4"),
        InlineKeyboardButton("🌱 အပိုင်း (၅) - ဝိဘတ် (Prepositions)", callback_data="lib_5"),
        InlineKeyboardButton("🌱 အပိုင်း (၆) - အထူးပြုစကားလုံး (Adjectives)", callback_data="lib_6"),
        InlineKeyboardButton("🌱 အပိုင်း (၇) - ကြိယာဝိဘတ် (Adverbs)", callback_data="lib_7"),
        InlineKeyboardButton("🌱 အပိုင်း (၈) - ဝါကျဆက် (Conjunctions)", callback_data="lib_8"),
        InlineKeyboardButton("🌿 အပိုင်း (၉) - S + V + O တည်ဆောက်ကွက်", callback_data="lib_9"),
        InlineKeyboardButton("🌿 အပိုင်း (၁၀) - Simple Present Tense", callback_data="lib_10"),
        InlineKeyboardButton("🌿 အပိုင်း (၁၁) - Present Continuous", callback_data="lib_11"),
        InlineKeyboardButton("🌿 အပိုင်း (၁၂) - Present Perfect", callback_data="lib_12"),
        InlineKeyboardButton("🌿 အပိုင်း (၁၃) - Simple Past Tense", callback_data="lib_13"),
        InlineKeyboardButton("🌿 အပိုင်း (၁၄) - Past Continuous", callback_data="lib_14"),
        InlineKeyboardButton("🌿 အပိုင်း (၁၅) - Past Perfect", callback_data="lib_15"),
        InlineKeyboardButton("🌿 အပိုင်း (၁၆) - Simple Future Tense", callback_data="lib_16"),
        InlineKeyboardButton("🌿 အပိုင်း (၁၇) - Future Continuous", callback_data="lib_17"),
        InlineKeyboardButton("🔥 အပိုင်း (၁၈) - Active & Passive (၁)", callback_data="lib_18"),
        InlineKeyboardButton("🔥 အပိုင်း (၁၉) - Active & Passive (၂)", callback_data="lib_19"),
        InlineKeyboardButton("🔥 အပိုင်း (၂၀) - Direct & Indirect Speech", callback_data="lib_20"),
        InlineKeyboardButton("🔥 အပိုင်း (၂၁) - Relative Clauses", callback_data="lib_21"),
        InlineKeyboardButton("🔥 အပိုင်း (၂၂) - Conditionals (If-clauses)", callback_data="lib_22"),
        InlineKeyboardButton("🔥 အပိုင်း (၂၃) - Question Tags", callback_data="lib_23"),
        InlineKeyboardButton("🔥 အပိုင်း (၂၄) - Degrees of Comparison", callback_data="lib_25"),
        InlineKeyboardButton("🔥 အပိုင်း (၂၅) - Modal Verbs", callback_data="lib_25"),
        InlineKeyboardButton("👑 အပိုင်း (၂၆) - Gerunds & Infinitives", callback_data="lib_26"),
        InlineKeyboardButton("👑 အပိုင်း (၂၇) - Vocabulary & Synonyms", callback_data="lib_27"),
        InlineKeyboardButton("👑 အပိုင်း (၂၈) - Essay Writing Patterns", callback_data="lib_28"),
        InlineKeyboardButton("👑 အပိုင်း (၂၉) - Paragraph Construction", callback_data="lib_29"),
        InlineKeyboardButton("👑 အပိုင်း (၃၀) - Grand Master Final Exam", callback_data="lib_30"),
        InlineKeyboardButton("📊 Profile & Rank", callback_data="profile"),
        InlineKeyboardButton("🎯 AI Quiz Battle", callback_data="quiz_start")
    )
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "🏯 ပင်မ မီနူးသို့ ပြန်ရောက်ပါပြီ စစ်သည်တော် MOHE။", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

