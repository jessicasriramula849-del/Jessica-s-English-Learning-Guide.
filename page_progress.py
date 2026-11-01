"""Progress dashboard and downloadable learning report."""

from __future__ import annotations

import json
from datetime import datetime

import streamlit as st

from content import LESSONS, READINGS, SITE_NAME
from core import (
    journey_percent,
    log_activity,
    page_header,
    safe,
    section_heading,
)


def _earned_badges() -> list[dict]:
    lessons_done = len(st.session_state.completed_lessons)
    readings_done = len(st.session_state.completed_readings)
    drafts = len(st.session_state.writing_entries)
    quiz_best = st.session_state.quiz_best
    words = len(st.session_state.flash_mastered)
    spelling = len(st.session_state.spelling_solved)

    return [
        {"icon": "🌱", "name": "First Step", "desc": "Complete your first lesson", "earned": lessons_done >= 1},
        {"icon": "🌿", "name": "Curious Mind", "desc": "Complete five lessons", "earned": lessons_done >= 5},
        {"icon": "🌳", "name": "Course Explorer", "desc": "Complete all 16 lessons", "earned": lessons_done >= len(LESSONS)},
        {"icon": "📖", "name": "Story Explorer", "desc": "Finish your first story", "earned": readings_done >= 1},
        {"icon": "📚", "name": "Bookworm", "desc": "Finish five stories", "earned": readings_done >= 5},
        {"icon": "✍️", "name": "First Draft", "desc": "Save your first piece of writing", "earned": drafts >= 1},
        {"icon": "🖋️", "name": "Wordsmith", "desc": "Save four pieces of writing", "earned": drafts >= 4},
        {"icon": "🧠", "name": "Quiz Whiz", "desc": "Score 8 or more in a quiz", "earned": quiz_best >= 8},
        {"icon": "🃏", "name": "Word Collector", "desc": "Mark ten words as known", "earned": words >= 10},
        {"icon": "🔤", "name": "Spelling Star", "desc": "Spell eight words correctly", "earned": spelling >= 8},
        {"icon": "🌻", "name": "Well-Rounded", "desc": "Read, write, and learn across the guide", "earned": lessons_done >= 8 and readings_done >= 4 and drafts >= 2},
        {"icon": "🏅", "name": "All-Rounder", "desc": "Complete every lesson and every story", "earned": lessons_done == len(LESSONS) and readings_done == len(READINGS)},
    ]


def _next_step() -> tuple[str, str]:
    if not st.session_state.completed_lessons:
        return "Begin with the alphabet", "Your first lesson is a gentle introduction to the 26 letters and their sounds."
    if not st.session_state.completed_readings:
        return "Read your first story", "A three-minute story is enough to turn today's lesson into real reading."
    if not st.session_state.writing_entries:
        return "Save one small draft", "The Introduce Yourself prompt asks for only about 70 words. Start with one sentence."
    if st.session_state.quiz_best < 5:
        return "Try a friendly quiz", "Ten questions, explained answers, no ranking. Use it to notice what to revisit."
    if len(st.session_state.completed_lessons) < len(LESSONS):
        return "Continue your lesson path", "Pick up the next lesson in the sequence and add one new structure to your English."
    return "Reread, revise, and enjoy", "You have travelled a long way. Return to a favourite story or write something new for pleasure."


def render_progress() -> None:
    page_header(
        "Your journey",
        "Notice how far you have come",
        "Progress is not a straight line, and it is not a competition. This page gathers your practice in one place so you can see the small steps adding up.",
        "🏅",
    )

    percent = journey_percent()
    lessons_done = len(st.session_state.completed_lessons)
    readings_done = len(st.session_state.completed_readings)
    drafts = len(st.session_state.writing_entries)
    words = len(st.session_state.flash_mastered)
    spelling = len(st.session_state.spelling_solved)

    overview_col, next_col = st.columns([1.05, 1])
    with overview_col:
        st.markdown(
            f"""
            <div class="card card-dark" style="min-height:205px">
                <div class="card-kicker" style="color:#ffe0a0">Overall journey</div>
                <h3 style="font-family:Georgia,serif;font-size:3.5rem;line-height:1;margin:0.45rem 0 0.3rem">{percent}%</h3>
                <p>A blend of lessons, reading, writing, quiz progress and vocabulary. There is no deadline attached to this number.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.progress(percent / 100)

    with next_col:
        step_title, step_body = _next_step()
        st.markdown(
            f"""
            <div class="card card-warm" style="min-height:205px">
                <div class="card-kicker">Your next best step</div>
                <h3>{safe(step_title)}</h3>
                <p>{safe(step_body)}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    section_heading("At a glance", "Your practice so far")
    metric_cols = st.columns(4)
    with metric_cols[0]:
        st.metric("Lessons", f"{lessons_done}/{len(LESSONS)}")
    with metric_cols[1]:
        st.metric("Stories", f"{readings_done}/{len(READINGS)}")
    with metric_cols[2]:
        st.metric("Drafts saved", str(drafts))
    with metric_cols[3]:
        st.metric("Quiz best", f"{st.session_state.quiz_best}/10")

    section_heading("Four kinds of growth", "Each one matters")
    growth_cols = st.columns(4)
    growth = [
        ("Lessons completed", lessons_done, len(LESSONS), "Structures and vocabulary you have studied."),
        ("Stories finished", readings_done, len(READINGS), "Real English read for meaning, not just words."),
        ("Writing saved", drafts, 4, "Four saved drafts is a rich notebook, not a quota."),
        ("Words marked known", words, 12, "Words you can recognise and use with growing ease."),
    ]
    for col, (label, value, total, note) in zip(growth_cols, growth):
        with col:
            st.markdown(
                f"""
                <div class="card" style="min-height:165px">
                    <div class="card-kicker">{safe(label)}</div>
                    <h3 style="font-family:Georgia,serif;font-size:2rem;margin:0.35rem 0 0.15rem">{min(value, total)}/{total}</h3>
                    <p>{safe(note)}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.progress(min(value / total, 1.0))

    # ------------------------------------------------------------------
    # Badges
    # ------------------------------------------------------------------
    section_heading("Small badges for real effort", "Nothing here expires")
    badges = _earned_badges()
    badge_html = ""
    for badge in badges:
        state_class = "earned" if badge["earned"] else "locked"
        mark = "Earned" if badge["earned"] else "Not yet"
        badge_html += f"""
        <div class="badge-card {state_class}">
            <div class="badge-icon">{badge["icon"]}</div>
            <div>
                <strong>{safe(badge["name"])}</strong>
                <span>{safe(badge["desc"])}</span>
                <span style="color:{'#8b6c36' if badge['earned'] else '#8b9791'};font-weight:700;margin-top:0.3rem">{mark}</span>
            </div>
        </div>
        """
    st.markdown(f"<div class='badge-grid'>{badge_html}</div>", unsafe_allow_html=True)

    # ------------------------------------------------------------------
    # Recent activity and rhythm
    # ------------------------------------------------------------------
    activity_col, rhythm_col = st.columns([1.05, 1])
    with activity_col:
        section_heading("Recent activity", "Your last few steps")
        if not st.session_state.activity:
            st.info("Your activity will appear here after you complete a lesson, story, quiz, or saved draft.")
        else:
            rows = ""
            for item in st.session_state.activity[:8]:
                rows += f"""
                <div class="activity-row">
                    <span class="activity-icon">{item["icon"]}</span>
                    <span class="activity-text">{safe(item["text"])}</span>
                    <span class="activity-time">{safe(item["time"])}</span>
                </div>
                """
            st.markdown(f"<div class='card' style='padding:0.4rem 1rem'>{rows}</div>", unsafe_allow_html=True)

    with rhythm_col:
        section_heading("A gentle weekly rhythm", "Adapt it freely")
        st.markdown(
            """
            <div class="week-grid">
                <div class="week-day"><strong>Mon</strong><p>One lesson, slowly</p></div>
                <div class="week-day"><strong>Tue</strong><p>Ten vocabulary cards</p></div>
                <div class="week-day"><strong>Wed</strong><p>Read one story</p></div>
                <div class="week-day"><strong>Thu</strong><p>Write five sentences</p></div>
                <div class="week-day"><strong>Fri</strong><p>Quick quiz or spelling</p></div>
                <div class="week-day"><strong>Sat</strong><p>Reread and review</p></div>
                <div class="week-day"><strong>Sun</strong><p>Rest, or follow curiosity</p></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption("Missing a day is not a failure. The next small step is always waiting.")

    # ------------------------------------------------------------------
    # Report
    # ------------------------------------------------------------------
    section_heading("Keep a copy of your progress", "Download a report")
    report = {
        "site": SITE_NAME,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "journey_percent": percent,
        "lessons_completed": [
            next(item["title"] for item in LESSONS if item["id"] == lesson_id)
            for lesson_id in st.session_state.completed_lessons
        ],
        "stories_completed": [
            next(item["title"] for item in READINGS if item["id"] == reading_id)
            for reading_id in st.session_state.completed_readings
        ],
        "quiz_best": st.session_state.quiz_best,
        "quiz_attempts": st.session_state.quiz_attempts,
        "vocabulary_known": sorted(st.session_state.flash_mastered),
        "spelling_solved": sorted(st.session_state.spelling_solved),
        "writing_entries": st.session_state.writing_entries,
        "recent_activity": st.session_state.activity,
    }
    report_json = json.dumps(report, indent=2, ensure_ascii=False)
    st.download_button(
        "Download my progress report",
        data=report_json,
        file_name="jessicas_english_progress_report.json",
        mime="application/json",
    )
    st.caption("The report includes your saved writing. Keep it somewhere private that you choose.")

    # ------------------------------------------------------------------
    # Reset
    # ------------------------------------------------------------------
    with st.expander("Reset my progress"):
        st.warning(
            "This clears completed lessons and stories, saved drafts, quiz scores, known words, spelling progress, "
            "and activity for this browser session. It cannot be undone."
        )
        confirm = st.checkbox("I understand and want to reset my progress", key="confirm_reset")
        if st.button("Reset all progress", type="primary", disabled=not confirm):
            st.session_state.completed_lessons = set()
            st.session_state.completed_readings = set()
            st.session_state.writing_entries = []
            st.session_state.quiz_best = 0
            st.session_state.quiz_attempts = 0
            st.session_state.quiz_result = None
            st.session_state.quiz_round += 1
            st.session_state.flash_mastered = set()
            st.session_state.spelling_solved = set()
            st.session_state.spelling_correct = 0
            st.session_state.spelling_attempts = 0
            st.session_state.activity = []
            log_activity("🌱", "Started a fresh learning journey.")
            st.rerun()
