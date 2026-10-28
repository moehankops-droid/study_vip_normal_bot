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
    },
    { 
        question: "She insisted _____ paying for the meal.", 
        options: ["on", "in", "at", "for"], 
        answer: "on",
        explanation: "'insist' နောက်တွင် Preposition 'on' ကို သုံးရပါသည်။" 
    },
    { 
        question: "I am looking forward to _____ you soon.", 
        options: ["see", "seeing", "seen", "saw"], 
        answer: "seeing",
        explanation: "'look forward to' နောက်တွင် Gerund (verb-ing) လိုက်ရပါသည်။" 
    },
    { 
        question: "The house was built _____ 1995.", 
        options: ["in", "on", "at", "by"], 
        answer: "in",
        explanation: "ခုနှစ်များ၏ ရှေ့တွင် Preposition 'in' ကို သုံးရပါသည်။" 
    },
    { 
        question: "Neither of the two answers _____ correct.", 
        options: ["is", "are", "were", "be"], 
        answer: "is",
        explanation: "'Neither of' ပြီးလျှင် Singular verb (is) ကို သုံးရပါသည်။" 
    },
    { 
        question: "He was accused _____ stealing the money.", 
        options: ["of", "for", "with", "by"], 
        answer: "of",
        explanation: "'accuse' ပြီးနောက် Preposition 'of' ကို သုံးရပါသည်။" 
    },
    { 
        question: "You had better _____ a doctor at once.", 
        options: ["see", "seeing", "saw", "seen"], 
        answer: "see",
        explanation: "'had better' နောက်တွင် Bare Infinitive (V1 - see) ကို သုံးရပါသည်။" 
    },
    { 
        question: "He speaks as if he _____ everything.", 
        options: ["knows", "knew", "has known", "knowing"], 
        answer: "knew",
        explanation: "မဖြစ်နိုင်သော အခြေအနေကို ဖော်ပြသည့် 'as if' နောက်တွင် Past tense (knew) သုံးရပါသည်။" 
    },
    { 
        question: "She succeeded _____ passing the examination.", 
        options: ["in", "on", "at", "with"], 
        answer: "in",
        explanation: "'succeed' ပြီးနောက် Preposition 'in' ကို သုံးရပါသည်။" 
    },
    { 
        question: "I would rather stay at home than _____ out tonight.", 
        options: ["go", "going", "went", "gone"], 
        answer: "go",
        explanation: "'would rather ... than' ပုံစံတွင် မူရင်း Verb (go) ကို သုံးရပါသည်။" 
    },
    { 
        question: "He is addicted _____ playing online games.", 
        options: ["to", "with", "in", "for"], 
        answer: "to",
        explanation: "'addicted' ပြီးနောက် Preposition 'to' ကို သုံးရပါသည်။" 
    },
    { 
        question: "Hardly had I arrived home _____ it started to rain.", 
        options: ["when", "than", "before", "after"], 
        answer: "when",
        explanation: "'Hardly... when' တွဲဖက်သုံးသော Correlative conjunction ဖြစ်ပါသည်။" 
    },
    { 
        question: "No sooner had we reached the station _____ the train departed.", 
        options: ["when", "than", "before", "then"], 
        answer: "than",
        explanation: "'No sooner... than' တွဲဖက်သုံးရပါသည်။" 
    },
    { 
        question: "She is too weak _____ walk.", 
        options: ["to", "for", "that", "so"], 
        answer: "to",
        explanation: "'too... to' ပုံစံအရ Adjective ပြီးနောက် 'to + V1' လိုက်ရပါသည်။" 
    },
    { 
        question: "He is so smart _____ he can solve any problem.", 
        options: ["that", "to", "as", "than"], 
        answer: "that",
        explanation: "'so... that' (အလွန်... ဖြစ်ေသာကြောင့်) ဆိုသည့် Result clause ဖြစ်သည်။" 
    },
    { 
        question: "Despite _____ hard, he didn't pass the exam.", 
        options: ["study", "studying", "studied", "studies"], 
        answer: "studying",
        explanation: "'Despite' ပြီးနောက် Gerund (studying) ကို သုံးရပါသည်။" 
    },
    { 
        question: "In spite _____ his illness, he went to work.", 
        options: ["of", "in", "on", "at"], 
        answer: "of",
        explanation: "'In spite of' သည် despite ကဲ့သို့ပင် အသေသုံး Preposition ဖြစ်သည်။" 
    },
    { 
        question: "He asked me where I _____.", 
        options: ["live", "lived", "am living", "living"], 
        answer: "lived",
        explanation: "Indirect Speech တွင် ရှေ့က Verb (asked) က Past ဖြစ်၍ နောက်က Tense လည်း Past (lived) ဖြစ်ရမည်။" 
    },
    { 
        question: "She told me that she _____ a new car.", 
        options: ["buy", "bought", "has bought", "is buying"], 
        answer: "bought",
        explanation: "Reporting verb က Past (told) ဖြစ်သောကြောင့် Past Tense (bought) သုံးရသည်။" 
    },
    { 
        question: "The teacher advised us _____ hard.", 
        options: ["study", "to study", "studying", "studied"], 
        answer: "to study",
        explanation: "'advise someone to do something' ပုံစံအရ Infinitive ('to study') ကို သုံးရသည်။" 
    },
    { 
        question: "My father made me _____ my room.", 
        options: ["clean", "to clean", "cleaning", "cleaned"], 
        answer: "clean",
        explanation: "'make' causative verb နောက်တွင် Bare Infinitive (clean) သုံးရသည်။" 
    },
    { 
        question: "If I _____ money, I would buy a new phone.", 
        options: ["have", "had", "has", "having"], 
        answer: "had",
        explanation: "Second Conditional ပုံစံ (If + V2, Subject + would + V1) ဖြစ်ပါသည်။" 
    },
    { 
        question: "Unless you hurry, you _____ miss the train.", 
        options: ["will", "won't", "can", "would"], 
        answer: "will",
        explanation: "'Unless' ပါသောဝါကျ၏ အဓိပ္ပာယ်မှာ မလုပ်ရင်ဖြစ်မည်ဆိုသည့် အနာဂတ်အခြေအနေဖြစ်၍ 'will' သုံးသည်။" 
    },
    { 
        question: "She speaks English as if she _____ a native speaker.", 
        options: ["is", "were", "be", "was"], 
        answer: "were",
        explanation: "'as if' ဖြင့် မဖြစ်နိုင်သော အခြေအနေကို ညွှန်ပြရာတွင် 'were' ကိုသာ အမြဲသုံးသည်။" 
    },
    { 
        question: "I wish I _____ how to swim.", 
        options: ["know", "knew", "known", "knowing"], 
        answer: "knew",
        explanation: "မဖြစ်နိုင်သော ဆန္ဒကိုဖော်ပြသည့် 'I wish' ပြီးနောက် Past tense (knew) သုံးရသည်။" 
    },
    { 
        question: "The boy _____ won the prize is my cousin.", 
        options: ["who", "which", "whom", "whose"], 
        answer: "who",
        explanation: "လူပုဂ္ဂိုလ် (Subject) ကို ကိုယ်စားပြုသော Relative Pronoun မှာ 'who' ဖြစ်သည်။" 
    },
    { 
        question: "This is the village _____ I was born.", 
        options: ["which", "where", "who", "when"], 
        answer: "where",
        explanation: "နေရာဌာန (Place) ကို ကိုယ်စားပြုသော Relative Pronoun မှာ 'where' ဖြစ်သည်။" 
    },
    { 
        question: "He is the person _____ opinion I respect most.", 
        options: ["who", "whom", "whose", "which"], 
        answer: "whose",
        explanation: "ပိုင်ဆိုင်မှုကိုပြသော Relative Pronoun မှာ 'whose' ဖြစ်သည်။" 
    },
    { 
        question: "The book _____ you lent me was very interesting.", 
        options: ["who", "whom", "which", "where"], 
        answer: "which",
        explanation: "ပစ္စည်းအရာဝတ္ထုကို ကိုယ်စားပြုသော Relative Pronoun မှာ 'which' ဖြစ်သည်။" 
    },
    { 
        question: "She is used _____ early in the morning.", 
        options: ["to get up", "to getting up", "get up", "getting up"], 
        answer: "to getting up",
        explanation: "'be used to' ပြီးနောက် Gerund (getting up) ကို အသုံးပြုရပါသည်။" 
    },
    { 
        question: "He used to _____ cigarettes, but he stopped now.", 
        options: ["smoke", "smoking", "smoked", "be smoking"], 
        answer: "smoke",
        explanation: "အတိတ်က လုပ်လေ့ရှိခဲ့မှုကိုပြသည့် 'used to' ပြီးနောက် Verb မူရင်း (smoke) လိုက်ရသည်။" 
    },
    { 
        question: "Neither of the boys _____ completed the task.", 
        options: ["has", "have", "are", "were"], 
        answer: "has",
        explanation: "'Neither of' ပြီးနောက် Singular verb (has) ကို အသုံးပြုရပါသည်။" 
    },
    { 
        question: "All the money _____ been spent.", 
        options: ["has", "have", "are", "were"], 
        answer: "has",
        explanation: "'Money' သည် Uncountable noun ဖြစ်၍ Singular verb (has) ကို သုံးရသည်။" 
    },
    { 
        question: "Measles _____ a dangerous disease for children.", 
        options: ["is", "are", "were", "have"], 
        answer: "is",
        explanation: "ရောဂါအမည်များ ('Measles') သည် ပုံစံအဆစ်ပါသော်လည်း Singular (is) ဖြစ်သည်။" 
    },
    { 
        question: "A number of students _____ absent today.", 
        options: ["is", "are", "was", "has"], 
        answer: "are",
        explanation: "'A number of' ပြီးနောက် Plural verb ('are') ကို သုံးရပါသည်။" 
    },
    { 
        question: "The number of students in our class _____ forty.", 
        options: ["is", "are", "were", "have"], 
        answer: "is",
        explanation: "'The number of' ၏ Subject မှာ 'The number' ဖြစ်၍ Singular verb ('is') သုံးရသည်။" 
    },
    { 
        question: "Scarcely had we stepped outside _____ it began to rain.", 
        options: ["when", "than", "before", "after"], 
        answer: "when",
        explanation: "'Scarcely... when' တွဲဖက်သုံးသော Correlative conjunction ဖြစ်သည်။" 
    },
    { 
        question: "Seldom _____ I seen such a beautiful sunset.", 
        options: ["have", "has", "do", "did"], 
        answer: "have",
        explanation: "ဝါကျရှေ့ဆုံးတွင် Negative adverb ('Seldom') ပါလာပါက Inversion ဖြစ်၍ 'have I seen' ဖြစ်ရမည်။" 
    },
    { 
        question: "Not only he but also his friends _____ coming.", 
        options: ["is", "are", "was", "has"], 
        answer: "are",
        explanation: "'Not only... but also' တွင် verb သည် နီးစပ်ရာ Subject ('friends' - Plural) နှင့် လိုက်ဖက်ရမည်။" 
    },
    { 
        question: "The captain along with his crew members _____ drowned.", 
        options: ["was", "were", "is", "are"], 
        answer: "was",
        explanation: "'along with' ဖြင့် ဆက်ထားပါက ရှေ့ဆုံး Subject ('captain' - Singular) ကိုသာ မူတည်ရသည်။" 
    },
    { 
        question: "Each boy and each girl _____ given a prize.", 
        options: ["was", "were", "are", "have"], 
        answer: "was",
        explanation: "'Each' ဖြင့် သီးသန့်စီ ချိတ်ဆက်ထားသောကြောင့် Singular verb ('was') သုံးရသည်။" 
    }
];
