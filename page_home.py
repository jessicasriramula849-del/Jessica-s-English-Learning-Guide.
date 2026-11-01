"""Home page for the learning guide."""

from datetime import date

import streamlit as st

from content import (
    DAILY_WORDS,
    LESSONS,
    LEVEL_DETAILS,
    READINGS,
    SITE_NAME,
    WRITING_PROMPTS,
)
from core import (
    PAGE_LEARN,
    PAGE_PRACTICE,
    PAGE_READ,
    PAGE_WRITE,
    chip,
    go_to,
    lesson_by_id,
    reading_by_id,
    safe,
    section_heading,
)


def _start_beginning() -> None:
    st.session_state.learn_level = "All levels"
    st.session_state.selected_lesson = "alphabet"
    st.session_state.page = PAGE_LEARN


def _open_lesson(lesson_id: str) -> None:
    st.session_state.learn_level = "All levels"
    st.session_state.selected_lesson = lesson_id
    st.session_state.page = PAGE_LEARN


def _open_reading(reading_id: str) -> None:
    st.session_state.reading_level = "All levels"
    st.session_state.selected_reading = reading_id
    st.session_state.page = PAGE_READ


def _open_level(level: str) -> None:
    st.session_state.learn_level = level
    st.session_state.page = PAGE_LEARN


def _open_writing() -> None:
    st.session_state.writing_level = "All levels"
    st.session_state.page = PAGE_WRITE


def render_home() -> None:
    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-kicker">✦ Read · Write · Speak · Grow</div>
            <h1>
                Jessica's English Learning Guide
                <span>For Students And Adults Of All Ages</span>
            </h1>
            <p>
                A warm, free place to begin English from the very first letter — or to return,
                rebuild, and finally feel at home in the language. Learn one small step at a time,
                at your own pace, with no sign-in and no pressure.
            </p>
            <div class="hero-chips">
                <span>16 guided lessons</span>
                <span>8 graded stories</span>
                <span>8 writing studios</span>
                <span>Instant practice checks</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right, spacer = st.columns([1.25, 1.15, 1.3])
    with left:
        st.button(
            "Start from the beginning →",
            type="primary",
            use_container_width=True,
            on_click=_start_beginning,
        )
    with right:
        st.button(
            "Explore all lessons",
            use_container_width=True,
            on_click=go_to,
            args=(PAGE_LEARN,),
        )
    with spacer:
        st.caption("No account. No cost. Just begin.")

    st.markdown(
        f"""
        <div class="stat-strip">
            <div class="stat"><strong>{len(LESSONS)}</strong><span>step-by-step lessons</span></div>
            <div class="stat"><strong>{len(READINGS)}</strong><span>graded reading stories</span></div>
            <div class="stat"><strong>{len(WRITING_PROMPTS)}</strong><span>guided writing prompts</span></div>
            <div class="stat"><strong>All ages</strong><span>clear, respectful, self-paced</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ------------------------------------------------------------------
    # Continue learning
    # ------------------------------------------------------------------
    section_heading("Pick up where you left off", "Your next small step")

    next_lesson = next(
        (item for item in LESSONS if item["id"] not in st.session_state.completed_lessons),
        LESSONS[0],
    )
    next_reading = next(
        (item for item in READINGS if item["id"] not in st.session_state.completed_readings),
        READINGS[0],
    )

    lesson_done = next_lesson["id"] in st.session_state.completed_lessons
    reading_done = next_reading["id"] in st.session_state.completed_readings

    col_a, col_b = st.columns(2)
    with col_a:
        lesson_status = "Revisit a favourite" if lesson_done else "Continue your lessons"
        st.markdown(
            f"""
            <div class="card">
                <span class="card-icon">📚</span>
                <div class="card-kicker">{safe(lesson_status)}</div>
                <h3>{safe(next_lesson["title"])}</h3>
                <p>{safe(next_lesson["subtitle"])}</p>
                <div style="margin-top:0.8rem">
                    {chip(next_lesson["level"], "sage")}
                    {chip(f"{next_lesson['minutes']} min", "gold")}
                    {chip("Lesson " + str(next(i for i, x in enumerate(LESSONS, 1) if x["id"] == next_lesson["id"])), "muted")}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.button(
            "Open this lesson",
            key="home_open_lesson",
            use_container_width=True,
            on_click=_open_lesson,
            args=(next_lesson["id"],),
        )

    with col_b:
        reading_status = "Return to a story" if reading_done else "Grow through reading"
        st.markdown(
            f"""
            <div class="card card-warm">
                <span class="card-icon">📖</span>
                <div class="card-kicker">{safe(reading_status)}</div>
                <h3>{safe(next_reading["title"])}</h3>
                <p>{safe(next_reading["intro"])}</p>
                <div style="margin-top:0.8rem">
                    {chip(next_reading["level"], "sage")}
                    {chip(f"{next_reading['minutes']} min", "gold")}
                    {chip(next_reading["focus"], "muted")}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.button(
            "Open this story",
            key="home_open_reading",
            use_container_width=True,
            on_click=_open_reading,
            args=(next_reading["id"],),
        )

    # ------------------------------------------------------------------
    # Learning paths
    # ------------------------------------------------------------------
    section_heading("A path for every season of life", "Choose a starting point")

    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown(
            """
            <div class="card path-card">
                <div class="level-row"><span class="level-icon">🌱</span><span class="chip chip-sage">Foundation</span></div>
                <h3>Start from the very beginning</h3>
                <p>Letters, sounds, greetings, numbers and your first clear sentences.</p>
                <ul class="card-list">
                    <li>Alphabet and letter sounds</li>
                    <li>Introducing yourself</li>
                    <li>Nouns, articles and simple present</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.button("Begin at Foundation", key="home_path_foundation", use_container_width=True, on_click=_open_level, args=("Foundation",))

    with p2:
        st.markdown(
            """
            <div class="card path-card">
                <div class="level-row"><span class="level-icon">🌿</span><span class="chip chip-gold">Beginner · Growing</span></div>
                <h3>Build everyday confidence</h3>
                <p>Questions, past and future tenses, descriptions, and longer reading.</p>
                <ul class="card-list">
                    <li>Ask and answer naturally</li>
                    <li>Tell stories about your life</li>
                    <li>Write clear messages and emails</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.button("Build the basics", key="home_path_build", use_container_width=True, on_click=_open_level, args=("Beginner",))

    with p3:
        st.markdown(
            """
            <div class="card path-card">
                <div class="level-row"><span class="level-icon">🌻</span><span class="chip chip-coral">Confident</span></div>
                <h3>Express yourself with nuance</h3>
                <p>Life experience, conditionals, polite English, idioms and inference.</p>
                <ul class="card-list">
                    <li>Present perfect and conditionals</li>
                    <li>Professional, polite writing</li>
                    <li>Read between the lines</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.button("Explore Confident", key="home_path_confident", use_container_width=True, on_click=_open_level, args=("Confident",))

    # ------------------------------------------------------------------
    # Three ways to practise
    # ------------------------------------------------------------------
    section_heading("Three ways to grow, every week", "Read. Write. Practise.")

    t1, t2, t3 = st.columns(3)
    with t1:
        st.markdown(
            """
            <div class="card card-dark">
                <span class="card-icon">📖</span>
                <div class="card-kicker" style="color:#ffe0a0">Read</div>
                <h3>Stories that meet you at your level</h3>
                <p>Eight short, original stories from first words to confident inference. Every story has a glossary and comprehension questions.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.button("Go to reading", key="home_read_cta", use_container_width=True, on_click=go_to, args=(PAGE_READ,))

    with t2:
        st.markdown(
            """
            <div class="card">
                <span class="card-icon">✍️</span>
                <div class="card-kicker">Write</div>
                <h3>Guided writing, from a first line to a full opinion</h3>
                <p>Use sentence starters, model answers and a friendly practice check that looks at clarity, structure and conventions — without judging you.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.button("Open the writing studio", key="home_write_cta", use_container_width=True, on_click=_open_writing)

    with t3:
        st.markdown(
            """
            <div class="card card-warm">
                <span class="card-icon">🎯</span>
                <div class="card-kicker">Practise</div>
                <h3>Words, spelling and a quick quiz</h3>
                <p>Flip vocabulary cards, test your spelling, and take a ten-question check. Answers come with a short explanation every time.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.button("Enter the practice zone", key="home_practice_cta", use_container_width=True, on_click=go_to, args=(PAGE_PRACTICE,))

    # ------------------------------------------------------------------
    # Word of the day + note
    # ------------------------------------------------------------------
    section_heading("A little inspiration for today", date.today().strftime("%B %d, %Y"))

    word = DAILY_WORDS[date.today().toordinal() % len(DAILY_WORDS)]
    note_col, word_col = st.columns([1.05, 0.95])
    with note_col:
        st.markdown(
            """
            <div class="note-card">
                <span class="quote-mark">“</span>
                <p>You do not need to know every word to speak with warmth. You need one brave sentence,
                a listening ear, and the willingness to try again. That is how every fluent person began.</p>
                <div class="signature">A note from Jessica</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with word_col:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-kicker">Word of the day</div>
                <h3 style="font-size:2rem;margin:0.25rem 0 0.1rem">{safe(word["word"])}</h3>
                <p style="color:#7b8b84;font-size:0.78rem">/{safe(word["pron"])}/</p>
                <p style="margin-top:0.65rem;color:#4f625a;font-size:0.94rem">{safe(word["meaning"])}</p>
                <p style="margin-top:0.65rem;color:#8b7050;font-style:italic">“{safe(word["example"])}”</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.button(
            "Try a vocabulary card",
            key="home_word_cta",
            use_container_width=True,
            on_click=go_to,
            args=(PAGE_PRACTICE,),
        )

    # ------------------------------------------------------------------
    # Every age, every pace
    # ------------------------------------------------------------------
    section_heading("Made for every age and every pace", "What makes this guide different")
    st.markdown(
        f"""
        <div class="card" style="background:rgba(220,235,221,0.38)">
            <div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1.3rem">
                <div>
                    <div class="card-kicker">No assumptions</div>
                    <h3 style="font-size:1.1rem">Begin without shame</h3>
                    <p>Lessons begin with the alphabet and build in small, logical steps. Adults and students can start at the same door without feeling talked down to.</p>
                </div>
                <div>
                    <div class="card-kicker">No rush</div>
                    <h3 style="font-size:1.1rem">Your pace is the right pace</h3>
                    <p>There are no timers, rankings or public scores. Return when you can. A ten-minute session still counts as progress.</p>
                </div>
                <div>
                    <div class="card-kicker">No performance</div>
                    <h3 style="font-size:1.1rem">Practise honestly</h3>
                    <p>Checks are here to teach, not to judge. Every answer includes an explanation, and every draft is yours to revise.</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
