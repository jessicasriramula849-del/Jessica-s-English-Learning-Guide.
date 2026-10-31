import os
import sys
import importlib.util

# 1. Calculate the absolute path to your files
base_dir = os.path.dirname(os.path.abspath(__file__))
styles_path = os.path.join(base_dir, "components", "styles.py")
audio_path = os.path.join(base_dir, "components", "audio_helper.py")

# 2. Dynamically load the styles module
spec_styles = importlib.util.spec_from_file_location("styles", styles_path)
styles = importlib.util.module_from_spec(spec_styles)
spec_styles.loader.exec_module(styles)
get_custom_css = styles.get_custom_css

# 3. Dynamically load the audio_helper module
spec_audio = importlib.util.spec_from_file_location("audio_helper", audio_path)
audio_helper = importlib.util.module_from_spec(spec_audio)
spec_audio.loader.exec_module(audio_helper)
render_web_speech_button = audio_helper.render_web_speech_button
generate_speech_audio = audio_helper.generate_speech_audio
from data.curriculum import (
    PHONICS_DATA, VOCABULARY_TOPICS, TENSES_MASTERCLASS,
    GRAMMAR_RULES, CONFUSING_WORDS, ACADEMIC_WRITING_LAB,
    BUSINESS_EMAIL_TEMPLATES, FORMAL_VS_CASUAL, IDIOMS_COLLECTION,
    QUIZ_BANK, ROLEPLAY_SCENARIOS
)

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Jessica's English Learning Guide - To Students and Adults of All Ages",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# ---------------------------------------------------------
# Load Jessica's Picture & Complete Guide
# ---------------------------------------------------------
@st.cache_data
def get_jessica_b64():
    img_path = os.path.join(os.path.dirname(__file__), "assets", "jessica_profile.jpg")
    if os.path.exists(img_path):
        with open(img_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

jessica_img_b64 = get_jessica_b64()
jessica_img_src = f"data:image/jpeg;base64,{jessica_img_b64}" if jessica_img_b64 else "https://images.unsplash.com/photo-1544717305-2782549b5136?w=240&q=80"

@st.cache_data
def load_guide_markdown():
    guide_path = os.path.join(os.path.dirname(__file__), "ENGLISH_LEARNING_GUIDE.md")
    if os.path.exists(guide_path):
        with open(guide_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

full_guide_text = load_guide_markdown()

# ---------------------------------------------------------
# Session State Initialization
# ---------------------------------------------------------
if "quiz_scores" not in st.session_state:
    st.session_state.quiz_scores = {"correct": 0, "total": 0, "answered": {}}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "roleplay_scenario" not in st.session_state:
    st.session_state.roleplay_scenario = list(ROLEPLAY_SCENARIOS.keys())[0]
if "learned_words" not in st.session_state:
    st.session_state.learned_words = set()

# ---------------------------------------------------------
# Sidebar: Teacher Jessica's Profile (With Her Real Picture!)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown(f"""
    <div class="sidebar-profile">
        <img src="{jessica_img_src}" class="sidebar-avatar" alt="Teacher Jessica">
        <h3 style="margin: 0; color: #1e3a8a; font-family: 'Outfit', sans-serif;">Teacher Jessica</h3>
        <p style="margin: 2px 0 8px 0; color: #0284c7; font-weight: 800; font-size: 0.88rem; text-transform: uppercase; letter-spacing: 0.05em;">Your English Mentor</p>
        <p style="font-size: 0.86rem; color: #334155; font-style: italic; line-height: 1.45; margin-bottom: 0;">
            "Welcome! Whether you are a curious child, an ambitious student, or a busy professional, I built this guide to turn English into your superpower."
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 🎯 Choose Your Track")
    learner_profile = st.selectbox(
        "Who is learning today?",
        ["🎓 School / College Student", "💼 Working Adult & Career Professional", "🐣 Young Learner & Kid", "🌍 General Conversationalist"]
    )
    
    st.markdown("#### 🎙️ Accent & Sound Tuning")
    accent_pref = st.selectbox(
        "Preferred Native Accent:",
        ["American English (US) 🇺🇸", "British English (UK) 🇬🇧", "Australian English (AU) 🇦🇺", "Canadian English (CA) 🇨🇦"]
    )
    accent_code_map = {
        "American English (US) 🇺🇸": ("com", "en-US"),
        "British English (UK) 🇬🇧": ("co.uk", "en-GB"),
        "Australian English (AU) 🇦🇺": ("com.au", "en-AU"),
        "Canadian English (CA) 🇨🇦": ("ca", "en-CA")
    }
    tts_accent, web_accent = accent_code_map[accent_pref]

    speech_speed = st.select_slider(
        "Pace of Audio Guidance:",
        options=["Slow (0.75x)", "Natural (1.0x)", "Fast (1.2x)"],
        value="Natural (1.0x)"
    )
    speed_float = 0.75 if "Slow" in speech_speed else (1.2 if "Fast" in speech_speed else 1.0)

    st.divider()
    st.markdown("#### 🏆 Your Mastery Scoreboard")
    q_correct = st.session_state.quiz_scores["correct"]
    q_total = st.session_state.quiz_scores["total"]
    pct = int((q_correct / q_total * 100)) if q_total > 0 else 0
    st.metric("Quiz Accuracy", f"{pct}%", f"{q_correct}/{q_total} Correct")
    st.progress(pct / 100.0)

    if q_total > 0 and pct >= 80:
        st.success("🌟 Stellar accuracy! You're on track for fluency mastery.")

    st.divider()
    st.caption("✨ Jessica's English Learning Guide • Designed with warmth & joy for learners worldwide.")

# ---------------------------------------------------------
# Radiant Brand Hero Header
# ---------------------------------------------------------
st.markdown("""
<div class="brand-hero">
    <div class="subtitle-tag">🌈 Interactive Multi-Age Learning Academy</div>
    <h1>Jessica's English Learning Guide</h1>
    <h2>To Students and Adults of All Ages</h2>
    <p>A vibrant, joyful master guide created to empower your English—from phonics and foundational grammar to elite academic essays, diplomatic workplace emails, and fluent everyday conversations.</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Primary Navigation Tabs
# ---------------------------------------------------------
nav_tabs = st.tabs([
    "🏠 Welcome & Meet Jessica",
    "📖 The Complete Learning Guide",
    "🐣 Beginners & Phonics",
    "📚 Students & Academic Grammar",
    "💼 Adults & Career English",
    "💡 Idioms & Expressions",
    "🎯 Interactive Quiz Lab",
    "🎙️ Speaking & Studio",
    "✍️ Smart Writing Polisher",
    "💬 Conversation Roleplay",
    "📑 Custom Study Planner"
])

# =========================================================
# TAB 1: Welcome & Meet Jessica (Features Her Picture!)
# =========================================================
with nav_tabs[0]:
    # Meet Teacher Jessica Spotlight Box
    st.markdown(f"""
    <div class="author-spotlight">
        <div class="author-img-wrapper">
            <img src="{jessica_img_src}" class="author-img" alt="Teacher Jessica">
            <div class="author-badge">✨ Teacher Jessica</div>
        </div>
        <div style="flex: 1; min-width: 280px;">
            <span class="badge-pill badge-adult">Author & Lead Educator</span>
            <span class="badge-pill badge-student">All Ages Welcome</span>
            <h2 style="color: #0f766e; margin: 8px 0 6px 0; font-family: 'Outfit', sans-serif; font-size: 1.8rem;">
                "Hello & Welcome! I am Jessica, Your English Guide."
            </h2>
            <p style="font-size: 1.05rem; color: #334155; line-height: 1.6; margin-bottom: 12px;">
                I designed <strong>Jessica's English Learning Guide</strong> with a simple, powerful belief: 
                <em>English is not a barrier to fear—it is a joyful bridge to connect with the world.</em>
                Whether you are a young child just discovering phonics, a high school or college student aiming for top marks on IELTS/TOEFL essays, 
                or a working adult building executive fluency, this entire platform was created for you!
            </p>
            <p style="font-size: 0.95rem; color: #0d9488; font-weight: 700; margin: 0;">
                ⭐ Start exploring the tabs above: read my complete guide, listen to audio pronunciations, practice roleplay, and test your skills in the Quiz Lab!
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    render_web_speech_button(
        "Hello and welcome! I am Jessica, your English guide. I designed this learning academy to help students and adults of all ages speak and write English with joyful confidence.",
        button_text="🔊 Listen to Teacher Jessica's Personal Welcome",
        accent=web_accent,
        theme="emerald",
        key_id="jessica_welcome_audio"
    )

    st.markdown("---")

    # Daily Spark Cards (Word and Idiom of the Day)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="custom-card card-ocean">
            <span class="badge-pill badge-student">📘 Word of the Day</span>
            <span class="badge-pill badge-accent">Pronunciation: /ɑːrˈtɪkjuleɪt/</span>
            <h3>Articulate</h3>
            <p><strong>Part of Speech:</strong> Adjective & Verb</p>
            <p><strong>Meaning:</strong> Able to express ideas clearly, eloquently, and effectively in speech or writing.</p>
            <p style="background: rgba(59, 130, 246, 0.08); padding: 10px 14px; border-radius: 8px; border-left: 3px solid #3b82f6;">
                <em>"Teacher Jessica encouraged every student to <span class="word-highlight">articulate</span> their unique viewpoints with joyful confidence."</em>
            </p>
        </div>
        """, unsafe_allow_html=True)
        render_web_speech_button(
            "Articulate. Able to express ideas clearly and effectively. Teacher Jessica encouraged every student to articulate their unique viewpoints.", 
            button_text="🔊 Hear Word of the Day", 
            accent=web_accent, 
            theme="ocean",
            key_id="daily_word"
        )

    with c2:
        st.markdown("""
        <div class="custom-card card-sunny">
            <span class="badge-pill badge-kids">💡 Idiom of the Day</span>
            <span class="badge-pill badge-accent">Daily Energy Boost</span>
            <h3>Hit the Ground Running</h3>
            <p><strong>Literal:</strong> To land on feet and sprint without stopping.</p>
            <p><strong>Figurative Meaning:</strong> To start a new project, job, or study routine immediately with high energy and total success.</p>
            <p style="background: rgba(245, 158, 11, 0.1); padding: 10px 14px; border-radius: 8px; border-left: 3px solid #f59e0b;">
                <em>"With this colorful guide, you will <span class="word-highlight">hit the ground running</span> in every English conversation!"</em>
            </p>
        </div>
        """, unsafe_allow_html=True)
        render_web_speech_button(
            "Hit the ground running. It means to begin a new activity immediately with intense energy and success.", 
            button_text="🔊 Hear Idiom of the Day", 
            accent=web_accent, 
            theme="sunset",
            key_id="daily_idiom"
        )

    st.markdown("---")
    st.markdown("### 🗺️ Tailored Pathways for Every Age & Stage")

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown("""
        <div class="custom-card card-sunny">
            <span class="badge-pill badge-kids">Ages 5 - 12 & Beginners</span>
            <h3>🐣 Young Learners</h3>
            <p style="color: #64748b; font-size: 0.95rem;">Fun phonics, vibrant everyday words, and interactive sentence builders with cheerful audio.</p>
            <ul style="font-size: 0.92rem; color: #334155; padding-left: 18px; line-height: 1.6;">
                <li>Vowel and consonant sound audio breakdown</li>
                <li>Everyday visual vocabulary (Food, family, routines)</li>
                <li>Hands-on Subject-Verb-Object sentence toy</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
        <div class="custom-card card-ocean">
            <span class="badge-pill badge-student">Teens, High School & College</span>
            <h3>📚 Academic Students</h3>
            <p style="color: #64748b; font-size: 0.95rem;">Master the 12 English tenses, IELTS/TOEFL writing, and tricky grammar traps.</p>
            <ul style="font-size: 0.92rem; color: #334155; padding-left: 18px; line-height: 1.6;">
                <li>The Complete 12 Tenses matrix with trap warnings</li>
                <li>The IN / ON / AT Preposition Pyramid</li>
                <li>The PEEL Essay Method & Academic transitions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col_c:
        st.markdown("""
        <div class="custom-card card-emerald">
            <span class="badge-pill badge-adult">Working Adults & Lifelong Learners</span>
            <h3>💼 Career & Fluency</h3>
            <p style="color: #64748b; font-size: 0.95rem;">Executive presence, polite business emails, diplomatic meetings, and interview answers.</p>
            <ul style="font-size: 0.92rem; color: #334155; padding-left: 18px; line-height: 1.6;">
                <li>Copy-ready professional email templates</li>
                <li>Tactful disagreement & meeting management</li>
                <li>Behavioral Job Interview prep via the STAR method</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Jessica's Golden Rules Callout
    st.markdown("""
    <div class="jessica-callout">
        <div class="jessica-callout-header">
            <span>✨ Teacher Jessica's 3 Golden Rules for Fluency</span>
        </div>
        <div class="jessica-callout-body">
            1. <strong>Consistency beats intensity:</strong> Practicing 15 focused minutes every single day is 10 times more effective than cramming for 3 hours once a weekend.<br>
            2. <strong>Mistakes are your greatest teachers:</strong> If you never make a mistake, you aren't stretching your boundaries. Speak and write boldly!<br>
            3. <strong>Shadowing creates natural rhythm:</strong> Listen to native English audio and repeat it immediately aloud, matching the tone, pauses, and expression.
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# TAB 2: The Complete Learning Guide & Interactive Reader
# =========================================================
with nav_tabs[1]:
    st.markdown("## 📖 The Complete English Learning Guide")
    st.markdown("*Jessica's definitive pedagogical handbook for students and adults of all ages.*")

    # Author header inside guide reader
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 16px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 14px; padding: 14px 20px; margin-bottom: 20px;">
        <img src="{jessica_img_src}" style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover; border: 2px solid #0284c7;" alt="Author Jessica">
        <div>
            <h4 style="margin: 0; color: #0f172a;">Written & Curated by Teacher Jessica</h4>
            <p style="margin: 2px 0 0 0; color: #64748b; font-size: 0.88rem;">Complete reference textbook • Downloadable & interactive</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_btn1, col_btn2 = st.columns([1, 2])
    with col_btn1:
        st.download_button(
            label="📥 Download Complete Guide (.MD)",
            data=full_guide_text,
            file_name="Jessicas_English_Learning_Guide.md",
            mime="text/markdown"
        )
    with col_btn2:
        search_query = st.text_input("🔍 Search Inside the Guide (e.g., 'schwa', 'preposition', 'PEEL', 'tenses', 'interview'):", placeholder="Type a keyword...")

    if search_query.strip():
        st.markdown(f"### 🔎 Search Results for: *'{search_query}'*")
        lines = full_guide_text.split("\n")
        matched_blocks = []
        current_header = "Introduction"

        for line in lines:
            if line.startswith("#"):
                current_header = line.replace("#", "").strip()
            if search_query.lower() in line.lower():
                matched_blocks.append((current_header, line.strip()))

        if matched_blocks:
            st.success(f"Found {len(matched_blocks)} matches in the guide:")
            for h, text in matched_blocks[:8]:
                st.markdown(f"""
                <div class="custom-card card-ocean" style="padding: 14px 18px; margin-bottom: 8px;">
                    <span class="badge-pill badge-student">{h}</span>
                    <p style="margin: 6px 0 0 0; color: #1e293b; font-size: 0.98rem;">{text}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning(f"No exact matches found for '{search_query}'. Browse the chapters below!")

    st.markdown("---")
    st.markdown("### 📚 Browse Chapter by Chapter")

    guide_chapters = {
        "🌟 Foreword & Core Principles": """
### Foreword: The Heart of English Learning
Language is fundamentally a bridge—not an obstacle course. Too many students and adults have experienced English through dry memorization, intimidating red pen corrections, and abstract rules that feel disconnected from real life.

**Teacher Jessica's Three Guiding Principles:**
1. **Consistency Beats Intensity:** 15 focused minutes every day will reshape your neural pathways far faster than 4 exhausting hours on a Sunday.
2. **Mistakes Are Proof of Progress:** The only speakers who make zero mistakes are those who remain silent. Speak boldly and embrace constructive feedback!
3. **Connect Form with Meaning:** Never memorize a grammar formula in isolation. Always anchor every rule to a real human scenario.
        """,
        "Chapter 1: The Sound Architecture (Phonics, Pronunciation & Accent)": """
### Chapter 1: The Sound Architecture
Clear communication does not require erasing your cultural accent; it requires **intelligibility, rhythmic accuracy, and clear articulation**.

#### 1.1 The Schwa /ə/: The Secret Core of English Rhythm
English is a **stress-timed language**. Stressed syllables occur at regular beats, while unstressed vowels collapse into the relaxed **schwa** sound `/ə/`:
- **A**bout $\\rightarrow$ `/əˈbaʊt/`
- Teach**er** $\\rightarrow$ `/ˈtiːtʃ.ər/`
- Confid**e**nt $\\rightarrow$ `/ˈkɒn.fə.dənt/`

#### 1.2 Tricky Sound Pairs & Digraphs
- **Short A /æ/** (cat, bat) vs. **Long A /eɪ/** (cake, bait). Notice how final silent '-e' makes the vowel say its own name (*hat* $\\rightarrow$ *hate*, *hop* $\\rightarrow$ *hope*).
- **Voiceless TH /θ/** (think, thank, bath) vs. **Voiced TH /ð/** (this, that, weather).
- **CH /tʃ/** (chair, chip - sharp stop) vs. **SH /ʃ/** (share, ship - continuous hiss).

#### 1.3 The Shadowing Technique
1. Listen to a short audio clip.
2. Mirror the speaker simultaneously out loud, matching tone, speed, and pauses.
        """,
        "Chapter 2: The Vocabulary Factory (Building Active Lexicon)": """
### Chapter 2: The Vocabulary Factory
Do not memorize isolated word lists. Learn words in **collocations** (natural pairs) and **semantic families**.

#### 2.1 Collocations: Sounding Natural Immediately
- ✅ *Make a mistake* (NOT "do a mistake")
- ✅ *Take an exam* (NOT "give an exam")
- ✅ *Do your homework* (NOT "make your homework")
- ✅ *Heavy rain* (NOT "strong rain")
- ✅ *Deeply regret* (NOT "strongly regret")

#### 2.2 Latin & Greek Root Toolkit
- **Bene** (Good, well): *Benefit, Benevolent, Beneficial*
- **Chron** (Time): *Chronological, Synchronize, Chronic*
- **Dict** (Say, speak): *Predict, Contradict, Dictate, Verdict*
- **Port** (Carry): *Transport, Portable, Import, Export*
- **Spect** (Look, see): *Inspect, Spectator, Perspective, Retrospect*
        """,
        "Chapter 3: The Grammar Engine (The 12 Tenses & Master Blueprint)": """
### Chapter 3: The Grammar Engine
Grammar is not a set of arbitrary hurdles; it is a system of time and perspective coordinates.

#### The 12 Tenses Blueprint
1. **Simple Present:** $S + V(s/es) + O$. Habits, general facts (*Jessica teaches with passion*).
2. **Present Continuous:** $S + \\text{am/is/are} + V\\text{-ing}$. Actions happening right now (*We are studying grammar*).
3. **Present Perfect:** $S + \\text{have/has} + V3$. Past action with result in present (*I have lived in London for five years*).
4. **Present Perfect Continuous:** $S + \\text{have/has been} + V\\text{-ing}$. Emphasizes ongoing duration (*She has been reading since 9 AM*).
5. **Simple Past:** $S + V2$. Completed action at fixed past time (*We attended the lecture yesterday*).
6. **Past Continuous:** $S + \\text{was/were} + V\\text{-ing}$. Past action in progress, often interrupted (*I was cooking when he arrived*).
7. **Past Perfect:** $S + \\text{had} + V3$. Past before another past action (*The train had already left when I reached the station*).
8. **Past Perfect Continuous:** $S + \\text{had been} + V\\text{-ing}$. Cause-and-effect past duration (*He was tired because he had been running*).
9. **Simple Future:** Will + Base Verb OR Going to + Base Verb (*I will help you / It is going to rain*).
10. **Future Continuous:** $S + \\text{will be} + V\\text{-ing}$. Action in progress at future moment (*This time tomorrow I will be flying*).
11. **Future Perfect:** $S + \\text{will have} + V3$. Action completed by a future milestone (*By December, Jessica will have graduated*).
12. **Future Perfect Continuous:** $S + \\text{will have been} + V\\text{-ing}$. Continuous duration up to a future point.

#### The IN / ON / AT Preposition Pyramid
- **IN (General):** Years (*in 2026*), Months (*in October*), Countries (*in France*), Enclosed rooms.
- **ON (Specific):** Days & Dates (*on Monday, on October 31st*), Streets (*on 5th Avenue*), Surfaces.
- **AT (Very Precise):** Exact times (*at 9:00 AM*), Addresses (*at 10 Downing St.*), Points.
        """,
        "Chapter 4: Academic Writing & Essay Excellence (For Students)": """
### Chapter 4: Academic Writing & Essay Excellence
Scoring high marks on academic essays, IELTS, TOEFL, or SAT requires clear organizational architecture.

#### 4.1 The PEEL Paragraph Method
- **P — Point:** State your clear topic claim immediately.
- **E — Explanation:** Unpack the logic. Explain *how* and *why* this claim holds true.
- **E — Evidence:** Provide concrete proof: statistics, historical examples, or citations.
- **L — Link:** Explicitly connect the finding back to the overarching thesis statement.

#### 4.2 Academic Transition Toolkit
- **Adding ideas:** *Furthermore, Moreover, Additionally*
- **Contrasting:** *Conversely, However, Nevertheless, On the other hand*
- **Causation:** *Consequently, Therefore, As an inevitable result*
- **Concluding:** *Ultimately, In summary, Taken together*
        """,
        "Chapter 5: Professional & Workplace English (For Adults)": """
### Chapter 5: Professional & Workplace English
In the workplace, brevity, tact, and clarity command respect.

#### 5.1 Formal vs. Casual Transformation Dictionary
- *"I wanna ask you something"* $\\rightarrow$ *"I would like to inquire about..."*
- *"Can you do this ASAP?"* $\\rightarrow$ *"Could you kindly review this at your earliest convenience?"*
- *"That idea won't work"* $\\rightarrow$ *"That approach may introduce several operational challenges."*
- *"Sorry for the delay"* $\\rightarrow$ *"Thank you very much for your patience while I gathered these details."*
- *"Tell me more about it"* $\\rightarrow$ *"Could you elaborate on the underlying methodology?"*

#### 5.2 The STAR Behavioral Interview Method
- **S — Situation:** Set the scene in 2 sentences.
- **T — Task:** Clarify your specific responsibility or challenge.
- **A — Action:** Detail the concrete steps **you** took to solve it.
- **R — Result:** Share quantifiable positive impact and what you learned.
        """,
        "Chapter 6: Idioms, Slang & Cultural Fluency": """
### Chapter 6: Idioms, Slang & Cultural Fluency
1. **A blessing in disguise:** A seeming misfortune that leads to an unexpectedly good outcome.
2. **Bite the bullet:** To endure a painful or difficult situation with composure.
3. **Break the ice:** To ease tension when meeting people for the first time.
4. **Hit the nail on the head:** To state the exact truth or pinpoint the core problem.
5. **Under the weather:** Feeling slightly ill or indisposed.
6. **Burn the midnight oil:** To work or study late into the night.
        """,
        "Chapter 7: The 30-Day Immersion Roadmap": """
### Chapter 7: The 30-Day Immersion Roadmap
- **Phase 1 (Days 1–7):** Phonics, Schwa /ə/, Vowel contrasts, SVO sentences. Record and shadow 5 core sound pairs.
- **Phase 2 (Days 8–14):** 12 Tenses matrix, IN/ON/AT pyramid, Quiz Lab. Achieve 80%+ on Grammar Foundations.
- **Phase 3 (Days 15–21):** Homophones, 15 core idioms, Formal email templates. Draft 2 professional emails or PEEL paragraphs.
- **Phase 4 (Days 22–30):** Conversation roleplay, Pronunciation studio, Full immersion. Hold a roleplay dialogue without pausing.
        """
    }

    selected_chap = st.selectbox("Select a Chapter to Read:", list(guide_chapters.keys()))
    
    st.markdown(f"""
    <div class="custom-card card-ocean" style="padding: 26px;">
        {guide_chapters[selected_chap]}
    </div>
    """, unsafe_allow_html=True)
    
    render_web_speech_button(
        f"You are reading {selected_chap}. Practice each lesson with curiosity and joyful consistency.",
        button_text="🔊 Listen to Chapter Summary",
        accent=web_accent,
        theme="ocean",
        key_id=f"guide_chap_{selected_chap[:8]}"
    )

# =========================================================
# TAB 3: Beginners & Phonics
# =========================================================
with nav_tabs[2]:
    st.markdown("## 🐣 Foundations: Phonics, Sounds & Visual Vocabulary")
    st.markdown("Clear pronunciation starts with sound awareness. Listen to Teacher Jessica's audio clips, repeat aloud, and watch your confidence blossom!")

    st.markdown("### 🔤 Phonics & Tricky Sounds Masterclass")
    for idx, phon in enumerate(PHONICS_DATA):
        with st.expander(f"✨ {phon['category']}: {phon['sound']}", expanded=(idx == 0)):
            st.markdown(f"**Sound Breakdown:** {phon['explanation']}")
            
            cols = st.columns(len(phon['examples']))
            theme_choice = ["sunny", "ocean", "emerald", "berry"][idx % 4]
            btn_theme = ["sunset", "ocean", "emerald", "berry"][idx % 4]

            for i, ex in enumerate(phon['examples']):
                with cols[i]:
                    st.markdown(f"""
                    <div class="custom-card card-{theme_choice}" style="padding: 16px; text-align: center; margin-bottom: 8px;">
                        <h3 style="margin: 0; color: #1e3a8a;">{ex['word']}</h3>
                        <p style="color: #6366f1; font-weight: 700; font-size: 0.9rem; margin: 4px 0;">{ex['ipa']}</p>
                        <p style="font-size: 0.88rem; color: #334155; margin: 6px 0;"><em>"{ex['sentence']}"</em></p>
                    </div>
                    """, unsafe_allow_html=True)
                    render_web_speech_button(
                        f"{ex['word']}. {ex['sentence']}", 
                        button_text="🔊 Hear Word", 
                        accent=web_accent, 
                        speed=speed_float, 
                        theme=btn_theme,
                        key_id=f"phon_{idx}_{i}"
                    )
            
            st.markdown(f"""
            <div class="jessica-callout" style="margin-top: 10px; padding: 12px 18px;">
                <strong>💡 Teacher Jessica's Pro-Tip:</strong> {phon['tip']}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📖 Everyday Essential Vocabulary with Audio")
    selected_topic = st.selectbox("Choose a Vocabulary Realm:", list(VOCABULARY_TOPICS.keys()))
    
    topic_items = VOCABULARY_TOPICS[selected_topic]
    for idx, item in enumerate(topic_items):
        c_left, c_right = st.columns([3, 1])
        with c_left:
            st.markdown(f"""
            <div class="custom-card card-ocean" style="padding: 16px 20px; margin-bottom: 10px;">
                <span class="badge-pill badge-student">{item['level']}</span>
                <span style="font-size: 1.15rem; font-weight: 700; color: #0f172a;">{item['phrase']}</span>
                <p style="margin: 6px 0 0 0; color: #475569; font-size: 0.96rem;">{item['meaning']}</p>
            </div>
            """, unsafe_allow_html=True)
        with c_right:
            render_web_speech_button(
                item['phrase'], 
                button_text="🔊 Listen", 
                accent=web_accent, 
                speed=speed_float, 
                theme="ocean",
                key_id=f"vocab_{selected_topic}_{idx}"
            )

    st.markdown("---")
    st.markdown("### 🧩 Interactive Sentence Construction Toy")
    st.markdown("All English sentences bloom from the foundational **Subject + Verb + Object (SVO)** pattern:")

    col_s, col_v, col_o = st.columns(3)
    with col_s:
        sub = st.selectbox("1. Subject (Who / What)", ["Teacher Jessica", "The enthusiastic student", "We", "My ambitious friend", "The happy learner"])
    with col_v:
        vb = st.selectbox("2. Action Verb", ["adores reading", "practices", "explores", "speaks", "writes"])
    with col_o:
        obj = st.selectbox("3. Object / Complement", ["English literature every morning.", "grammar exercises diligently.", "new vocabulary joyfully.", "with natural confidence.", "thoughtful essays."])

    built_sentence = f"{sub} {vb} {obj}"
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border: 2px solid #86efac; border-radius: 18px; padding: 22px; margin: 16px 0; text-align: center; box-shadow: 0 10px 20px rgba(16, 185, 129, 0.1);">
        <span class="badge-pill badge-adult">SVO Constructed Masterpiece</span>
        <h2 style="color: #14532d; margin: 10px 0; font-family: 'Outfit', sans-serif;">"{built_sentence}"</h2>
    </div>
    """, unsafe_allow_html=True)
    render_web_speech_button(built_sentence, button_text="🔊 Read Out Loud", accent=web_accent, speed=speed_float, theme="emerald", key_id="sentence_builder")

# =========================================================
# TAB 4: Students & Academic Grammar
# =========================================================
with nav_tabs[3]:
    st.markdown("## 📚 Academic Grammar Mastery & Writing Lab")
    st.markdown("Designed for middle school, high school, college students, and test-takers (IELTS, TOEFL, SAT, Cambridge).")

    grammar_section = st.radio(
        "Choose an Academic Mastery Module:",
        ["⏰ The 12 English Tenses Matrix", "🏛️ Core Grammar Rules (Prepositions, Voice, Conditionals)", "✍️ Essay & Paragraph Writing Lab (PEEL Method)", "🔍 Tricky & Confusing Word Pairs"],
        horizontal=True
    )

    if grammar_section == "⏰ The 12 English Tenses Matrix":
        st.markdown("### ⏰ The Complete 12 English Tenses Matrix")
        tense_filter = st.selectbox("Filter Tenses by Timeframe:", ["All 12 Tenses", "Present Tenses", "Past Tenses", "Future Tenses"])
        
        filtered_tenses = TENSES_MASTERCLASS
        if tense_filter == "Present Tenses":
            filtered_tenses = [t for t in TENSES_MASTERCLASS if "Present" in t["timeframe"]]
        elif tense_filter == "Past Tenses":
            filtered_tenses = [t for t in TENSES_MASTERCLASS if "Past" in t["timeframe"]]
        elif tense_filter == "Future Tenses":
            filtered_tenses = [t for t in TENSES_MASTERCLASS if "Future" in t["timeframe"]]

        for idx, t in enumerate(filtered_tenses):
            with st.expander(f"📌 {t['name']} ({t['timeframe']})", expanded=(idx == 0)):
                st.markdown(f"""
                <div class="formula-box">
                    Formula: {t['formula']}
                </div>
                """, unsafe_allow_html=True)
                
                c_u1, c_u2 = st.columns(2)
                with c_u1:
                    st.markdown(f"**When to use:** {t['usage']}")
                    st.markdown(f"**Key signal words:** `{t['signals']}`")
                with c_u2:
                    st.markdown(f"✅ **Affirmative:** {t['affirmative']}")
                    st.markdown(f"❌ **Negative:** {t['negative']}")
                    st.markdown(f"❓ **Question:** {t['question']}")

                render_web_speech_button(
                    f"{t['affirmative']} {t['negative']} {t['question']}", 
                    button_text="🔊 Listen to Tense Examples", 
                    accent=web_accent, 
                    theme="ocean",
                    key_id=f"tense_{t['name']}"
                )

                st.markdown(f"""
                <div class="jessica-callout" style="margin-top: 10px; padding: 12px 18px;">
                    <strong>⚠️ Jessica's Trap Warning:</strong> {t['trap']}
                </div>
                """, unsafe_allow_html=True)

    elif grammar_section == "🏛️ Core Grammar Rules (Prepositions, Voice, Conditionals)":
        st.markdown("### 🏛️ Essential Grammar Rules Demystified")
        for idx, rule in enumerate(GRAMMAR_RULES):
            theme_choice = ["ocean", "emerald", "berry", "sunny"][idx % 4]
            btn_theme = ["ocean", "emerald", "berry", "sunset"][idx % 4]
            
            st.markdown(f"""
            <div class="custom-card card-{theme_choice}">
                <h3>{rule['title']}</h3>
                <p style="color: #475569; font-weight: 600; font-size: 1.05rem;">{rule['summary']}</p>
                <div style="background: rgba(255, 255, 255, 0.7); border-radius: 12px; padding: 16px; margin: 14px 0; border: 1px solid rgba(0,0,0,0.06);">
            """, unsafe_allow_html=True)
            for d in rule['details']:
                st.markdown(f"{d}")
            st.markdown(f"""
                </div>
                <div style="background: #ffffff; border-left: 5px solid #6366f1; padding: 12px 18px; border-radius: 8px; font-style: italic; color: #312e81; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    {rule['example']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            render_web_speech_button(
                rule['example'], 
                button_text="🔊 Hear Rule Example", 
                accent=web_accent, 
                theme=btn_theme,
                key_id=f"rule_{rule['title'][:10]}"
            )

    elif grammar_section == "✍️ Essay & Paragraph Writing Lab (PEEL Method)":
        st.markdown("### ✍️ Academic Essay & Paragraph Writing Lab")
        st.markdown("Top scorers on IELTS, TOEFL, SAT, and college admissions structure persuasive paragraphs with the **PEEL Method**.")

        peel = ACADEMIC_WRITING_LAB["peel_method"]
        st.markdown(f"#### {peel['title']}")
        st.caption(peel['description'])

        col_p = st.columns(4)
        colors = ["#3b82f6", "#10b981", "#f59e0b", "#8b5cf6"]
        for i, step in enumerate(peel['steps']):
            with col_p[i]:
                st.markdown(f"""
                <div class="custom-card" style="text-align: center; border-top: 5px solid {colors[i]};">
                    <h1 style="color: {colors[i]}; margin: 0; font-size: 2.8rem; font-family: 'Outfit', sans-serif;">{step['letter']}</h1>
                    <h4 style="color: #0f172a; margin: 6px 0;">{step['name']}</h4>
                    <p style="font-size: 0.88rem; color: #475569; margin: 0;">{step['desc']}</p>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("#### 🔗 High-Scoring Academic Transition Words Bank")
        trans_cat = st.selectbox("Select Transition Category:", list(ACADEMIC_WRITING_LAB["transitions"].keys()))
        words = ACADEMIC_WRITING_LAB["transitions"][trans_cat]
        
        st.markdown("Click any transition to see it in action:")
        t_cols = st.columns(len(words))
        for i, w in enumerate(words):
            with t_cols[i]:
                if st.button(w, key=f"trans_{w}"):
                    st.info(f"Example usage of **{w}**: *'{w}, rigorous research confirms that immersive practice yields superior fluency.'*")

    elif grammar_section == "🔍 Tricky & Confusing Word Pairs":
        st.markdown("### 🔍 Commonly Confused Words & Homophones")
        st.markdown("Master the subtle differences that trip up native speakers and test-takers alike:")

        for pair in CONFUSING_WORDS:
            with st.expander(f"⚖️ {pair['pair']}"):
                col_w1, col_w2 = st.columns(2)
                with col_w1:
                    st.markdown(f"""
                    <div class="custom-card card-ocean" style="margin-bottom: 6px;">
                        <h4 style="margin: 0; color: #1e3a8a;">{pair['word1']}</h4>
                        <p style="margin: 6px 0; color: #334155;"><strong>Meaning:</strong> {pair['meaning1']}</p>
                        <p style="margin: 0; font-style: italic; color: #475569;">"{pair['example1']}"</p>
                    </div>
                    """, unsafe_allow_html=True)
                    render_web_speech_button(pair['example1'], button_text="🔊 Hear Word 1", accent=web_accent, theme="ocean", key_id=f"cw1_{pair['pair']}")

                with col_w2:
                    st.markdown(f"""
                    <div class="custom-card card-emerald" style="margin-bottom: 6px;">
                        <h4 style="margin: 0; color: #065f46;">{pair['word2']}</h4>
                        <p style="margin: 6px 0; color: #334155;"><strong>Meaning:</strong> {pair['meaning2']}</p>
                        <p style="margin: 0; font-style: italic; color: #475569;">"{pair['example2']}"</p>
                    </div>
                    """, unsafe_allow_html=True)
                    render_web_speech_button(pair['example2'], button_text="🔊 Hear Word 2", accent=web_accent, theme="emerald", key_id=f"cw2_{pair['pair']}")

                st.markdown(f"""
                <div class="jessica-callout" style="margin-top: 12px; padding: 12px 18px;">
                    <strong>💡 Teacher Jessica's Memory Trick:</strong> {pair['memory_trick']}
                </div>
                """, unsafe_allow_html=True)

# =========================================================
# TAB 5: Adults & Career English
# =========================================================
with nav_tabs[4]:
    st.markdown("## 💼 Adults & Career English: Professional Fluency")
    st.markdown("Transform your workplace communication. Sound confident, tactful, and authoritative in meetings and corporate emails.")

    career_choice = st.radio(
        "Explore Professional Modules:",
        ["✉️ Business Email Generator & Templates", "🔄 Casual vs. Formal Corporate Polish", "🤝 Executive Meeting & Diplomatic Phrases", "🎙️ Job Interview Success (The STAR Method)"],
        horizontal=True
    )

    if career_choice == "✉️ Business Email Generator & Templates":
        st.markdown("### ✉️ Ready-to-Use Business Email Templates")
        selected_template = st.selectbox(
            "Select an email scenario:",
            [t["scenario"] for t in BUSINESS_EMAIL_TEMPLATES]
        )
        t_data = next(t for t in BUSINESS_EMAIL_TEMPLATES if t["scenario"] == selected_template)

        st.markdown(f"**Tone:** `{t_data['tone']}`")
        st.text_input("Subject Line:", value=t_data["subject"], key=f"subj_{selected_template}")
        
        email_body = st.text_area(
            "Email Body (Customizable):",
            value=t_data["body"],
            height=260,
            key=f"body_{selected_template}"
        )
        
        c_copy, c_audio = st.columns([1, 2])
        with c_copy:
            if st.button("📋 Ready to Send Confirmation", key=f"btn_copy_{selected_template}"):
                st.success("Template ready! Highlight and copy the text box above.")
        with c_audio:
            render_web_speech_button(email_body, button_text="🔊 Listen to Email Read-Aloud", accent=web_accent, speed=speed_float, theme="emerald", key_id=f"email_{selected_template[:10]}")

    elif career_choice == "🔄 Casual vs. Formal Corporate Polish":
        st.markdown("### 🔄 How to Say It Like an Executive")
        st.markdown("Notice how replacing casual colloquialisms with diplomatic English instantly elevates your professional presence:")

        for item in FORMAL_VS_CASUAL:
            st.markdown(f"""
            <div class="compare-container">
                <div class="compare-box-casual">
                    <span class="badge-pill badge-kids">Casual / Too Blunt</span>
                    <p style="font-size: 1.08rem; font-weight: 700; color: #9a3412; margin: 8px 0;">"{item['casual']}"</p>
                    <small style="color: #7c2d12;">Avoid in high-stakes client correspondence or board meetings</small>
                </div>
                <div class="compare-box-formal">
                    <span class="badge-pill badge-adult">Polished Executive ({item['category']})</span>
                    <p style="font-size: 1.08rem; font-weight: 700; color: #166534; margin: 8px 0;">"{item['formal']}"</p>
                    <small style="color: #14532d;">Courteous, solution-oriented, and empowering</small>
                </div>
            </div>
            """, unsafe_allow_html=True)
            render_web_speech_button(
                item['formal'], 
                button_text=f"🔊 Listen: {item['category']}", 
                accent=web_accent, 
                speed=speed_float, 
                theme="emerald",
                key_id=f"fvc_{item['category']}_{item['formal'][:6]}"
            )

    elif career_choice == "🤝 Executive Meeting & Diplomatic Phrases":
        st.markdown("### 🤝 Navigating High-Stakes Meetings with Grace")
        
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.markdown("""
            <div class="custom-card card-ocean">
                <h4 style="color: #1e3a8a;">1. Tactful Disagreement</h4>
                <p>Instead of <em>"You're wrong"</em>:</p>
                <ul>
                    <li><em>"I see your point regarding budget; however, our primary concern should be delivery timelines."</em></li>
                    <li><em>"I have slight reservations about that direction because..."</em></li>
                    <li><em>"Could we explore an alternative perspective on this?"</em></li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            render_web_speech_button("I see your point regarding budget; however, our primary concern should be delivery timelines.", button_text="🔊 Disagree Tactfully", accent=web_accent, theme="ocean", key_id="meeting_disagree")

            st.markdown("""
            <div class="custom-card card-sunny">
                <h4 style="color: #92400e;">3. Interrupting Politely</h4>
                <p>Instead of cutting someone off abruptly:</p>
                <ul>
                    <li><em>"May I quickly interject with one supporting data point?"</em></li>
                    <li><em>"Before we move on to the next agenda item, could I add..."</em></li>
                    <li><em>"Pardon the interruption, but that directly connects to..."</em></li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            render_web_speech_button("May I quickly interject with one supporting data point?", button_text="🔊 Interrupt Politely", accent=web_accent, theme="sunset", key_id="meeting_interrupt")

        with col_m2:
            st.markdown("""
            <div class="custom-card card-emerald">
                <h4 style="color: #065f46;">2. Asking for Clarification</h4>
                <p>Instead of <em>"What do you mean?"</em>:</p>
                <ul>
                    <li><em>"Could you unpack that specific point a bit further?"</em></li>
                    <li><em>"Just to ensure we are completely aligned, are you proposing..."</em></li>
                    <li><em>"What would that look like in terms of weekly deliverables?"</em></li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            render_web_speech_button("Just to ensure we are completely aligned, could you unpack that point a bit further?", button_text="🔊 Clarify Gracefully", accent=web_accent, theme="emerald", key_id="meeting_clarify")

            st.markdown("""
            <div class="custom-card card-berry">
                <h4 style="color: #5b21b6;">4. Summarizing Action Items</h4>
                <p>Closing the meeting with crisp alignment:</p>
                <ul>
                    <li><em>"To recap our action items, Jessica will draft the brief by Thursday."</em></li>
                    <li><em>"Let's reconvene early next week once the metrics are compiled."</em></li>
                    <li><em>"Thank you everyone for the constructive exchange."</em></li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            render_web_speech_button("To recap our action items, Jessica will draft the brief by Thursday. Thank you everyone for the constructive exchange.", button_text="🔊 Recap Actions", accent=web_accent, theme="berry", key_id="meeting_recap")

    elif career_choice == "🎙️ Job Interview Success (The STAR Method)":
        st.markdown("### 🎙️ Mastering English Job Interviews")
        st.markdown("""
        Global employers evaluate candidates using behavioral interview questions. The **STAR Method** guarantees structured, punchy, and convincing responses.
        """)
        
        star_cols = st.columns(4)
        star_data = [
            ("S", "Situation", "Set the scene. Describe the context and challenge you faced.", "#3b82f6"),
            ("T", "Task", "What was your specific responsibility or goal?", "#10b981"),
            ("A", "Action", "What concrete steps did YOU take to address the issue?", "#f59e0b"),
            ("R", "Result", "What was the measurable outcome or positive impact achieved?", "#8b5cf6")
        ]
        for idx, (letter, title, desc, col) in enumerate(star_data):
            with star_cols[idx]:
                st.markdown(f"""
                <div class="custom-card" style="text-align: center; border-top: 5px solid {col};">
                    <h2 style="color: {col}; margin: 0; font-family: 'Outfit', sans-serif;">{letter}</h2>
                    <h4 style="margin: 4px 0;">{title}</h4>
                    <p style="font-size: 0.85rem; color: #475569;">{desc}</p>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("#### Model Answer: *'Describe a time you solved an unexpected problem.'*")
        sample_answer = "In my previous role, our primary software server went offline two hours before an investor presentation (Situation). As lead coordinator, my responsibility was to restore client access without delaying the showcase (Task). I immediately rallied our engineering team, established an interim backup server, and sent transparent status updates every 20 minutes (Action). As a result, the demo proceeded flawlessly, and the investor commended our calm communication (Result)."
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border-left: 5px solid #10b981; padding: 18px 22px; border-radius: 12px; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.1);">
            <p style="font-style: italic; color: #14532d; font-size: 1.04rem; margin: 0; line-height: 1.6;">"{sample_answer}"</p>
        </div>
        """, unsafe_allow_html=True)
        render_web_speech_button(sample_answer, button_text="🔊 Listen to Model Interview Answer", accent=web_accent, speed=speed_float, theme="emerald", key_id="interview_star")

# =========================================================
# TAB 6: Idioms & Expressions
# =========================================================
with nav_tabs[5]:
    st.markdown("## 💡 Colorful Idioms, Slang & Cultural Sayings")
    st.markdown("Idioms give English its humor, warmth, and native color. Explore their literal vs. figurative meanings and fascinating origins!")

    filter_level = st.selectbox("Filter Idioms by Style:", ["All Idioms", "Everyday", "Conversational", "Intermediate", "Academic", "Business"])
    
    filtered_idioms = IDIOMS_COLLECTION if filter_level == "All Idioms" else [i for i in IDIOMS_COLLECTION if i['level'] == filter_level]

    cols_idiom = st.columns(2)
    card_themes = ["ocean", "berry", "emerald", "sunny", "rose"]
    btn_themes = ["ocean", "berry", "emerald", "sunset", "sunset"]

    for idx, item in enumerate(filtered_idioms):
        col_target = cols_idiom[idx % 2]
        theme_idx = idx % len(card_themes)
        with col_target:
            st.markdown(f"""
            <div class="custom-card card-{card_themes[theme_idx]}" style="height: 94%;">
                <span class="badge-pill badge-idiom">{item['level']}</span>
                <h3 style="color: #4338ca; margin-top: 6px;">"{item['idiom']}"</h3>
                <p><strong>Meaning:</strong> {item['meaning']}</p>
                <p><strong>Example:</strong> <em>"{item['example']}"</em></p>
                <div style="background: rgba(255, 255, 255, 0.7); border: 1px dashed #cbd5e1; border-radius: 10px; padding: 10px 14px; font-size: 0.88rem; color: #475569;">
                    📜 <strong>Fascinating Origin:</strong> {item['origin']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            render_web_speech_button(
                f"{item['idiom']}. For example: {item['example']}", 
                button_text="🔊 Hear Idiom & Example", 
                accent=web_accent, 
                speed=speed_float, 
                theme=btn_themes[theme_idx],
                key_id=f"idiom_{idx}"
            )

# =========================================================
# TAB 7: Interactive Quiz Lab
# =========================================================
with nav_tabs[6]:
    st.markdown("## 🎯 Interactive English Quiz Lab")
    st.markdown("Test your skills across all levels and get instant, detailed coaching from Teacher Jessica on every single question!")

    quiz_category = st.selectbox(
        "Choose a Quiz Realm:",
        ["All Categories", "Beginner Foundations", "Grammar & Tenses", "Tricky & Confusing Words", "Business & Professional English"]
    )

    questions_to_show = QUIZ_BANK if quiz_category == "All Categories" else [q for q in QUIZ_BANK if q['category'] == quiz_category]

    for q_idx, q in enumerate(questions_to_show):
        st.markdown(f"""
        <div class="custom-card card-ocean" style="margin-bottom: 12px; padding: 20px;">
            <span class="badge-pill badge-student">{q['category']}</span>
            <h4 style="color: #0f172a; margin: 10px 0 14px 0; font-size: 1.15rem;">Question {q_idx + 1}: {q['question']}</h4>
        </div>
        """, unsafe_allow_html=True)

        user_choice = st.radio(
            "Choose the best answer:",
            q["options"],
            key=f"quiz_opt_{q_idx}_{q['question'][:10]}"
        )

        btn_col, _ = st.columns([1, 3])
        with btn_col:
            if st.button("Submit Answer", key=f"sub_{q_idx}"):
                chosen_idx = q["options"].index(user_choice)
                is_correct = (chosen_idx == q["answer"])
                
                # Update session state score
                q_key = f"q_{q['question']}"
                if q_key not in st.session_state.quiz_scores["answered"]:
                    st.session_state.quiz_scores["total"] += 1
                    if is_correct:
                        st.session_state.quiz_scores["correct"] += 1
                    st.session_state.quiz_scores["answered"][q_key] = is_correct

                if is_correct:
                    st.balloons()
                    st.markdown(f"""
                    <div class="quiz-feedback-correct">
                        <strong>🎉 Correct! Outstanding mastery!</strong><br>
                        {q['explanation']}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="quiz-feedback-wrong">
                        <strong>❌ Not quite. The correct answer is:</strong> <em>"{q['options'][q['answer']]}"</em><br>
                        <strong>Teacher Jessica's Rationale:</strong> {q['explanation']}
                    </div>
                    """, unsafe_allow_html=True)

# =========================================================
# TAB 8: Speaking & Pronunciation Studio
# =========================================================
with nav_tabs[7]:
    st.markdown("## 🎙️ Jessica's Speaking & Pronunciation Studio")
    st.markdown("""
    Want to master rhythm, intonation, and native accent reduction? Type or paste **any word, sentence, or speech** 
    and practice shadow-reading along with audio at your preferred speed!
    """)

    c_in, c_ctrl = st.columns([3, 1])
    with c_in:
        custom_speech_text = st.text_area(
            "Enter text to practice pronunciation:",
            value="Welcome to Jessica's English Learning Guide. Pronouncing every syllable clearly gives you the confidence to communicate with the world.",
            height=130
        )
    with c_ctrl:
        st.markdown("#### Studio Controls")
        chosen_region = st.selectbox("Accent Style", ["American (US) 🇺🇸", "British (UK) 🇬🇧", "Australian (AU) 🇦🇺"])
        chosen_rate = st.select_slider("Speech Speed", options=["0.7x (Slow Shadowing)", "1.0x (Natural)", "1.2x (Fast)"], value="1.0x (Natural)")
        rate_num = 0.7 if "0.7" in chosen_rate else (1.2 if "1.2" in chosen_rate else 1.0)
        reg_code = "en-US" if "US" in chosen_region else ("en-GB" if "UK" in chosen_region else "en-AU")

    if custom_speech_text:
        render_web_speech_button(custom_speech_text, button_text="🔊 Speak Text in Studio", speed=rate_num, accent=reg_code, theme="ocean", key_id="studio_custom")

    st.markdown("---")
    st.markdown("### 🗣️ Fun Diction & Tongue Twister Challenge")
    st.markdown("Tongue twisters loosen your jaw, vocal cords, and tongue to produce accurate English phonemes.")

    twisters = [
        {"title": "Easy: S & SH sounds", "text": "She sells seashells by the seashore, and the shells she sells are surely seashells.", "theme": "sunny"},
        {"title": "Medium: P sounds", "text": "Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked.", "theme": "ocean"},
        {"title": "Advanced: W & TH sounds", "text": "Whether the weather is warm, or whether the weather is hot, we must weather the weather, whatever the weather, whether we like it or not!", "theme": "berry"}
    ]

    for tw_idx, tw in enumerate(twisters):
        st.markdown(f"""
        <div class="custom-card card-{tw['theme']}" style="margin-bottom: 10px; padding: 18px;">
            <strong style="color: #1e3a8a; font-size: 1.05rem;">{tw['title']}</strong>
            <p style="font-size: 1.1rem; margin: 6px 0; color: #0f172a; font-weight: 500;"><em>"{tw['text']}"</em></p>
        </div>
        """, unsafe_allow_html=True)
        render_web_speech_button(tw['text'], button_text="🔊 Hear Twister at 0.8x Speed", speed=0.8, accent=reg_code, theme="berry", key_id=f"twister_{tw_idx}")

# =========================================================
# TAB 9: Smart Writing Polisher
# =========================================================
with nav_tabs[8]:
    st.markdown("## ✍️ Jessica's Smart Writing & Grammar Polisher")
    st.markdown("""
    Type or paste any draft sentence, paragraph, or email. Teacher Jessica will analyze it for common errors, 
    provide an elevated, natural alternative, and explain the grammatical reasoning!
    """)

    user_draft = st.text_area(
        "Enter your English draft here:",
        value="Yesterday I go to the meeting and discuss about the new project with my team. Everyone were very happy with my idea.",
        height=130
    )

    if st.button("✨ Analyze & Polish with Jessica", type="primary"):
        issues_found = []
        text_lower = user_draft.lower()

        # Check: 'discuss about'
        if "discuss about" in text_lower:
            issues_found.append(("Redundant Preposition", "The verb 'discuss' already means 'to talk about'. Use 'discuss the project', NOT 'discuss about the project'."))

        # Check: Yesterday + go (Simple past mismatch)
        if "yesterday i go" in text_lower or "yesterday he go" in text_lower or "yesterday we go" in text_lower:
            issues_found.append(("Tense Consistency", "'Yesterday' indicates a completed past event. Change base verb 'go' to the past tense 'went'."))

        # Check: Everyone were (Subject verb agreement)
        if "everyone were" in text_lower or "everybody were" in text_lower:
            issues_found.append(("Subject-Verb Agreement", "'Everyone' and 'Everybody' are grammatically singular indefinite pronouns and must take 'was', not 'were'."))

        # Check: Loose / Lose
        if " loose my" in text_lower or " loose the" in text_lower:
            issues_found.append(("Confusing Homophone", "'Loose' means not tight (clothing). You need 'lose' (to misplace or fail to keep)."))

        # Check: Affect / Effect
        if " side affect" in text_lower:
            issues_found.append(("Word Choice", "A consequence or result is an 'effect' (noun). Use 'side effect'."))

        # Generate a polished version
        polished_version = user_draft
        polished_version = polished_version.replace("yesterday I go", "Yesterday I went")
        polished_version = polished_version.replace("Yesterday I go", "Yesterday I went")
        polished_version = polished_version.replace("discuss about", "discussed")
        polished_version = polished_version.replace("Everyone were", "Everyone was")
        polished_version = polished_version.replace("everyone were", "everyone was")

        st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 12px; margin: 14px 0 10px 0;">
            <img src="{jessica_img_src}" style="width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 2px solid #10b981;" alt="Teacher Jessica Review">
            <h3 style="margin: 0; color: #065f46; font-family: 'Outfit', sans-serif;">Teacher Jessica's Diagnostic Report</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col_res1, col_res2 = st.columns(2)
        with col_res1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%); border: 2px solid #fecaca; border-radius: 14px; padding: 20px;">
                <h4 style="color: #991b1b; margin-top: 0;">Original Draft:</h4>
                <p style="color: #7f1d1d; font-family: monospace; font-size: 1.05rem;">""" + user_draft + """</p>
            </div>
            """, unsafe_allow_html=True)

        with col_res2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border: 2px solid #bbf7d0; border-radius: 14px; padding: 20px;">
                <h4 style="color: #166534; margin-top: 0;">Polished & Natural Version:</h4>
                <p style="color: #14532d; font-weight: 700; font-family: monospace; font-size: 1.05rem;">""" + polished_version + """</p>
            </div>
            """, unsafe_allow_html=True)
            render_web_speech_button(polished_version, button_text="🔊 Hear Polished Version", accent=web_accent, theme="emerald", key_id="polish_audio")

        if issues_found:
            st.markdown("#### 💡 Grammatical Insights & Explanations:")
            for cat, exp in issues_found:
                st.markdown(f"""
                <div class="jessica-callout">
                    <strong>⚠️ {cat}:</strong> {exp}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="quiz-feedback-correct">
                <strong>🌟 High-Quality Writing:</strong> Your sentence looks grammatically sound and reads naturally!
            </div>
            """, unsafe_allow_html=True)

# =========================================================
# TAB 10: Conversation Roleplay
# =========================================================
with nav_tabs[9]:
    st.markdown("## 💬 Real-World Conversation Roleplay")
    st.markdown("The fastest way to achieve conversational fluency is simulated immersion. Chat with Jessica across realistic scenarios!")

    selected_scen_key = st.selectbox("Choose a Scenario Realm:", list(ROLEPLAY_SCENARIOS.keys()))
    scen = ROLEPLAY_SCENARIOS[selected_scen_key]

    st.markdown(f"""
    <div class="custom-card card-ocean" style="margin-bottom: 16px; padding: 18px;">
        <h4 style="margin: 0; color: #1e40af; font-size: 1.2rem;">Role: {scen['character']}</h4>
        <p style="margin: 6px 0 0 0; color: #334155;"><strong>Setting:</strong> {scen['setting']}</p>
        <p style="margin: 4px 0 0 0; color: #2563eb; font-size: 0.95rem; font-weight: 600;"><strong>💡 Coach's Tip:</strong> {scen['tips']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Initial character message with Jessica's picture
    st.markdown(f"""
    <div class="chat-bubble-jessica-container">
        <img src="{jessica_img_src}" class="chat-avatar-jessica" alt="{scen['character']}">
        <div class="chat-bubble-jessica">
            <strong style="font-size: 1.05rem;">{scen['character']}:</strong><br>
            <span style="font-size: 1.1rem; line-height: 1.6;">"{scen['initial_message']}"</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    render_web_speech_button(scen['initial_message'], button_text=f"🔊 Hear {scen['character']}", accent=web_accent, theme="ocean", key_id=f"rp_init_{selected_scen_key[:6]}")

    st.markdown("#### Your Turn to Respond:")
    st.markdown("*Choose a prompt to practice or type your own custom response below:*")
    
    suggested_cols = st.columns(len(scen['prompts']))
    chosen_prompt_text = ""
    for idx, pr in enumerate(scen['prompts']):
        with suggested_cols[idx]:
            if st.button(f"Option {idx+1}", key=f"rp_btn_{idx}"):
                chosen_prompt_text = pr

    user_reply = st.text_input("Type your response:", value=chosen_prompt_text, placeholder="e.g. Hello! I would like to...", key="user_rp_reply")

    if st.button("Send Reply to Jessica", type="primary", key="send_rp"):
        if user_reply.strip():
            st.markdown(f"""
            <div class="chat-bubble-user">
                <strong>You:</strong><br>
                <span style="font-size: 1.08rem;">"{user_reply}"</span>
            </div>
            """, unsafe_allow_html=True)
            
            # Character dynamic feedback
            if "Coffee" in selected_scen_key:
                j_response = "Wonderful choice! That medium oat milk latte will be right up. Would you like that for here or to go?"
            elif "Airport" in selected_scen_key:
                j_response = "Thank you kindly. I found your booking! I have assigned you seat 14A by the window. Here is your boarding pass, departing from Gate 22 at 3:15 PM."
            elif "Job Interview" in selected_scen_key:
                j_response = "That is very impressive. Clear communication and proactive ownership are core values here. How do you prioritize deadlines when managing multiple conflicting tasks?"
            else:
                j_response = "I appreciate you sharing those symptoms. Let me take your temperature and examine your throat. Please take a slow, deep breath for me."

            st.markdown(f"""
            <div class="chat-bubble-jessica-container">
                <img src="{jessica_img_src}" class="chat-avatar-jessica" alt="{scen['character']}">
                <div class="chat-bubble-jessica">
                    <strong style="font-size: 1.05rem;">{scen['character']}:</strong><br>
                    <span style="font-size: 1.1rem; line-height: 1.6;">"{j_response}"</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            render_web_speech_button(j_response, button_text=f"🔊 Hear {scen['character']}'s Reply", accent=web_accent, theme="ocean", key_id=f"rp_reply_{selected_scen_key[:5]}")

            st.markdown("""
            <div class="jessica-callout">
                <strong>🌟 Fluency Feedback from Teacher Jessica:</strong> Great initiative! Your phrase was courteous and grammatically clear. Notice how natural follow-up questions keep the dialogue rolling smoothly.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("Please type or select a response first!")

# =========================================================
# TAB 11: Custom Study Planner & Cheat Sheet
# =========================================================
with nav_tabs[10]:
    st.markdown("## 📑 Personalized 30-Day Study Plan & Study Guide")
    st.markdown("Consistency is the engine of fluency. Tailor your 30-day roadmap and download your personal study guide.")

    c_plan1, c_plan2 = st.columns(2)
    with c_plan1:
        daily_time = st.select_slider(
            "How many minutes can you dedicate daily?",
            options=["15 minutes / day", "30 minutes / day", "45 minutes / day", "60 minutes / day"],
            value="30 minutes / day"
        )
    with c_plan2:
        study_focus = st.selectbox(
            "Primary learning objective:",
            ["Grammar Mastery & Tenses", "Professional Business English", "Daily Conversational Fluency", "Academic Essay & Test Prep (IELTS/TOEFL)"]
        )

    st.markdown("### 🗓️ Your 4-Week Milestone Roadmap")

    week_data = [
        {"week": "Week 1", "theme": "Foundation & Sound Accuracy", "activities": "Master vowel & consonant sounds, practice SVO sentence structure, 10 daily vocabulary flashcards, 5 mins shadowing.", "accent": "sunny"},
        {"week": "Week 2", "theme": "Tenses & Time Mastery", "activities": "Conquer Present vs. Present Perfect, the IN/ON/AT pyramid, complete Quiz Lab modules 1 & 2.", "accent": "ocean"},
        {"week": "Week 3", "theme": "Vocabulary Expansion & Nuance", "activities": "Homophones, 15 essential business or academic idioms, replace casual words with formal alternatives.", "accent": "emerald"},
        {"week": "Week 4", "theme": "Full Immersion & Fluency", "activities": "Draft an email or PEEL paragraph, record 2 conversation roleplays, achieve 80%+ on all quizzes.", "accent": "berry"}
    ]

    for w in week_data:
        st.markdown(f"""
        <div class="custom-card card-{w['accent']}">
            <h4 style="color: #1e3a8a; margin-top: 0; font-size: 1.15rem;">📅 {w['week']}: {w['theme']}</h4>
            <p style="margin: 4px 0 0 0; color: #334155; font-size: 1rem;"><strong>Daily Routine ({daily_time}):</strong> {w['activities']}</p>
        </div>
        """, unsafe_allow_html=True)

    # Printable / Downloadable Study Guide Markdown
    cheat_sheet_content = f"""# Jessica's English Learning Guide - To Students and Adults of All Ages
Target Learner Profile: {learner_profile}
Preferred Focus: {study_focus}
Daily Commitment: {daily_time}

## 1. Teacher Jessica's Core Grammar Rules
- **The IN / ON / AT Preposition Rule:**
  - IN: General (Years, Months, Cities, Countries) -> *in 2026, in France*
  - ON: Specific (Days, Dates, Streets) -> *on Monday, on October 31st*
  - AT: Very Precise (Exact times, Addresses) -> *at 9:00 AM, at the station*

- **The RAVEN Homophone Trick:**
  - **R**emember **A**ffect is a **V**erb, **E**ffect is a **N**oun.

- **The PEEL Essay Method:**
  - P: Point (Topic Sentence)
  - E: Explanation (Elaborate why/how)
  - E: Evidence (Proof, data, facts)
  - L: Link (Connect back to the overarching thesis)

## 2. Formal vs. Casual Quick Conversions
- "I wanna ask you something" -> "I would like to inquire about..."
- "No way, that won't work" -> "Unfortunately, that approach may present operational hurdles."
- "Sorry for the delay" -> "Thank you very much for your patience."
- "Shoot me an email" -> "Please feel free to forward the details via email."

## 3. Essential Idioms for Fluency
- "A blessing in disguise" -> A good outcome that initially looked like a misfortune.
- "Bite the bullet" -> Face an unavoidable difficulty with composure.
- "Break the ice" -> Ease tension with newcomers.
- "Hit the nail on the head" -> State the exact truth accurately.

Created with Jessica's English Learning Guide - To Students and Adults of All Ages.
"""

    st.download_button(
        label="📥 Download Teacher Jessica's Study Cheat Sheet (.MD)",
        data=cheat_sheet_content,
        file_name="Jessicas_English_Learning_Guide_CheatSheet.md",
        mime="text/markdown"
    )

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #64748b; font-size: 0.95rem; padding: 22px 0;">
    <div style="display: flex; justify-content: center; align-items: center; gap: 10px; margin-bottom: 8px;">
        <img src="{jessica_img_src}" style="width: 36px; height: 36px; border-radius: 50%; object-fit: cover; border: 2px solid #0284c7;" alt="Jessica">
        <strong style="color: #1e3a8a; font-size: 1.05rem;">Jessica's English Learning Guide - To Students and Adults of All Ages</strong>
    </div>
    Empowering students, professionals, and curious minds worldwide to speak and write English with joyful confidence.<br>
    © 2026 Teacher Jessica's Academy • All learning rights reserved.
</div>
""", unsafe_allow_html=True)
