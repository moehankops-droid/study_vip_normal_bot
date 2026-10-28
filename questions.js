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
    {
        question: "She _____ to the market every morning.",
        options: ["go", "goes", "going", "gone"],
        answer: "goes",
        explanation: "Present Simple Tense ဖြစ်ပြီး Subject 'She' က Singular ဖြစ်သောကြောင့် verb မှာ 's' ထည့်ရပါမည်။"
    },
    {
        question: "They _____ football in the yard right now.",
        options: ["play", "plays", "are playing", "played"],
        answer: "are playing",
        explanation: "Right now ပါရှိသဖြင့် Present Continuous Tense (are + verb-ing) ကို သုံးရပါမည်။"
    },
    {
        question: "I _____ this movie yesterday.",
        options: ["watch", "watches", "watched", "am watching"],
        answer: "watched",
        explanation: "Yesterday (မနေ့က) ဟု အရင်အချိန်ကို ညွှန်ပြနေသဖြင့် Past Simple Tense (V2 - watched) ကို သုံးရပါမည်။"
    },
    {
        question: "If I were a bird, I _____ fly across the world.",
        options: ["will", "would", "can", "shall"],
        answer: "would",
        explanation: "Second Conditional ပုံစံ (If + V2, Subject + would + V1) ဖြစ်ပါသည်။"
    },
    {
        question: "He has _____ his homework already.",
        options: ["do", "did", "doing", "done"],
        answer: "done",
        explanation: "Present Perfect Tense (has/have + V3) ဖြစ်သဖြင့် 'done' (V3) ကို သုံးရပါမည်။"
    },
    {
        question: "The sun _____ in the east.",
        options: ["rise", "rises", "rose", "is rising"],
        answer: "rises",
        explanation: "အမြဲမှန်ကန်နေသော သဘာဝတရားဖြစ်၍ Present Simple Tense (rises) ကို သုံးရပါသည်။"
    },
    {
        question: "Look! The baby _____.",
        options: ["sleep", "sleeps", "is sleeping", "slept"],
        answer: "is sleeping",
        explanation: "Look! ဟု အာရုံစိုက်ခိုင်းနေချိန်တွင် ဖြစ်ပျက်နေသောလုပ်ရပ်ဖြစ်၍ Present Continuous ကို သုံးရပါသည်။"
    },
    {
        question: "Water _____ at 100 degrees Celsius.",
        options: ["boil", "boils", "boiled", "is boiling"],
        answer: "boils",
        explanation: "သိပ္ပံနည်းကျ အမှန်တရားဖြစ်သဖြင့် Present Simple Tense (boils) ဖြစ်သည်။"
    },
    {
        question: "She is _____ than her sister.",
        options: ["tall", "taller", "tallest", "more tall"],
        answer: "taller",
        explanation: "နှိုင်းယှဉ်ပြခြင်း (Comparative degree) ဖြစ်၍ adjective ပုံစံတွင် 'er' ထည့်ရပါမည်။"
    },
    {
        question: "Mount Everest is the _____ mountain in the world.",
        options: ["high", "higher", "highest", "most high"],
        answer: "highest",
        explanation: "အမြင့်ဆုံးဟု အများစုထဲမှ ရွေးချယ်နှိုင်းယှဉ်ခြင်း (Superlative degree) ဖြစ်၍ 'est' ထည့်ရပါသည်။"
    },
    {
        question: "She sings very _____.",
        options: ["good", "well", "better", "best"],
        answer: "well",
        explanation: "Verb (sings) ကို ညွှန်ပြmodify လုပ်ရန် Adverb ('well') ကို သုံးရပါသည်။"
    },
    {
        question: "This book is _____ than that one.",
        options: ["interesting", "more interesting", "most interesting", "interest"],
        answer: "more interesting",
        explanation: "နာမ်ပုဒ်ရှည် (adjective with 2+ syllables) များကို နှိုင်းယှဉ်လျှင် 'more' ထည့်ရပါသည်။"
    },
    {
        question: "He didn't _____ to school yesterday.",
        options: ["went", "go", "goes", "gone"],
        answer: "go",
        explanation: "Did/Didn't ပြီးပါက Verb မူရင်း (V1 - go) ကိုသာ ပြန်သုံးရပါသည်။"
    },
    {
        question: "Have you ever _____ to Yangon?",
        options: ["be", "was", "been", "go"],
        answer: "been",
        explanation: "Present Perfect Tense မေးခွန်းဖြစ်၍ 'be' ၏ V3 ဖြစ်သော 'been' ကို သုံးရပါသည်။"
    },
    {
        question: "The letter was _____ by John.",
        options: ["write", "wrote", "written", "writing"],
        answer: "written",
        explanation: "Passive Voice ပုံစံ (was/were + V3) ဖြစ်၍ 'written' ကို သုံးရပါသည်။"
    },
    {
        question: "She is interested _____ learning English.",
        options: ["in", "on", "at", "with"],
        answer: "in",
        explanation: "Interested နှင့် တွဲဖက်သုံးသော Preposition မှာ 'in' ဖြစ်ပါသည်။"
    },
    {
        question: "Cats are afraid _____ dogs.",
        options: ["of", "from", "with", "at"],
        answer: "of",
        explanation: "Afraid နှင့် တွဲသုံးသော Preposition မှာ 'of' ဖြစ်သည်။"
    },
    {
        question: "He is good _____ playing chess.",
        options: ["in", "on", "at", "with"],
        answer: "at",
        explanation: "ကျွမ်းကျင်မှုကိုဖော်ပြသော good နှင့် တွဲသုံးသည်မှာ 'at' ဖြစ်ပါသည်။"
    },
    {
        question: "She has been living here _____ five years.",
        options: ["since", "for", "from", "during"],
        answer: "for",
        explanation: "ကာလအပိုင်းအခြား (Duration - 5 years) ကိုပြလျှင် 'for' ကို သုံးရပါသည်။"
    },
    {
        question: "I have known him _____ 2020.",
        options: ["for", "since", "from", "in"],
        answer: "since",
        explanation: "စတင်သည့် အချိန်အတိအကျ (Point of time - 2020) ကိုပြလျှင် 'since' ကို သုံးရသည်။"
    },
    {
        question: "Neither John _____ Mary is coming.",
        options: ["or", "nor", "and", "but"],
        answer: "nor",
        explanation: "Neither နှင့် တွဲဖက်သုံးသော conjunction မှာ 'nor' ဖြစ်ပါသည်။"
    },
    {
        question: "Either you _____ he has to go.",
        options: ["and", "nor", "or", "but"],
        answer: "or",
        explanation: "Either နှင့် တွဲဖက်သုံးသည်မှာ 'or' ဖြစ်ပါသည်။"
    },
    {
        question: "She speaks English very _____.",
        options: ["fluent", "fluently", "fluency", "more fluent"],
        answer: "fluently",
        explanation: "စကားပြောပုံကို ညွှန်ပြရန် Adverb ('fluently') လိုအပ်ပါသည်။"
    },
    {
        question: "He is _____ honest man.",
        options: ["a", "an", "the", "no article"],
        answer: "an",
        explanation: "Honest ၏ အသံထွက်မှာ သရအသံ (အို-နက်) ဖြစ်သောကြောင့် 'an' ကို သုံးရပါသည်။"
    },
    {
        question: "I saw _____ elephant at the zoo.",
        options: ["a", "an", "the", "none"],
        answer: "an",
        explanation: "Elephant သည် သရသံဖြင့် စတင်သောကြောင့် 'an' သုံးရပါသည်။"
    },
    {
        question: "She bought _____ new car yesterday.",
        options: ["a", "an", "the", "some"],
        answer: "a",
        explanation: "Consonant (ဗျည်းသံ) ဖြင့်စတင်ပြီး တစ်ခုတည်းကို ရည်ညွှန်းသဖြင့် 'a' သုံးရသည်။"
    },
    {
        question: "The police _____ looking for the thief.",
        options: ["is", "are", "was", "has"],
        answer: "are",
        explanation: "Police သည် Plural noun (အများကိန်း) သဘောဆောင်သဖြင့် 'are' ကို သုံးရပါသည်။"
    },
    {
        question: "Mathematics _____ my favorite subject.",
        options: ["is", "are", "were", "have"],
        answer: "is",
        explanation: "ဘာသာရပ်အမည်များသည် ပုံစံအားဖြင့် အများကိန်းပုံပေါ်သော်လည်း အနက်အားဖြင့် Singular ဖြစ်၍ 'is' သုံးသည်။"
    },
    {
        question: "A group of students _____ playing outside.",
        options: ["is", "are", "were", "have"],
        answer: "is",
        explanation: "Subject အဓိက ခေါင်းစဉ်မှာ 'A group' (Singular) ဖြစ်သောကြောင့် 'is' သုံးရပါသည်။"
    },
    {
        question: "Each of the boys _____ a prize.",
        options: ["get", "gets", "are getting", "have got"],
        answer: "gets",
        explanation: "Each ဖြင့်စတင်သော Subject များသည် Singular သဘောဖြစ်၍ Verb မှာ 's' ပါရပါမည်။"
    },
    {
        question: "Bread and butter _____ my daily breakfast.",
        options: ["is", "are", "were", "be"],
        answer: "is",
        explanation: "တွဲဖက်စားသုံးလေ့ရှိသော အစားအစာတစ်ခုတည်းကို ညွှန်ပြသဖြင့် Singular (is) အဖြစ် သတ်မှတ်သည်။"
    },
    {
        question: "My scissors _____ on the table.",
        options: ["is", "are", "has", "was"],
        answer: "are",
        explanation: "Scissors ကဲ့သို့ နှစ်ခြမ်းပါသော ပစ္စည်းများကို အများကိန်း (are) ဟོ သတ်မှတ်သည်။"
    },
    {
        question: "Ten miles _____ a long distance to walk.",
        options: ["is", "are", "were", "have"],
        answer: "is",
        explanation: "အကွာအဝေး၊ ပမာဏ၊ အချိန်တို့ကို တစ်ခုတည်းသော ပမာဏအဖြစ် ယူဆ၍ Singular (is) သုံးသည်။"
    },
    {
        question: "Neither of them _____ the answer.",
        options: ["know", "knows", "are knowing", "known"],
        answer: "knows",
        explanation: "Neither of ပြီးနောက် Singular verb (knows) ကို သုံးရပါသည်။"
    },
    {
        question: "Who _____ the window?",
        options: ["break", "broke", "broken", "breaking"],
        answer: "broke",
        explanation: "အတိတ်တွင် ပြီးမြောက်သွားသော အလုပ်အတွက် Past tense (broke) သုံးရပါသည်။"
    },
    {
        question: "This is the house _____ I was born.",
        options: ["which", "where", "who", "when"],
        answer: "where",
        explanation: "နေရာဌာန (Place) ကို ကိုယ်စားပြုသော Relative Pronoun မှာ 'where' ဖြစ်သည်။"
    },
    {
        question: "The man _____ stole the car was caught.",
        options: ["which", "who", "whom", "whose"],
        answer: "who",
        explanation: "လူပုဂ္ဂိုလ် (Subject) ကို ကိုယ်စားပြုသော Relative pronoun မှာ 'who' ဖြစ်သည်။"
    },
    {
        question: "She asked me where I _____.",
        options: ["live", "lived", "am living", "living"],
        answer: "lived",
        explanation: "Indirect Speech ဖြစ်သောကြောင့် ရှေ့ Verb (asked - Past) နှင့် လိုက်ဖက်အောင် Past tense (lived) သုံးရသည်။"
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
