// Study Bot VLP Pro - Dictionary & Vocabulary Data Bank

// ၁။ မူလ ဝေါဟာရ ဘဏ် (Default Vocabulary Bank)
const defaultVocabularyBank = [
    { word: "Achieve", pos: "verb", myanmar: "အောင်မြင်အောင် ဆောင်ရွက်သည်", example: "He wants to achieve All A grades in his exam." },
    { word: "Active Recall", pos: "noun", myanmar: "ပြန်လည်ထုတ်ဖော် မှတ်မိခြင်း စာကျက်နည်း", example: "Active recall helps you remember lesson concepts faster." },
    { word: "Capital", pos: "noun", myanmar: "ရင်းနှီးမြှုပ်နှံငွေ / မြို့တော်", example: "They scale their business capital step by step." },
    { word: "Continuously", pos: "adverb", myanmar: "မပြတ် ဆက်တိုက်", example: "It rained continuously all night long." },
    { word: "Demonstrate", pos: "verb", myanmar: "လက်တွေ့ ပြသသည်", example: "The teacher demonstrated the experiment in class." },
    { word: "Emergency", pos: "noun", myanmar: "အရေးပေါ် အခြေအနေ", example: "Always save money for emergency situations." },
    { word: "Environment", pos: "noun", myanmar: "ပတ်ဝန်းကျင်", example: "We should keep our school environment clean." },
    { word: "Experiment", pos: "noun", myanmar: "သိပ္ပံ စမ်းသပ်ချက်", example: "We conducted a science experiment in the lab." },
    { word: "Fluently", pos: "adverb", myanmar: "ကျွမ်းကျင်စွာ / ရေရေလည်လည်", example: "She can speak English fluently." },
    { word: "Hobby", pos: "noun", myanmar: "ဝါသနာ", example: "Playing chess is my favorite hobby." },
    { word: "Investment", pos: "noun", myanmar: "ရင်းနှီးမြှုပ်နှံမှု", example: "Proper investment brings good daily profit." },
    { word: "Methodology", pos: "noun", myanmar: "နည်းလမ်း / စနစ်", example: "Using a proper study methodology saves time." },
    { word: "Opportunity", pos: "noun", myanmar: "အခွင့်အရေး", example: "Do not miss the opportunity to learn coding." },
    { word: "Predict", pos: "verb", myanmar: "ကြိုတင် ခန့်မှန်းသည်", example: "Look at the clouds, I predict it will rain." },
    { word: "Profit", pos: "noun", myanmar: "အသားတင် အမြတ်ငွေ", example: "The daily profit is recorded in the tracker app." },
    { word: "Proportionally", pos: "adverb", myanmar: "အချိုးကျကျ", example: "Profit shares increase proportionally with capital." },
    { word: "Retention", pos: "noun", myanmar: "မှတ်ဉာဏ် ထိန်းသိမ်းနိုင်မှု", example: "Flashcards improve long-term memory retention." },
    { word: "Schedule", pos: "noun", myanmar: "အချိန်ဇယား", example: "Stick to your daily study schedule." },
    { word: "Spaced Repetition", pos: "noun", myanmar: "အကွာအဝေးခြား ပြန်လည်နွှေးခြင်း", example: "Spaced repetition prevents forgetting new words." },
    { word: "Strategy", pos: "noun", myanmar: "ဗျူဟာ / အစီအစဉ်", example: "He plays chess with a smart strategy." }
];

// ၂။ Local Storage မှ Custom Words များနှင့် default များကို ပေါင်းစပ်ဖတ်ရှုသည့် Function
function getVocabularyBank() {
    let customWords = JSON.parse(localStorage.getItem("customVocabList")) || [];
    let baseBank = (typeof defaultVocabularyBank !== 'undefined') ? defaultVocabularyBank : [];
    return [...baseBank, ...customWords];
}

// ၃. UI (Input Box) မှတဆင့် စကားလုံးအသစ် တိုက်ရိုက် Save သည့် Function
function addNewCustomWord() {
    const wordInput = document.getElementById("new-word-input");
    const meaningInput = document.getElementById("new-meaning-input");
    const wText = wordInput.value.trim();
    const mText = meaningInput.value.trim();

    if (!wText || !mText) { 
        alert("ကျေးဇူးပြု၍ စကားလုံးနှင့် အဓိပ္ပာယ် နှစ်ခုစလုံး ဖြည့်စွက်ပါ!"); 
        return; 
    }

    let customWords = JSON.parse(localStorage.getItem("customVocabList")) || [];
    customWords.push({ word: wText, pos: "custom", myanmar: mText, example: "User Saved Word" });
    
    localStorage.setItem("customVocabList", JSON.stringify(customWords));

    wordInput.value = ""; 
    meaningInput.value = "";
    
    // UI ပေါ်ရှိ စာရင်းကိုပါ တစ်ခါတည်း update လုပ်ပေးရန်
    if (typeof renderVocabularyList === 'function') {
        renderVocabularyList();
    }
    
    if (typeof playSound === 'function') {
        playSound('correct');
    }
    
    alert("🎉 စကားလုံးအသစ် အောင်မြင်စွာ မှတ်သားပြီးပါပြီ!");
}
