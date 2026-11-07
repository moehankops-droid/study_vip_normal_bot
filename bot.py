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
        "💡 **How to develop SMART Goals?** 🎯[span_0](start_span)[span_0](end_span)[span_1](start_span)[span_1](end_span)[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span)[span_4](start_span)[span_4](end_span)\n\n"
        "🟢 SMART goals ဆိုတာ ကိုယ့်ရဲ့ personal development အတွက် အသုံးဝင်တဲ့ goals သတ်မှတ်နည်းပါ[span_5](start_span)[span_5](end_span)[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span)[span_8](start_span)[span_8](end_span)[span_9](start_span)[span_9](end_span)။\n\n"
        "📌 **Specific:** ဘာလုပ်မယ်၊ ဘာကြောင့်လုပ်မယ်[span_10](start_span)[span_10](end_span)[span_11](start_span)[span_11](end_span)[span_12](start_span)[span_12](end_span)[span_13](start_span)[span_13](end_span)။\n"
        "📝 **Measurable:** progress တွေကို တိုင်းတာမယ်[span_14](start_span)[span_14](end_span)[span_15](start_span)[span_15](end_span)[span_16](start_span)[span_16](end_span)[span_17](start_span)[span_17](end_span)။\n"
        "💻 **Attainable:** resource ကောင်းကောင်းရှာမယ်[span_18](start_span)[span_18](end_span)[span_19](start_span)[span_19](end_span)[span_20](start_span)[span_20](end_span)။\n"
        "✔️ **Realistic:** လက်တွေ့ကျတာကို ထားမယ်[span_21](start_span)[span_21](end_span)[span_22](start_span)[span_22](end_span)[span_23](start_span)[span_23](end_span)။\n"
        "⏰ **Timely:** အချိန်အတိအကျ သတ်မှတ်မယ်[span_24](start_span)[span_24](end_span)[span_25](start_span)[span_25](end_span)[span_26](start_span)[span_26](end_span)။"
    )
    # စာအသစ်ပြောင်းလဲပြီး အောက်ဆုံးတွင် Back ခလုတ်တစ်ခုတည်းသာ တွဲပြမည်
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

# ၆။ ကျေးဇူးတင်စကားများ
@dp.callback_query_handler(text="lesson_thanks")
async def send_thanks_lesson(call: types.CallbackQuery):
    text = (
        "🎁 **Thank you လို့ပြောမယ့်အစား သုံးရန်**[span_27](start_span)[span_27](end_span)[span_28](start_span)[span_28](end_span)\n\n"
        "🟩 Many Thanks / Thank you[span_29](start_span)[span_29](end_span)[span_30](start_span)[span_30](end_span)\n"
        "🟦 I can't thank you enough. / Thanks a bunch[span_31](start_span)[span_31](end_span)[span_32](start_span)[span_32](end_span)\n"
        "🟪 I appreciate it / Thanks a million[span_33](start_span)[span_33](end_span)[span_34](start_span)[span_34](end_span)"
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

# ၇။ တောင်းပန်စကားများ
@dp.callback_query_handler(text="lesson_sorry")
async def send_sorry_lesson(call: types.CallbackQuery):
    text = (
        "🙇 **တောင်းပန်ခြင်း & မသိကြောင်းပြခြင်း**[span_35](start_span)[span_35](end_span)\n\n"
        "🔸 **I'm sorry for that / I apologize / I regret that**[span_36](start_span)[span_36](end_span)\n"
        "🔸 **I don't know / I have no idea / It's beyond me**[span_37](start_span)[span_37](end_span)"
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

# ၈။ Writing Tips
@dp.callback_query_handler(text="lesson_writing")
async def send_writing_lesson(call: types.CallbackQuery):
    text = (
        "✍️ **Writing & To-do List Tips**[span_38](start_span)[span_38](end_span)[span_39](start_span)[span_39](end_span)[span_40](start_span)[span_40](end_span)[span_41](start_span)[span_41](end_span)\n\n"
        "⏰ မနက်အိပ်ယာထချိန်နဲ့ ညအိပ်ယာမဝင်ခင်မှာ အချိန် ၁၀ မိနစ်မှ ၁၅ မိနစ်ပေးပြီး To-do list တွေနဲ့ Journal ရေးပါ[span_42](start_span)[span_42](end_span)[span_43](start_span)[span_43](end_span)[span_44](start_span)[span_44](end_span)[span_45](start_span)[span_45](end_span)။"
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

# ၉။ အခြေခံအင်္ဂလိပ်စာ
@dp.callback_query_handler(text="lesson_basic")
async def send_basic_lesson(call: types.CallbackQuery):
    text = (
        "🌱 **နံပါတ် တွဲသုံး အခြေခံအင်္ဂလိပ်စာ**[span_46](start_span)[span_46](end_span)\n\n"
        "1️⃣ 8 parts of Speech[span_47](start_span)[span_47](end_span)\n"
        "2️⃣ Sentence Structures[span_48](start_span)[span_48](end_span)\n"
        "3️⃣ Subject-verb Agreement[span_49](start_span)[span_49](end_span)\n"
        "4️⃣ Articles (a, an, the)[span_50](start_span)[span_50](end_span)\n"
        "5️⃣ Tenses (12 မျိုး)[span_51](start_span)[span_51](end_span)"
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

# ၁၀။ Future Tense
@dp.callback_query_handler(text="lesson_future")
async def send_future_lesson(call: types.CallbackQuery):
    text = (
        "🌟 **Future Tense (အနာဂတ် လေ့ကျင့်ခန်း)**[span_52](start_span)[span_52](end_span)[span_53](start_span)[span_53](end_span)[span_54](start_span)[span_54](end_span)[span_55](start_span)[span_55](end_span)[span_56](start_span)[span_56](end_span)\n\n"
        "• **Future Simple:** I will read the book tomorrow.[span_57](start_span)[span_57](end_span)[span_58](start_span)[span_58](end_span)\n"
        "• **Future Continuous:** I will be reading at 5PM tomorrow.[span_59](start_span)[span_59](end_span)"
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

# ၁၁။ Confusing Words
@dp.callback_query_handler(text="lesson_confusing")
async def send_confusing_lesson(call: types.CallbackQuery):
    text = (
        "🔍 **Confusing Words (အမေ့ပျောက်များ)**[span_60](start_span)[span_60](end_span)\n\n"
        "• **It's vs Its**[span_61](start_span)[span_61](end_span)\n"
        "• **A vs An**[span_62](start_span)[span_62](end_span)\n"
        "• **Do vs Make**[span_63](start_span)[span_63](end_span)"
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

# ၁၂။ လက်တွေ့ To-do
@dp.callback_query_handler(text="practice_todo")
async def practice_todo_handler(call: types.CallbackQuery):
    text = (
        "📝 **လက်တွေ့ To-do List & Time လေ့ကျင့်ခန်း**[span_64](start_span)[span_64](end_span)[span_65](start_span)[span_65](end_span)\n\n"
        "✔️ *I gonna eat breakfast at 8 AM.*[span_66](start_span)[span_66](end_span)\n"
        "✔️ *I will shower at 12 PM.*[span_67](start_span)[span_67](end_span)\n"
        "✔️ *I want to eat banana for dinner.*[span_68](start_span)[span_68](end_span)"
    )
    await call.message.edit_text(text, reply_markup=get_back_menu(), parse_mode="Markdown")
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
