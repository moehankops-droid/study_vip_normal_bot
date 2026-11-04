import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Your Bot Token
API_TOKEN = '8437112340:AAEgXfvJ07jeBnGCtTsZgG69zHLCDBaOjRI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# AI Quiz pool to prevent repeating questions
QUIZ_POOL = [
    {
        "q": "Correct the sentence: 'He go to school every day.'",
        "ans": ["he goes to school every day", "goes"],
        "hint": "Simple Present Tense တွင် Subject က He ဖြစ်ပါက Verb မှာ s/es ထည့်ရပါမည်။"
    },
    {
        "q": "Correct the sentence: 'They plays football on Sundays.'",
        "ans": ["they play football on sundays", "play"],
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
        "hint": "now ပါရှိသောကြောင့် Present Continuous Tense (is/am/are + V-ing) ကို သုံးပါ။"
    },
    {
        "q": "Correct the sentence: 'She will goes to Yangon tomorrow.'",
        "ans": ["she will go to yangon tomorrow", "go"],
        "hint": "will နောက်တွင် Verb ၏ မူလရင်းမြစ် (V1) သာ လိုက်ရပါမည်။"
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
        InlineKeyboardButton("🎯 AI ကျင့်စဉ်နှင့် တိုက်ရိုက်ယှဉ်ပြိုင်ရန် (Quiz Battle)", callback_data="quiz_start")
    )
    
    welcome_text = (
        "🏯 မင်္ဂလာပါ စစ်သည်တော် MOHE။\n"
        "အင်္ဂလိပ်စာ ကျင့်စဉ်စာကြည့်တိုက် (Library Mode) မှ ကြိုဆိုပါတယ်။\n\n"
        "လေ့လာလိုသော အပိုင်း (သို့မဟုတ်) ကျင့်စဉ်ကို ရွေးချယ်ပါ!"
    )
    await message.answer(welcome_text, reply_markup=keyboard)

# Callback Handler for Library Sections (with practice buttons below)
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('lib_'))
async def process_library(callback_query: types.CallbackQuery):
    code = callback_query.data.split('_')[1]
    
    details = {
        "1": "📚 **အပိုင်း (၁) - အခြေခံ ဝါကျတည်ဆောက်ခြင်း ကျင့်စဉ်**\n\n• **အဓိက အချက်များ:**\n- S + V (နာမ်/စားနာမ် + ကြိယာ)\n- S + V + O (နာမ်/စားနာမ် + ကြိယာ + ကံ)\n- S + V + C (နာမ်/စားနာမ် + ကြိယာ + ဖြည့်စွက်စာ)\n• **လေ့ကျင့်ရန်:** နေ့စဉ်သုံး ရိုးရှင်းသော ဝါကျများကို ဤပုံစံအတိုင်း အရင်တည်ဆောက်ပါ။",
        "2": "📚 **အပိုင်း (၂) - ပစ္စုပ္ပန်ကာလ ကျင့်စဉ်များ**\n\n• **Simple Present Tense:** Subject + V1 (s/es)\n  - ဥပမာ: I play chess every day.\n• **Present Continuous Tense:** Subject + is/am/are + V-ing\n  - ဥပမာ: I am studying now.",
        "3": "📚 **အပိုင်း (၃) - အတိတ်ကာလ ကျင့်စဉ်များ**\n\n• **Simple Past Tense:** Subject + V2\n  - ဥပမာ: I studied yesterday.\n• **Past Continuous Tense:** Subject + was/were + V-ing\n  - ဥပမာ: She was reading when I came.",
        "4": "📚 **အပိုင်း (၄) - အနာဂတ်ကာလ ကျင့်စဉ်များ**\n\n• **Simple Future Tense:** Subject + will + V1\n  - ဥပမာ: I will code tomorrow.",
        "5": "📚 **အပိုင်း (၅) - အဆင့်မြင့် ဝါကျဆက်စပ်ခြင်း ကျင့်စဉ်**\n\n• **Active & Passive Voice**\n• **Relative Clauses (Who, Which, That)**",
        "6": "📚 **အပိုင်း (၆) - အလုံးစုံ စစ်ဆေးသည့် နောက်ဆုံးကျင့်စဉ်**\n• သင်ယူခဲ့သမျှ အားလုံးကို ပြန်လည်စစ်ဆေးသည့် အဆင့်။"
    }
    
    text = details.get(code, "ကျင့်စဉ် အချက်အလက်များ...")
    
    # Adding interactive buttons below the text so user can practice or go back
    action_kb = InlineKeyboardMarkup(row_width=1)
    action_kb.add(
        InlineKeyboardButton("🎯 ဤအပိုင်းအတွက် AI Quiz ဆက်ဖြေမည်", callback_data="quiz_start"),
        InlineKeyboardButton("⬅️ ပင်မစာကြည့်တိုက်သို့ ပြန်ရန်", callback_data="back_home")
    )
    
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text, reply_markup=action_kb, parse_mode="Markdown")

# AI Training Quiz Battle Mode Start
@dp.callback_query_handler(lambda c: c.data == 'quiz_start')
async def start_ai_quiz(callback_query: types.CallbackQuery):
    # Pick a random question so it doesn't repeat easily
    current_q = random.choice(QUIZ_POOL)
    
    quiz_text = (
        "🤖 **AI ကျင့်စဉ်နှင့် တိုက်ရိုက်ယှဉ်ပြိုင်ရန် (Quiz Battle)**\n\n"
        f"⚔️ **စိန်ခေါ်မှု မေးခွန်း:**\n{current_q['q']}\n\n"
        "💡 *အရိပ်အမြွက်:* သင့်ရဲ့ အဖြေကို ချတ်ဘောက်စ်ထဲမှာ တိုက်ရိုက် ရေးပို့ပေးပါ (ဥပမာ - မှန်ကန်သော စာသား သို့မဟုတ် စကားလုံး)။ AI Bot က တိုက်ခိုက်မှုကို စစ်ဆေးပေးပါမယ်!"
    )
    back_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ ပင်မစာကြည့်တိုက်သို့ ပြန်ရန်", callback_data="back_home"))
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, quiz_text, reply_markup=back_kb, parse_mode="Markdown")

# Message handler for Quiz Answer checking against AI
@dp.message_handler(lambda message: message.text and not message.text.startswith('/'))
async def check_quiz_answer(message: types.Message):
    user_answer = message.text.strip().lower()
    
    # Check if user answer matches any condition
    is_correct = any(ans in user_answer for ans in ["goes", "play", "studied", "am writing", "go", "correct", "မှန်"])
    
    if is_correct:
        reply_text = (
            "✨ **တိုက်ခိုက်မှု အောင်မြင်သည်! AI Bot ကို အနိုင်ယူလိုက်ပြီ 🔥**\n"
            "• ရရှိသော အမှတ်: +50 XP\n"
            "• စုစုပေါင်းအမှတ်: 200 pts\n\n"
            "ဆက်လက်တိုက်ခိုက်ရန် သို့မဟုတ် အခြားလေ့ကျင့်ခန်းသို့ သွားရန် /start ကို နှိပ်ပါ။"
        )
    else:
        reply_text = (
            "❌ **တိုက်ခိုက်မှု လွဲချော်သွားသည်! AI Bot က တိုက်ခိုက်လိုက်သည် 🛡️**\n"
            "သင်၏အဖြေမှာ အနည်းငယ် မှားယွင်းနေပါသည်။ စာလုံးပေါင်း သို့မဟုတ် Tense ကို သေချာာ ပြန်စစ်ကြည့်ပါဦး သူငယ်ချင်း။"
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
        InlineKeyboardButton("🎯 AI ကျင့်စဉ်နှင့် တိုက်ရိုက်ယှဉ်ပြိုင်ရန် (Quiz Battle)", callback_data="quiz_start")
    )
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "🏯 ပင်မ စာကြည့်တိုက်သို့ ပြန်ရောက်ပါပြီ စစ်သည်တော် MOHE။", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
