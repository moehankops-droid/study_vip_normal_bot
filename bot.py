import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Your Bot Token
API_TOKEN = '8437112340:AAEgXfvJ07jeBnGCtTsZgG69zHLCDBaOjRI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

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
        InlineKeyboardButton("🎯 AI ကျင့်စဉ်နှင့် တိုက်ရိုက်ယှဉ်ပြိုင်ရန် (Quiz Battle)", callback_data="quiz")
    )
    
    welcome_text = (
        "🏯 မင်္ဂလာပါ စစ်သည်တော် MOHE။\n"
        "အင်္ဂလိပ်စာ ကျင့်စဉ်စာကြည့်တိုက် (Library Mode) မှ ကြိုဆိုပါတယ်။\n\n"
        "လေ့လာလိုသော အပိုင်း (သို့မဟုတ်) ကျင့်စဉ်ကို ရွေးချယ်ပါ!"
    )
    await message.answer(welcome_text, reply_markup=keyboard)

# Callback Handler for Library Sections
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('lib_'))
async def process_library(callback_query: types.CallbackQuery):
    code = callback_query.data.split('_')[1]
    
    details = {
        "1": "📚 **ပိုင်း (၁) - အခြေခံ ဝါကျတည်ဆောက်ခြင်း ကျင့်စဉ်**\n\n• **အဓိက အချက်များ:**\n- S + V (နာမ်/စားနာမ် + ကြိယာ)\n- S + V + O (နာမ်/စားနာမ် + ကြိယာ + ကံ)\n- S + V + C (နာမ်/စားနာမ် + ကြိယာ + ဖြည့်စွက်စာ)\n• **လေ့ကျင့်ရန်:** နေ့စဉ်သုံး ရိုးရှင်းသော ဝါကျများကို ဤပုံစံအတိုင်း အရင်တည်ဆောက်ပါ။",
        "2": "📚 **ပိုင်း (၂) - ပစ္စုပ္ပန်ကာလ ကျင့်စဉ်များ**\n\n• **Simple Present Tense:** Subject + V1 (s/es)\n  - ဥပမာ: I play chess every day. (နေ့စဉ်လုပ်ဆောင်သော အလေ့အထများအတွက်)\n• **Present Continuous Tense:** Subject + is/am/are + V-ing\n  - ဥပမာ: I am studying now. (ယခုလက်ရှိ လုပ်ဆောင်နေဆဲ)",
        "3": "📚 **ပိုင်း (၃) - အတိတ်ကာလ ကျင့်စဉ်များ**\n\n• **Simple Past Tense:** Subject + V2\n  - ဥပမာ: I studied yesterday. (အတိတ်က ပြီးဆုံးသွားသော အလုပ်များ)\n• **Past Continuous Tense:** Subject + was/were + V-ing\n  - ဥပမာ: She was reading when I came. (အတိတ်တွင် တစ်ချိန်တည်း ဖြစ်ပျက်နေဆဲ)",
        "4": "📚 **ပိုင်း (၄) - အနာဂတ်ကာလ ကျင့်စဉ်များ**\n\n• **Simple Future Tense:** Subject + will + V1\n  - ဥပမာ: I will code tomorrow. (နောင်လာမည့် အနာဂတ်တွင် လုပ်မည့်အရာများ)\n• **Future Plan:** အနာဂတ် အစီအစဉ်များကို ပြောဆိုပုံများ။",
        "5": "📚 **ပိုင်း (၅) - အဆင့်မြင့် ဝါကျဆက်စပ်ခြင်း ကျင့်စဉ်**\n\n• **Active & Passive Voice:**\n  - တက်ကြွဝါကျနှင့် ခံ동ါဝကျ ပြောင်းလဲပုံများ။\n• **Relative Clauses:**\n  - Who, Which, That စသည့် ဆက်စပ်စာလုံးများ သုံး၍ ဝါကျရှည်များ တည်ဆောက်ခြင်း။",
        "6": "📚 **ပိုင်း (၆) - အလုံးစုံ စစ်ဆေးသည့် နောက်ဆုံးကျင့်စဉ်**\n\n• **စုံလင်သော စာမေးပွဲပုံစံ:** သင်ယူခဲ့သမျှ အခြေခံနှင့် အဆင့်မြင့် ကျင့်စဉ်များကို ပေါင်းစပ်ကာ ကိုယ်ပိုင် အက်ဆေးနှင့် ဝါကျပြင်ဆင်မှုများ ပြုလုပ်ရန် အဆင့်။"
    }
    
    text = details.get(code, "ကျင့်စဉ် အချက်အလက်များ...")
    
    back_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ ပင်မစာကြည့်တိုက်သို့ ပြန်ရန်", callback_data="back_home"))
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text, reply_markup=back_kb, parse_mode="Markdown")

# AI Training Quiz Battle Mode
@dp.callback_query_handler(lambda c: c.data == 'quiz')
async def start_ai_quiz(callback_query: types.CallbackQuery):
    quiz_text = (
        "🤖 **AI ကျင့်စဉ်နှင့် တိုက်ရိုက်ယှဉ်ပြိုင်ရန် (Quiz Battle)**\n\n"
        "စိန်ခေါ်မှု မေးခွန်း:\n"
        "*Correct the sentence:* 'He go to school every day.'\n\n"
        "သင့်ရဲ့ အဖြေကို ချတ်ဘောက်စ်ထဲမှာ စာသားနဲ့ ရေးပို့ပေးပါ (ဥပမာ - He goes...)။ AI Bot က မှန်/မမှန် ချက်ချင်း စစ်ဆေးပေးပါမယ်!"
    )
    back_kb = InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ ပင်မစာကြည့်တိုက်သို့ ပြန်ရန်", callback_data="back_home"))
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, quiz_text, reply_markup=back_kb, parse_mode="Markdown")

# Message handler for Quiz Answer checking
@dp.message_handler(lambda message: message.text and "ဖရိန်" not in message.text)
async def check_quiz_answer(message: types.Message):
    user_answer = message.text.strip().lower()
    if "goes" in user_answer or "correct" in user_answer or "မှန်" in user_answer:
        reply_text = (
            "✨ **တိုက်ခိုက်မှု အောင်မြင်သည်! အမှတ် +50 ရရှိပါသည်။**\n"
            "စုစုပေါင်းအမှတ်: 150 pts\n"
            "အဆင့်: အခြေခံ ကျင့်စဉ် အောင်မြင်သူ"
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
        InlineKeyboardButton("🎯 AI ကျင့်စဉ်နှင့် တိုက်ရိုက်ယှဉ်ပြိုင်ရန် (Quiz Battle)", callback_data="quiz")
    )
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "🏯 ပင်မ စာကြည့်တိုက်သို့ ပြန်ရောက်ပါပြီ စစ်သည်တော် MOHE။", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
