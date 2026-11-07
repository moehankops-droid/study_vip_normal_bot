from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

API_TOKEN = '8437112340:AAEV-a5qzKjtC-N2_KLacw8oizi-SLQ1yJI'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# ၁။ ရောင်စုံအီမိုဂျီ ဇယားကွက် (Grid) ပုံစံ မီနူးခလုတ်များ
def get_study_menu():
    keyboard = InlineKeyboardMarkup(row_width=2) # တစ်တန်းကို ခလုတ် ၂ ခုစီ
    
    btn_smart = InlineKeyboardButton("🎯 SMART Goals", callback_data="lesson_smart")
    btn_thanks = InlineKeyboardButton("🙏 ကျေးဇူးတင်စကားများ", callback_data="lesson_thanks")
    btn_sorry = InlineKeyboardButton("🙇 တောင်းပန်စကားများ", callback_data="lesson_sorry")
    btn_writing = InlineKeyboardButton("✍️ Writing Tips", callback_data="lesson_writing")
    btn_basic = InlineKeyboardButton("🌱 ပထမအခြေခံ English", callback_data="lesson_basic")
    btn_future = InlineKeyboardButton("🌟 Future Tense", callback_data="lesson_future")
    btn_confusing = InlineKeyboardButton("🔍 Confusing Words", callback_data="lesson_confusing")
    btn_rank = InlineKeyboardButton("📊 Profile & Rank", callback_data="profile_rank")
    
    keyboard.add(btn_smart, btn_thanks)
    keyboard.add(btn_sorry, btn_writing)
    keyboard.add(btn_basic, btn_future)
    keyboard.add(btn_confusing, btn_rank)
    
    return keyboard

# ၂။ /start သို့မဟုတ် /menu ဖြင့် မီနူးခေါ်ရန်
@dp.message_handler(commands=['start', 'menu'])
async def send_welcome(message: types.Message):
    welcome_text = (
        "🌟 **မင်္ဂလာပါ သူငယ်ချင်း!**\n\n"
        "📖 အင်္ဂလိပ်စာလေ့လာရန် လိုအပ်သော သင်ခန်းစာများနှင့် နေ့စဉ်လေ့ကျင့်ခန်းများကို အောက်ပါ ရောင်စုံမီနူးမှ ရွေးချယ်လေ့လာနိုင်ပါပြီ။"
    )
    await message.reply(welcome_text, reply_markup=get_study_menu(), parse_mode="Markdown")

# ၃။ SMART Goals သင်ခန်းစာ
@dp.callback_query_handler(text="lesson_smart")
async def send_smart_lesson(call: types.CallbackQuery):
    text = (
        "💡 **How to develop SMART Goals?** 🎯\n\n"
        "🟢 SMART goals ဆိုတာ ကိုယ့်ရဲ့ personal or professional development အတွက် အသုံးဝင်တဲ့ goals တွေသတ်မှတ်နည်းပဲ ဖြစ်ပါတယ်။\n\n"
        "📌 **Specific:** ကိုယ်လိုချင်တာဘာလဲ(What)၊ ဘာကြောင့်လုပ်ချင်တာလဲ(Why)၊ ဘယ်လိုရအောင်လုပ်မလဲ(How)၊ ဘယ်အချိန်မှာရအောင်လုပ်မလဲ(When) ဆိုတဲ့ တိကျတဲ့ ရည်ရွယ်ချက်ထားရမယ်။\n"
        "📝 **Measurable:** ကိုယ့်ရဲ့ progress တွေကို တိုင်းတာခြင်းပါ။\n"
        "💻 **Attainable:** ကိုယ်ထားထားတဲ့ Goals တွေကို ရယူဖို့ resources ကောင်းကောင်းရှာတတ်ဖို့လိုပါတယ်။\n"
        "✔️ **Realistic:** လက်တွေ့ကျဖို့လည်းလိုပါတယ်။\n"
        "⏰ **Timely:** အချိန်သတ်မှတ်ပါ။"
    )
    await call.message.answer(text, parse_mode="Markdown")
    await call.answer()

# ၄။ ကျေးဇူးတင်စကားများ
@dp.callback_query_handler(text="lesson_thanks")
async def send_thanks_lesson(call: types.CallbackQuery):
    text = (
        "🎁 **ကျေးဇူးတင်ပါတယ် (Thank you လို့ပြောမယ့်အစား သုံးကြည့်ပါ)**\n\n"
        "🟩 Thank you\n"
        "🟩 Many Thanks\n"
        "🟦 I can't thank you enough.\n"
        "🟦 Thanks a bunch\n"
        "🟪 I appreciate it\n"
        "🟪 Thanks a million\n\n"
        "⚡ သင်ဟာ meaning တစ်လုံးကို ကျွယ်ကျွယ် ပြန့်ပြန့်သုံးတတ်နေပြီဆိုရင် မဆိုးလှတဲ့ English level ကိုရောက်နေပြီ ဖြစ်ပါတယ်။"
    )
    await call.message.answer(text, parse_mode="Markdown")
    await call.answer()

# ၅။ တောင်းပန်စကားများ
@dp.callback_query_handler(text="lesson_sorry")
async def send_sorry_lesson(call: types.CallbackQuery):
    text = (
        "🙇 **တောင်းပန်ပါတယ် & မသိဘူး (Phrases)**\n\n"
        "🔸 **တောင်းပန်ပါတယ်:**\n"
        "• I'm sorry for that.\n"
        "• I apologize\n"
        "• I regret that.\n\n"
        "🔸 **မသိဘူး:**\n"
        "• I don't know.\n"
        "• I have no idea.\n"
        "• It's beyond me."
    )
    await call.message.answer(text, parse_mode="Markdown")
    await call.answer()

# ၆။ Writing Tips
@dp.callback_query_handler(text="lesson_writing")
async def send_writing_lesson(call: types.CallbackQuery):
    text = (
        "✍️ **Writing Tips! It works 💯 all the time.**\n\n"
        "⏰ Writing လေ့ကျင့်ဖို့အတွက် အကောင်းဆုံးအချိန်က မနက်အိပ်ယာထချိန်နဲ့ ညအိပ်ယာမဝင်ခင်အချိန်ပဲ ဖြစ်ပါတယ်။\n\n"
        "🌅 **မနက်ခင်း:** အိပ်ယာထချင်း စာရွက်နဲ့ ဘောပင် သို့မဟုတ် ဖုန်း note ထဲမှာ 'တစ်နေ့တာလုပ်ဆောင်မယ့် To-do-list' တွေကို ချရေးပါ။ 📝\n"
        "🌙 **ညအိပ်ယာမဝင်ခင်:** Jounaling ပြန်လုပ်ပါ။ တစ်နေ့တာဖြစ်ပျက်သမျှကို ပြန်ချရေးပါ။"
    )
    await call.message.answer(text, parse_mode="Markdown")
    await call.answer()

# ၇။ အခြေခံအင်္ဂလိပ်စာ
@dp.callback_query_handler(text="lesson_basic")
async def send_basic_lesson(call: types.CallbackQuery):
    text = (
        "🌱 **နံပါတ် တွဲသုံး အခြေခံအင်္ဂလိပ်စာ**\n\n"
        "1️⃣ **8 parts of Speech** (Noun, Verb, Adjective, Adverb, Pronoun, Preposition, Conjunction, Interjection)\n"
        "2️⃣ **Sentence Structures** (Simple, Compound, Complex, Compound-complex)\n"
        "3️⃣ **Subject-verb Agreement**\n"
        "4️⃣ **Articles** (a, an, the)\n"
        "5️⃣ **Tenses (12 မျိုး)**"
    )
    await call.message.answer(text, parse_mode="Markdown")
    await call.answer()

# ၈။ Future Tense
@dp.callback_query_handler(text="lesson_future")
async def send_future_lesson(call: types.CallbackQuery):
    text = (
        "🌟 **Future Tense (အနာဂတ်)**\n\n"
        "အနာဂတ်အကြောင်းပြောမှာ ဖြစ်တဲ့အတွက် 'လိမ့်မည်' ဆိုတဲ့ အဓိပ္ပာယ် 'will' ကို အသုံးပြုပါတယ်။\n\n"
        "1️⃣ **Future Simple (will + V1)**\n"
        "• eg. I will read the book tomorrow.\n"
        "2️⃣ **Future Continuous (will + be + Ving)**\n"
        "• eg. I will be reading the book at 5PM tomorrow.\n"
        "3️⃣ **Future Perfect (will + have + V3)**\n"
        "• eg. I will have read the book by tomorrow.\n"
        "4️⃣ **Future Perfect Continuous (will + have + been + Ving)**\n"
        "• eg. I'll have been reading for two hours by the time you arrive."
    )
    await call.message.answer(text, parse_mode="Markdown")
    await call.answer()

# ၉။ Confusing Words
@dp.callback_query_handler(text="lesson_confusing")
async def send_confusing_lesson(call: types.CallbackQuery):
    text = (
        "🔍 **အမှားများတတ်သော အခြေခံစကားလုံးများ**\n\n"
        "📌 **It's vs Its**\n"
        "• It's = It is သို့မဟုတ် It has ကို အတိုကောက်သုံးခြင်း။\n"
        "• Its = ပိုင်ဆိုင်မှုကို ပြခြင်း\n\n"
        "📌 **A vs An**\n"
        "• A = သာမန် ဗျည်းသံ (consonant sound) ရှေ့တွင်သုံးသည်။\n"
        "• An = သရသံ (vowel sound - a, e, i, o, u) ရှေ့တွင်သုံးသည်။\n\n"
        "📌 **Do vs Make**\n"
        "• Do = တာဝန်လုပ်ငန်းတစ်ခုခုကို လုပ်ဆောင်ရာတွင် သုံးသည်။\n"
        "• Make = အသစ်ဖန်တီးတာ၊ ပစ္စည်းပြုလုပ်ရာတွင် သုံးသည်။"
    )
    await call.message.answer(text, parse_mode="Markdown")
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

