import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# 🔑 မင်းရဲ့ Bot Token အစစ်အမှန်
TOKEN = "8437112340:AAEgXfvJ07jeBnGCtTsZgG69zHLCDBaOjRI"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# ယာယီ အမှတ်စာရင်း သိမ်းဆည်းရန် Dictionary
user_scores = {}

# 🏆 Level အလိုက် Rank (သိုင်းအဆင့်) သတ်မှတ်ပေးသည့် စနစ်
def get_rank(points):
    if points >= 5000:
        return "👑 Level 6: Grandmaster (ဂရင်းမာစာ ကျင့်ကြံသူ)"
    elif points >= 3500:
        return "⚡ Level 5: Master (ဂရန်းမား တိုက်ပွဲ အထူးအဆင့်)"
    elif points >= 2200:
        return "🛡️ Level 4: Advanced (အဆင့်မြင့် တိုက်ကွက် စစ်သည်)"
    elif points >= 1200:
        return "🌳 Level 3: Intermediate (အလယ်အလတ် ကျင့်ကြံသူ)"
    elif points >= 500:
        return "🌿 Level 2: Beginner (အခြေခံ အထက် ကျင့်ကြံသူ)"
    else:
        return "🌱 Level 1: Novice (အခြေခံ စတင်သူ)"

# 📱 ပင်မ Menu Keyboard ခလုတ်များ
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.row(KeyboardButton("🥋 Level 1 (🌱 Novice)"), KeyboardButton("⚔️ Level 2 (🌿 Beginner)"))
main_keyboard.row(KeyboardButton("🔥 Level 3 (🌳 Inter)"), KeyboardButton("🛡️ Level 4 (⚡ Adv)"))
main_keyboard.row(KeyboardButton("⚡ Level 5 (🌟 Master)"), KeyboardButton("👑 Level 6 (🏆 G-Master)"))
main_keyboard.row(KeyboardButton("📊 My Rank & Leaderboard"), KeyboardButton("🎯 Training Quiz"))

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(
        f"🥋 မင်္ဂလာပါ စစ်သည်တော် {message.from_user.first_name}!\n"
        "အင်္ဂလိပ်စာ သိုင်းကျင့်စဉ် (Study RPG Bot) မှ ကြိုဆိုပါတယ်။\n\n"
        "လေ့ကျင့်လိုသော Level သိုင်းကွက် ခလုတ်များကို နှိပ်ပြီး စတင်လိုက်ပါ!",
        reply_markup=main_keyboard
    )

@dp.message_handler()
async def handle_menu(message: types.Message):
    user_id = message.from_user.id
    text = message.text

    # --- Level 1 ---
    if text == "🥋 Level 1 (🌱 Novice)":
        await message.answer(
            "🌱 **Level 1: အခြေခံဆုံး အုတ်မြစ် (Novice Stage)**\n\n"
            "1. **Basic Patterns:** S+V, S+V+O, S+V+C\n"
            "2. **Simple Present Tense:** Subject + V1 (s/es)\n"
            "   • *I play chess every day.*\n"
            "3. **Simple Past Tense:** Subject + V2\n"
            "   • *I studied English yesterday.*\n"
            "4. **Simple Future Tense:** Subject + will + V1\n"
            "   • *I will code tomorrow.*"
        )

    # --- Level 2 ---
    elif text == "⚔️ Level 2 (🌿 Beginner)":
        await message.answer(
            "🌿 **Level 2: လက်ရှိနှင့် ဆက်စပ်မှုများ (Beginner Stage)**\n\n"
            "5. **Continuous Tenses:** Present, Past, Future Continuous\n"
            "   • *I am coding right now.*\n"
            "6. **Prepositions:** In, On, At (အချိန်နှင့် နေရာပြ)\n"
            "7. **Wh- Questions:** Who, What, Where, When, Why, How\n"
            "   • *What are you doing?*"
        )

    # --- Level 3 ---
    elif text == "🔥 Level 3 (🌳 Inter)":
        await message.answer(
            "🌳 **Level 3: ပြီးမြောက်မှုနှင့် နေ့စဉ်သုံး ပုံစံများ (Intermediate Stage)**\n\n"
            "8. **Perfect Tenses:** Subject + have/has/had + V3\n"
            "   • *I have finished my task.*\n"
            "9. **Daily Conversation Patterns:**\n"
            "   • *I want to + V1* (လုပ်ချင်သည်)\n"
            "   • *It's time to + V1* (အချိန်ကျပြီ)\n"
            "   • *I used to + V1* (အရင်က လုပ်ဖူးသည်)\n"
            "10. **Comparison Degrees:** Fast -> Faster -> Fastest\n"
            "11. **Gerunds & Infinitives:** (V-ing / To + V1)"
        )

    # --- Level 4 ---
    elif text == "🛡️ Level 4 (⚡ Adv)":
        await message.answer(
            "🛡️ **Level 4: အဆင့်မြင့် တိုက်ကွက်များ (Advanced Stage)**\n\n"
            "12. **Perfect Continuous Tenses:** Have/Has/Had been + V-ing\n"
            "13. **Modals:** Can, Could, Must, Should, Have to\n"
            "14. **Active & Passive Voice:**\n"
            "   • *English is spoken here.*\n"
            "15. **Relative Clauses:** Who, Which, That, Whose\n"
            "16. **Question Tags:** *You code, don't you?*"
        )

    # --- Level 5 ---
    elif text == "⚡ Level 5 (🌟 Master)":
        await message.answer(
            "🌟 **Level 5: ဂရန်းမား တိုက်ပွဲ အထူးအဆင့် (Master Stage)**\n\n"
            "17. **Conditionals (Type 1, 2, 3):** If Clauses\n"
            "   • *If you practice, you will win.*\n"
            "18. **Direct & Indirect Speech:** Reporting speech\n"
            "19. **Causative Verbs:** Have, Make, Get, Let\n"
            "20. **Subjunctive Mood & Conjunctions**"
        )

    # --- Level 6 ---
    elif text == "👑 Level 6 (🏆 G-Master)":
        await message.answer(
            "🏆 **Level 6: ဂရင်းမာစာ ကျင့်ကြံသူ (Grandmaster Stage)**\n\n"
            "21. **Prefixes & Suffixes:** Un-, Dis-, -ful, -less\n"
            "22. **Error Spotting:** သဒ္ဒါအမှား ရှာဖွေတိုက်ထုတ်ခြင်း\n"
            "23. **Word Collocations:** စကားလုံးတွဲဖက် အသုံးများ\n"
            "24. **Idioms & Phrasal Verbs:** စကားပုံများနှင့် တွဲဖက်ကြိယာများ"
        )

    # --- Leaderboard & Rank ---
    elif text == "📊 My Rank & Leaderboard":
        pts = user_scores.get(user_id, 100)
        rank_title = get_rank(pts)
        await message.answer(
            f"🏆 **ထိပ်တန်း ကျင့်ကြံသူများ အဆင့်စာရင်း**\n\n"
            f"👤 **ကျင့်ကြံသူ:** {message.from_user.first_name}\n"
            f"⚡ **ရမှတ်:** {pts} pts\n"
            f"🛡️ **လက်ရှိအဆင့်:** {rank_title}"
        )

    # --- Quiz Mode ---
    elif text == "🎯 Training Quiz":
        await message.answer(
            "🎯 **သိုင်းကွက် စိန်ခေါ်မှု မေးခွန်း:**\n\n"
            "She _____ (play / plays) chess every day.\n\n"
            "အမှန်ကင်းသော အဖြေကို ရေးပို့ပါ!"
        )

    # --- Answer Handling ---
    else:
        current_pts = user_scores.get(user_id, 100)
        user_scores[user_id] = current_pts + 50
        await message.answer(
            f"✨ တိုက်ခိုက်မှု အောင်မြင်သည်! အမှတ် +50 ရရှိပါသည်။\n"
            f"စုစုပေါင်းအမှတ်: {user_scores[user_id]} pts\n"
            f"အဆင့်: {get_rank(user_scores[user_id])}"
        )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
            
