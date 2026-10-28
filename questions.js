const questionsBank = [
    { 
        question: "She _____ to school every day.", 
        options: ["go", "goes", "going", "gone"], 
        answer: "goes",
        explanation: "'Every day' ဖြစ်သောကြောင့် Present Simple Tense ဖြင့် Subject (She) က singular မို့ 'goes' ဖြစ်သည်။" 
    },
    { 
        question: "They _____ football in the yard right now.", 
        options: ["play", "plays", "are playing", "played"], 
        answer: "are playing",
        explanation: "'right now' ပါရှိသောကြောင့် Present Continuous Tense 'are playing' ကို သုံးရပါသည်။" 
    },
    { 
        question: "He has _____ his homework already.", 
        options: ["finish", "finishes", "finished", "finishing"], 
        answer: "finished",
        explanation: "'already' ပါဝင်ပြီး ပြီးစီးသွားသောကြောင့် Present Perfect Tense 'finished' ဖြစ်သည်။" 
    },
    { 
        question: "My mother _____ cooking when I arrived home.", 
        options: ["is", "was", "were", "are"], 
        answer: "was",
        explanation: "အတိတ်ကာလတွင် ဖြစ်နေစဉ် အခြားအလုပ်ဝင်လုပ်သည့် Past Continuous Tense ဖြစ်ပြီး subject က singular မို့ 'was' ဖြစ်သည်။" 
    },
    { 
        question: "She _____ her grandmother next week.", 
        options: ["visit", "visited", "will visit", "visiting"], 
        answer: "will visit",
        explanation: "'next week' ဖြစ်သောကြောင့် Future Simple Tense 'will visit' ကို သုံးရပါသည်။" 
    },
    { 
        question: "Look! The birds _____ in the sky.", 
        options: ["fly", "flies", "are flying", "flew"], 
        answer: "are flying",
        explanation: "'Look!' ဟု အာရုံစိုက်ခိုင်းထားသဖြင့် ယခုလက်ရှိဖြစ်နေသည့် Present Continuous 'are flying' ဖြစ်သည်။" 
    },
    { 
        question: "Water _____ at 100 degrees Celsius.", 
        options: ["boil", "boils", "boiled", "boiling"], 
        answer: "boils",
        explanation: "သိပ္ပံနည်းကျ အမှန်တရားဖြစ်၍ Present Simple Tense ဖြင့် 'boils' ဖြစ်သည်။" 
    },
    { 
        question: "I _____ English for three years.", 
        options: ["learn", "learned", "have learned", "learning"], 
        answer: "have learned",
        explanation: "အချိန်ကာလတစ်ခုအထိ ဆက်တိုက်လုပ်ဆောင်လာမှုကို Present Perfect Tense ဖြင့် သုံးရသည်။" 
    },
    { 
        question: "They _____ a new car last month.", 
        options: ["buy", "buys", "bought", "buying"], 
        answer: "bought",
        explanation: "'last month' (အတိတ်ကာလ) ဖြစ်သောကြောင့် Past Simple Tense 'bought' ဖြစ်သည်။" 
    },
    { 
        question: "While I was reading, he _____ television.", 
        options: ["watch", "watched", "was watching", "is watching"], 
        answer: "was watching",
        explanation: "အတိတ်တွင် တစ်ပြိုင်နက်ဖြစ်ပျက်နေသော Past Continuous Tense နှစ်ခုကို ယှဉ်သုံးထားခြင်းဖြစ်သည်။" 
    },
    { 
        question: "A knife is used _____ cutting things.", 
        options: ["for", "to", "with", "by"], 
        answer: "for",
        explanation: "ဘာအတွက်အသုံးပြုသည်ကို ဖော်ပြရာတွင် 'be used for + V-ing' ကို သုံးရသည်။" 
    },
    { 
        question: "He is taller _____ his brother.", 
        options: ["then", "than", "to", "as"], 
        answer: "than",
        explanation: "နှိုင်းယှဉ်ပြသည့် Comparative Degree တွင် 'than' ကို မဖြစ်မနေ တွဲရသည်။" 
    },
    { 
        question: "English _____ all over the world.", 
        options: ["speak", "spoke", "is spoken", "speaks"], 
        answer: "is spoken",
        explanation: "Passive Voice ဖြစ်သောကြောင့် 'is + V3' (is spoken) ကို သုံးရပါသည်။" 
    },
    { 
        question: "She is good _____ playing the piano.", 
        options: ["at", "in", "on", "with"], 
        answer: "at",
        explanation: "ကျွမ်းကျင်မှုကိုဖော်ပြသည့်အခါ 'good at' ဟု သုံးရိုးထုံးစံရှိသည်။" 
    },
    { 
        question: "The cat is sleeping _____ the table.", 
        options: ["on", "in", "at", "over"], 
        answer: "on",
        explanation: "မျက်နှာပြင်ပေါ်တွင် ရှိနေခြင်းကို 'on' ဖြင့် ဖော်ပြသည်။" 
    },
    { 
        question: "He was born _____ 2012.", 
        options: ["in", "on", "at", "by"], 
        answer: "in",
        explanation: "ခုနှစ်များကိုဖော်ပြသည့်အခါ 'in' preposition ကို သုံးရသည်။" 
    },
    { 
        question: "Listen _____ me carefully.", 
        options: ["to", "at", "for", "in"], 
        answer: "to",
        explanation: "'listen' နောက်တွင် 'to' ကို တွဲသုံးရပါသည်။" 
    },
    { 
        question: "This book is _____ than that one.", 
        options: ["interesting", "more interesting", "most interesting", "interest"], 
        answer: "more interesting",
        explanation: "အသံထ syllables များသော adjective ဖြစ်၍ နှိုင်းယှဉ်ရာတွင် 'more' ထည့်ရသည်။" 
    },
    { 
        question: "Ann is the _____ girl in the class.", 
        options: ["tall", "taller", "tallest", "more tall"], 
        answer: "tallest",
        explanation: "အုပ်စုထဲတွင် အမြင့်ဆုံးဟု Superlative ဖြင့် နှိုင်းယှဉ်ထားသည်။" 
    },
    { 
        question: "He runs _____ than me.", 
        options: ["fast", "faster", "fastest", "more fast"], 
        answer: "faster",
        explanation: "Comparative Degree ဖြစ်၍ 'faster' ကို သုံးရသည်။" 
    },
    { 
        question: "What is the synonym of 'begin'?", 
        options: ["start", "end", "stop", "finish"], 
        answer: "start",
        explanation: "'begin' နှင့် အဓိပ္ပာယ်တူ စကားလုံးမှာ 'start' ဖြစ်သည်။" 
    },
    { 
        question: "What is the antonym of 'happy'?", 
        options: ["glad", "sad", "joyful", "excited"], 
        answer: "sad",
        explanation: "'happy' ၏ ဆန့်ကျင်ဘက် အဓိပ္ပာယ်မှာ 'sad' ဖြစ်သည်။" 
    },
    { 
        question: "He said that he _____ tired.", 
        options: ["is", "was", "will be", "has been"], 
        answer: "was",
        explanation: "Reporting verb မှာ Past (said) ဖြစ်သဖြင့် အထဲက Tense လည်း Past (was) ဖြစ်ရပါမည်။" 
    },
    { 
        question: "Unless you work hard, you _____ pass.", 
        options: ["will", "won't", "can", "would"], 
        answer: "won't",
        explanation: "Unless သည် အငြင်းအနက်ဆောင်သဖြင့် ဒုတိယဝါကျတွင် 'won't' သုံးရပါသည်။" 
    },
    { 
        question: "I wish I _____ a millionaire.", 
        options: ["am", "was", "were", "be"], 
        answer: "were",
        explanation: "မဖြစ်နိုင်သော ဆန္ဒကိုဖော်ပြသည့် Subjunctive mood တွင် 'were' ကိုသာ အမြဲသုံးသည်။" 
    },
    { 
        question: "Hardly had I arrived at the station _____ the train left.", 
        options: ["when", "than", "then", "before"], 
        answer: "when",
        explanation: "Hardly ... များနှင့် တွဲဖက်သုံးသော conjunction မှာ 'when' ဖြစ်သည်။" 
    },
    { 
        question: "No sooner had I reached home _____ it started to rain.", 
        options: ["when", "than", "then", "before"], 
        answer: "than",
        explanation: "No sooner နှင့် တွဲဖက်သုံးသည်မှာ 'than' ဖြစ်ပါသည်။" 
    },
    { 
        question: "Despite _____ hard, he failed the exam.", 
        options: ["study", "studying", "studied", "studies"], 
        answer: "studying",
        explanation: "Despite ပြီးနောက် Gerund (verb-ing) ကို အသုံးပြုရပါသည်။" 
    },
    { 
        question: "In spite _____ the rain, we went out.", 
        options: ["of", "in", "on", "at"], 
        answer: "of",
        explanation: "In spite နှင့် တွဲသုံးသော preposition မှာ 'of' ဖြစ်သည် (Despite နှင့် အတူတူပင်)။" 
    },
    { 
        question: "She prefers coffee _____ tea.", 
        options: ["than", "to", "over", "from"], 
        answer: "to",
        explanation: "Prefer ဖြင့် နှိုင်းယှဉ်ပြလျှင် 'than' မဟုတ်ဘဲ 'to' ကို သုံးရသည်။" 
    },
    { 
        question: "He congratulated me _____ my success.", 
        options: ["on", "in", "at", "for"], 
        answer: "on",
        explanation: "Congratulate နှင့် တွဲဖက်သုံးသော Preposition မှာ 'on' ဖြစ်ပါသည်။" 
    },
    { 
        question: "She is capable _____ doing this job.", 
        options: ["of", "in", "at", "with"], 
        answer: "of",
        explanation: "Capable နှင့် တွဲသုံးသော Preposition မှာ 'of' ဖြစ်သည်။" 
    },
    { 
        question: "He prevented me _____ going there.", 
        options: ["from", "of", "to", "at"], 
        answer: "from",
        explanation: "Prevent နှင့် တွဲဖက်သုံးသော Preposition မှာ 'from' ဖြစ်သည်။" 
    },
    { 
        question: "Thank you _____ your help.", 
        options: ["for", "with", "to", "of"], 
        answer: "for",
        explanation: "ကျေးဇူးတင်မှုကို ဖော်ပြရာတွင် Thank you 'for' ဟု သုံးရပါသည်။" 
    }
];
