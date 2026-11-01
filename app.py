import streamlit as st
import random
import json
from datetime import datetime

# ──────────────────────────────────────────────────────────────
# Page configuration
# ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Jessica's English Learning Guide",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────────────────────
# Custom CSS for a polished, welcoming look
# ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Global */
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Merriweather:wght@400;700&display=swap');

    .main .block-container { padding-top: 1rem; max-width: 1100px; }

    /* Hero banner */
    .hero-banner {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 18px;
        padding: 2.5rem 2rem;
        color: white;
        text-align: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px rgba(102,126,234,.35);
    }
    .hero-banner h1 {
        font-family: 'Nunito', sans-serif;
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: .4rem;
    }
    .hero-banner p {
        font-size: 1.1rem;
        opacity: .92;
    }

    /* Section cards */
    .section-card {
        background: #ffffff;
        border-radius: 14px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        border-left: 5px solid #667eea;
        box-shadow: 0 2px 12px rgba(0,0,0,.06);
    }
    .section-card h3 {
        font-family: 'Nunito', sans-serif;
        color: #4a4a6a;
        margin-top: 0;
    }

    /* Lesson card */
    .lesson-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
    }
    .lesson-card h4 { margin-top: 0; color: #3d3d5c; }

    /* Story card */
    .story-box {
        background: #fffbf0;
        border: 2px solid #f0e6d2;
        border-radius: 14px;
        padding: 1.5rem;
        font-family: 'Merriweather', serif;
        font-size: 1.05rem;
        line-height: 1.9;
        margin-bottom: 1rem;
    }

    /* Quiz option highlight */
    .quiz-correct {
        background: #d4edda;
        border-left: 4px solid #28a745;
        padding: .6rem 1rem;
        border-radius: 6px;
        margin: .3rem 0;
    }
    .quiz-wrong {
        background: #f8d7da;
        border-left: 4px solid #dc3545;
        padding: .6rem 1rem;
        border-radius: 6px;
        margin: .3rem 0;
    }

    /* Level badges */
    .badge-beginner {
        display: inline-block;
        background: #28a745;
        color: white;
        padding: 3px 12px;
        border-radius: 20px;
        font-size: .82rem;
        font-weight: 700;
    }
    .badge-intermediate {
        display: inline-block;
        background: #ffc107;
        color: #333;
        padding: 3px 12px;
        border-radius: 20px;
        font-size: .82rem;
        font-weight: 700;
    }
    .badge-advanced {
        display: inline-block;
        background: #dc3545;
        color: white;
        padding: 3px 12px;
        border-radius: 20px;
        font-size: .82rem;
        font-weight: 700;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f8f9ff 0%, #eef1ff 100%);
    }
    section[data-testid="stSidebar"] h1 {
        font-family: 'Nunito', sans-serif;
        font-size: 1.3rem;
        color: #4a4a6a;
    }

    /* Metric cards */
    .metric-row {
        display: flex; gap: 1rem; margin-bottom: 1.2rem; flex-wrap: wrap;
    }
    .metric-card {
        flex: 1; min-width: 140px;
        background: white;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 2px 10px rgba(0,0,0,.06);
    }
    .metric-card .num {
        font-size: 1.8rem; font-weight: 800; color: #667eea;
    }
    .metric-card .label {
        font-size: .85rem; color: #888;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0 1rem;
        color: #aaa;
        font-size: .85rem;
    }
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────
# Session-state defaults
# ──────────────────────────────────────────────────────────────
defaults = {
    "quiz_score": 0,
    "quiz_total": 0,
    "writing_submissions": [],
    "current_quiz": None,
    "vocab_index": 0,
    "reading_level": "Beginner",
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ──────────────────────────────────────────────────────────────
# DATA — Lessons, stories, vocabulary, quizzes
# ──────────────────────────────────────────────────────────────

ALPHABET_DATA = [
    ("A a", "Apple 🍎", "/æ/ as in **a**pple"),
    ("B b", "Ball ⚽", "/b/ as in **b**all"),
    ("C c", "Cat 🐱", "/k/ as in **c**at"),
    ("D d", "Dog 🐶", "/d/ as in **d**og"),
    ("E e", "Egg 🥚", "/ɛ/ as in **e**gg"),
    ("F f", "Fish 🐟", "/f/ as in **f**ish"),
    ("G g", "Goat 🐐", "/ɡ/ as in **g**oat"),
    ("H h", "Hat 🎩", "/h/ as in **h**at"),
    ("I i", "Ice cream 🍦", "/ɪ/ as in **i**ce cream"),
    ("J j", "Juice 🧃", "/dʒ/ as in **j**uice"),
    ("K k", "Kite 🪁", "/k/ as in **k**ite"),
    ("L l", "Lion 🦁", "/l/ as in **l**ion"),
    ("M m", "Moon 🌙", "/m/ as in **m**oon"),
    ("N n", "Nest 🪺", "/n/ as in **n**est"),
    ("O o", "Orange 🍊", "/ɒ/ as in **o**range"),
    ("P p", "Pen 🖊️", "/p/ as in **p**en"),
    ("Q q", "Queen 👑", "/kw/ as in **q**ueen"),
    ("R r", "Rain 🌧️", "/r/ as in **r**ain"),
    ("S s", "Sun ☀️", "/s/ as in **s**un"),
    ("T t", "Tree 🌳", "/t/ as in **t**ree"),
    ("U u", "Umbrella ☂️", "/ʌ/ as in **u**mbrella"),
    ("V v", "Violin 🎻", "/v/ as in **v**iolin"),
    ("W w", "Water 💧", "/w/ as in **w**ater"),
    ("X x", "X-ray 🩻", "/ks/ as in bo**x**"),
    ("Y y", "Yellow 💛", "/j/ as in **y**ellow"),
    ("Z z", "Zebra 🦓", "/z/ as in **z**ebra"),
]

GRAMMAR_LESSONS = {
    "Beginner": [
        {
            "title": "1. Nouns — Naming Words",
            "content": """
**What is a noun?** A noun is a word that names a person, place, thing, or idea.

**Examples:**
| Type | Examples |
|------|----------|
| Person | teacher, doctor, Jessica, mother |
| Place | school, park, London, kitchen |
| Thing | book, chair, phone, apple |
| Idea | love, happiness, freedom, education |

**Practice:** Look around you right now. Can you name 5 things you see? Those are all nouns!

**Singular & Plural:**
- One **book** → Two **books**
- One **box** → Two **boxes**
- One **baby** → Two **babies**
- One **child** → Two **children** (irregular)
""",
        },
        {
            "title": "2. Pronouns — Words That Replace Nouns",
            "content": """
**Pronouns** take the place of nouns so we don't repeat the same word.

| Subject | Object | Possessive |
|---------|--------|------------|
| I | me | my / mine |
| you | you | your / yours |
| he | him | his |
| she | her | her / hers |
| it | it | its |
| we | us | our / ours |
| they | them | their / theirs |

**Example:**
- ❌ *Jessica likes Jessica's cat. Jessica plays with Jessica's cat every day.*
- ✅ *Jessica likes **her** cat. **She** plays with **it** every day.*
""",
        },
        {
            "title": "3. Verbs — Action Words",
            "content": """
**Verbs** tell us what someone or something **does**.

**Common verbs:** eat, drink, run, walk, read, write, speak, listen, sleep, play

**The verb "to be"** is special and very important:

| Subject | Present | Past |
|---------|---------|------|
| I | am | was |
| you | are | were |
| he/she/it | is | was |
| we/they | are | were |

**Examples:**
- I **am** a student.
- She **reads** a book every day.
- They **played** football yesterday.
""",
        },
        {
            "title": "4. Simple Sentences",
            "content": """
A **sentence** is a group of words that expresses a complete thought.

**Every sentence needs:**
1. A **subject** (who or what)
2. A **verb** (action or state)

**Basic pattern:** Subject + Verb + Object

| Subject | Verb | Object |
|---------|------|--------|
| I | eat | breakfast |
| She | reads | books |
| They | play | football |
| The cat | drinks | milk |

**Types of sentences:**
- **Statement:** The sun is bright.
- **Question:** Is the sun bright?
- **Exclamation:** How bright the sun is!
- **Command:** Close the door.
""",
        },
        {
            "title": "5. Articles — A, An, The",
            "content": """
**Articles** come before nouns.

| Article | When to Use | Example |
|---------|-------------|---------|
| **a** | Before consonant sounds (first mention) | **a** book, **a** cat |
| **an** | Before vowel sounds (first mention) | **an** apple, **an** egg |
| **the** | When we know which one | **the** sun, **the** book on the table |

**Tips:**
- Use **a/an** when talking about something for the **first time**.
- Use **the** when both speaker and listener know **which one**.
- Some things always use **the**: the sun, the moon, the sky, the internet.

**Example:**
> I saw **a** dog in the park. **The** dog was very friendly.
""",
        },
    ],
    "Intermediate": [
        {
            "title": "1. Tenses — Past, Present, Future",
            "content": """
**English has 12 main tenses.** Let's learn the most important ones:

### Present Tenses
| Tense | Structure | Example | Use |
|-------|-----------|---------|-----|
| Simple Present | Subject + V(s/es) | She **reads** every day. | Habits, facts |
| Present Continuous | am/is/are + V-ing | She **is reading** now. | Happening now |
| Present Perfect | have/has + past participle | She **has read** 3 books. | Past → present connection |

### Past Tenses
| Tense | Structure | Example | Use |
|-------|-----------|---------|-----|
| Simple Past | Subject + V-ed/irregular | She **read** yesterday. | Completed past action |
| Past Continuous | was/were + V-ing | She **was reading** at 8 PM. | Ongoing past action |

### Future Tenses
| Tense | Structure | Example | Use |
|-------|-----------|---------|-----|
| Simple Future | will + V | She **will read** tomorrow. | Future plans/predictions |
| Going to | am/is/are going to + V | She **is going to read** tonight. | Planned intentions |
""",
        },
        {
            "title": "2. Adjectives & Adverbs",
            "content": """
### Adjectives (describe nouns)
- The **tall** man. / A **beautiful** flower. / The sky is **blue**.

**Order of adjectives:** Opinion → Size → Age → Shape → Color → Origin → Material
> A **lovely little old rectangular green French silver** box.

### Adverbs (describe verbs, adjectives, or other adverbs)
- She runs **quickly**. / He is **very** tall. / She sings **beautifully**.

**Common adverb types:**
| Type | Examples |
|------|----------|
| Manner (how?) | slowly, carefully, happily |
| Time (when?) | yesterday, now, soon |
| Place (where?) | here, there, everywhere |
| Frequency (how often?) | always, never, sometimes |

**Tip:** Many adverbs are formed by adding **-ly** to an adjective:
slow → slow**ly**, careful → careful**ly**, happy → happi**ly**
""",
        },
        {
            "title": "3. Prepositions",
            "content": """
**Prepositions** show the relationship between words (position, time, direction).

### Place Prepositions
| Preposition | Meaning | Example |
|-------------|---------|---------|
| in | inside | The cat is **in** the box. |
| on | surface | The book is **on** the table. |
| at | specific point | I am **at** school. |
| between | in the middle | The park is **between** the bank and the shop. |
| under | below | The dog is **under** the bed. |
| behind | at the back | The garden is **behind** the house. |

### Time Prepositions
| Preposition | Use With | Example |
|-------------|----------|---------|
| in | months, years, seasons | **in** January, **in** 2024, **in** summer |
| on | days, dates | **on** Monday, **on** July 4th |
| at | clock times, festivals | **at** 3 PM, **at** Christmas |
""",
        },
        {
            "title": "4. Conjunctions — Joining Words",
            "content": """
**Conjunctions** connect words, phrases, or sentences.

### Coordinating Conjunctions (FANBOYS)
| Conjunction | Use | Example |
|-------------|-----|---------|
| **F**or | reason | I stayed home, **for** it was raining. |
| **A**nd | addition | I like tea **and** coffee. |
| **N**or | negative addition | I don't like tea, **nor** do I like coffee. |
| **B**ut | contrast | I'm tired **but** happy. |
| **O**r | choice | Do you want tea **or** coffee? |
| **Y**et | contrast | It's small **yet** powerful. |
| **S**o | result | It rained, **so** I stayed home. |

### Subordinating Conjunctions
**because, although, if, when, while, before, after, until, since**

> I study English **because** I want to travel.
> **Although** it was raining, we went for a walk.
> **If** you study hard, you **will** pass the exam.
""",
        },
    ],
    "Advanced": [
        {
            "title": "1. Conditional Sentences",
            "content": """
### The Four Conditionals

| Type | If Clause | Main Clause | Example |
|------|-----------|-------------|---------|
| **Zero** (facts) | If + present | present | If you heat water to 100°C, it **boils**. |
| **First** (possible) | If + present | will + verb | If it **rains**, I **will stay** home. |
| **Second** (unlikely) | If + past | would + verb | If I **had** a million dollars, I **would travel**. |
| **Third** (impossible past) | If + had + past participle | would have + past participle | If I **had studied**, I **would have passed**. |

### Mixed Conditionals
Past condition → present result:
> If I **had studied** medicine (past), I **would be** a doctor now (present).

Present condition → past result:
> If I **were** braver (present), I **would have spoken** up (past).
""",
        },
        {
            "title": "2. Passive Voice",
            "content": """
In **passive voice**, the object of the action becomes the subject of the sentence.

**Active → Passive pattern:** Object + be (conjugated) + past participle (+ by agent)

| Tense | Active | Passive |
|-------|--------|---------|
| Simple Present | She **writes** letters. | Letters **are written** (by her). |
| Simple Past | She **wrote** a letter. | A letter **was written** (by her). |
| Present Perfect | She **has written** a letter. | A letter **has been written**. |
| Future | She **will write** a letter. | A letter **will be written**. |
| Modal | She **can write** letters. | Letters **can be written**. |

**When to use passive voice:**
- The doer is unknown: *My car **was stolen**.* 
- The action is more important than the doer: *The bridge **was built** in 1990.*
- In formal/scientific writing: *The experiment **was conducted** twice.*
""",
        },
        {
            "title": "3. Reported Speech",
            "content": """
**Reported (indirect) speech** tells what someone said without quoting exact words.

### Tense Changes in Reported Speech
| Direct Speech | Reported Speech |
|---------------|-----------------|
| "I **am** happy." | She said she **was** happy. |
| "I **like** pizza." | He said he **liked** pizza. |
| "I **will** come." | She said she **would** come. |
| "I **can** swim." | He said he **could** swim. |
| "I **have finished**." | She said she **had finished**. |

### Other Changes
| Direct | Reported |
|--------|----------|
| today | that day |
| tomorrow | the next day |
| yesterday | the day before |
| here | there |
| this | that |
| now | then |

**Reporting questions:**
- "Where do you live?" → She asked where I **lived**.
- "Are you happy?" → He asked if/whether I **was** happy.
""",
        },
        {
            "title": "4. Phrasal Verbs",
            "content": """
**Phrasal verbs** = verb + preposition/adverb. The meaning often changes completely!

### Essential Phrasal Verbs

| Phrasal Verb | Meaning | Example |
|-------------|---------|---------|
| **give up** | stop trying | Don't **give up** — keep learning! |
| **look up** | search for information | **Look up** the word in a dictionary. |
| **turn on/off** | activate/deactivate | **Turn on** the light, please. |
| **put off** | postpone | Don't **put off** your homework. |
| **come up with** | think of (an idea) | She **came up with** a great plan. |
| **look forward to** | anticipate with pleasure | I **look forward to** meeting you. |
| **get along with** | have a good relationship | I **get along with** my neighbors. |
| **run out of** | have no more | We've **run out of** milk. |
| **figure out** | understand / solve | I can't **figure out** this puzzle. |
| **break down** | stop working / become emotional | My car **broke down** on the highway. |

**Tip:** Keep a phrasal verb journal — write new ones you encounter with example sentences!
""",
        },
    ],
}

VOCABULARY_SETS = {
    "Greetings & Introductions 👋": [
        ("Hello / Hi", "A common way to greet someone.", "Hello! How are you?"),
        ("Good morning", "Greeting used in the morning.", "Good morning, teacher!"),
        ("Good afternoon", "Greeting used after noon.", "Good afternoon, everyone."),
        ("Good evening", "Greeting used in the evening.", "Good evening, sir."),
        ("Goodbye / Bye", "Saying farewell.", "Goodbye! See you tomorrow."),
        ("My name is…", "Introducing yourself.", "My name is Jessica."),
        ("Nice to meet you", "Polite phrase when meeting someone new.", "Nice to meet you, Sarah!"),
        ("How are you?", "Asking about someone's well-being.", "How are you today?"),
        ("I'm fine, thank you", "Responding to 'How are you?'", "I'm fine, thank you. And you?"),
        ("Please", "Polite word for requests.", "Can I have some water, please?"),
        ("Thank you", "Expressing gratitude.", "Thank you for your help!"),
        ("You're welcome", "Response to 'Thank you'.", "You're welcome!"),
        ("Excuse me", "Getting attention politely.", "Excuse me, where is the library?"),
        ("I'm sorry", "Apologizing.", "I'm sorry I'm late."),
    ],
    "Numbers 🔢": [
        ("1 — one", "The first number.", "I have one brother."),
        ("2 — two", "The second number.", "She has two cats."),
        ("3 — three", "The third number.", "There are three books."),
        ("4 — four", "", "I waited four hours."),
        ("5 — five", "", "Five students passed."),
        ("10 — ten", "", "Count to ten."),
        ("20 — twenty", "", "I am twenty years old."),
        ("50 — fifty", "", "He ran fifty meters."),
        ("100 — one hundred", "", "There are one hundred pages."),
        ("1,000 — one thousand", "", "The city has one thousand people."),
    ],
    "Colors 🎨": [
        ("Red", "The color of fire and roses.", "The car is red."),
        ("Blue", "The color of the sky and ocean.", "The sky is blue."),
        ("Green", "The color of grass and leaves.", "The grass is green."),
        ("Yellow", "The color of the sun and bananas.", "The banana is yellow."),
        ("Orange", "The color of oranges and sunsets.", "She wore an orange dress."),
        ("Purple", "A mix of red and blue.", "The flowers are purple."),
        ("Black", "The darkest color.", "He has a black car."),
        ("White", "The lightest color.", "Snow is white."),
        ("Brown", "The color of chocolate and earth.", "The dog is brown."),
        ("Pink", "A light shade of red.", "She likes pink flowers."),
    ],
    "Family 👨‍👩‍👧‍👦": [
        ("Mother / Mom", "Your female parent.", "My mother is a teacher."),
        ("Father / Dad", "Your male parent.", "My father works at a hospital."),
        ("Sister", "A female sibling.", "I have two sisters."),
        ("Brother", "A male sibling.", "My brother is older than me."),
        ("Grandmother", "Your parent's mother.", "My grandmother makes great cookies."),
        ("Grandfather", "Your parent's father.", "My grandfather tells great stories."),
        ("Aunt", "Your parent's sister.", "My aunt lives in London."),
        ("Uncle", "Your parent's brother.", "My uncle is a pilot."),
        ("Cousin", "Your aunt or uncle's child.", "I play with my cousin every weekend."),
        ("Husband / Wife", "A married partner.", "Her husband is a doctor."),
    ],
    "Food & Drinks 🍕": [
        ("Bread", "A basic baked food.", "I eat bread for breakfast."),
        ("Rice", "A grain eaten worldwide.", "Rice is popular in Asia."),
        ("Egg", "Laid by chickens, very nutritious.", "I had two eggs for breakfast."),
        ("Milk", "A white drink from cows.", "Children should drink milk."),
        ("Water", "Essential for life.", "Drink eight glasses of water a day."),
        ("Apple", "A common fruit.", "An apple a day keeps the doctor away."),
        ("Chicken", "A common type of meat.", "We had chicken for dinner."),
        ("Vegetable", "Plants used as food.", "Eat your vegetables!"),
        ("Coffee", "A hot drink made from beans.", "She drinks coffee every morning."),
        ("Tea", "A hot drink made from leaves.", "Would you like some tea?"),
    ],
    "Daily Activities 🏃": [
        ("Wake up", "Stop sleeping.", "I wake up at 7 AM."),
        ("Brush teeth", "Clean your teeth.", "Brush your teeth twice a day."),
        ("Take a shower", "Wash your body.", "I take a shower every morning."),
        ("Eat breakfast", "Have the first meal.", "I eat breakfast at 8 AM."),
        ("Go to school/work", "Travel to school or workplace.", "She goes to school by bus."),
        ("Study", "Learn new things.", "I study English every day."),
        ("Cook", "Prepare food.", "My mother cooks dinner."),
        ("Watch TV", "Look at television.", "We watch TV in the evening."),
        ("Read a book", "Look at and understand written words.", "I read a book before bed."),
        ("Go to sleep", "Start sleeping.", "I go to sleep at 10 PM."),
    ],
    "Common Phrases 💬": [
        ("I don't understand", "When you can't comprehend.", "I'm sorry, I don't understand."),
        ("Can you repeat that?", "Asking someone to say it again.", "Can you repeat that, please?"),
        ("How do you say…?", "Asking for a word.", "How do you say 'casa' in English?"),
        ("What does … mean?", "Asking for a definition.", "What does 'beautiful' mean?"),
        ("I agree / I disagree", "Expressing opinion.", "I agree with you."),
        ("In my opinion…", "Sharing your view.", "In my opinion, this is a good idea."),
        ("Could you help me?", "Asking for assistance.", "Could you help me, please?"),
        ("It doesn't matter", "It's not important.", "It doesn't matter, don't worry."),
        ("I'm looking for…", "Searching for something.", "I'm looking for the train station."),
        ("How much does it cost?", "Asking the price.", "How much does this book cost?"),
    ],
}

READING_PASSAGES = {
    "Beginner": [
        {
            "title": "🐶 My Dog Max",
            "text": """My name is Lily. I am ten years old. I have a dog. His name is Max. Max is a small brown dog. He has big brown eyes and a short tail.

Every morning, I wake up and play with Max. He likes to run in the garden. He likes to catch the ball. I throw the ball, and Max runs very fast to get it. Then he brings the ball back to me.

Max eats dog food two times a day. He drinks a lot of water. After eating, he likes to sleep on his bed near the window. Max is a good dog. I love Max very much. He is my best friend.""",
            "questions": [
                {
                    "q": "What is the dog's name?",
                    "options": ["Rex", "Max", "Buddy", "Spot"],
                    "answer": "Max",
                },
                {
                    "q": "What color is the dog?",
                    "options": ["White", "Black", "Brown", "Golden"],
                    "answer": "Brown",
                },
                {
                    "q": "What does Max like to catch?",
                    "options": ["A stick", "A ball", "A frisbee", "A bone"],
                    "answer": "A ball",
                },
                {
                    "q": "How many times a day does Max eat?",
                    "options": ["One time", "Two times", "Three times", "Four times"],
                    "answer": "Two times",
                },
                {
                    "q": "Where does Max sleep?",
                    "options": [
                        "On Lily's bed",
                        "In the garden",
                        "Near the window",
                        "In the kitchen",
                    ],
                    "answer": "Near the window",
                },
            ],
        },
        {
            "title": "🏫 A Day at School",
            "text": """My name is Tom. I go to Green Hill School. I am in Class 3. My teacher is Mrs. Brown. She is very kind.

School starts at 8 o'clock in the morning. First, we have English class. I like English very much. We learn new words and read stories. After English, we have Math. Math is a little difficult, but I try my best.

At 10 o'clock, we have a break. I play with my friends in the playground. My best friend is Sam. We play football together.

After the break, we have Science. I like Science because we do experiments. At 12 o'clock, we eat lunch in the dining hall. The food is good. After lunch, we have Art class. I like to draw and paint. School finishes at 3 o'clock. My mother picks me up and we go home.""",
            "questions": [
                {
                    "q": "What is Tom's teacher's name?",
                    "options": ["Mrs. Smith", "Mrs. Brown", "Mrs. Green", "Mrs. White"],
                    "answer": "Mrs. Brown",
                },
                {
                    "q": "What time does school start?",
                    "options": ["7 o'clock", "8 o'clock", "9 o'clock", "10 o'clock"],
                    "answer": "8 o'clock",
                },
                {
                    "q": "What sport does Tom play with Sam?",
                    "options": ["Basketball", "Cricket", "Football", "Tennis"],
                    "answer": "Football",
                },
                {
                    "q": "What time does school finish?",
                    "options": ["2 o'clock", "3 o'clock", "4 o'clock", "5 o'clock"],
                    "answer": "3 o'clock",
                },
            ],
        },
    ],
    "Intermediate": [
        {
            "title": "✈️ A Trip to London",
            "text": """Last summer, my family and I took a trip to London, England. It was my first time visiting another country, and I was very excited. We flew from New York, and the flight took about seven hours.

When we arrived in London, the first thing I noticed was that people drove on the left side of the road! It was very different from what I was used to. We took a taxi to our hotel, which was near the River Thames.

During our trip, we visited many famous places. We saw Big Ben, the large clock tower next to the Houses of Parliament. We visited the British Museum, where we saw ancient Egyptian mummies and Greek sculptures. My favorite place was the Tower of London, where the Crown Jewels are kept. The diamonds and rubies were absolutely stunning.

We also rode the London Eye, a giant Ferris wheel on the South Bank of the Thames. From the top, we could see the entire city. The view was breathtaking, especially at sunset.

One thing I loved about London was the food. We tried fish and chips, which is a traditional English dish. We also had afternoon tea at a fancy hotel, with tiny sandwiches and delicious scones with jam and cream. The tea was served in beautiful china cups.

I learned a lot of new English expressions during the trip. For example, in London, people say "brilliant" when something is great, and they call the subway "the Underground" or "the Tube." It was a wonderful experience, and I hope to visit London again someday.""",
            "questions": [
                {
                    "q": "How long was the flight from New York to London?",
                    "options": ["5 hours", "6 hours", "7 hours", "8 hours"],
                    "answer": "7 hours",
                },
                {
                    "q": "What side of the road do people drive on in London?",
                    "options": ["Right side", "Left side", "Both sides", "The middle"],
                    "answer": "Left side",
                },
                {
                    "q": "What is the narrator's favorite place in London?",
                    "options": [
                        "Big Ben",
                        "British Museum",
                        "Tower of London",
                        "London Eye",
                    ],
                    "answer": "Tower of London",
                },
                {
                    "q": "What do people in London call the subway?",
                    "options": [
                        "The Metro",
                        "The Tube",
                        "The Railway",
                        "The Express",
                    ],
                    "answer": "The Tube",
                },
                {
                    "q": "What traditional English dish did they try?",
                    "options": [
                        "Roast beef",
                        "Shepherd's pie",
                        "Fish and chips",
                        "Bangers and mash",
                    ],
                    "answer": "Fish and chips",
                },
            ],
        },
    ],
    "Advanced": [
        {
            "title": "🌍 The Impact of Technology on Language Learning",
            "text": """The landscape of language learning has undergone a remarkable transformation over the past two decades, driven largely by rapid advancements in technology. Where learners once relied solely on textbooks, classroom instruction, and perhaps cassette tapes for listening practice, they now have access to an unprecedented array of digital tools that make acquiring a new language more accessible, engaging, and personalized than ever before.

One of the most significant developments has been the rise of language learning applications. Platforms such as Duolingo, Babbel, and Rosetta Stone have democratized language education, making it possible for anyone with a smartphone to begin learning a new language at no cost or for a modest subscription fee. These applications employ sophisticated algorithms that adapt to each learner's proficiency level, spacing out review sessions based on the principles of spaced repetition — a technique that has been shown to dramatically improve long-term retention of new vocabulary and grammatical structures.

Artificial intelligence has further revolutionized the field by enabling real-time conversation practice with AI-powered chatbots and virtual tutors. Unlike human tutors, these AI systems are available around the clock, endlessly patient, and capable of providing immediate, detailed feedback on pronunciation, grammar, and vocabulary usage. While they cannot fully replicate the nuance and cultural awareness of a skilled human instructor, they serve as an invaluable supplement, particularly for learners who may not have access to native speakers in their daily lives.

However, technology is not without its limitations. Critics argue that the gamification of language learning — the use of points, streaks, and leaderboards — may foster a superficial engagement with the material, encouraging learners to prioritize completion of short exercises over the deep, sustained practice necessary for genuine fluency. Furthermore, the absence of authentic human interaction in many technology-based approaches means that learners may struggle with the pragmatic aspects of language use: understanding humor, navigating cultural norms, interpreting body language, and adapting their register to different social contexts.

Despite these challenges, the consensus among educators and linguists is that technology, when used thoughtfully and in conjunction with traditional methods, represents a powerful force for expanding access to language education worldwide. The key lies not in choosing between technology and human instruction, but in finding the optimal balance between the two — leveraging the efficiency and accessibility of digital tools while preserving the irreplaceable richness of human connection and cultural immersion.""",
            "questions": [
                {
                    "q": "According to the passage, what technique do language apps use to improve long-term retention?",
                    "options": [
                        "Immersive reading",
                        "Spaced repetition",
                        "Grammar translation",
                        "Total physical response",
                    ],
                    "answer": "Spaced repetition",
                },
                {
                    "q": "What advantage do AI tutors have over human tutors, according to the text?",
                    "options": [
                        "Better cultural understanding",
                        "More nuanced feedback",
                        "Available 24/7 and endlessly patient",
                        "Cheaper classroom setup",
                    ],
                    "answer": "Available 24/7 and endlessly patient",
                },
                {
                    "q": "What concern do critics raise about gamification in language learning?",
                    "options": [
                        "It is too expensive",
                        "It encourages superficial engagement",
                        "It replaces teachers entirely",
                        "It only works for children",
                    ],
                    "answer": "It encourages superficial engagement",
                },
                {
                    "q": "What is the consensus among educators according to the passage?",
                    "options": [
                        "Technology should replace traditional methods",
                        "Traditional methods are always better",
                        "Technology and traditional methods should be balanced",
                        "Language apps are ineffective",
                    ],
                    "answer": "Technology and traditional methods should be balanced",
                },
            ],
        },
    ],
}

WRITING_PROMPTS = {
    "Beginner": [
        {
            "title": "📝 Introduce Yourself",
            "instructions": "Write 5–8 sentences about yourself. Include your name, age, where you live, your family, and what you like to do.",
            "hints": "Use these sentence starters:\n- My name is…\n- I am … years old.\n- I live in…\n- I have … (brothers/sisters).\n- I like to…\n- My favorite … is…",
            "example": "My name is Sara. I am 12 years old. I live in a small town called Riverdale. I have one brother and one sister. My brother's name is Ali and my sister's name is Mina. I like to read books and play in the park. My favorite subject in school is English. I want to learn English very well so I can talk to people from other countries.",
        },
        {
            "title": "🏠 Describe Your Home",
            "instructions": "Write 5–8 sentences describing your home. Talk about the rooms, colors, and what you do in each room.",
            "hints": "Use these words:\n- bedroom, kitchen, bathroom, living room\n- big, small, clean, beautiful\n- There is / There are\n- I … in the (room).",
            "example": "I live in a small house with my family. There are four rooms in my house. The living room is big and has a blue sofa. I watch TV in the living room. The kitchen is small but clean. My mother cooks delicious food in the kitchen. My bedroom has a window. I can see the garden from my window. I read and study in my bedroom.",
        },
        {
            "title": "🐾 My Favorite Animal",
            "instructions": "Write 5–8 sentences about your favorite animal. Describe what it looks like, what it eats, and why you like it.",
            "hints": "Use these words:\n- It is … (big/small/fast/slow)\n- It has … (fur/feathers/scales)\n- It eats …\n- It lives in …\n- I like it because …",
            "example": "",
        },
    ],
    "Intermediate": [
        {
            "title": "📖 A Memorable Day",
            "instructions": "Write a short paragraph (80–120 words) about a memorable day in your life. What happened? How did you feel? Use past tenses.",
            "hints": "Include:\n- When it happened\n- Where you were\n- What happened\n- How you felt\n- Why it was memorable\n\nUseful phrases: I remember when…, It was a … day, I felt…, The best part was…",
            "example": "",
        },
        {
            "title": "💌 Write a Letter",
            "instructions": "Write a letter (80–120 words) to a friend inviting them to visit your city. Tell them about interesting places and activities.",
            "hints": "Letter structure:\n- Dear [name],\n- Opening: How are you? I hope you are well.\n- Body: I would like to invite you to… You can visit… We can…\n- Closing: I look forward to seeing you.\n- Yours, [your name]",
            "example": "",
        },
        {
            "title": "🗞️ My Opinion",
            "instructions": "Write a short opinion paragraph (80–120 words) on this topic: 'Is it better to learn English online or in a classroom?' Give reasons for your opinion.",
            "hints": "Structure:\n- State your opinion: In my opinion… / I believe that…\n- Give reasons: First, … Second, … Furthermore, …\n- Give an example: For example, …\n- Conclusion: In conclusion, … / To sum up, …",
            "example": "",
        },
    ],
    "Advanced": [
        {
            "title": "📰 Essay Writing",
            "instructions": "Write a 5-paragraph essay (200–300 words) on the topic: 'The advantages and disadvantages of social media.' Include an introduction, body paragraphs, and a conclusion.",
            "hints": "Essay structure:\n1. **Introduction:** Hook + background + thesis statement\n2. **Body 1:** Advantages (with examples)\n3. **Body 2:** Disadvantages (with examples)\n4. **Body 3:** Your balanced view\n5. **Conclusion:** Summary + final thought\n\nUse linking words: However, Moreover, On the other hand, In addition, Nevertheless, In conclusion",
            "example": "",
        },
        {
            "title": "🎭 Creative Writing — Short Story",
            "instructions": "Write a short story (200–300 words) that begins with this sentence: 'When I opened the door, I couldn't believe what I saw.'",
            "hints": "Include:\n- Setting (where and when)\n- Characters (who)\n- Problem/conflict\n- Resolution\n- Use descriptive adjectives and adverbs\n- Include dialogue using quotation marks\n- Use a variety of tenses",
            "example": "",
        },
        {
            "title": "📧 Formal Email",
            "instructions": "Write a formal email (150–200 words) to a university admissions office asking about their English language program. Ask about course dates, fees, accommodation, and requirements.",
            "hints": "Formal email structure:\n- Subject line: Inquiry About English Language Program\n- Dear Sir/Madam,\n- Purpose: I am writing to inquire about…\n- Questions: Could you please provide information regarding…?\n- Closing: I look forward to hearing from you.\n- Yours faithfully, [your name]",
            "example": "",
        },
    ],
}

QUIZ_QUESTIONS = {
    "Beginner": [
        {"q": "Choose the correct article: I saw ___ elephant at the zoo.", "options": ["a", "an", "the", "no article"], "answer": "an"},
        {"q": "Which word is a noun?", "options": ["quickly", "beautiful", "happiness", "run"], "answer": "happiness"},
        {"q": "Choose the correct pronoun: ___ is my sister. ___ name is Anna.", "options": ["She / Her", "Her / She", "He / His", "She / His"], "answer": "She / Her"},
        {"q": "What is the plural of 'child'?", "options": ["childs", "childes", "children", "childrens"], "answer": "children"},
        {"q": "Choose the correct verb: She ___ to school every day.", "options": ["go", "goes", "going", "gone"], "answer": "goes"},
        {"q": "Which sentence is correct?", "options": ["I am student.", "I am a student.", "I a student.", "I student am."], "answer": "I am a student."},
        {"q": "What is the opposite of 'hot'?", "options": ["warm", "cool", "cold", "heat"], "answer": "cold"},
        {"q": "Choose the correct word: The cat is ___ the table.", "options": ["in", "on", "at", "to"], "answer": "on"},
        {"q": "What day comes after Wednesday?", "options": ["Tuesday", "Thursday", "Friday", "Monday"], "answer": "Thursday"},
        {"q": "Choose the correct sentence:", "options": ["He don't like milk.", "He doesn't likes milk.", "He doesn't like milk.", "He not like milk."], "answer": "He doesn't like milk."},
    ],
    "Intermediate": [
        {"q": "Choose the correct tense: I ___ English for three years.", "options": ["study", "am studying", "have been studying", "was studying"], "answer": "have been studying"},
        {"q": "Which sentence uses the present perfect correctly?", "options": ["I have went to Paris.", "I have gone to Paris.", "I have go to Paris.", "I have going to Paris."], "answer": "I have gone to Paris."},
        {"q": "Choose the correct preposition: She arrived ___ Monday ___ 9 AM.", "options": ["on / at", "in / at", "at / on", "on / in"], "answer": "on / at"},
        {"q": "Identify the adverb: 'She sings beautifully.'", "options": ["She", "sings", "beautifully", "None"], "answer": "beautifully"},
        {"q": "Choose the correct conjunction: I wanted to go, ___ it was raining.", "options": ["so", "but", "and", "because"], "answer": "but"},
        {"q": "Which word is a comparative adjective?", "options": ["good", "better", "best", "well"], "answer": "better"},
        {"q": "Choose the correct form: If it rains, I ___ at home.", "options": ["stay", "will stay", "would stay", "stayed"], "answer": "will stay"},
        {"q": "'She asked me where I ___.' Choose the correct word.", "options": ["live", "lived", "living", "lives"], "answer": "lived"},
        {"q": "What does the phrasal verb 'give up' mean?", "options": ["donate", "surrender / stop trying", "lift higher", "return"], "answer": "surrender / stop trying"},
        {"q": "Choose the correct passive form: 'Someone stole my bike.' → 'My bike ___.'", "options": ["was stolen", "is stolen", "has stolen", "were stolen"], "answer": "was stolen"},
    ],
    "Advanced": [
        {"q": "Choose the correct sentence (subjunctive mood):", "options": ["I suggest that he goes.", "I suggest that he go.", "I suggest that he went.", "I suggest that he going."], "answer": "I suggest that he go."},
        {"q": "Identify the correct mixed conditional:", "options": ["If I studied, I would pass.", "If I had studied, I would be a doctor now.", "If I study, I will pass.", "If I had studied, I had passed."], "answer": "If I had studied, I would be a doctor now."},
        {"q": "'Hardly ___ I arrived when the phone rang.'", "options": ["did", "had", "have", "was"], "answer": "had"},
        {"q": "Choose the correct relative pronoun: 'The book ___ I told you about is on the shelf.'", "options": ["who", "whom", "which", "whose"], "answer": "which"},
        {"q": "Which sentence contains a dangling modifier?", "options": ["Walking to school, the dog barked at me.", "Walking to school, I heard a dog bark.", "While I was walking, the dog barked.", "The dog barked while I walked."], "answer": "Walking to school, the dog barked at me."},
        {"q": "What does the idiom 'break the ice' mean?", "options": ["Cause damage", "Make a situation less tense", "Start a fight", "Freeze something"], "answer": "Make a situation less tense"},
        {"q": "Choose the correct word: 'The data ___ inconclusive.' (formal English)", "options": ["is", "are", "was", "were"], "answer": "are"},
        {"q": "'Not only ___ she intelligent, but she is also kind.'", "options": ["is", "was", "does", "has"], "answer": "is"},
        {"q": "Choose the correct collocation: '___ a decision'", "options": ["do", "make", "take", "have"], "answer": "make"},
        {"q": "Which sentence correctly uses the past perfect?", "options": ["I had eaten before she arrived.", "I have eaten before she arrived.", "I ate before she had arrived.", "I had ate before she arrived."], "answer": "I had eaten before she arrived."},
    ],
}

TIPS_OF_THE_DAY = [
    "💡 **Read in English every day** — even 10 minutes helps! Start with children's books or simple news articles.",
    "💡 **Label items in your home** with sticky notes in English. You'll learn vocabulary naturally!",
    "💡 **Watch English movies with subtitles.** First with subtitles in your language, then in English, then without!",
    "💡 **Keep a vocabulary notebook.** Write 5 new words every day with their meaning and a sentence.",
    "💡 **Talk to yourself in English!** Describe what you're doing: 'I am making breakfast. I am eating toast.'",
    "💡 **Listen to English songs** and read the lyrics. Singing helps with pronunciation and memory!",
    "💡 **Don't be afraid of mistakes!** Every mistake is a chance to learn something new.",
    "💡 **Practice the 4 skills daily:** Reading, Writing, Listening, and Speaking.",
    "💡 **Set your phone language to English.** You'll learn tech vocabulary without even trying!",
    "💡 **Find an English study buddy.** Practicing with someone else keeps you motivated.",
    "💡 **Use new words in sentences right away.** If you learn a word, use it 5 times that day!",
    "💡 **Record yourself speaking English** and listen back. You'll notice improvement over time!",
]

# ──────────────────────────────────────────────────────────────
# Sidebar navigation
# ──────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("# 📚 Navigation")
    page = st.radio(
        "Go to:",
        [
            "🏠 Home",
            "🔤 Learn the Alphabet",
            "📖 Grammar Lessons",
            "📚 Vocabulary Builder",
            "📕 Read English",
            "✍️ Write English",
            "🧩 Take a Quiz",
            "📊 My Progress",
        ],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown("### 🎯 Your Level")
    user_level = st.selectbox("Select your level:", ["Beginner", "Intermediate", "Advanced"])
    st.markdown("---")

    # Tip of the day
    tip_index = datetime.now().timetuple().tm_yday % len(TIPS_OF_THE_DAY)
    st.markdown("### 📌 Tip of the Day")
    st.info(TIPS_OF_THE_DAY[tip_index])
    st.markdown("---")
    st.markdown(
        "<div style='text-align:center; color:#999; font-size:.78rem;'>"
        "Made with ❤️ by Jessica<br>© 2026"
        "</div>",
        unsafe_allow_html=True,
    )


# ══════════════════════════════════════════════════════════════
# PAGE: Home
# ══════════════════════════════════════════════════════════════
if page == "🏠 Home":
    st.markdown(
        """
    <div class="hero-banner">
        <h1>📚 Jessica's English Learning Guide</h1>
        <p><em>For Students And Adults Of All Ages</em></p>
        <p style="margin-top:.6rem;">Learn English • Read English • Write English — all from scratch!</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="metric-row">
        <div class="metric-card"><div class="num">26</div><div class="label">Alphabet Letters</div></div>
        <div class="metric-card"><div class="num">13</div><div class="label">Grammar Lessons</div></div>
        <div class="metric-card"><div class="num">7</div><div class="label">Vocabulary Sets</div></div>
        <div class="metric-card"><div class="num">4</div><div class="label">Reading Stories</div></div>
        <div class="metric-card"><div class="num">9</div><div class="label">Writing Exercises</div></div>
        <div class="metric-card"><div class="num">30</div><div class="label">Quiz Questions</div></div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("### 👋 Welcome!")
    st.markdown(
        """
    Welcome to **Jessica's English Learning Guide**! Whether you are a young student just starting out
    or an adult learning English for the first time, this website is for **you**.

    Here you will find everything you need to start learning English from **scratch**:
    """
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
        <div class="section-card">
            <h3>📖 Learn</h3>
            <p>Start with the <strong>alphabet</strong>, then move to <strong>grammar lessons</strong> covering nouns, verbs, tenses, and more — from beginner to advanced.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
        <div class="section-card">
            <h3>📕 Read</h3>
            <p>Practice reading with <strong>stories and passages</strong> at your level. Each story comes with <strong>comprehension questions</strong> to test your understanding.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
        <div class="section-card">
            <h3>✍️ Write</h3>
            <p>Improve your writing with <strong>guided exercises</strong>, helpful hints, and example texts. Practice writing about yourself, your opinions, and stories.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### 🚀 How to Get Started")
    st.markdown(
        """
    1. **Choose your level** in the sidebar (Beginner, Intermediate, or Advanced)
    2. **Start with the Alphabet** if you're a complete beginner
    3. **Work through Grammar Lessons** to build your foundation
    4. **Build your Vocabulary** with our themed word sets
    5. **Practice Reading** with our graded stories
    6. **Improve your Writing** with guided prompts
    7. **Test your knowledge** with our quizzes!

    > *"The journey of a thousand miles begins with a single step."* — Lao Tzu
    >
    > Your English learning journey starts **right here, right now**! 🌟
    """
    )


# ══════════════════════════════════════════════════════════════
# PAGE: Alphabet
# ══════════════════════════════════════════════════════════════
elif page == "🔤 Learn the Alphabet":
    st.markdown(
        """
    <div class="hero-banner" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
        <h1>🔤 The English Alphabet</h1>
        <p>26 letters — the building blocks of English!</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    The English alphabet has **26 letters**: 5 vowels (**A, E, I, O, U**) and 21 consonants.
    Learning the alphabet is the **first step** to reading and writing in English!
    """
    )

    # Display letters in a grid
    st.markdown("### 📋 All 26 Letters")

    cols = st.columns(4)
    for i, (letter, word, sound) in enumerate(ALPHABET_DATA):
        with cols[i % 4]:
            is_vowel = letter[0] in "AEIOU"
            bg = "#e8f5e9" if is_vowel else "#e3f2fd"
            border_color = "#43a047" if is_vowel else "#1e88e5"
            v_label = "🟢 Vowel" if is_vowel else "🔵 Consonant"
            st.markdown(
                f"""
            <div style="background:{bg}; border:2px solid {border_color}; border-radius:12px;
                        padding:.8rem; margin-bottom:.8rem; text-align:center;">
                <div style="font-size:2rem; font-weight:800;">{letter}</div>
                <div style="font-size:.85rem; color:#555;">{word}</div>
                <div style="font-size:.78rem; color:#888;">{sound}</div>
                <div style="font-size:.7rem; margin-top:4px;">{v_label}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.markdown("### ✏️ Practice: Type the Missing Letters")
    practice_word = random.choice(["APPLE", "HOUSE", "WATER", "HAPPY", "LEARN", "BRAIN", "STUDY", "CHAIR"])
    hidden_indices = sorted(random.sample(range(len(practice_word)), k=min(2, len(practice_word))))
    display = list(practice_word)
    for idx in hidden_indices:
        display[idx] = "_"
    st.markdown(f"**Fill in the blanks:** `{'  '.join(display)}`")
    user_answer = st.text_input("Type the complete word:", key="alphabet_practice")
    if user_answer:
        if user_answer.strip().upper() == practice_word:
            st.success(f"✅ Correct! The word is **{practice_word}**! 🎉")
        else:
            st.error(f"❌ Not quite. The correct word is **{practice_word}**. Try again!")


# ══════════════════════════════════════════════════════════════
# PAGE: Grammar Lessons
# ══════════════════════════════════════════════════════════════
elif page == "📖 Grammar Lessons":
    st.markdown(
        """
    <div class="hero-banner" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
        <h1>📖 Grammar Lessons</h1>
        <p>Build a strong foundation in English grammar</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    level_badge = {
        "Beginner": '<span class="badge-beginner">Beginner</span>',
        "Intermediate": '<span class="badge-intermediate">Intermediate</span>',
        "Advanced": '<span class="badge-advanced">Advanced</span>',
    }
    st.markdown(f"### Current Level: {level_badge[user_level]}", unsafe_allow_html=True)

    lessons = GRAMMAR_LESSONS.get(user_level, [])
    if not lessons:
        st.info("No lessons available for this level yet. Please check back soon!")
    else:
        for lesson in lessons:
            with st.expander(f"📘 {lesson['title']}", expanded=False):
                st.markdown(lesson["content"])
                st.markdown("---")
                st.markdown("*✅ Mark this lesson as complete in your mind and move to the next one!*")

    st.markdown("---")
    st.markdown("### 📚 All Levels Available")
    all_cols = st.columns(3)
    for i, lvl in enumerate(["Beginner", "Intermediate", "Advanced"]):
        with all_cols[i]:
            count = len(GRAMMAR_LESSONS.get(lvl, []))
            st.metric(f"{lvl}", f"{count} lessons")


# ══════════════════════════════════════════════════════════════
# PAGE: Vocabulary Builder
# ══════════════════════════════════════════════════════════════
elif page == "📚 Vocabulary Builder":
    st.markdown(
        """
    <div class="hero-banner" style="background: linear-gradient(135deg, #a18cd1 0%, #fbc2eb 100%);">
        <h1>📚 Vocabulary Builder</h1>
        <p>Learn new words and build your English word power!</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    selected_set = st.selectbox("Choose a vocabulary set:", list(VOCABULARY_SETS.keys()))
    words = VOCABULARY_SETS[selected_set]

    st.markdown(f"### {selected_set}")
    st.markdown(f"*This set has **{len(words)}** words to learn.*")

    # Display mode
    display_mode = st.radio("Display mode:", ["📋 Word List", "🃏 Flashcards"], horizontal=True)

    if display_mode == "📋 Word List":
        for word, definition, example in words:
            st.markdown(
                f"""
            <div class="lesson-card">
                <h4>{word}</h4>
                <p><strong>Meaning:</strong> {definition}</p>
                <p><strong>Example:</strong> <em>{example}</em></p>
            </div>
            """,
                unsafe_allow_html=True,
            )
    else:
        # Flashcard mode
        idx = st.session_state.vocab_index % len(words)
        word, definition, example = words[idx]

        st.markdown(
            f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    border-radius: 16px; padding: 2rem; color: white; text-align: center;
                    min-height: 200px; display:flex; flex-direction:column; justify-content:center;
                    margin: 1rem 0;">
            <div style="font-size: 2rem; font-weight: 800; margin-bottom: 1rem;">{word}</div>
            <div style="font-size: 1.1rem; opacity: .9;">{definition}</div>
            <div style="font-size: .95rem; font-style: italic; margin-top: .8rem; opacity: .8;">"{example}"</div>
            <div style="margin-top: 1rem; font-size: .85rem; opacity: .7;">Card {idx + 1} of {len(words)}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )
        col_prev, col_next = st.columns(2)
        with col_prev:
            if st.button("⬅️ Previous", use_container_width=True):
                st.session_state.vocab_index -= 1
                st.rerun()
        with col_next:
            if st.button("Next ➡️", use_container_width=True):
                st.session_state.vocab_index += 1
                st.rerun()


# ══════════════════════════════════════════════════════════════
# PAGE: Read English
# ══════════════════════════════════════════════════════════════
elif page == "📕 Read English":
    st.markdown(
        """
    <div class="hero-banner" style="background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);">
        <h1>📕 Read English</h1>
        <p>Practice reading with stories at your level</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    level_badge = {
        "Beginner": '<span class="badge-beginner">Beginner</span>',
        "Intermediate": '<span class="badge-intermediate">Intermediate</span>',
        "Advanced": '<span class="badge-advanced">Advanced</span>',
    }
    st.markdown(f"### Reading Level: {level_badge[user_level]}", unsafe_allow_html=True)

    passages = READING_PASSAGES.get(user_level, [])
    if not passages:
        st.info("No reading passages available for this level yet.")
    else:
        for p_idx, passage in enumerate(passages):
            st.markdown(f"### {passage['title']}")
            st.markdown(
                f'<div class="story-box">{passage["text"]}</div>', unsafe_allow_html=True
            )

            st.markdown("#### 📝 Comprehension Questions")
            for q_idx, question in enumerate(passage["questions"]):
                key = f"read_{user_level}_{p_idx}_{q_idx}"
                answer = st.radio(
                    question["q"],
                    question["options"],
                    key=key,
                    index=None,
                )
                if answer is not None:
                    if answer == question["answer"]:
                        st.markdown(
                            f'<div class="quiz-correct">✅ Correct! The answer is <strong>{question["answer"]}</strong>.</div>',
                            unsafe_allow_html=True,
                        )
                    else:
                        st.markdown(
                            f'<div class="quiz-wrong">❌ Not quite. The correct answer is <strong>{question["answer"]}</strong>.</div>',
                            unsafe_allow_html=True,
                        )
            st.markdown("---")


# ══════════════════════════════════════════════════════════════
# PAGE: Write English
# ══════════════════════════════════════════════════════════════
elif page == "✍️ Write English":
    st.markdown(
        """
    <div class="hero-banner" style="background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);">
        <h1>✍️ Write English</h1>
        <p>Practice your writing skills with guided exercises</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    level_badge = {
        "Beginner": '<span class="badge-beginner">Beginner</span>',
        "Intermediate": '<span class="badge-intermediate">Intermediate</span>',
        "Advanced": '<span class="badge-advanced">Advanced</span>',
    }
    st.markdown(f"### Writing Level: {level_badge[user_level]}", unsafe_allow_html=True)

    prompts = WRITING_PROMPTS.get(user_level, [])
    if not prompts:
        st.info("No writing exercises available for this level yet.")
    else:
        selected_prompt = st.selectbox(
            "Choose a writing exercise:",
            [p["title"] for p in prompts],
        )
        prompt = next(p for p in prompts if p["title"] == selected_prompt)

        st.markdown(f"### {prompt['title']}")

        st.markdown(
            f"""
        <div class="section-card">
            <h3>📋 Instructions</h3>
            <p>{prompt['instructions']}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        with st.expander("💡 Hints & Help", expanded=False):
            st.markdown(prompt["hints"])

        if prompt.get("example"):
            with st.expander("📖 See an Example", expanded=False):
                st.markdown(
                    f'<div class="story-box">{prompt["example"]}</div>',
                    unsafe_allow_html=True,
                )

        st.markdown("### ✏️ Your Writing")
        user_writing = st.text_area(
            "Write your answer here:",
            height=250,
            key=f"writing_{selected_prompt}",
            placeholder="Start writing here...",
        )

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("📊 Check Word Count", use_container_width=True):
                if user_writing.strip():
                    word_count = len(user_writing.split())
                    char_count = len(user_writing)
                    sentence_count = user_writing.count('.') + user_writing.count('!') + user_writing.count('?')
                    st.info(f"📊 **Word count:** {word_count} words | **Characters:** {char_count} | **Sentences:** ~{sentence_count}")
                else:
                    st.warning("Please write something first!")

        with col2:
            if st.button("💾 Save My Writing", use_container_width=True):
                if user_writing.strip():
                    st.session_state.writing_submissions.append(
                        {
                            "title": selected_prompt,
                            "text": user_writing,
                            "level": user_level,
                            "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                            "word_count": len(user_writing.split()),
                        }
                    )
                    st.success("✅ Your writing has been saved! Check 'My Progress' to see all your submissions.")
                else:
                    st.warning("Please write something first!")

        # Writing tips
        st.markdown("---")
        st.markdown("### ✨ Writing Tips")
        tips_col1, tips_col2 = st.columns(2)
        with tips_col1:
            st.markdown(
                """
            - ✅ Start each sentence with a **capital letter**
            - ✅ End each sentence with a **period (.)**, **question mark (?)**, or **exclamation mark (!)**
            - ✅ Use **paragraphs** to organize your ideas
            """
            )
        with tips_col2:
            st.markdown(
                """
            - ✅ Check your **spelling** before submitting
            - ✅ Use **different sentence structures** — don't start every sentence the same way
            - ✅ Read your writing **out loud** to check if it sounds natural
            """
            )


# ══════════════════════════════════════════════════════════════
# PAGE: Quiz
# ══════════════════════════════════════════════════════════════
elif page == "🧩 Take a Quiz":
    st.markdown(
        """
    <div class="hero-banner" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);">
        <h1>🧩 Take a Quiz</h1>
        <p>Test your English knowledge!</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    level_badge = {
        "Beginner": '<span class="badge-beginner">Beginner</span>',
        "Intermediate": '<span class="badge-intermediate">Intermediate</span>',
        "Advanced": '<span class="badge-advanced">Advanced</span>',
    }
    st.markdown(f"### Quiz Level: {level_badge[user_level]}", unsafe_allow_html=True)

    questions = QUIZ_QUESTIONS.get(user_level, [])

    if not questions:
        st.info("No quiz available for this level yet.")
    else:
        st.markdown(f"*Answer all **{len(questions)}** questions, then click **Submit Quiz** to see your score!*")

        with st.form("quiz_form"):
            answers = {}
            for i, q in enumerate(questions):
                st.markdown(f"**Question {i + 1}:** {q['q']}")
                answers[i] = st.radio(
                    f"Select your answer for Q{i+1}:",
                    q["options"],
                    key=f"quiz_{user_level}_{i}",
                    index=None,
                    label_visibility="collapsed",
                )
                st.markdown("---")

            submitted = st.form_submit_button("📝 Submit Quiz", use_container_width=True)

            if submitted:
                score = 0
                total = len(questions)
                for i, q in enumerate(questions):
                    if answers[i] == q["answer"]:
                        score += 1

                st.session_state.quiz_score = score
                st.session_state.quiz_total = total

                # Results
                percentage = (score / total) * 100
                if percentage == 100:
                    emoji = "🏆"
                    message = "PERFECT SCORE! You're an English superstar!"
                elif percentage >= 80:
                    emoji = "🌟"
                    message = "Excellent work! You really know your stuff!"
                elif percentage >= 60:
                    emoji = "👍"
                    message = "Good job! Keep practicing to improve!"
                elif percentage >= 40:
                    emoji = "💪"
                    message = "Not bad! Review the lessons and try again!"
                else:
                    emoji = "📚"
                    message = "Keep studying! Practice makes perfect!"

                st.markdown(
                    f"""
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                            border-radius: 16px; padding: 2rem; color: white; text-align: center;
                            margin: 1rem 0;">
                    <div style="font-size: 3rem;">{emoji}</div>
                    <div style="font-size: 2rem; font-weight: 800; margin: .5rem 0;">
                        {score} / {total}
                    </div>
                    <div style="font-size: 1.2rem; opacity: .9;">{percentage:.0f}%</div>
                    <div style="font-size: 1rem; margin-top: .5rem; opacity: .85;">{message}</div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

                # Show corrections
                st.markdown("### 📋 Review Your Answers")
                for i, q in enumerate(questions):
                    user_ans = answers[i]
                    correct = q["answer"]
                    if user_ans == correct:
                        st.markdown(
                            f'<div class="quiz-correct">✅ <strong>Q{i+1}:</strong> {q["q"]}<br>Your answer: <strong>{user_ans}</strong></div>',
                            unsafe_allow_html=True,
                        )
                    else:
                        st.markdown(
                            f'<div class="quiz-wrong">❌ <strong>Q{i+1}:</strong> {q["q"]}<br>Your answer: <strong>{user_ans or "No answer"}</strong> — Correct answer: <strong>{correct}</strong></div>',
                            unsafe_allow_html=True,
                        )


# ══════════════════════════════════════════════════════════════
# PAGE: My Progress
# ══════════════════════════════════════════════════════════════
elif page == "📊 My Progress":
    st.markdown(
        """
    <div class="hero-banner" style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);">
        <h1>📊 My Progress</h1>
        <p>Track your learning journey</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Quiz results
    st.markdown("### 🧩 Latest Quiz Results")
    if st.session_state.quiz_total > 0:
        score = st.session_state.quiz_score
        total = st.session_state.quiz_total
        pct = (score / total) * 100

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Score", f"{score}/{total}")
        with col2:
            st.metric("Percentage", f"{pct:.0f}%")
        with col3:
            if pct >= 80:
                st.metric("Rating", "⭐ Excellent")
            elif pct >= 60:
                st.metric("Rating", "👍 Good")
            elif pct >= 40:
                st.metric("Rating", "💪 Keep Going")
            else:
                st.metric("Rating", "📚 Study More")
    else:
        st.info("You haven't taken a quiz yet. Go to **🧩 Take a Quiz** to test your knowledge!")

    st.markdown("---")

    # Writing submissions
    st.markdown("### ✍️ My Writing Submissions")
    if st.session_state.writing_submissions:
        for i, sub in enumerate(reversed(st.session_state.writing_submissions)):
            with st.expander(
                f"📝 {sub['title']} — {sub['level']} — {sub['word_count']} words — {sub['time']}"
            ):
                st.markdown(f'<div class="story-box">{sub["text"]}</div>', unsafe_allow_html=True)
    else:
        st.info("You haven't submitted any writing yet. Go to **✍️ Write English** to start writing!")

    st.markdown("---")

    # Study recommendations
    st.markdown("### 🎯 What to Study Next")
    st.markdown(
        f"""
    Based on your current level (**{user_level}**), here's a suggested study plan:
    """
    )

    if user_level == "Beginner":
        st.markdown(
            """
        1. ✅ **Start with the Alphabet** — Make sure you know all 26 letters
        2. 📖 **Grammar Lessons 1–5** — Learn nouns, pronouns, verbs, sentences, and articles
        3. 📚 **Vocabulary:** Greetings, Numbers, Colors, and Family
        4. 📕 **Read:** "My Dog Max" and "A Day at School"
        5. ✍️ **Write:** Introduce yourself and describe your home
        6. 🧩 **Take the Beginner Quiz** — Aim for 80%+!
        """
        )
    elif user_level == "Intermediate":
        st.markdown(
            """
        1. 📖 **Grammar:** Master tenses, adjectives & adverbs, prepositions, and conjunctions
        2. 📚 **Vocabulary:** Daily Activities, Common Phrases, Food & Drinks
        3. 📕 **Read:** "A Trip to London" — practice comprehension
        4. ✍️ **Write:** A memorable day, a letter to a friend, or an opinion paragraph
        5. 🧩 **Take the Intermediate Quiz** — Aim for 80%+!
        """
        )
    else:
        st.markdown(
            """
        1. 📖 **Grammar:** Conditionals, passive voice, reported speech, and phrasal verbs
        2. 📚 **Vocabulary:** Review all sets — focus on using words in context
        3. 📕 **Read:** "The Impact of Technology on Language Learning"
        4. ✍️ **Write:** An essay, a short story, or a formal email
        5. 🧩 **Take the Advanced Quiz** — Aim for 90%+!
        """
        )


# ──────────────────────────────────────────────────────────────
# Footer
# ──────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    """
<div class="footer">
    📚 <strong>Jessica's English Learning Guide For Students And Adults Of All Ages</strong><br>
    Made with ❤️ using Streamlit | © 2026 Jessica's English Learning Guide
</div>
""",
    unsafe_allow_html=True,
)
