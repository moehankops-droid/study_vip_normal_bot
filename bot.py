from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

API_TOKEN = '8437112340:AAEV-a5qzKjtC-N2_KLacw8oizi-SLQ1yJI'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# ၁။ ပင်မ မီနူးခလုတ်များ (Grid Menu)
def get_study_menu():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("🎯 SMART Goals", callback_data="lesson_smart"),
        InlineKeyboardButton("🙏 ကျေးဇူးတင်စကားများ", callback_data="lesson_thanks")
    )
    keyboard.add(
        InlineKeyboardButton("🙇 တောင်းပန်စကားများ", callback_data="lesson_sorry"),
        InlineKeyboardButton("✍️ Writing & To-do", callback_data="lesson_writing")
    )
    keyboard.add(
        InlineKeyboardButton("🌱 ပထမအခြေခံ English", callback_data="lesson_basic"),
        InlineKeyboardButton("🌟 Future Tense", callback_data="lesson_future")
    )
    keyboard.add(
        InlineKeyboardButton("🔍 Confusing Words", callback_data="lesson_confusing"),
        InlineKeyboardButton("📝 လက်တွေ့ To-do", callback_data="practice_todo")
    )
    keyboard.add(InlineKeyboardButton("📊 Profile & Rank", callback_data="profile_rank"))
    return keyboard

# ၂။ Back ခလုတ်
def get_back_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🔙 Main Menu သို့", callback_data="back_to_menu"))
    return keyboard

# ၃။ /start သို့မဟုတ် /menu
@dp.message_handler(commands=['start', 'menu'])
async def send_welcome(message: types.Message):
    text = "🌟 **မင်္ဂလာပါ သူငယ်ချင်း!**\n\n📖 လေ့လာလိုသော သင်ခန်းစာကို အောက်ပါ မီနူးမှ ရွေးချယ်ပါ:"
    await message.reply(text, reply_markup=get_study_menu(), parse_mode="Markdown")

# ၄။ Main Menu သို့ ပြန်ရန်
@dp.callback_query_handler(text="back_to_menu")
async def back_to_menu_handler(call: types.CallbackQuery):
    text = "🌟 **ပင်မ မီနူးသို့ ပြန်ရောက်ပါပြီ!**\n\n📖 ဆက်လက် လေ့လာရန်:"
    await call.message.edit_text(text, reply_markup=get_study_menu(), parse_mode="Markdown")
    await call.answer()

# ၅။ SMART Goals
@dp.callback_query_handler(text="lesson_smart")
async def send_smart_lesson(call: types.CallbackQuery):
    text = (
        "💡 **How to develop SMART Goals?** 🎯\n\n"
        "🟢 SMART goals ဆိုတာ ကိုယ့်ရဲ့ personal development အတွက် အသုံးဝင်တဲ့ goals သတ်မှတ်နည်းပါပဲ။\n\n"
        "📌 **Specific:** ဘာလုပ်မယ်၊ ဘာကြောင့်လုပ်မယ်။\n"
        "📝 **Measurable:** progress တွေကို တိုင်းတာမယ်။\n"
        "💻 **Attainable:** resource ကောင်းကောင်းရှာမယ်။\n"
        "✔️ **Realistic:** လက်တွေ့ကျတာကို ထားမယ်။\n"
        "⏰ **Timely:** အချိန်အတိအကျ သတ်မှတ်မယ်။"
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

# ၆။ ကျေးဇူးတင်စကားများ
@dp.callback_query_handler(text="lesson_thanks")
async def send_thanks_lesson(call: types.CallbackQuery):
    text = (
        "🎁 **Thank you လို့ပြောမယ့်အစား သုံးရန်**\n\n"
        "🟩 **Many Thanks**\n"
        "🟩 **Thank you**\n"
        "🟦 **I can't thank you enough**\n"
        "🟦 **Thanks a bunch**\n"
        "🟪 **I appreciate it**\n"
        "🟪 **Thanks a million**"
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

# ၇။ တောင်းပန်စကားများ
@dp.callback_query_handler(text="lesson_sorry")
async def send_sorry_lesson(call: types.CallbackQuery):
    text = (
        "🙇 **တောင်းပန်ခြင်း & မသိကြောင်းပြခြင်း**\n\n"
        "🔸 **တောင်းပန်ရန်:** I'm sorry for that / I apologize\n"
        "🔸 **မသိကြောင်း:** I don't know / I have no idea"
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

# ၈။ Writing Tips
@dp.callback_query_handler(text="lesson_writing")
async def send_writing_lesson(call: types.CallbackQuery):
    text = (
        "✍️ **Writing & To-do List Tips**\n\n"
        "⏰ မနက်အိပ်ယာထချိန်နဲ့ ညအိပ်ယာမဝင်ခင် အချိန် ၁၀ မိနစ်ပေးပြီး To-do list တွေနဲ့ Journal ရေးပါ။"
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

# ၉။ အခြေခံအင်္ဂလိပ်စာ
@dp.callback_query_handler(text="lesson_basic")
async def send_basic_lesson(call: types.CallbackQuery):
    text = (
        "🌱 **အခြေခံအင်္ဂလိပ်စာ**\n\n"
        "1️⃣ **8 parts of Speech**\n"
        "2️⃣ **Sentence Structures**\n"
        "3️⃣ **Subject-verb Agreement**\n"
        "4️⃣ **Articles (a, an, the)**\n"
        "5️⃣ **Tenses (12 မျိုး)**"
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

# ၁၀။ Future Tense
@dp.callback_query_handler(text="lesson_future")
async def send_future_lesson(call: types.CallbackQuery):
    text = (
        "🌟 **Future Tense (အနာဂတ်)**\n\n"
        "• **Future Simple:** I will read tomorrow.\n"
        "• **Future Continuous:** I will be reading at 5PM."
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

# ၁၁။ Confusing Words
@dp.callback_query_handler(text="lesson_confusing")
async def send_colored_confusing(call: types.CallbackQuery):
    text = (
        "🔍 **Confusing Words**\n\n"
        "• **It's vs Its**\n"
        "• **A vs An**\n"
        "• **Do vs Make**"
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

# ၁၂။ လက်တွေ့ To-do
@dp.callback_query_handler(text="practice_todo")
async def practice_todo_handler(call: types.CallbackQuery):
    text = (
        "📝 **လက်တွေ့ To-do List**\n\n"
        "✔️ *I gonna eat breakfast at 8 AM.*\n"
        "✔️ *I will shower at 12 PM.*\n"
        "✔️ *I want to eat banana for dinner.*"
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
