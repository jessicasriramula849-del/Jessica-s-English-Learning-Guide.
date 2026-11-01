"""Learning content for Jessica's English Learning Guide."""

SITE_NAME = "Jessica's English Learning Guide For Students And Adults Of All Ages"
SHORT_NAME = "Jessica's English Learning Guide"

LEVELS = ["Foundation", "Beginner", "Growing", "Confident"]

LEVEL_DETAILS = {
    "Foundation": {
        "label": "Start from zero",
        "description": "Letters, first words, simple sentences, and everyday introductions.",
        "icon": "🌱",
    },
    "Beginner": {
        "label": "Build the basics",
        "description": "Present tense, questions, describing things, and useful conversation.",
        "icon": "🌿",
    },
    "Growing": {
        "label": "Speak with more confidence",
        "description": "Past and future tenses, longer sentences, and clearer writing.",
        "icon": "🌳",
    },
    "Confident": {
        "label": "Express yourself",
        "description": "Complex ideas, polite email, idioms, and reading between the lines.",
        "icon": "🌻",
    },
}

LESSONS = [
    {
        "id": "alphabet",
        "level": "Foundation",
        "title": "The English Alphabet & Letter Sounds",
        "subtitle": "Meet the 26 letters that unlock every English word.",
        "minutes": 10,
        "goals": [
            "Recognise uppercase and lowercase letters",
            "Name the five vowels",
            "Understand the difference between a letter's name and its sound",
        ],
        "sections": [
            {
                "heading": "26 letters, endless possibilities",
                "body": "English uses 26 letters. We put letters together to make words. Every word you will ever read is built from this small family.",
                "examples": [
                    "Uppercase: A B C D E",
                    "Lowercase: a b c d e",
                    "A word: c + a + t = cat",
                ],
            },
            {
                "heading": "Vowels and consonants",
                "body": "Five letters are vowels: A, E, I, O and U. The other 21 letters are consonants. Vowels help us say every syllable clearly.",
                "examples": [
                    "Vowels: A, E, I, O, U",
                    "Consonants: B, C, D, F, G ... and the rest",
                    "Every English word contains at least one vowel sound.",
                ],
            },
            {
                "heading": "A letter has a name and a sound",
                "body": "When we say the alphabet, we say letter names. When we read a word, we usually say letter sounds. Some letters can make more than one sound.",
                "examples": [
                    "The letter B is named 'bee' and sounds like /b/ in book.",
                    "The letter C can sound like /k/ in cat or /s/ in city.",
                    "Say each sound slowly: m - a - p. Now say it quickly: map.",
                ],
            },
        ],
        "vocab": [
            {"word": "letter", "meaning": "a written symbol such as A or b", "example": "The first letter of 'apple' is A."},
            {"word": "alphabet", "meaning": "all 26 letters in order", "example": "We learn the alphabet first."},
            {"word": "vowel", "meaning": "A, E, I, O or U", "example": "The word 'open' begins with a vowel."},
            {"word": "consonant", "meaning": "any letter that is not a vowel", "example": "B, D and M are consonants."},
            {"word": "sound", "meaning": "what a letter or word sounds like", "example": "The sound of S is like a quiet snake."},
        ],
        "check": {
            "question": "How many letters are in the English alphabet?",
            "options": ["21", "24", "26", "30"],
            "answer": 2,
            "explanation": "The English alphabet has 26 letters: 5 vowels and 21 consonants.",
        },
    },
    {
        "id": "greetings",
        "level": "Foundation",
        "title": "Greetings & Introducing Yourself",
        "subtitle": "Say hello, share your name, and begin a friendly conversation.",
        "minutes": 12,
        "goals": [
            "Choose a greeting for different times of day",
            "Introduce yourself in a few clear sentences",
            "Ask and answer simple personal questions",
        ],
        "sections": [
            {
                "heading": "Start with a greeting",
                "body": "A greeting opens the door to conversation. Use 'Hi' or 'Hello' with friends and family. Use 'Good morning', 'Good afternoon' or 'Good evening' in more formal situations.",
                "examples": [
                    "Hi, Ana! How are you?",
                    "Good morning, Mr. Lee.",
                    "Good evening. It is nice to meet you.",
                ],
            },
            {
                "heading": "Share who you are",
                "body": "A simple introduction follows a reliable pattern: name, place, and one friendly detail. You do not need long, complicated sentences.",
                "examples": [
                    "My name is Sam. I am from Canada.",
                    "I am a student, and I am learning English.",
                    "This is my friend, Priya. She is a nurse.",
                ],
            },
            {
                "heading": "Keep the conversation moving",
                "body": "Ask a question after you answer one. This turns an introduction into a real conversation.",
                "examples": [
                    "A: What is your name?  B: I am Daniel. And you?",
                    "A: Where are you from?  B: I am from Brazil. Where are you from?",
                    "A: Nice to meet you.  B: Nice to meet you too.",
                ],
            },
        ],
        "vocab": [
            {"word": "greeting", "meaning": "words you say when you meet someone", "example": "A smile is a friendly greeting."},
            {"word": "introduce", "meaning": "to tell someone your name or another person's name", "example": "Let me introduce my sister."},
            {"word": "from", "meaning": "the place where you were born or live", "example": "I am from Kenya."},
            {"word": "meet", "meaning": "to see and speak to someone for the first time", "example": "Nice to meet you."},
            {"word": "formal", "meaning": "polite and suitable for an official situation", "example": "'Good afternoon' is more formal than 'Hi'."},
        ],
        "check": {
            "question": "Someone says, 'Nice to meet you.' What is the best reply?",
            "options": ["Nice to meet you too.", "I am fine, thank you.", "See you yesterday.", "My name is Monday."],
            "answer": 0,
            "explanation": "A natural reply is 'Nice to meet you too.' It returns the friendly greeting.",
        },
    },
    {
        "id": "numbers",
        "level": "Foundation",
        "title": "Numbers, Days, Months & Dates",
        "subtitle": "Talk about time, birthdays, prices, and everyday plans.",
        "minutes": 12,
        "goals": [
            "Use cardinal and ordinal numbers",
            "Say the days of the week and months of the year",
            "Use in, on and at correctly with time expressions",
        ],
        "sections": [
            {
                "heading": "Numbers you can use",
                "body": "Cardinal numbers count things: one, two, three. Ordinal numbers show order: first, second, third. We use ordinal numbers for dates.",
                "examples": [
                    "I have two brothers.",
                    "Her birthday is on the third of June.",
                    "The shop is on the first floor.",
                ],
            },
            {
                "heading": "Days and months",
                "body": "There are seven days in a week and twelve months in a year. Days and months begin with a capital letter in English.",
                "examples": [
                    "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday",
                    "January, February, March, April, May, June, July, August, September, October, November, December",
                    "I work from Monday to Friday.",
                ],
            },
            {
                "heading": "In, on or at?",
                "body": "Use 'in' for months, years and long periods. Use 'on' for days and dates. Use 'at' for a clock time or a specific moment.",
                "examples": [
                    "My birthday is in September.",
                    "The class is on Tuesday.",
                    "The meeting starts at 9:30.",
                ],
            },
        ],
        "vocab": [
            {"word": "date", "meaning": "the day, month and year", "example": "What is the date today?"},
            {"word": "birthday", "meaning": "the day each year when you celebrate being born", "example": "My birthday is in April."},
            {"word": "ordinal", "meaning": "a number that shows position or order", "example": "First, second and third are ordinal numbers."},
            {"word": "week", "meaning": "seven days", "example": "There are seven days in a week."},
            {"word": "month", "meaning": "one of the twelve parts of a year", "example": "July is a summer month."},
        ],
        "check": {
            "question": "Choose the correct sentence.",
            "options": ["I was born in May.", "I was born on May.", "I was born at May.", "I was born to May."],
            "answer": 0,
            "explanation": "Use 'in' before a month: in May, in July, in December.",
        },
    },
    {
        "id": "nouns-articles",
        "level": "Beginner",
        "title": "Nouns & Articles: a, an, the",
        "subtitle": "Name the world clearly and choose the right little word before it.",
        "minutes": 14,
        "goals": [
            "Identify common and proper nouns",
            "Choose a or an based on sound",
            "Use the for something specific",
        ],
        "sections": [
            {
                "heading": "Nouns name people, places and things",
                "body": "A noun can name a person, place, thing or idea. Common nouns are general, while proper nouns name a particular person or place and begin with a capital letter.",
                "examples": [
                    "Common nouns: teacher, city, book, kindness",
                    "Proper nouns: Ms. Rivera, Tokyo, Monday",
                    "Nouns can be singular (one book) or plural (three books).",
                ],
            },
            {
                "heading": "A or an?",
                "body": "Use 'a' before a consonant sound and 'an' before a vowel sound. It is the sound that matters, not only the first letter.",
                "examples": [
                    "a book, a university (a 'you' sound)",
                    "an apple, an hour (a silent h)",
                    "She has a dog and an umbrella.",
                ],
            },
            {
                "heading": "The means we both know which one",
                "body": "Use 'the' for a specific thing, something already mentioned, or something unique. Use no article for general ideas in the plural or for many uncountable nouns.",
                "examples": [
                    "I saw a cat. The cat was black.",
                    "Please close the door. (the door in this room)",
                    "I like music. (music in general)",
                ],
            },
        ],
        "vocab": [
            {"word": "noun", "meaning": "a word for a person, place, thing or idea", "example": "Chair, hope and London are nouns."},
            {"word": "article", "meaning": "a small word such as a, an or the", "example": "Put an article before the noun."},
            {"word": "singular", "meaning": "one", "example": "The singular form is 'child'."},
            {"word": "plural", "meaning": "more than one", "example": "The plural form is 'children'."},
            {"word": "specific", "meaning": "clearly known and not general", "example": "This is the specific book I wanted."},
        ],
        "check": {
            "question": "I ate ___ apple after lunch.",
            "options": ["a", "an", "the", "no article"],
            "answer": 1,
            "explanation": "'Apple' begins with a vowel sound, so we use 'an'.",
        },
    },
    {
        "id": "simple-present",
        "level": "Beginner",
        "title": "Simple Present: Everyday Actions",
        "subtitle": "Describe routines, habits, and things that are generally true.",
        "minutes": 15,
        "goals": [
            "Form affirmative simple present sentences",
            "Add -s for he, she and it",
            "Make negatives and questions with do and does",
        ],
        "sections": [
            {
                "heading": "Use the simple present for routines",
                "body": "The simple present describes habits, routines, schedules, and facts. The verb usually stays in its base form, except with he, she or it.",
                "examples": [
                    "I drink tea every morning.",
                    "She works at a hospital.",
                    "Water boils at 100 degrees Celsius.",
                ],
            },
            {
                "heading": "The he / she / it rule",
                "body": "With he, she or it, add -s or -es to the verb. If the verb ends in a consonant + y, change y to i and add -es.",
                "examples": [
                    "He walks to school.",
                    "Maya watches the news.",
                    "The baby cries when she is hungry.",
                ],
            },
            {
                "heading": "Negatives and questions",
                "body": "Use do not (don't) or does not (doesn't) plus the base verb. In questions, put do or does first. After does, the main verb does not take -s.",
                "examples": [
                    "I do not eat meat.",
                    "She doesn't work on Sundays.",
                    "Do you speak French?",
                    "Does he live nearby?",
                ],
            },
        ],
        "vocab": [
            {"word": "routine", "meaning": "things you do regularly", "example": "My morning routine is simple."},
            {"word": "habit", "meaning": "something you do often, almost automatically", "example": "Reading is a good habit."},
            {"word": "base verb", "meaning": "the simplest form of a verb", "example": "Walk, eat and study are base verbs."},
            {"word": "negative", "meaning": "a sentence that says something is not true", "example": "I don't like cold coffee."},
            {"word": "schedule", "meaning": "a plan of times and activities", "example": "The train schedule is on the wall."},
        ],
        "check": {
            "question": "She ___ coffee every morning.",
            "options": ["drink", "drinks", "drinking", "is drink"],
            "answer": 1,
            "explanation": "With 'she', add -s to the verb: she drinks.",
        },
    },
    {
        "id": "sentence-building",
        "level": "Beginner",
        "title": "Building a Clear Sentence",
        "subtitle": "Turn words into complete ideas with confidence.",
        "minutes": 12,
        "goals": [
            "Find the subject and the verb",
            "Use subject + verb + object order",
            "Add details without losing clarity",
        ],
        "sections": [
            {
                "heading": "Every complete sentence needs a subject and a verb",
                "body": "The subject tells us who or what the sentence is about. The verb tells us what happens or what the subject is. A group of words without both is usually a fragment.",
                "examples": [
                    "The children / laugh. (subject + verb)",
                    "My neighbour / grows / tomatoes. (subject + verb + object)",
                    "Fragment: Because it was raining.  Complete: We stayed inside because it was raining.",
                ],
            },
            {
                "heading": "The usual English order",
                "body": "English often follows subject + verb + object. Place details such as time and place after the main idea, although a time phrase can also begin the sentence.",
                "examples": [
                    "Aisha / reads / a novel.",
                    "Aisha reads a novel on the bus every morning.",
                    "Every morning, Aisha reads a novel on the bus.",
                ],
            },
            {
                "heading": "Begin and end clearly",
                "body": "Start every sentence with a capital letter. End with a full stop, a question mark or an exclamation mark. These small signals help readers follow your meaning.",
                "examples": [
                    "My brother cooks dinner. (statement)",
                    "Can your brother cook dinner? (question)",
                    "What a wonderful dinner! (exclamation)",
                ],
            },
        ],
        "vocab": [
            {"word": "subject", "meaning": "who or what a sentence is about", "example": "In 'The dog barks', the subject is 'the dog'."},
            {"word": "verb", "meaning": "a word showing an action or state", "example": "Run, think and be are verbs."},
            {"word": "object", "meaning": "the person or thing affected by an action", "example": "In 'I read a book', 'a book' is the object."},
            {"word": "fragment", "meaning": "an incomplete sentence", "example": "'After the movie' is a fragment."},
            {"word": "clause", "meaning": "a group of words with a subject and verb", "example": "The clause 'she smiled' can stand alone."},
        ],
        "check": {
            "question": "Which group of words is a complete sentence?",
            "options": ["Because I was tired.", "The tall tree near the gate.", "My sister sings beautifully.", "After the long meeting."],
            "answer": 2,
            "explanation": "'My sister sings beautifully' has a subject (my sister) and a verb (sings).",
        },
    },
    {
        "id": "pronouns",
        "level": "Beginner",
        "title": "Pronouns & Possessives",
        "subtitle": "Avoid repetition and show who owns what.",
        "minutes": 13,
        "goals": [
            "Use subject and object pronouns",
            "Choose possessive adjectives correctly",
            "Understand possessive pronouns",
        ],
        "sections": [
            {
                "heading": "Subject and object pronouns",
                "body": "A subject pronoun does the action. An object pronoun receives the action or follows a preposition.",
                "examples": [
                    "I / you / he / she / it / we / they",
                    "me / you / him / her / it / us / them",
                    "She called me. I spoke to her.",
                ],
            },
            {
                "heading": "Possessive adjectives come before a noun",
                "body": "Use my, your, his, her, its, our and their to show who owns something. They always sit before the noun.",
                "examples": [
                    "My phone is charging.",
                    "Their house has a red door.",
                    "The dog wagged its tail.",
                ],
            },
            {
                "heading": "Possessive pronouns stand alone",
                "body": "Use mine, yours, his, hers, ours and theirs when the noun is already understood. Do not add a noun after these words.",
                "examples": [
                    "This umbrella is mine.",
                    "That coat is hers.",
                    "Our seats are near the front. Where are theirs?",
                ],
            },
        ],
        "vocab": [
            {"word": "pronoun", "meaning": "a word used instead of a noun", "example": "Instead of saying 'Marta' again, say 'she'."},
            {"word": "subject pronoun", "meaning": "a pronoun that performs the action", "example": "They live upstairs."},
            {"word": "object pronoun", "meaning": "a pronoun that receives the action", "example": "Please call him."},
            {"word": "possessive", "meaning": "showing ownership", "example": "'My' is a possessive word."},
            {"word": "preposition", "meaning": "a word such as in, on, at or with", "example": "The gift is for us."},
        ],
        "check": {
            "question": "This is Maria's bag. It is ___.",
            "options": ["her", "she", "hers", "her's"],
            "answer": 2,
            "explanation": "'Hers' is the possessive pronoun. It stands alone and replaces 'her bag'.",
        },
    },
    {
        "id": "questions",
        "level": "Growing",
        "title": "Questions: Who, What, Where, When, Why, How",
        "subtitle": "Ask clearly and keep conversations moving.",
        "minutes": 14,
        "goals": [
            "Form yes/no questions with be and do",
            "Use question words for specific information",
            "Keep the correct word order",
        ],
        "sections": [
            {
                "heading": "Yes/no questions",
                "body": "With the verb 'be', put the verb before the subject. With action verbs, use do or does before the subject. The main verb stays in its base form.",
                "examples": [
                    "Are you ready?",
                    "Is the shop open?",
                    "Do you like spicy food?",
                    "Does she need a lift?",
                ],
            },
            {
                "heading": "Information questions",
                "body": "Most information questions follow this order: question word + auxiliary verb + subject + main verb. Think of it as a train with a fixed carriage order.",
                "examples": [
                    "Where do you live?",
                    "What does he do?",
                    "When did they arrive?",
                    "How can I help you?",
                ],
            },
            {
                "heading": "Questions with prepositions",
                "body": "In everyday English, the preposition often comes at the end of the question. This can sound surprising, but it is natural.",
                "examples": [
                    "Who are you waiting for?",
                    "What are you looking at?",
                    "Which city do you live in?",
                ],
            },
        ],
        "vocab": [
            {"word": "question word", "meaning": "a word such as who, what or where that asks for information", "example": "Where is the station?"},
            {"word": "auxiliary", "meaning": "a helping verb such as do, be or have", "example": "Do you know the answer?"},
            {"word": "word order", "meaning": "the arrangement of words in a sentence", "example": "English questions have a special word order."},
            {"word": "specific", "meaning": "exact and clearly defined", "example": "She asked a specific question about the price."},
            {"word": "polite", "meaning": "respectful and considerate", "example": "'Could you help me?' is polite."},
        ],
        "check": {
            "question": "Where ___ you live?",
            "options": ["are", "do", "does", "is"],
            "answer": 1,
            "explanation": "Use 'do' with 'you' for a simple present question: Where do you live?",
        },
    },
    {
        "id": "past-simple",
        "level": "Growing",
        "title": "Past Simple: Talking About Yesterday",
        "subtitle": "Tell stories and share what happened before now.",
        "minutes": 15,
        "goals": [
            "Form the past simple of regular verbs",
            "Recognise common irregular verbs",
            "Use was, were, didn't and past-time expressions",
        ],
        "sections": [
            {
                "heading": "Regular verbs add -ed",
                "body": "For most regular verbs, add -ed. If the verb ends in e, add -d. If a short verb ends in consonant-vowel-consonant, double the final consonant.",
                "examples": [
                    "walk → walked",
                    "arrive → arrived",
                    "stop → stopped",
                    "study → studied",
                ],
            },
            {
                "heading": "Irregular verbs change shape",
                "body": "Many common verbs do not use -ed. These irregular forms need to be learned through use and repetition. Keep a small list and review it often.",
                "examples": [
                    "go → went, see → saw, eat → ate",
                    "have → had, make → made, take → took",
                    "I went to the market and bought three oranges.",
                ],
            },
            {
                "heading": "Negatives, questions, and was/were",
                "body": "Use did not (didn't) + base verb for negatives, and did + subject + base verb for questions. Use was or were for the past of 'be'.",
                "examples": [
                    "I didn't watch the film.",
                    "Did you finish your work?",
                    "She was tired. They were at home.",
                    "We visited the museum last Saturday.",
                ],
            },
        ],
        "vocab": [
            {"word": "past", "meaning": "a time before now", "example": "Yesterday is in the past."},
            {"word": "regular verb", "meaning": "a verb that forms the past with -ed", "example": "Play becomes played."},
            {"word": "irregular verb", "meaning": "a verb with a special past form", "example": "Go becomes went."},
            {"word": "yesterday", "meaning": "the day before today", "example": "I called her yesterday."},
            {"word": "event", "meaning": "something that happens", "example": "The concert was a happy event."},
        ],
        "check": {
            "question": "Yesterday, I ___ to the store.",
            "options": ["go", "gone", "went", "goed"],
            "answer": 2,
            "explanation": "'Go' is irregular. Its past simple form is 'went'.",
        },
    },
    {
        "id": "future",
        "level": "Growing",
        "title": "The Future: will & going to",
        "subtitle": "Make predictions, promises, and plans.",
        "minutes": 14,
        "goals": [
            "Use will for decisions, promises and predictions",
            "Use going to for plans and visible evidence",
            "Use the present continuous for arrangements",
        ],
        "sections": [
            {
                "heading": "Will for quick decisions and promises",
                "body": "Use will + base verb when you decide at the moment of speaking, make a promise, or offer help. It is also common for general predictions.",
                "examples": [
                    "The phone is ringing. I will answer it.",
                    "I will help you with those bags.",
                    "I think people will live longer in the future.",
                ],
            },
            {
                "heading": "Going to for plans and evidence",
                "body": "Use be going to + base verb for a plan made before now, or when you can see evidence that something is about to happen.",
                "examples": [
                    "We are going to visit my aunt on Sunday.",
                    "Look at those clouds. It is going to rain.",
                    "She is going to study nursing next year.",
                ],
            },
            {
                "heading": "Present continuous for arrangements",
                "body": "For a fixed arrangement with another person or a time in your diary, the present continuous is natural.",
                "examples": [
                    "I am meeting the dentist at 3 p.m. tomorrow.",
                    "They are flying to Rome on Friday.",
                    "We are having dinner with friends tonight.",
                ],
            },
        ],
        "vocab": [
            {"word": "prediction", "meaning": "a statement about what you think will happen", "example": "My prediction is that prices will rise."},
            {"word": "promise", "meaning": "a serious statement that you will do something", "example": "I promise I will call."},
            {"word": "arrangement", "meaning": "a plan made with someone else", "example": "I have an arrangement to meet Leo at noon."},
            {"word": "evidence", "meaning": "something you can see or know that supports an idea", "example": "Dark clouds are evidence of rain."},
            {"word": "decision", "meaning": "a choice you make", "example": "It was a difficult decision."},
        ],
        "check": {
            "question": "Look at those clouds! It ___ rain.",
            "options": ["will", "is going to", "goes to", "is will"],
            "answer": 1,
            "explanation": "We can see evidence (the clouds), so 'is going to' is the most natural choice.",
        },
    },
    {
        "id": "adjectives-adverbs",
        "level": "Growing",
        "title": "Adjectives, Adverbs & Comparisons",
        "subtitle": "Add colour and detail to your sentences.",
        "minutes": 15,
        "goals": [
            "Place adjectives before nouns or after be",
            "Form adverbs of manner and frequency",
            "Compare two or more things correctly",
        ],
        "sections": [
            {
                "heading": "Adjectives describe nouns",
                "body": "An adjective gives more information about a noun. It can come before the noun or after a linking verb such as be, seem or feel.",
                "examples": [
                    "A quiet street. The street is quiet.",
                    "She seems tired today.",
                    "That was an interesting conversation.",
                ],
            },
            {
                "heading": "Adverbs describe verbs, adjectives or other adverbs",
                "body": "Many adverbs of manner end in -ly. They often come after the verb or object. Adverbs of frequency usually come before the main verb.",
                "examples": [
                    "He speaks clearly.",
                    "She carefully opened the letter.",
                    "I usually walk to work.",
                    "They are always kind to visitors.",
                ],
            },
            {
                "heading": "Comparatives and superlatives",
                "body": "Use -er and -est for many short adjectives. Use more and most for longer adjectives. Some common adjectives are irregular.",
                "examples": [
                    "small → smaller → the smallest",
                    "comfortable → more comfortable → the most comfortable",
                    "good → better → the best",
                    "This room is brighter than that one.",
                ],
            },
        ],
        "vocab": [
            {"word": "adjective", "meaning": "a word that describes a noun", "example": "Warm, honest and blue are adjectives."},
            {"word": "adverb", "meaning": "a word that describes a verb, adjective or adverb", "example": "She sings beautifully."},
            {"word": "comparative", "meaning": "comparing two things", "example": "This bag is lighter than that one."},
            {"word": "superlative", "meaning": "comparing three or more things and showing the extreme", "example": "It is the tallest building in the city."},
            {"word": "frequency", "meaning": "how often something happens", "example": "Always, often and never show frequency."},
        ],
        "check": {
            "question": "She speaks English ___.",
            "options": ["fluent", "fluently", "more fluent", "fluency"],
            "answer": 1,
            "explanation": "Use the adverb 'fluently' to describe how she speaks. The verb 'speaks' needs an adverb.",
        },
    },
    {
        "id": "linking-words",
        "level": "Growing",
        "title": "Linking Ideas: and, but, because, so",
        "subtitle": "Connect your thoughts so readers can follow your logic.",
        "minutes": 13,
        "goals": [
            "Join ideas with and, but and or",
            "Show reasons and results with because and so",
            "Use however and although in more formal writing",
        ],
        "sections": [
            {
                "heading": "Add, contrast, or choose",
                "body": "Use 'and' to add similar information, 'but' to show contrast, and 'or' to present a choice. These are coordinating conjunctions.",
                "examples": [
                    "I bought bread and milk.",
                    "The room was small but comfortable.",
                    "Would you like tea or coffee?",
                ],
            },
            {
                "heading": "Show reasons and results",
                "body": "Use 'because' before a reason. Use 'so' before a result. The order can change, but the meaning stays clear.",
                "examples": [
                    "I stayed home because I was unwell.",
                    "I was unwell, so I stayed home.",
                    "Because the bus was late, we missed the film.",
                ],
            },
            {
                "heading": "Formal linking words",
                "body": "'However' introduces a contrasting sentence. 'Although' introduces a contrasting clause. They make writing flow smoothly but should not be overused.",
                "examples": [
                    "The plan was expensive. However, it was worth it.",
                    "Although it was raining, the match continued.",
                    "First, prepare the ingredients. Then, heat the pan. Finally, serve the meal.",
                ],
            },
        ],
        "vocab": [
            {"word": "contrast", "meaning": "a clear difference between two things", "example": "The contrast between the two designs is obvious."},
            {"word": "reason", "meaning": "why something happens", "example": "The reason for the delay was heavy traffic."},
            {"word": "result", "meaning": "what happens because of something", "example": "The result of the storm was a power cut."},
            {"word": "conjunction", "meaning": "a word that joins parts of a sentence", "example": "And, but and because are conjunctions."},
            {"word": "flow", "meaning": "the smooth movement from one idea to the next", "example": "Linking words improve the flow of a paragraph."},
        ],
        "check": {
            "question": "I took an umbrella ___ it was raining.",
            "options": ["but", "because", "or", "although"],
            "answer": 1,
            "explanation": "'Because' introduces the reason: it was raining.",
        },
    },
    {
        "id": "present-perfect",
        "level": "Confident",
        "title": "Present Perfect: Experience & Change",
        "subtitle": "Connect the past to the present with have or has + past participle.",
        "minutes": 16,
        "goals": [
            "Form the present perfect with have or has",
            "Talk about life experience with ever and never",
            "Use for and since correctly",
        ],
        "sections": [
            {
                "heading": "The shape of the present perfect",
                "body": "Use have or has + the past participle. Regular past participles end in -ed. Many common verbs are irregular, such as eaten, seen, written and been.",
                "examples": [
                    "I have visited Canada twice.",
                    "She has finished her report.",
                    "They have never tried sushi.",
                ],
            },
            {
                "heading": "Experience, not a specific time",
                "body": "Use the present perfect for experiences when the exact time is not important. If you name a finished past time, use the past simple instead.",
                "examples": [
                    "I have seen that film. (at some point in my life)",
                    "I saw that film last Friday. (specific finished time)",
                    "Have you ever lived abroad?",
                ],
            },
            {
                "heading": "For and since",
                "body": "Use 'for' with a length of time and 'since' with a starting point. The action or situation continues up to now.",
                "examples": [
                    "I have worked here for five years.",
                    "She has lived in Toronto since 2019.",
                    "We have been friends for a long time.",
                ],
            },
        ],
        "vocab": [
            {"word": "experience", "meaning": "something you have done or lived through", "example": "Travel is a valuable experience."},
            {"word": "past participle", "meaning": "the verb form used after have or has", "example": "The past participle of 'write' is 'written'."},
            {"word": "since", "meaning": "from a starting point in time", "example": "I have known her since 2018."},
            {"word": "for", "meaning": "used with a length of time", "example": "We waited for two hours."},
            {"word": "abroad", "meaning": "in or to another country", "example": "He has never travelled abroad."},
        ],
        "check": {
            "question": "I ___ never eaten sushi.",
            "options": ["am", "have", "has", "had"],
            "answer": 1,
            "explanation": "Use 'have' with 'I' in the present perfect: I have never eaten sushi.",
        },
    },
    {
        "id": "conditionals",
        "level": "Confident",
        "title": "Conditionals: If This, Then That",
        "subtitle": "Talk about possibilities, plans, and imagined situations.",
        "minutes": 16,
        "goals": [
            "Use the zero conditional for facts",
            "Use the first conditional for real future possibilities",
            "Use the second conditional for imagined situations",
        ],
        "sections": [
            {
                "heading": "Zero conditional: facts",
                "body": "Use if + present simple, then present simple for things that are generally true. You can often replace 'if' with 'when'.",
                "examples": [
                    "If you heat ice, it melts.",
                    "When I drink coffee late, I cannot sleep.",
                    "Plants die if they do not get water.",
                ],
            },
            {
                "heading": "First conditional: real possibilities",
                "body": "Use if + present simple, then will + base verb for a possible future situation and its result.",
                "examples": [
                    "If it rains, I will stay home.",
                    "If you study a little every day, you will improve.",
                    "She will call you if she needs help.",
                ],
            },
            {
                "heading": "Second conditional: imagination",
                "body": "Use if + past simple, then would + base verb for an unreal or unlikely present or future situation. With the verb 'be', use 'were' in formal English.",
                "examples": [
                    "If I had more time, I would learn the piano.",
                    "If I were you, I would apply for the job.",
                    "What would you do if you won the lottery?",
                ],
            },
        ],
        "vocab": [
            {"word": "condition", "meaning": "something that must happen for a result to occur", "example": "The condition for entry is a ticket."},
            {"word": "possibility", "meaning": "something that might happen", "example": "There is a possibility of snow tonight."},
            {"word": "imagine", "meaning": "to form a picture in your mind", "example": "Imagine living by the sea."},
            {"word": "unlikely", "meaning": "not probable", "example": "It is unlikely to snow in summer."},
            {"word": "result", "meaning": "the outcome of an action or condition", "example": "The result was better than expected."},
        ],
        "check": {
            "question": "If it rains tomorrow, I ___ stay home.",
            "options": ["will", "would", "am", "did"],
            "answer": 0,
            "explanation": "This is a real future possibility, so use the first conditional: if + present, will + base verb.",
        },
    },
    {
        "id": "polite-english",
        "level": "Confident",
        "title": "Polite English & Clear Emails",
        "subtitle": "Ask for help, set boundaries, and write messages people appreciate.",
        "minutes": 15,
        "goals": [
            "Make polite requests with could and would",
            "Soften requests and disagreements",
            "Write a short, clear email",
        ],
        "sections": [
            {
                "heading": "Polite requests",
                "body": "Use could, would, or 'Do you mind...?' to make a request sound respectful. Add 'please' where it feels natural, but do not repeat it in every sentence.",
                "examples": [
                    "Could you send me the file?",
                    "Would you mind closing the window?",
                    "I would appreciate your help with this.",
                ],
            },
            {
                "heading": "Soften what you say",
                "body": "English speakers often use cautious phrases to avoid sounding direct or harsh. This is especially useful at work and with people you do not know well.",
                "examples": [
                    "I think there may be a small mistake.",
                    "I'm afraid I can't attend on Friday.",
                    "Would it be possible to meet next week?",
                ],
            },
            {
                "heading": "A reliable email structure",
                "body": "A clear email has a subject, a greeting, a short purpose, the necessary details, a clear next step, and a polite closing. Keep paragraphs short.",
                "examples": [
                    "Subject: Question about Friday's meeting",
                    "Dear Ms. Chen, I hope you are well. I am writing to ask ...",
                    "Thank you for your time. Best regards, Alex",
                ],
            },
        ],
        "vocab": [
            {"word": "request", "meaning": "a polite ask for something", "example": "She made a simple request for more time."},
            {"word": "appreciate", "meaning": "to be grateful for something", "example": "I appreciate your patience."},
            {"word": "regards", "meaning": "a polite closing word in a message", "example": "Best regards, Sam"},
            {"word": "tone", "meaning": "the feeling or attitude of your words", "example": "A friendly tone helps readers feel at ease."},
            {"word": "clarify", "meaning": "to make something easier to understand", "example": "Could you clarify the deadline?"},
        ],
        "check": {
            "question": "Which request is the most polite?",
            "options": ["Send me the report now.", "Could you send me the report, please?", "You must send it.", "Report. Now."],
            "answer": 1,
            "explanation": "'Could you ... please?' is polite and leaves room for the other person to respond.",
        },
    },
    {
        "id": "idioms",
        "level": "Confident",
        "title": "Idioms & Reading Between the Lines",
        "subtitle": "Understand what English really means in context.",
        "minutes": 16,
        "goals": [
            "Recognise common English idioms",
            "Use context to infer meaning",
            "Notice tone and implied meaning",
        ],
        "sections": [
            {
                "heading": "Idioms are groups of words with a special meaning",
                "body": "An idiom's meaning is not the literal meaning of each word. Context tells you what the speaker really intends.",
                "examples": [
                    "'Break the ice' means to help people feel comfortable.",
                    "'Under the weather' means feeling unwell.",
                    "'A piece of cake' means something very easy.",
                ],
            },
            {
                "heading": "Use the words around the idiom",
                "body": "When you meet an unfamiliar phrase, look for clues in the sentence. Ask: Is the situation positive or negative? What happened before and after?",
                "examples": [
                    "The exam was a piece of cake. I finished in ten minutes.",
                    "She looked under the weather, so I offered to drive her home.",
                    "He broke the ice with a funny story about his dog.",
                ],
            },
            {
                "heading": "Read for tone, not just facts",
                "body": "Writers suggest feelings through word choice. Words such as 'finally', 'unfortunately', or 'surprisingly' tell you how to read the sentence. A polite phrase can also hide a firm No.",
                "examples": [
                    "'That's an interesting idea.' (could be polite disagreement)",
                    "'Unfortunately, we are unable to offer you the position.' (a clear negative result, softened)",
                    "'I'd love to, but I'm fully booked.' (a polite refusal)",
                ],
            },
        ],
        "vocab": [
            {"word": "idiom", "meaning": "a phrase with a meaning different from its literal words", "example": "'Break a leg' means good luck."},
            {"word": "literal", "meaning": "the basic, exact meaning of words", "example": "The literal meaning of 'cold' is low temperature."},
            {"word": "context", "meaning": "the words and situation around something", "example": "Context helps you understand a new word."},
            {"word": "infer", "meaning": "to understand something not stated directly", "example": "We can infer that she was disappointed."},
            {"word": "tone", "meaning": "the attitude behind the words", "example": "Her tone was calm but firm."},
        ],
        "check": {
            "question": "What does 'break the ice' mean?",
            "options": ["Damage a frozen lake", "Help people feel more comfortable", "End a friendship", "Make a cold drink"],
            "answer": 1,
            "explanation": "'Break the ice' means to help people relax and start talking in a new or awkward situation.",
        },
    },
]

# ---------------------------------------------------------------------------
# Reading library
# ---------------------------------------------------------------------------

READINGS = [
    {
        "id": "first-day",
        "title": "My First Day at School",
        "level": "Foundation",
        "minutes": 3,
        "focus": "Simple present & feelings",
        "intro": "A short story about a new school, a kind teacher, and one small brave step.",
        "paragraphs": [
            "My name is Lina. Today is my first day at a new school. I feel nervous. I hold my bag tightly and look at the big red door.",
            "A teacher smiles at me. 'Good morning, Lina. Welcome to our class.' She shows me a seat near the window. A girl named Ava says hello. She has a bright yellow pencil.",
            "We read a short story about a clever fox. I do not understand every word, but I understand the story. At lunch, Ava shares an apple with me.",
            "After school, I walk home with a small smile. A new place is not easy, but kind people make it brighter.",
        ],
        "glossary": [
            {"word": "nervous", "meaning": "worried or a little afraid"},
            {"word": "tightly", "meaning": "with a strong hold"},
            {"word": "welcome", "meaning": "used to say you are happy someone is there"},
            {"word": "bright", "meaning": "full of light or strong in colour"},
            {"word": "share", "meaning": "to let someone use or have part of something"},
        ],
        "questions": [
            {
                "question": "How does Lina feel at the start of the story?",
                "options": ["Angry", "Nervous", "Bored", "Sleepy"],
                "answer": 1,
                "explanation": "The story says, 'I feel nervous.'",
            },
            {
                "question": "Who says hello to Lina?",
                "options": ["Ava", "The head teacher", "Her mother", "The fox"],
                "answer": 0,
                "explanation": "A girl named Ava says hello and later shares an apple.",
            },
            {
                "question": "What helps Lina feel better?",
                "options": ["A long test", "Kind people", "A new bag", "The rain"],
                "answer": 1,
                "explanation": "The last line says that kind people make a new place brighter.",
            },
        ],
    },
    {
        "id": "lost-cat",
        "title": "The Lost Cat",
        "level": "Foundation",
        "minutes": 4,
        "focus": "Past simple & community",
        "intro": "A cat disappears, and a quiet street discovers how much it cares.",
        "paragraphs": [
            "On Saturday morning, Mr. Patel opened his door and called, 'Mango! Breakfast!' No cat came. Mango, his orange cat, was missing.",
            "Mr. Patel walked to the end of the street. He asked his neighbours, 'Have you seen Mango?' Mrs. Rossi checked her garden. Two children looked under every car. Nobody had seen the cat.",
            "Then a small voice said, 'I saw an orange cat near the library.' It was Nora, who lived across the road. Everyone followed her. There was Mango, sitting on a warm library window ledge.",
            "Mr. Patel laughed with relief. That evening, he brought a plate of biscuits to Nora's family. 'For the best detective on the street,' he said.",
        ],
        "glossary": [
            {"word": "missing", "meaning": "not in the usual place; lost"},
            {"word": "neighbour", "meaning": "a person who lives near you"},
            {"word": "ledge", "meaning": "a narrow shelf along a wall or window"},
            {"word": "relief", "meaning": "the good feeling when a worry ends"},
            {"word": "detective", "meaning": "someone who solves a mystery"},
        ],
        "questions": [
            {
                "question": "What is the cat's name?",
                "options": ["Nora", "Mango", "Rossi", "Patel"],
                "answer": 1,
                "explanation": "The cat is called Mango.",
            },
            {
                "question": "Who saw the cat near the library?",
                "options": ["Mr. Patel", "Mrs. Rossi", "Nora", "A librarian"],
                "answer": 2,
                "explanation": "Nora said she saw an orange cat near the library.",
            },
            {
                "question": "Why does Mr. Patel bring biscuits?",
                "options": ["To thank Nora", "To feed Mango", "To sell them", "To welcome a new neighbour"],
                "answer": 0,
                "explanation": "He brings biscuits to thank Nora for finding Mango.",
            },
        ],
    },
    {
        "id": "market",
        "title": "A Trip to the Market",
        "level": "Beginner",
        "minutes": 4,
        "focus": "Shopping language & numbers",
        "intro": "A practical story full of useful words for buying food.",
        "paragraphs": [
            "Every Sunday, Amina visits the green market near her home. She takes a cloth bag and a short shopping list. First, she buys tomatoes and onions. The tomatoes are red and firm. They cost three dollars.",
            "Next, she stops at a bread stall. The baker has just taken warm loaves from the oven. 'I'll take one brown loaf, please,' Amina says. The baker wraps it in paper and wishes her a good day.",
            "At the last stall, Amina chooses a bunch of yellow bananas. She asks, 'How much are these?' The seller answers, 'Two dollars.' She pays and puts the bananas in her bag.",
            "On the way home, Amina sees a friend. They share a bench, a banana, and a few minutes of easy conversation. The market is not only for food; it is also a place to meet.",
        ],
        "glossary": [
            {"word": "stall", "meaning": "a small table or shop in a market"},
            {"word": "loaf", "meaning": "bread baked in one large piece"},
            {"word": "bunch", "meaning": "a group of things held or growing together"},
            {"word": "firm", "meaning": "solid and not soft"},
            {"word": "conversation", "meaning": "a talk between people"},
        ],
        "questions": [
            {
                "question": "What does Amina buy first?",
                "options": ["Bread", "Bananas", "Tomatoes and onions", "A cloth bag"],
                "answer": 2,
                "explanation": "The first purchase is tomatoes and onions.",
            },
            {
                "question": "How much are the bananas?",
                "options": ["One dollar", "Two dollars", "Three dollars", "Five dollars"],
                "answer": 1,
                "explanation": "The seller says the bananas are two dollars.",
            },
            {
                "question": "What does the story suggest about the market?",
                "options": ["It is only for tourists", "It is a social place too", "It sells only bread", "It is always empty"],
                "answer": 1,
                "explanation": "The last paragraph says the market is also a place to meet people.",
            },
        ],
    },
    {
        "id": "pancakes",
        "title": "Making Pancakes Together",
        "level": "Beginner",
        "minutes": 5,
        "focus": "Instructions & sequence words",
        "intro": "A recipe story with clear steps, family teamwork, and a small kitchen mistake.",
        "paragraphs": [
            "On rainy mornings, Ben and his grandfather make pancakes. They have a simple routine. Ben measures the flour while Grandpa cracks the eggs. Then Ben pours in the milk and stirs until the batter is smooth.",
            "Grandpa heats the pan and adds a little butter. 'Wait for the pan to get hot,' he says. Ben waits. He is not very patient, but he watches the butter shine and melt.",
            "The first pancake is a little crooked. Ben laughs. 'It looks like a map of an island!' Grandpa flips it carefully. The second one is round and golden. Soon there is a warm stack on the table.",
            "They eat their pancakes with berries and honey. Ben decides that the crooked one tastes just as good as the perfect one. 'Next time,' he says, 'I'll make the first pancake round.' Grandpa smiles. 'Next time,' he agrees.",
        ],
        "glossary": [
            {"word": "measure", "meaning": "to find an exact amount"},
            {"word": "batter", "meaning": "a thick mixture used to make pancakes or cake"},
            {"word": "crooked", "meaning": "not straight or perfectly shaped"},
            {"word": "flip", "meaning": "to turn something over quickly"},
            {"word": "stack", "meaning": "a pile of things placed on top of each other"},
        ],
        "questions": [
            {
                "question": "Who cracks the eggs?",
                "options": ["Ben", "Grandpa", "Ben's mother", "The narrator"],
                "answer": 1,
                "explanation": "Grandpa cracks the eggs while Ben measures the flour.",
            },
            {
                "question": "What does the first pancake look like?",
                "options": ["A perfect circle", "A map of an island", "A small boat", "A yellow pencil"],
                "answer": 1,
                "explanation": "Ben says it looks like a map of an island.",
            },
            {
                "question": "Which word means 'to turn something over quickly'?",
                "options": ["measure", "stir", "flip", "melt"],
                "answer": 2,
                "explanation": "To 'flip' a pancake is to turn it over quickly.",
            },
        ],
    },
    {
        "id": "bus-driver",
        "title": "The Bus Driver's Secret",
        "level": "Growing",
        "minutes": 6,
        "focus": "Past continuous & inference",
        "intro": "A warm story about a bus route, a daily habit, and a surprising reason.",
        "paragraphs": [
            "Every morning at 7:15, Mr. Okafor drove the number 42 bus through the city. He knew every stop, every crack in the road, and most of his passengers by name. He also knew that an elderly woman, Mrs. Bell, always sat in the front seat on the left.",
            "One Monday, Mrs. Bell was not there. Mr. Okafor waited an extra ten seconds at her stop, but the doors closed and the bus moved on. He kept looking at the empty seat in his mirror. At the end of his route, he asked another driver if she had seen Mrs. Bell. Nobody knew.",
            "The next morning, he arrived early at her street. The curtains were closed. He knocked on the door of the small yellow house. A nurse opened it. 'Mrs. Bell is fine,' she said. 'She is staying with her daughter this week. But she asked me to give you this.'",
            "It was a hand-drawn card: a bus, a smiling driver, and the words 'Thank you for always waiting.' Mr. Okafor put the card above his dashboard. For the rest of the week, he drove his route with a quiet smile, and he still paused for ten extra seconds at her stop.",
        ],
        "glossary": [
            {"word": "passenger", "meaning": "a person travelling in a vehicle"},
            {"word": "route", "meaning": "the path a bus or train follows"},
            {"word": "curtain", "meaning": "a cloth that covers a window"},
            {"word": "dashboard", "meaning": "the panel in front of a driver"},
            {"word": "pause", "meaning": "to stop for a short time"},
        ],
        "questions": [
            {
                "question": "Why did Mr. Okafor wait ten extra seconds?",
                "options": ["The bus was early", "He was looking for Mrs. Bell", "He was checking the road", "He wanted to talk to another driver"],
                "answer": 1,
                "explanation": "He waited at Mrs. Bell's stop because she always travelled at that time.",
            },
            {
                "question": "Where was Mrs. Bell?",
                "options": ["In hospital", "At the market", "Staying with her daughter", "On another bus"],
                "answer": 2,
                "explanation": "The nurse explains that Mrs. Bell is staying with her daughter.",
            },
            {
                "question": "What can we infer about Mr. Okafor?",
                "options": ["He dislikes his job", "He cares about his passengers", "He is new to the route", "He wants a new bus"],
                "answer": 1,
                "explanation": "His concern, the visit, and the extra pause show that he cares about his passengers.",
            },
        ],
    },
    {
        "id": "new-friend",
        "title": "A Letter from a New Friend",
        "level": "Growing",
        "minutes": 6,
        "focus": "Letter writing & present perfect",
        "intro": "An email between two pen pals shows how to share news and ask thoughtful questions.",
        "paragraphs": [
            "Dear Amara,",
            "Hello from Edinburgh! I have now been here for three weeks, and the city still surprises me every day. I have walked up a hill with a castle on top and I have eaten a very strange but delicious dish made with potatoes and haggis. I have not yet tried the famous deep-fried chocolate bar, but my new friend Callum says I must.",
            "I have started a photography class on Tuesday evenings. There are eight people in the group, and our teacher is patient and funny. Last week, we took pictures of the old streets at sunset. I was nervous about showing my work, but everyone was kind. My favourite photo is of a tiny red door between two grey buildings.",
            "What have you been doing since your exams ended? Have you visited your grandmother's farm? You mentioned that you wanted to learn how to make bread. I would love to hear how it went. Send a photo if you can!",
            "Write soon,",
            "Nadia",
        ],
        "glossary": [
            {"word": "pen pal", "meaning": "a friend you write to, often in another place"},
            {"word": "delicious", "meaning": "very tasty"},
            {"word": "sunset", "meaning": "the time when the sun goes down"},
            {"word": "patient", "meaning": "able to wait calmly without becoming annoyed"},
            {"word": "mention", "meaning": "to speak or write about something briefly"},
        ],
        "questions": [
            {
                "question": "How long has Nadia been in Edinburgh?",
                "options": ["Three days", "Three weeks", "Three months", "Three years"],
                "answer": 1,
                "explanation": "Nadia writes, 'I have now been here for three weeks.'",
            },
            {
                "question": "What has Nadia not tried yet?",
                "options": ["Haggis", "A photography class", "The deep-fried chocolate bar", "Walking up the hill"],
                "answer": 2,
                "explanation": "She says she has not yet tried the deep-fried chocolate bar.",
            },
            {
                "question": "Why does Nadia ask about the farm?",
                "options": ["She wants to visit it", "She remembers Amara's plans", "She needs bread", "She is moving there"],
                "answer": 1,
                "explanation": "Nadia remembers that Amara wanted to visit her grandmother's farm and learn to make bread.",
            },
        ],
    },
    {
        "id": "sleep",
        "title": "Why We Need Sleep",
        "level": "Confident",
        "minutes": 7,
        "focus": "Main ideas & supporting details",
        "intro": "A clear explanation of what sleep does for the body and mind.",
        "paragraphs": [
            "Sleep can look like a passive activity, but the brain remains busy throughout the night. During sleep, the body repairs tissue, strengthens the immune system, and stores new memories. This is one reason why a good night's sleep often makes a difficult problem feel easier in the morning.",
            "Sleep happens in cycles. Each cycle includes lighter and deeper stages, as well as a stage called REM sleep. During REM sleep, the eyes move quickly beneath closed eyelids and dreams are common. Most adults need seven to nine hours of sleep, although the exact amount varies from person to person.",
            "Modern life can make sleep difficult. Bright screens late at night, stress, and irregular schedules all send mixed signals to the body's internal clock. Experts often suggest keeping a regular bedtime, dimming lights in the evening, and avoiding caffeine late in the day.",
            "Sleep is not a luxury or a sign of laziness. It is an essential part of health, much like food and exercise. Treating sleep as a priority can improve concentration, mood, and long-term well-being.",
        ],
        "glossary": [
            {"word": "passive", "meaning": "involving little action"},
            {"word": "immune system", "meaning": "the body's defence against illness"},
            {"word": "cycle", "meaning": "a repeated series of events"},
            {"word": "irregular", "meaning": "not following a steady pattern"},
            {"word": "essential", "meaning": "extremely important and necessary"},
        ],
        "questions": [
            {
                "question": "What is the main idea of the passage?",
                "options": ["Dreams are always strange", "Sleep is essential for health", "Caffeine helps people sleep", "Adults need less sleep than children"],
                "answer": 1,
                "explanation": "The passage explains the benefits of sleep and argues that it is essential for health.",
            },
            {
                "question": "According to the passage, what happens during sleep?",
                "options": ["The brain stops working", "The body repairs tissue", "The body needs less food", "The heart stops briefly"],
                "answer": 1,
                "explanation": "The first paragraph says the body repairs tissue during sleep.",
            },
            {
                "question": "Which suggestion is NOT mentioned?",
                "options": ["Keep a regular bedtime", "Dim the lights", "Avoid late caffeine", "Sleep in a cold room"],
                "answer": 3,
                "explanation": "The passage does not mention keeping the room cold.",
            },
        ],
    },
    {
        "id": "community-garden",
        "title": "The Community Garden",
        "level": "Confident",
        "minutes": 8,
        "focus": "Cause, effect & community",
        "intro": "How an empty city lot became a shared garden, a classroom, and a friendship.",
        "paragraphs": [
            "For years, the corner lot on Hazel Street was a patch of cracked concrete and weeds. Residents walked past it without looking twice. Then a retired teacher named Mr. Adeyemi posted a simple notice on the community board: 'Would anyone like to grow something here?'",
            "The first meeting attracted only six people. They had no funding and very little equipment. A local café donated old wooden crates. A hardware store gave them a bag of seeds and a broken hose, which a neighbour repaired in his garage. By spring, the concrete had been covered with raised beds.",
            "The garden changed more than the view. Children learned where vegetables come from. Older residents shared recipes and stories. A group of teenagers built a small bench from reclaimed wood. When a heatwave damaged half the tomato plants, neighbours took turns carrying water at dawn.",
            "Today, the garden produces more food than the members can eat, so a box at the entrance offers extra produce to anyone who needs it. A sign above the gate reads, 'Grown together.' It is a fitting description of a place that began with one question and a great deal of patience.",
        ],
        "glossary": [
            {"word": "lot", "meaning": "an empty area of land"},
            {"word": "funding", "meaning": "money provided for a project"},
            {"word": "reclaimed", "meaning": "saved and reused"},
            {"word": "heatwave", "meaning": "a long period of unusually hot weather"},
            {"word": "produce", "meaning": "fruit and vegetables grown for food"},
        ],
        "questions": [
            {
                "question": "Who first suggested the garden?",
                "options": ["A local café owner", "Mr. Adeyemi", "A group of teenagers", "The city council"],
                "answer": 1,
                "explanation": "Mr. Adeyemi posted the notice that began the project.",
            },
            {
                "question": "How did the community get supplies?",
                "options": ["From a large government grant", "From donations and repairs by neighbours", "By selling vegetables", "From a school"],
                "answer": 1,
                "explanation": "A café donated crates, a hardware store gave seeds and a hose, and a neighbour repaired the hose.",
            },
            {
                "question": "What does 'Grown together' suggest?",
                "options": ["Only vegetables grew there", "The garden is a shared achievement", "The garden is closed to the public", "The garden was built quickly"],
                "answer": 1,
                "explanation": "The sign reflects how the garden grew through collective effort and relationships.",
            },
        ],
    },
]

# ---------------------------------------------------------------------------
# Writing studio
# ---------------------------------------------------------------------------

WRITING_PROMPTS = [
    {
        "id": "introduce",
        "title": "Introduce Yourself",
        "level": "Foundation",
        "kind": "Personal",
        "target": 70,
        "scenario": "Write a short introduction for a new class, a community group, or an English study group.",
        "instructions": [
            "Say your name and where you are from.",
            "Share two things you enjoy.",
            "Add one goal for your English learning.",
        ],
        "starters": [
            "Hello, my name is ...",
            "I am from ...",
            "In my free time, I enjoy ...",
            "My goal is to ...",
        ],
        "model": "Hello, my name is Mina. I am from Busan, South Korea, and I live with my two sisters. In my free time, I enjoy cooking and walking by the river. I am learning English because I want to speak with more confidence at work. I am happy to meet everyone in this group.",
        "checklist": ["Capital letter at the start", "Full stops at the end", "At least two details about you", "A clear goal"],
    },
    {
        "id": "daily-life",
        "title": "A Day in My Life",
        "level": "Foundation",
        "kind": "Personal",
        "target": 100,
        "scenario": "Describe an ordinary day from morning to evening. This is excellent practice for simple present and time expressions.",
        "instructions": [
            "Start with what you do in the morning.",
            "Use time words such as first, then, after that and finally.",
            "Include one thing you enjoy and one thing you find difficult.",
        ],
        "starters": [
            "My day usually begins at ...",
            "First, I ...",
            "After that, I ...",
            "In the evening, I ...",
        ],
        "model": "My day usually begins at seven o'clock. First, I make tea and eat a simple breakfast. Then I take the bus to work. I work in a small office and answer customers' questions. After that, I come home and cook dinner. In the evening, I study English for twenty minutes. I enjoy this quiet time, but I sometimes find new words difficult. Finally, I read a few pages of a book before I sleep.",
        "checklist": ["Time order is clear", "Verbs agree with the subject", "At least four daily activities", "A closing sentence"],
    },
    {
        "id": "favourite-place",
        "title": "Describe a Favourite Place",
        "level": "Beginner",
        "kind": "Descriptive",
        "target": 120,
        "scenario": "Describe a place that makes you feel calm or happy. Help the reader see, hear and feel it.",
        "instructions": [
            "Name the place and explain where it is.",
            "Describe what you can see, hear and smell.",
            "Explain why it matters to you.",
        ],
        "starters": [
            "My favourite place is ...",
            "It is located ...",
            "When I am there, I can see ...",
            "This place matters to me because ...",
        ],
        "model": "My favourite place is a small public garden behind the library in my town. It is quiet in the early morning. When I am there, I can see old trees, a narrow path and a fountain with three stone birds. I can hear water and the soft voices of people passing by. The air smells of wet grass after rain. I like to sit on the same wooden bench and write in my notebook. This place matters to me because it gives me a peaceful pause in a busy week.",
        "checklist": ["A clear location", "Details for at least three senses", "Adjectives that create a picture", "A personal reason"],
    },
    {
        "id": "thank-you",
        "title": "Write a Thank-You Message",
        "level": "Beginner",
        "kind": "Everyday",
        "target": 80,
        "scenario": "A neighbour helped you carry heavy shopping home. Write a short, warm message of thanks.",
        "instructions": [
            "Say clearly what you are thanking the person for.",
            "Mention how their help made a difference.",
            "Offer a friendly closing.",
        ],
        "starters": [
            "Dear ...",
            "Thank you so much for ...",
            "It made a real difference because ...",
            "I hope ...",
        ],
        "model": "Dear Mr. Owen,\n\nThank you so much for helping me carry my shopping home yesterday. The bags were much heavier than I expected, and your kindness made a difficult afternoon much easier. I really appreciate the time you took to help.\n\nI hope your tomato plants grow well this summer. Please knock on my door if you ever need a hand with anything.\n\nWarm wishes,\nDaniel",
        "checklist": ["Clear reason for thanks", "Warm but not exaggerated tone", "A greeting and closing", "Correct punctuation"],
    },
    {
        "id": "email-help",
        "title": "An Email to Ask for Help",
        "level": "Growing",
        "kind": "Practical",
        "target": 120,
        "scenario": "You are taking an evening course. Write a polite email asking your teacher for help with a task you do not understand.",
        "instructions": [
            "Write a clear subject line.",
            "Explain the situation briefly.",
            "Make one specific request and suggest a next step.",
        ],
        "starters": [
            "Subject: Question about ...",
            "Dear ...",
            "I am writing to ask ...",
            "Would it be possible to ...?",
        ],
        "model": "Subject: Question about the presentation task\n\nDear Ms. Alvarez,\n\nI hope you are well. I am writing to ask for some guidance with the presentation task for next week. I understand the main idea, but I am unsure how to divide the information between my three slides.\n\nWould it be possible to meet for ten minutes after class on Thursday? I have attached my draft so you can see what I have so far. If Thursday is not convenient, I am also free on Friday morning.\n\nThank you for your time.\n\nBest regards,\nPriya Shah",
        "checklist": ["Specific subject line", "Polite request", "A clear next step", "Professional closing"],
    },
    {
        "id": "changed-day",
        "title": "The Day Everything Changed",
        "level": "Growing",
        "kind": "Narrative",
        "target": 180,
        "scenario": "Write a short story about a day when something unexpected happened. It can be realistic or imaginative.",
        "instructions": [
            "Begin close to the important moment.",
            "Use past simple and past continuous to show action and background.",
            "Include one detail that reveals how the character felt.",
        ],
        "starters": [
            "The morning began like any other ...",
            "I was ... when I heard ...",
            "For a moment, I could not ...",
            "Looking back, I realise ...",
        ],
        "model": "The morning began like any other. I was locking my bicycle outside the bakery when I heard a small, urgent sound beneath the delivery van. At first, I thought it was a bird. Then I saw a grey cat pressed against the back tyre, too frightened to move.\n\nThe driver was still inside the shop. I knocked on the window and pointed. He stopped the engine at once. Together, we knelt beside the van. The cat stared at us with wide green eyes. I held out my hand and waited, not moving. After a long moment, it crept forward and pressed its head against my fingers.\n\nLooking back, I realise that the day did not change my whole life. It changed something smaller: I learned that patience can be a kind of rescue.",
        "checklist": ["Strong opening", "Past tenses used clearly", "Sensory detail", "An ending that reflects on the event"],
    },
    {
        "id": "language-opinion",
        "title": "Should Everyone Learn Another Language?",
        "level": "Confident",
        "kind": "Opinion",
        "target": 220,
        "scenario": "Write a balanced opinion piece for an adult education magazine. Take a clear position and support it.",
        "instructions": [
            "State your opinion in the introduction.",
            "Give two reasons with examples or evidence.",
            "Acknowledge a different view, then respond to it.",
            "End with a practical conclusion.",
        ],
        "starters": [
            "In my view, ...",
            "One reason is that ...",
            "Some people argue that ...",
            "However, ...",
            "A practical way forward is ...",
        ],
        "model": "In my view, learning another language is valuable for almost everyone, although the reasons differ from person to person. A second language is not simply a collection of words; it is a way of entering another person's world.\n\nOne reason is practical. Even basic language skills can improve access to work, travel and public services. A shop assistant who can greet a customer in their language creates trust in seconds. Another reason is cognitive: learning new sounds and structures keeps the mind flexible and encourages careful listening.\n\nSome people argue that translation technology will soon make language learning unnecessary. However, translation can tell us what was said; it rarely helps us build a relationship while saying it. Machines cannot replace the small courage of trying a new phrase and the goodwill it creates.\n\nA practical conclusion is that everyone need not become fluent. Short, consistent practice can be enough to make daily life friendlier and a little larger.",
        "checklist": ["Clear thesis", "Two developed reasons", "Counterargument addressed", "Formal linking words", "Balanced conclusion"],
    },
    {
        "id": "future-self",
        "title": "A Letter to Your Future Self",
        "level": "Confident",
        "kind": "Reflective",
        "target": 160,
        "scenario": "Write a letter to yourself one year from now. Reflect on what you hope to learn and who you hope to become.",
        "instructions": [
            "Use a friendly, honest tone.",
            "Mention one challenge you are facing now.",
            "Describe one small habit you want to keep.",
            "Ask your future self a question.",
        ],
        "starters": [
            "Dear future me,",
            "Right now, I am ...",
            "I hope you have ...",
            "Please remember ...",
            "What did you learn about ...?",
        ],
        "model": "Dear future me,\n\nRight now, I am learning English one page at a time. Sometimes I feel embarrassed when I speak slowly, but I am trying to remember that slow is still progress. I hope you have kept going, even on the weeks when work was busy and the words refused to stay in your memory.\n\nPlease remember how much courage it took to attend your first conversation class. Keep the habit of reading for ten minutes before bed, even if you are tired. Small practice is better than perfect plans.\n\nBy now, perhaps you have had your first real conversation with a colleague in English. What did you learn about yourself when you did not understand everything? I would like to know.\n\nWith hope,\nYou",
        "checklist": ["Reflective tone", "One current challenge", "One habit to continue", "A question for the future"],
    },
]

WRITING_TIPS = [
    {
        "title": "The anatomy of a strong sentence",
        "icon": "🧱",
        "body": "A clear sentence has a subject (who or what) and a verb (the action or state). Keep related words close together. If a sentence feels too long, split it.",
        "example": "Confusing: The letter that arrived yesterday from my cousin who lives in Spain is on the table.\nClearer: The letter from my cousin in Spain arrived yesterday. It is on the table.",
    },
    {
        "title": "A paragraph that readers can follow",
        "icon": "🧭",
        "body": "Start with a topic sentence. Add two or three supporting details. Finish with a closing or linking sentence. One main idea per paragraph is a reliable guide.",
        "example": "Topic sentence: Public libraries offer more than books.\nSupport: They provide internet access and quiet workspaces.\nClosing: For many people, they are a lifeline.",
    },
    {
        "title": "Punctuation that does its job",
        "icon": "✏️",
        "body": "Use a full stop for a complete statement, a question mark for a direct question, and a comma for short pauses or lists. An apostrophe shows possession (Maya's coat) or a contraction (don't).",
        "example": "I bought bread, milk and apples.\nMaya's coat is on the chair.\nDo you need a bag?",
    },
    {
        "title": "Linking words make writing flow",
        "icon": "🔗",
        "body": "Use linking words to show how ideas fit together. Do not use them only to decorate a sentence; each one should express a real relationship.",
        "example": "Adding: also, in addition\nContrasting: but, however, although\nCause: because, since\nResult: so, therefore\nSequence: first, then, finally",
    },
    {
        "title": "Three common mistakes to check",
        "icon": "🔎",
        "body": "Read your work once for each of these: subject-verb agreement (she works), plural forms (two books), and missing words (a, an, the). A short final read-through catches more than you expect.",
        "example": "Before: My sister work in a office.\nAfter: My sister works in an office.",
    },
    {
        "title": "Writing a clear email",
        "icon": "📧",
        "body": "Use a specific subject line. State your purpose in the first two sentences. Put details in short paragraphs. End with one clear next step and a polite closing.",
        "example": "Subject: Request to change Thursday's meeting\nDear Sam,\nI am writing to ask whether we could move our meeting to Friday morning...",
    },
]

# ---------------------------------------------------------------------------
# Practice zone
# ---------------------------------------------------------------------------

FLASHCARDS = [
    {"word": "curious", "category": "Learning", "meaning": "wanting to know or understand something", "example": "The child was curious about how the machine worked.", "pron": "KYOOR-ee-us"},
    {"word": "improve", "category": "Learning", "meaning": "to become better", "example": "A little practice every day will improve your writing.", "pron": "im-PROOV"},
    {"word": "confident", "category": "Learning", "meaning": "feeling sure about your ability", "example": "She felt confident after practising her speech.", "pron": "KON-fih-dent"},
    {"word": "patient", "category": "Learning", "meaning": "able to wait calmly", "example": "Be patient with yourself when you learn something new.", "pron": "PAY-shent"},
    {"word": "mistake", "category": "Learning", "meaning": "something done incorrectly", "example": "A mistake is a chance to learn.", "pron": "mih-STAYK"},
    {"word": "neighbour", "category": "Everyday", "meaning": "a person who lives near you", "example": "Our neighbour brought us some soup.", "pron": "NAY-ber"},
    {"word": "borrow", "category": "Everyday", "meaning": "to use something and return it later", "example": "May I borrow your pen?", "pron": "BOR-oh"},
    {"word": "appointment", "category": "Everyday", "meaning": "an arranged time to meet someone", "example": "I have a dentist appointment at four.", "pron": "uh-POINT-ment"},
    {"word": "receipt", "category": "Everyday", "meaning": "a paper showing you paid", "example": "Keep the receipt in case you need a refund.", "pron": "rih-SEET"},
    {"word": "queue", "category": "Everyday", "meaning": "a line of people waiting", "example": "There was a long queue at the bus stop.", "pron": "kyoo"},
    {"word": "colleague", "category": "Work", "meaning": "a person you work with", "example": "My colleague helped me prepare the report.", "pron": "KOL-eeg"},
    {"word": "deadline", "category": "Work", "meaning": "the latest time to finish something", "example": "The deadline is Friday at noon.", "pron": "DED-line"},
    {"word": "responsible", "category": "Work", "meaning": "having a duty to take care of something", "example": "She is responsible for the new project.", "pron": "rih-SPON-suh-bul"},
    {"word": "negotiate", "category": "Work", "meaning": "to discuss something to reach an agreement", "example": "We need to negotiate a new schedule.", "pron": "nih-GOH-shee-ayt"},
    {"word": "feedback", "category": "Work", "meaning": "comments about how well something was done", "example": "Thank you for your helpful feedback.", "pron": "FEED-bak"},
    {"word": "grateful", "category": "Feelings", "meaning": "feeling thankful", "example": "I am grateful for your support.", "pron": "GRAYT-ful"},
    {"word": "anxious", "category": "Feelings", "meaning": "worried or nervous", "example": "He felt anxious before the interview.", "pron": "ANG-shus"},
    {"word": "relieved", "category": "Feelings", "meaning": "happy that a worry has ended", "example": "I was relieved to hear the good news.", "pron": "rih-LEEVD"},
    {"word": "frustrated", "category": "Feelings", "meaning": "annoyed because something is difficult", "example": "She felt frustrated when the internet stopped working.", "pron": "FRUS-tray-ted"},
    {"word": "delighted", "category": "Feelings", "meaning": "very pleased", "example": "We are delighted to welcome you.", "pron": "dih-LY-ted"},
    {"word": "luggage", "category": "Travel", "meaning": "the bags you take when travelling", "example": "My luggage is in the overhead locker.", "pron": "LUG-ij"},
    {"word": "departure", "category": "Travel", "meaning": "the act of leaving, especially on a journey", "example": "Check the departure board for your gate.", "pron": "dih-PAR-cher"},
    {"word": "destination", "category": "Travel", "meaning": "the place you are travelling to", "example": "Paris is our final destination.", "pron": "des-tih-NAY-shun"},
    {"word": "souvenir", "category": "Travel", "meaning": "something you buy to remember a place", "example": "She bought a small souvenir from the museum.", "pron": "soo-vuh-NEER"},
    {"word": "journey", "category": "Travel", "meaning": "the act of travelling from one place to another", "example": "The journey takes about two hours.", "pron": "JUR-nee"},
    {"word": "available", "category": "Work", "meaning": "ready to be used or able to meet", "example": "Are you available on Monday afternoon?", "pron": "uh-VAY-luh-bul"},
]

QUIZ_QUESTIONS = [
    {"question": "Choose the correct article: I saw ___ elephant at the zoo.", "options": ["a", "an", "the", "no article"], "answer": 1, "explanation": "'Elephant' begins with a vowel sound, so use 'an'."},
    {"question": "She ___ breakfast at seven every morning.", "options": ["eat", "eats", "eating", "is eat"], "answer": 1, "explanation": "With she, add -s: she eats."},
    {"question": "Which word is a pronoun?", "options": ["table", "quickly", "they", "green"], "answer": 2, "explanation": "'They' replaces a noun and is a subject pronoun."},
    {"question": "I ___ my keys yesterday.", "options": ["lose", "lost", "losing", "have lose"], "answer": 1, "explanation": "'Lose' is irregular; the past simple is 'lost'."},
    {"question": "We ___ visit the museum next Saturday. We have already bought tickets.", "options": ["are going to", "will maybe", "go to", "visited"], "answer": 0, "explanation": "A planned future activity uses 'be going to'."},
    {"question": "What does 'under the weather' mean?", "options": ["Standing in the rain", "Feeling unwell", "Travelling by plane", "Feeling very happy"], "answer": 1, "explanation": "'Under the weather' is an idiom meaning unwell."},
    {"question": "Choose the correct question: ___ you like coffee?", "options": ["Are", "Do", "Does", "Is"], "answer": 1, "explanation": "Use 'Do' with 'you' and an action verb."},
    {"question": "This is my book. The book is ___.", "options": ["my", "me", "mine", "I"], "answer": 2, "explanation": "'Mine' is the possessive pronoun that stands alone."},
    {"question": "I have lived here ___ 2020.", "options": ["for", "since", "from", "at"], "answer": 1, "explanation": "'Since' is used with a starting point in time."},
    {"question": "If I ___ more time, I would learn the guitar.", "options": ["have", "had", "will have", "am having"], "answer": 1, "explanation": "The second conditional uses if + past simple, would + base verb."},
    {"question": "Which sentence is the most polite?", "options": ["Give me the form.", "Could you send me the form, please?", "Send the form now.", "Form. Now."], "answer": 1, "explanation": "'Could you ... please?' is a polite request."},
    {"question": "Choose the best linking word: I was tired, ___ I finished my homework.", "options": ["but", "because", "or", "so that"], "answer": 0, "explanation": "'But' shows contrast between feeling tired and finishing the work."},
    {"question": "What is the plural of 'child'?", "options": ["childs", "childes", "children", "childrens"], "answer": 2, "explanation": "'Child' has the irregular plural 'children'."},
    {"question": "Which word means 'very pleased'?", "options": ["anxious", "delighted", "frustrated", "patient"], "answer": 1, "explanation": "'Delighted' means very pleased."},
    {"question": "He speaks English ___.", "options": ["fluent", "fluently", "more fluent", "fluency"], "answer": 1, "explanation": "Use the adverb 'fluently' to describe how he speaks."},
    {"question": "Choose the complete sentence.", "options": ["After the long day.", "The tall tree by the gate.", "My brother cooks dinner.", "Because it was raining."], "answer": 2, "explanation": "'My brother cooks dinner' has a subject and a verb."},
]

SPELLING_WORDS = [
    {"word": "because", "definition": "for the reason that", "hint": "b _ _ _ _ _ e"},
    {"word": "beautiful", "definition": "very pleasing to look at", "hint": "b _ _ _ _ _ _ _ l"},
    {"word": "friend", "definition": "a person you like and know well", "hint": "f _ _ _ _ d"},
    {"word": "necessary", "definition": "needed; essential", "hint": "n _ _ _ _ _ _ _ y"},
    {"word": "tomorrow", "definition": "the day after today", "hint": "t _ _ _ _ _ _ w"},
    {"word": "restaurant", "definition": "a place where you pay to eat meals", "hint": "r _ _ _ _ _ _ _ _ t"},
    {"word": "different", "definition": "not the same", "hint": "d _ _ _ _ _ _ _ t"},
    {"word": "environment", "definition": "the natural world around us", "hint": "e _ _ _ _ _ _ _ _ _ t"},
    {"word": "knowledge", "definition": "information and understanding", "hint": "k _ _ _ _ _ _ _ e"},
    {"word": "schedule", "definition": "a plan of times and activities", "hint": "s _ _ _ _ _ _ e"},
    {"word": "language", "definition": "a system of words used for communication", "hint": "l _ _ _ _ _ _ e"},
    {"word": "definitely", "definition": "without doubt; certainly", "hint": "d _ _ _ _ _ _ _ _ y"},
]

DAILY_WORDS = [
    {"word": "steadily", "pron": "STED-ih-lee", "meaning": "in a regular, continuous way", "example": "Her English improved steadily through small daily practice."},
    {"word": "encourage", "pron": "in-KUR-ij", "meaning": "to give someone confidence to do something", "example": "A good teacher will encourage you to ask questions."},
    {"word": "clarity", "pron": "KLAIR-ih-tee", "meaning": "the quality of being clear and easy to understand", "example": "She rewrote the email for clarity."},
    {"word": "adapt", "pron": "uh-DAPT", "meaning": "to change in order to fit a new situation", "example": "Learners adapt their study habits as they grow."},
    {"word": "thoughtful", "pron": "THAWT-ful", "meaning": "considerate and careful about others", "example": "That was a thoughtful question."},
    {"word": "progress", "pron": "PROH-gres", "meaning": "movement toward a better or more complete state", "example": "Progress matters more than perfection."},
    {"word": "flexible", "pron": "FLEK-suh-bul", "meaning": "able to change or bend easily", "example": "A flexible learning plan is easier to keep."},
]
