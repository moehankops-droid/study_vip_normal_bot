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
        question: "A person who writes books is called a _____.", 
        options: ["teacher", "doctor", "writer", "driver"], 
        answer: "writer",
        explanation: "စာအုပ်ရေးသူကို 'writer' (စာရေးဆရာ) ဟု ခေါ်သည်။" 
    },
    { 
        question: "The opposite of 'cold' is _____.", 
        options: ["cool", "warm", "hot", "freezing"], 
        answer: "hot",
        explanation: "'cold' (အေးသော) ၏ ဆန့်ကျင်ဘက်မှာ 'hot' (ပူသော) ဖြစ်သည်။" 
    },
    { 
        question: "We use a pen for _____.", 
        options: ["eating", "writing", "sleeping", "running"], 
        answer: "writing",
        explanation: "ဖောင်တိန်ကို စာရေးရန်အတွက် အသုံးပြုသည်။" 
    },
    { 
        question: "She _____ her breakfast before she went to school.", 
        options: ["eat", "ate", "had eaten", "has eaten"], 
        answer: "had eaten",
        explanation: "အတိတ်တွင် ပထမဆုံးပြီးဆုံးခဲ့သောလုပ်ရပ်ဖြစ်၍ Past Perfect Tense သုံးရသည်။" 
    },
    { 
        question: "If it rains, we _____ at home.", 
        options: ["stay", "stayed", "will stay", "would stay"], 
        answer: "will stay",
        explanation: "First Conditional ဖြစ်၍ main clause တွင် 'will + V1' ဖြစ်သည်။" 
    },
    { 
        question: "He is the _____ boy in our class.", 
        options: ["tall", "taller", "tallest", "more tall"], 
        answer: "tallest",
        explanation: "အမြင့်ဆုံးဖြစ်ကြောင်း ညွှန်းဆိုသော Superlative ဖြစ်သည်။" 
    },
    { 
        question: "This book belongs _____ me.", 
        options: ["to", "for", "with", "at"], 
        answer: "to",
        explanation: "'belong' နောက်တွင် 'to' ဖြင့် တွဲသုံးရသည်။" 
    },
    { 
        question: "I have known him _____ five years.", 
        options: ["since", "for", "from", "during"], 
        answer: "for",
        explanation: "အချိန်ကာလ ကြာမြင့်ချိန်ကို ဖော်ပြရာတွင် 'for' ကို သုံးသည်။" 
    },
    { 
        question: "She has lived here _____ 2020.", 
        options: ["since", "for", "from", "in"], 
        answer: "since",
        explanation: "စတင်သည့်အချိန်အတိအကျကို ဖော်ပြရန် 'since' ကို သုံးသည်။" 
    },
    { 
        question: "He speaks English very _____.", 
        options: ["good", "better", "well", "best"], 
        answer: "well",
        explanation: "Verb ကိုထူးပြုသောကြောင့် Adverb ဖြစ်သည့် 'well' ကို သုံးရသည်။" 
    },
    { 
        question: "Mount Everest is the _____ mountain in the world.", 
        options: ["high", "higher", "highest", "most high"], 
        answer: "highest",
        explanation: "အမြင့်ဆုံးတောင်ဖြစ်၍ Superlative 'highest' ဖြစ်သည်။" 
    },
    { 
        question: "Neither John nor his brothers _____ present yesterday.", 
        options: ["was", "were", "is", "are"], 
        answer: "were",
        explanation: "နီးစပ်ရာ subject ဖြစ်သော 'brothers' (plural) နှင့် လိုက်လျောညီထွေရှိရမည်။" 
    },
    { 
        question: "Bread and butter _____ my favorite breakfast.", 
        options: ["is", "are", "were", "be"], 
        answer: "is",
        explanation: "အစားအစာတစ်ခုတည်းအဖြစ် ယူဆသော Singular Idea ဖြစ်၍ 'is' ဖြစ်သည်။" 
    },
    { 
        question: "Open the door, _____?", 
        options: ["do you", "will you", "don't you", "aren't you"], 
        answer: "will you",
        explanation: "Imperative sentence ၏ Question Tag မှာ 'will you' ဖြစ်သည်။" 
    },
    { 
        question: "Let's go for a walk, _____?", 
        options: ["shall we", "will you", "don't we", "let us"], 
        answer: "shall we",
        explanation: "'Let's' ပါသောဝါကျ၏ Question Tag မှာ 'shall we' ဖြစ်သည်။" 
    },
    { 
        question: "She is afraid _____ spiders.", 
        options: ["of", "from", "with", "at"], 
        answer: "of",
        explanation: "'afraid' နောက်တွင် 'of' ဖြင့် တွဲသုံးရသည်။" 
    },
    { 
        question: "He congratulated me _____ my success.", 
        options: ["for", "on", "at", "in"], 
        answer: "on",
        explanation: "ဂုဏ်ပြုသည်ကို ဖော်ပြရာတွင် 'congratulate on' ဟု သုံးသည်။" 
    },
    { 
        question: "By this time tomorrow, we _____ our exam.", 
        options: ["finish", "will finish", "will have finished", "finished"], 
        answer: "will have finished",
        explanation: "အနာဂတ်အချိန်တစ်ခုမတိုင်မီ ပြီးစီးမည့်လုပ်ရပ်ဖြစ်၍ Future Perfect ဖြစ်သည်။" 
    },
    { 
        question: "Physics _____ my favorite subject.", 
        options: ["is", "are", "were", "have"], 
        answer: "is",
        explanation: "ဘာသာရပ်အမည်ဖြစ်၍ ပုံစံအဆစ်ပါသော်လည်း Singular အဖြစ် 'is' သုံးသည်။" 
    },
    { 
        question: "The news _____ true.", 
        options: ["is", "are", "were", "have been"], 
        answer: "is",
        explanation: "'news' သည် uncountable noun ဖြစ်ပြီး Singular ယူသည်။" 
    },
    { 
        question: "She sings _____ than her sister.", 
        options: ["sweet", "sweeter", "sweetly", "more sweetly"], 
        answer: "more sweetly",
        explanation: "Adverb ၏ Comparative form ဖြစ်၍ 'more sweetly' ဖြစ်သည်။" 
    },
    { 
        question: "He runs as _____ as a deer.", 
        options: ["fast", "faster", "fastest", "more fast"], 
        answer: "fast",
        explanation: "'as... as' ကြားတွင် Positive degree ဖြစ်သည့် 'fast' ကို သုံးရသည်။" 
    },
    { 
        question: "One of the boys _____ absent today.", 
        options: ["is", "are", "were", "have"], 
        answer: "is",
        explanation: "'One of' ပြီးနောက် plural noun လာသော်လည်း verb သည် 'One' ကိုမူတည်၍ Singular ယူသည်။" 
    },
    { 
        question: "Each of the students _____ a book.", 
        options: ["has", "have", "are having", "were"], 
        answer: "has",
        explanation: "'Each' သည် Singular အဖြစ် ခံယူသောကြောင့် 'has' ကို သုံးရသည်။" 
    },
    { 
        question: "The jury _____ divided in their opinions.", 
        options: ["was", "were", "is", "has"], 
        answer: "were",
        explanation: "အဖွဲ့ဝင်ချင်း သဘောကွဲလွဲနေသဖြင့် Plural verb 'were' ကို သုံးရသည်။" 
    },
    { 
        question: "Ten miles _____ a long distance to walk.", 
        options: ["is", "are", "were", "have"], 
        answer: "is",
        explanation: "အကွာအဝေးပမာဏတစ်ခုလုံးကို စုစုပေါင်း Singular အဖြစ် သတ်မှတ်သည်။" 
    },
    { 
        question: "He is senior _____ me in service.", 
        options: ["than", "to", "from", "with"], 
        answer: "to",
        explanation: "Latin comparative များနှင့်အတူ 'than' အစား 'to' ကို သုံးရသည်။" 
    },
    { 
        question: "Prevention is better _____ cure.", 
        options: ["then", "than", "to", "as"], 
        answer: "than",
        explanation: "စကားပုံနှိုင်းယှဉ်ချက်တွင် 'better than' ဟု သုံးသည်။" 
    }
];
