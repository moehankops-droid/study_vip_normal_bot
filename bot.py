from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

API_TOKEN = '8437112340:AAEV-a5qzKjtC-N2_KLacw8oizi-SLQ1yJI'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# ၁။ ပင်မ မီနူးခလုတ်များ (Grid Menu)
def get_study_menu():
    keyboard = InlineKeyboardMarkup(row_width=2)
    
    btn_smart = InlineKeyboardButton("🎯 SMART Goals", callback_data="lesson_smart")
    btn_thanks = InlineKeyboardButton("🙏 ကျေးဇူးတင်စကားများ", callback_data="lesson_thanks")
    btn_sorry = InlineKeyboardButton("🙇 တောင်းပန်စကားများ", callback_data="lesson_sorry")
    btn_writing = InlineKeyboardButton("✍️ Writing & To-do", callback_data="lesson_writing")
    btn_basic = InlineKeyboardButton("🌱 ပထမအခြေခံ English", callback_data="lesson_basic")
    btn_future = InlineKeyboardButton("🌟 Future Tense", callback_data="lesson_future")
    btn_confusing = InlineKeyboardButton("🔍 Confusing Words", callback_data="lesson_confusing")
    btn_practice = InlineKeyboardButton("📝 လက်တွေ့ To-do", callback_data="practice_todo")
    btn_rank = InlineKeyboardButton("📊 Profile & Rank", callback_data="profile_rank")
    
    keyboard.add(btn_smart, btn_thanks)
    keyboard.add(btn_sorry, btn_writing)
    keyboard.add(btn_basic, btn_future)
    keyboard.add(btn_confusing, btn_practice)
    keyboard.add(btn_rank)
    
    return keyboard

# ၂။ သင်ခန်းစာများတွင် အောက်ဆုံးမှ Back (Main Menu သို့) ပြန်သွားမည့် ခလုတ်
def get_back_menu():
    keyboard = InlineKeyboardMarkup()
    btn_back = InlineKeyboardButton("🔙 Main Menu သို့", callback_data="back_to_menu")
    keyboard.add(btn_back)
    return keyboard

# ၃။ /start သို့မဟုတ် /menu ဖြင့် မီနူးပြရန်
@dp.message_handler(commands=['start', 'menu'])
async def send_welcome(message: types.Message):
    welcome_text = (
        "🌟 **မင်္ဂလာပါ သူငယ်ချင်း!**\n\n"
        "📖 အင်္ဂလိပ်စာလေ့လာရန် လိုအပ်သော သင်ခန်းစာများကို အောက်ပါ မီနူးမှ ရွေးချယ်ပါ:"
    )
    await message.reply(welcome_text, reply_markup=get_study_menu(), parse_mode="Markdown")

# ၄။ Main Menu သို့ ပြန်သွားရန် Callback
@dp.callback_query_handler(text="back_to_menu")
async def back_to_menu_handler(call: types.CallbackQuery):
    welcome_text = (
        "🌟 **ပင်မ မီနူးသို့ ပြန်ရောက်ပါပြီ!**\n\n"
        "📖 လေ့လာလိုသည့် သင်ခန်းစာကို ဆက်လက်ရွေးချယ်ပါ:"
    )
    await call.message.edit_text(welcome_text, reply_markup=get_study_menu(), parse_mode="Markdown")
    await call.answer()

# ၅။ SMART Goals သင်ခန်းစာ
@dp.callback_query_handler(text="lesson_smart")
async def send_smart_lesson(call: types.CallbackQuery):
    text = (
        "💡 **How to develop SMART Goals?** 🎯\n\n"
        "🟢 SMART goals ဆိုတာ ကိုယ့်ရဲ့ personal development အတွက် အသုံးဝင်တဲ့ goals သတ်မှတ်နည်းပါ ဖြစ်ပါတယ်။\n\n"
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
        "🟩 Many Thanks / Thank you\n"
        "🟦 I can't thank you enough. / Thanks a bunch\n"
        "🟪 I appreciate it / Thanks a million"
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

# ၇။ တောင်းပန်စကားများ
@dp.callback_query_handler(text="lesson_sorry")
async def send_sorry_lesson(call: types.CallbackQuery):
    text = (
        "🙇 **တောင်းပန်ခြင်း & မသိကြောင်းပြခြင်း**\n\n"
        "🔸 **I'm sorry for that / I apologize / I regret that**\n"
        "🔸 **I don't know / I have no idea / It's beyond me**"
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

# ၈။ Writing Tips
@dp.callback_query_handler(text="lesson_writing")
async def send_writing_lesson(call: types.CallbackQuery):
    text = (
        "✍️ **Writing & To-do List Tips**\n\n"
        "⏰ မနက်အိပ်ယာထချိန်နဲ့ ညအိပ်ယာမဝင်ခင်မှာ အချိန် ၁၀ မိနစ်မှ ၁၅ မိနစ်ပေးပြီး To-do list တွေနဲ့ Journal ရေးပါ။"
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

# ၉။ အခြေခံအင်္ဂလိပ်စာ
@dp.callback_query_handler(text="lesson_basic")
async def send_basic_lesson(call: types.CallbackQuery):
    text = (
        "🌱 **နံပါတ် တွဲသုံး အခြေခံအင်္ဂလိပ်စာ**\n\n"
        "1️⃣ 8 parts of Speech\n"
        "2️⃣ Sentence Structures\n"
        "3️⃣ Subject-verb Agreement\n"
        "4️⃣ Articles (a, an, the)\n"
        "5️⃣ Tenses (12 မျိုး)"
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

# ၁၀။ Future Tense
@dp.callback_query_handler(text="lesson_future")
async def send_future_lesson(call: types.CallbackQuery):
    text = (
        "🌟 **Future Tense (အနာဂတ် လေ့ကျင့်ခန်း)**\n\n"
        "• **Future Simple:** I will read the book tomorrow.\n"
        "• **Future Continuous:** I will be reading at 5PM tomorrow."
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

# ၁၁။ Confusing Words
@dp.callback_query_handler(text="lesson_confusing")
async def send_confusing_lesson(call: types.CallbackQuery):
    text = (
        "🔍 **Confusing Words (အမေ့ပျောက်များ)**\n\n"
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
        "📝 **လက်တွေ့ To-do List & Time လေ့ကျင့်ခန်း**\n\n"
        "✔️ *I gonna eat breakfast at 8 AM.*\n"
        "✔️ *I will shower at 12 PM.*\n"
        "✔️ *I want to eat banana for dinner.*"
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
