"""Shared state, layout, and visual helpers for the learning guide."""

from __future__ import annotations

import html
from datetime import datetime

import streamlit as st

from content import LESSONS, READINGS, SITE_NAME

PAGE_HOME = "🏠 Home"
PAGE_LEARN = "📚 Learn English"
PAGE_READ = "📖 Read English"
PAGE_WRITE = "✍️ Write English"
PAGE_PRACTICE = "🎯 Practice Zone"
PAGE_PROGRESS = "🏅 My Progress"
PAGES = [PAGE_HOME, PAGE_LEARN, PAGE_READ, PAGE_WRITE, PAGE_PRACTICE, PAGE_PROGRESS]

DEFAULTS = {
    "page": PAGE_HOME,
    "large_text": False,
    "completed_lessons": set(),
    "completed_readings": set(),
    "writing_entries": [],
    "quiz_best": 0,
    "quiz_attempts": 0,
    "quiz_round": 0,
    "quiz_result": None,
    "flash_mastered": set(),
    "spelling_solved": set(),
    "spelling_correct": 0,
    "spelling_attempts": 0,
    "activity": [],
    "learn_level": "All levels",
    "selected_lesson": LESSONS[0]["id"],
    "reading_level": "All levels",
    "selected_reading": READINGS[0]["id"],
    "writing_level": "All levels",
    "selected_prompt": "introduce",
    "flash_index": 0,
    "flash_reveal": False,
    "flash_category": "All words",
    "spell_index": 0,
    "spelling_result": None,
}


def init_state() -> None:
    for key, value in DEFAULTS.items():
        if key not in st.session_state:
            st.session_state[key] = value


def safe(value: object) -> str:
    return html.escape(str(value))


def go_to(page: str) -> None:
    st.session_state.page = page


def log_activity(icon: str, text: str) -> None:
    entry = {
        "icon": icon,
        "text": text,
        "time": datetime.now().strftime("%b %d, %I:%M %p"),
    }
    st.session_state.activity.insert(0, entry)
    del st.session_state.activity[12:]


def journey_percent() -> int:
    lesson_part = len(st.session_state.completed_lessons) / max(len(LESSONS), 1) * 30
    reading_part = len(st.session_state.completed_readings) / max(len(READINGS), 1) * 25
    writing_part = min(len(st.session_state.writing_entries) / 4, 1) * 20
    quiz_part = min(st.session_state.quiz_best / 10, 1) * 15
    words_part = min(len(st.session_state.flash_mastered) / 12, 1) * 10
    return int(round(lesson_part + reading_part + writing_part + quiz_part + words_part))


def lesson_by_id(lesson_id: str) -> dict:
    return next(item for item in LESSONS if item["id"] == lesson_id)


def reading_by_id(reading_id: str) -> dict:
    return next(item for item in READINGS if item["id"] == reading_id)


def prompt_by_id(prompt_id: str):
    from content import WRITING_PROMPTS

    return next(item for item in WRITING_PROMPTS if item["id"] == prompt_id)


def page_header(eyebrow: str, title: str, subtitle: str, icon: str = "") -> None:
    icon_html = f"<span class='page-icon'>{safe(icon)}</span>" if icon else ""
    st.markdown(
        f"""
        <div class="page-head">
            <div class="page-head-row">{icon_html}<span class="eyebrow">{safe(eyebrow)}</span></div>
            <h1>{safe(title)}</h1>
            <p>{safe(subtitle)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_heading(title: str, note: str = "") -> None:
    note_html = f"<span>{safe(note)}</span>" if note else ""
    st.markdown(
        f"<div class='section-heading'><h2>{safe(title)}</h2>{note_html}</div>",
        unsafe_allow_html=True,
    )


def chip(text: str, tone: str = "sage") -> str:
    return f"<span class='chip chip-{tone}'>{safe(text)}</span>"


def linked_selectbox(
    label: str,
    ids: list[str],
    state_key: str,
    widget_key: str,
    label_fn,
    help_text: str | None = None,
) -> str:
    """A selectbox that displays friendly labels while storing stable IDs.

    Streamlit's format_func works well in the browser but is not supported by
    AppTest when widget state is serialised. This helper keeps the displayed
    labels and the stored identifiers separate without using format_func.
    """
    labels = [label_fn(item_id) for item_id in ids]
    id_by_label = dict(zip(labels, ids))

    current = st.session_state.get(state_key)
    if current not in ids:
        current = ids[0]
        st.session_state[state_key] = current

    expected_label = label_fn(current)
    if st.session_state.get(widget_key) != expected_label:
        # This runs before the widget is created, so it is safe to set its state.
        st.session_state[widget_key] = expected_label

    def _sync() -> None:
        st.session_state[state_key] = id_by_label[st.session_state[widget_key]]

    choice = st.selectbox(
        label,
        labels,
        key=widget_key,
        on_change=_sync,
        help=help_text,
    )
    return id_by_label[choice]


def inject_css(large_text: bool = False) -> None:
    size_rule = (
        """
        .stApp { font-size: 1.08rem; }
        .story-paragraph { font-size: 1.2rem !important; }
        .lesson-section p { font-size: 1.05rem; }
        """
        if large_text
        else ""
    )
    st.markdown(
        """
        <style>
        :root {
            --forest: #174f42;
            --forest-deep: #103a31;
            --sage: #dcebdd;
            --sage-mid: #b9d6c4;
            --cream: #fbf7ef;
            --paper: #fffdf8;
            --coral: #d8684d;
            --gold: #e4ad45;
            --ink: #1a312b;
            --muted: #63746d;
            --line: #e8dfd1;
            --soft-shadow: 0 14px 40px rgba(37, 62, 53, 0.08);
        }

        html, body, [class*="css"] {
            font-family: "Segoe UI", "Trebuchet MS", Arial, sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at 100% 0%, rgba(228, 173, 69, 0.10), transparent 28rem),
                radial-gradient(circle at 0% 28%, rgba(185, 214, 196, 0.25), transparent 32rem),
                var(--cream);
            color: var(--ink);
        }

        .block-container {
            max-width: 1180px;
            padding-top: 2.2rem;
            padding-bottom: 4rem;
        }

        #MainMenu, footer { visibility: hidden; }
        header[data-testid="stHeader"] { background: transparent; }

        h1, h2, h3, h4 {
            color: var(--ink);
            letter-spacing: -0.02em;
        }

        p, li { line-height: 1.7; }

        [data-testid="stSidebar"] {
            background: linear-gradient(175deg, #123f35 0%, #1b5b4b 72%, #2b6d57 100%);
            border-right: 1px solid rgba(255, 255, 255, 0.08);
        }

        [data-testid="stSidebar"] * { color: #f8f3e7; }
        [data-testid="stSidebar"] .stCaption, [data-testid="stSidebar"] small { color: rgba(248, 243, 231, 0.68) !important; }
        [data-testid="stSidebar"] hr { border-color: rgba(255, 255, 255, 0.14); }

        [data-testid="stSidebar"] [data-testid="stRadio"] > label,
        [data-testid="stSidebar"] [data-testid="stWidgetLabel"] { color: rgba(248, 243, 231, 0.6) !important; }

        [data-testid="stSidebar"] [role="radiogroup"] { gap: 0.22rem; }

        [data-testid="stSidebar"] [role="radiogroup"] label {
            padding: 0.62rem 0.72rem;
            border-radius: 0.75rem;
            transition: background 0.15s ease, transform 0.15s ease;
            border: 1px solid transparent;
        }

        [data-testid="stSidebar"] [role="radiogroup"] label:hover {
            background: rgba(255, 255, 255, 0.08);
            transform: translateX(2px);
        }

        [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
            background: rgba(255, 255, 255, 0.14);
            border-color: rgba(255, 255, 255, 0.18);
        }

        [data-testid="stSidebar"] [role="radiogroup"] label p {
            font-size: 0.95rem;
            font-weight: 600;
        }

        [data-testid="stSidebar"] [data-baseweb="checkbox"] span,
        [data-testid="stSidebar"] [data-baseweb="toggle"] span { color: #f8f3e7; }

        .side-brand {
            display: flex;
            gap: 0.8rem;
            align-items: center;
            margin: 0.2rem 0 0.35rem;
        }

        .side-mark {
            width: 46px;
            height: 46px;
            border-radius: 14px;
            background: var(--gold);
            color: #17352d !important;
            font-family: Georgia, serif;
            font-weight: 800;
            font-size: 1.7rem;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.16);
        }

        .side-title {
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.12rem;
            line-height: 1.12;
            font-weight: 700;
            color: #fffaf0 !important;
        }

        .side-tagline {
            color: rgba(248, 243, 231, 0.68) !important;
            font-size: 0.79rem;
            line-height: 1.5;
            margin: 0.2rem 0 1.25rem;
        }

        .side-label {
            color: rgba(248, 243, 231, 0.54) !important;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            font-size: 0.64rem;
            font-weight: 700;
            margin: 0.85rem 0 0.15rem;
        }

        .side-progress {
            margin-top: 0.35rem;
            padding: 0.9rem 0.85rem;
            border-radius: 0.9rem;
            background: rgba(255, 255, 255, 0.07);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .side-progress-top {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            font-size: 0.8rem;
            margin-bottom: 0.4rem;
        }

        .side-progress-top strong { color: #ffd985 !important; font-size: 0.95rem; }

        .side-progress-caption {
            color: rgba(248, 243, 231, 0.6) !important;
            font-size: 0.7rem;
            margin-top: 0.45rem;
            line-height: 1.4;
        }

        .side-footer {
            color: rgba(248, 243, 231, 0.48) !important;
            font-size: 0.68rem;
            line-height: 1.55;
            border-top: 1px solid rgba(255, 255, 255, 0.12);
            padding-top: 0.9rem;
            margin-top: 1.1rem;
        }

        [data-testid="stSidebar"] [data-testid="stProgress"] > div > div > div > div {
            background-color: #e4ad45;
        }

        [data-testid="stSidebar"] [data-testid="stProgress"] > div > div {
            background-color: rgba(255, 255, 255, 0.14);
        }

        .hero {
            position: relative;
            overflow: hidden;
            background: linear-gradient(125deg, #123f35 0%, #1b5b4b 58%, #2f715c 100%);
            border-radius: 1.8rem;
            padding: clamp(2.2rem, 5vw, 4.2rem);
            color: #fffaf0;
            box-shadow: 0 24px 60px rgba(23, 79, 66, 0.18);
            isolation: isolate;
        }

        .hero::before {
            content: "";
            position: absolute;
            width: 390px;
            height: 390px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(228, 173, 69, 0.44), transparent 68%);
            right: -120px;
            top: -150px;
            z-index: -1;
        }

        .hero::after {
            content: "";
            position: absolute;
            width: 260px;
            height: 260px;
            border-radius: 50%;
            border: 1px solid rgba(255, 255, 255, 0.18);
            right: 8%;
            bottom: -170px;
            z-index: -1;
        }

        .hero-kicker {
            display: inline-flex;
            gap: 0.5rem;
            align-items: center;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.18);
            color: #ffe5a3 !important;
            border-radius: 999px;
            padding: 0.35rem 0.8rem;
            font-size: 0.68rem;
            font-weight: 700;
            letter-spacing: 0.13em;
            text-transform: uppercase;
            margin-bottom: 1.3rem;
        }

        .hero h1 {
            color: #fffaf0;
            font-family: Georgia, "Times New Roman", serif;
            font-size: clamp(2.35rem, 5.2vw, 4.35rem);
            line-height: 1.02;
            letter-spacing: -0.04em;
            margin: 0;
            max-width: 980px;
        }

        .hero h1 span {
            display: block;
            color: #b9d6c4;
            font-size: 0.53em;
            line-height: 1.2;
            letter-spacing: -0.02em;
            margin-top: 0.65rem;
            font-style: italic;
            font-weight: 400;
        }

        .hero p {
            color: rgba(255, 250, 240, 0.82);
            max-width: 660px;
            font-size: clamp(1rem, 1.5vw, 1.12rem);
            line-height: 1.75;
            margin: 1.5rem 0 0;
        }

        .hero-chips {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 1.5rem;
        }

        .hero-chips span {
            font-size: 0.74rem;
            color: rgba(255, 250, 240, 0.78);
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.12);
            padding: 0.32rem 0.65rem;
            border-radius: 999px;
        }

        .button-row { margin-top: -0.15rem; }

        .stButton > button,
        .stDownloadButton > button,
        .stFormSubmitButton > button {
            border-radius: 0.78rem;
            border: 1px solid var(--line);
            background: var(--paper);
            color: var(--ink);
            font-weight: 650;
            padding: 0.55rem 1rem;
            transition: all 0.16s ease;
            box-shadow: none;
        }

        .stButton > button:hover,
        .stDownloadButton > button:hover,
        .stFormSubmitButton > button:hover {
            border-color: var(--forest);
            color: var(--forest);
            transform: translateY(-1px);
            box-shadow: 0 6px 16px rgba(23, 79, 66, 0.10);
        }

        .stButton > button[kind="primary"],
        .stFormSubmitButton > button[kind="primary"] {
            background: var(--forest);
            color: #fffaf0;
            border-color: var(--forest);
        }

        .stButton > button[kind="primary"]:hover,
        .stFormSubmitButton > button[kind="primary"]:hover {
            background: var(--forest-deep);
            color: #fff;
            border-color: var(--forest-deep);
        }

        .stButton > button:focus:not(:active) { border-color: var(--forest); color: var(--forest); }

        [data-testid="stForm"] {
            background: rgba(255, 253, 248, 0.72);
            border: 1px solid var(--line);
            border-radius: 1.15rem;
            padding: 1.2rem 1.25rem;
        }

        [data-testid="stTextArea"] textarea,
        [data-testid="stTextInput"] input {
            border-radius: 0.7rem;
            border-color: #dcd2c2;
            background: #fffdf8;
            line-height: 1.65;
        }

        [data-testid="stTextArea"] textarea:focus,
        [data-testid="stTextInput"] input:focus {
            border-color: var(--forest);
            box-shadow: 0 0 0 1px var(--forest);
        }

        [data-testid="stSelectbox"] > div > div,
        [data-testid="stMultiSelect"] > div > div {
            border-radius: 0.7rem;
            border-color: #dcd2c2;
            background: #fffdf8;
        }

        [data-testid="stTabs"] [data-baseweb="tab-list"] {
            gap: 0.25rem;
            border-bottom: 1px solid var(--line);
        }

        [data-testid="stTabs"] button[data-baseweb="tab"] {
            border-radius: 0.7rem 0.7rem 0 0;
            padding: 0.65rem 1rem;
            color: var(--muted);
            font-weight: 600;
        }

        [data-testid="stTabs"] button[aria-selected="true"] {
            color: var(--forest);
            background: rgba(220, 235, 221, 0.55);
        }

        [data-testid="stMetric"] {
            background: var(--paper);
            border: 1px solid var(--line);
            border-radius: 1rem;
            padding: 1rem 1.1rem;
            box-shadow: 0 6px 18px rgba(37, 62, 53, 0.04);
        }

        [data-testid="stMetricLabel"] { color: var(--muted); }
        [data-testid="stMetricValue"] { color: var(--forest); font-family: Georgia, serif; }

        [data-testid="stProgress"] > div > div > div > div {
            background: linear-gradient(90deg, var(--forest), #5d987c);
            border-radius: 999px;
        }

        .page-head { margin: 0.25rem 0 1.9rem; max-width: 900px; }
        .page-head-row { display: flex; align-items: center; gap: 0.6rem; }
        .page-icon { font-size: 1.15rem; }

        .eyebrow, .page-head .eyebrow {
            color: var(--coral);
            font-size: 0.7rem;
            font-weight: 800;
            letter-spacing: 0.15em;
            text-transform: uppercase;
        }

        .page-head h1 {
            font-family: Georgia, "Times New Roman", serif;
            font-size: clamp(2.1rem, 4.4vw, 3.55rem);
            line-height: 1.06;
            letter-spacing: -0.035em;
            margin: 0.5rem 0 0.65rem;
        }

        .page-head p {
            color: var(--muted);
            font-size: 1.04rem;
            line-height: 1.72;
            margin: 0;
            max-width: 760px;
        }

        .section-heading {
            display: flex;
            align-items: baseline;
            justify-content: space-between;
            gap: 1rem;
            margin: 2.1rem 0 0.9rem;
            border-bottom: 1px solid var(--line);
            padding-bottom: 0.6rem;
        }

        .section-heading h2 {
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.55rem;
            margin: 0;
            letter-spacing: -0.025em;
        }

        .section-heading span { color: var(--muted); font-size: 0.8rem; }

        .stat-strip {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 0.75rem;
            margin: 1rem 0 0.25rem;
        }

        .stat {
            background: rgba(255, 253, 248, 0.9);
            border: 1px solid var(--line);
            border-radius: 1rem;
            padding: 0.95rem 1rem;
        }

        .stat strong {
            display: block;
            color: var(--forest);
            font-family: Georgia, serif;
            font-size: 1.55rem;
            line-height: 1.1;
        }

        .stat span { color: var(--muted); font-size: 0.75rem; }

        .card {
            background: var(--paper);
            border: 1px solid var(--line);
            border-radius: 1.2rem;
            padding: 1.3rem 1.35rem;
            box-shadow: 0 8px 24px rgba(37, 62, 53, 0.045);
            height: 100%;
        }

        .card h3 {
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.25rem;
            line-height: 1.25;
            margin: 0.55rem 0 0.45rem;
        }

        .card p { color: var(--muted); font-size: 0.9rem; line-height: 1.65; margin: 0; }
        .card .card-icon { font-size: 1.4rem; }
        .card .card-kicker { color: var(--coral); font-size: 0.65rem; text-transform: uppercase; letter-spacing: 0.11em; font-weight: 800; }

        .card-dark {
            background: linear-gradient(135deg, #174f42, #286a55);
            color: #fffaf0;
            border: none;
        }

        .card-dark h3, .card-dark p { color: #fffaf0; }
        .card-dark p { color: rgba(255, 250, 240, 0.76); }

        .card-warm {
            background: linear-gradient(135deg, #fff8e8, #fffdf8);
            border-color: #f0dfba;
        }

        .card-list { margin: 0.65rem 0 0; padding: 0; list-style: none; }
        .card-list li {
            color: var(--muted);
            font-size: 0.84rem;
            line-height: 1.55;
            padding: 0.23rem 0;
        }

        .card-list li::before { content: "✓"; color: var(--forest); font-weight: 800; margin-right: 0.45rem; }

        .chip {
            display: inline-block;
            padding: 0.23rem 0.55rem;
            border-radius: 999px;
            font-size: 0.68rem;
            font-weight: 700;
            letter-spacing: 0.02em;
            margin: 0 0.25rem 0.25rem 0;
        }

        .chip-sage { background: var(--sage); color: #1b5b4b; }
        .chip-coral { background: #f9e4dd; color: #a64630; }
        .chip-gold { background: #fff0c9; color: #7d5712; }
        .chip-muted { background: #eee9df; color: #65716d; }

        .path-card { min-height: 225px; }
        .path-card .level-row { display: flex; justify-content: space-between; align-items: center; }
        .path-card .level-icon { font-size: 1.5rem; }
        .path-card h3 { margin-top: 0.7rem; }
        .path-card p { min-height: 3.1rem; }

        .lesson-head {
            background: linear-gradient(128deg, #174f42 0%, #235f4e 68%, #326f5a 100%);
            color: #fffaf0;
            border-radius: 1.3rem;
            padding: 1.6rem 1.7rem;
            margin-bottom: 1.15rem;
            box-shadow: 0 14px 36px rgba(23, 79, 66, 0.13);
        }

        .lesson-head .eyebrow { color: #ffe0a0; }
        .lesson-head h2 {
            color: #fffaf0;
            font-family: Georgia, serif;
            font-size: clamp(1.65rem, 3vw, 2.4rem);
            line-height: 1.12;
            margin: 0.45rem 0 0.4rem;
        }

        .lesson-head p { color: rgba(255, 250, 240, 0.78); margin: 0; font-size: 1rem; }

        .lesson-head .meta { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.9rem; }
        .lesson-head .meta span {
            background: rgba(255, 255, 255, 0.09);
            border: 1px solid rgba(255, 255, 255, 0.13);
            border-radius: 999px;
            padding: 0.24rem 0.55rem;
            font-size: 0.7rem;
            color: rgba(255, 250, 240, 0.8);
        }

        .goal-box {
            background: rgba(220, 235, 221, 0.45);
            border: 1px solid #cfe1d2;
            border-radius: 1.05rem;
            padding: 1.15rem 1.3rem;
            margin-bottom: 0.6rem;
        }

        .goal-box h4 {
            margin: 0 0 0.55rem;
            color: var(--forest);
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.12em;
        }

        .goal-box ul { margin: 0; padding-left: 1.1rem; }
        .goal-box li { color: #315d4d; font-size: 0.91rem; line-height: 1.6; }

        .lesson-section { margin: 1.45rem 0 1.6rem; }
        .lesson-section h3 {
            font-family: Georgia, serif;
            font-size: 1.48rem;
            margin: 0 0 0.5rem;
            letter-spacing: -0.025em;
        }

        .lesson-section p { color: #43564f; line-height: 1.78; margin: 0 0 0.7rem; }

        .example-box {
            background: #fffaf0;
            border-left: 4px solid var(--gold);
            border-radius: 0 0.7rem 0.7rem 0;
            padding: 0.85rem 1rem;
            margin-top: 0.7rem;
        }

        .example-label {
            display: block;
            color: #9a6d1a;
            font-size: 0.65rem;
            font-weight: 800;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-bottom: 0.3rem;
        }

        .example-box ul { margin: 0; padding-left: 1.1rem; }
        .example-box li { color: #4f4a3d; font-size: 0.9rem; line-height: 1.65; margin: 0.15rem 0; }

        .vocab-card {
            background: #fffdf8;
            border: 1px solid var(--line);
            border-radius: 0.9rem;
            padding: 0.85rem 0.95rem;
            min-height: 120px;
            margin-bottom: 0.55rem;
        }

        .vocab-card strong { color: var(--forest); font-size: 0.98rem; }
        .vocab-card span { display: block; color: #68756f; font-size: 0.78rem; line-height: 1.45; margin-top: 0.2rem; }
        .vocab-card em { display: block; color: #8b7050; font-size: 0.76rem; line-height: 1.45; margin-top: 0.35rem; }

        .story-paragraph {
            color: #34473f;
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.08rem;
            line-height: 1.92;
            margin: 0 0 1.05rem;
        }

        .story-title {
            font-family: Georgia, serif;
            font-size: clamp(2rem, 4vw, 2.9rem);
            line-height: 1.1;
            margin: 0.6rem 0 0.5rem;
            letter-spacing: -0.035em;
        }

        .story-meta { color: var(--muted); font-size: 0.8rem; margin-bottom: 1.2rem; }
        .story-intro { color: #63746d; font-style: italic; font-size: 1rem; margin-bottom: 1.5rem; }

        .tool-card {
            background: rgba(220, 235, 221, 0.38);
            border: 1px solid #d5e3d6;
            border-radius: 1rem;
            padding: 1rem 1.05rem;
            margin-bottom: 0.8rem;
        }

        .tool-card h4 {
            color: var(--forest);
            font-size: 0.74rem;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin: 0 0 0.45rem;
        }

        .tool-card ul { margin: 0; padding-left: 1rem; }
        .tool-card li { color: #53675f; font-size: 0.82rem; line-height: 1.55; margin: 0.17rem 0; }

        .glossary-row {
            display: flex;
            gap: 0.65rem;
            border-bottom: 1px solid #eee5d8;
            padding: 0.48rem 0;
            font-size: 0.82rem;
        }

        .glossary-row strong { color: var(--forest); min-width: 100px; }
        .glossary-row span { color: #68756f; }

        .prompt-card {
            background: linear-gradient(135deg, #fff8e8, #fffdf8);
            border: 1px solid #f0dfba;
            border-radius: 1.1rem;
            padding: 1.25rem 1.35rem;
            margin-bottom: 0.8rem;
        }

        .prompt-card h3 { font-family: Georgia, serif; margin: 0.45rem 0 0.4rem; font-size: 1.45rem; }
        .prompt-card p { color: #6b6352; font-size: 0.9rem; margin: 0; line-height: 1.6; }

        .starter-list { margin: 0.6rem 0 0; padding-left: 1.05rem; }
        .starter-list li { color: #6f6249; font-size: 0.84rem; line-height: 1.55; }

        .mini-stats {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 0.5rem;
            margin: 0.8rem 0 0.3rem;
        }

        .mini-stat {
            background: #fffdf8;
            border: 1px solid var(--line);
            border-radius: 0.75rem;
            padding: 0.6rem 0.7rem;
        }

        .mini-stat strong { display: block; color: var(--forest); font-family: Georgia, serif; font-size: 1.18rem; }
        .mini-stat span { color: var(--muted); font-size: 0.65rem; }

        .tip-card {
            background: #fffdf8;
            border: 1px solid var(--line);
            border-radius: 1rem;
            padding: 1rem 1.1rem;
            margin-bottom: 0.6rem;
        }

        .tip-card h4 { margin: 0.3rem 0; font-size: 1rem; }
        .tip-card p { color: var(--muted); font-size: 0.86rem; line-height: 1.62; }
        .tip-example {
            background: #f8f3e9;
            border-radius: 0.6rem;
            padding: 0.55rem 0.7rem;
            color: #5f5a4d;
            font-size: 0.78rem;
            line-height: 1.55;
            white-space: pre-wrap;
        }

        .flash-card {
            background: linear-gradient(135deg, #174f42, #2a6a55);
            color: #fffaf0;
            border-radius: 1.4rem;
            min-height: 285px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 2rem;
            box-shadow: 0 18px 40px rgba(23, 79, 66, 0.16);
            position: relative;
            overflow: hidden;
        }

        .flash-card::after {
            content: "";
            position: absolute;
            width: 220px;
            height: 220px;
            border-radius: 50%;
            background: rgba(228, 173, 69, 0.12);
            right: -80px;
            top: -90px;
        }

        .flash-card .flash-cat {
            color: #ffe0a0;
            font-size: 0.66rem;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            font-weight: 800;
            z-index: 1;
        }

        .flash-card .flash-word {
            font-family: Georgia, serif;
            font-size: clamp(2.4rem, 6vw, 4.2rem);
            line-height: 1.05;
            margin: 0.5rem 0 0.25rem;
            color: #fffaf0;
            z-index: 1;
        }

        .flash-card .flash-pron { color: #b9d6c4; font-size: 0.86rem; z-index: 1; }
        .flash-card .flash-reveal { margin-top: 1.15rem; z-index: 1; max-width: 530px; }
        .flash-card .flash-reveal p { color: #fffaf0; font-size: 1rem; line-height: 1.6; margin: 0.25rem 0; }
        .flash-card .flash-reveal em { color: #d9e8df; font-size: 0.88rem; }
        .flash-card .flash-hidden { color: rgba(255, 250, 240, 0.58); font-size: 0.82rem; margin-top: 1.2rem; z-index: 1; }

        .quiz-result-box {
            border-radius: 1rem;
            padding: 1rem 1.15rem;
            background: #f4f9f4;
            border: 1px solid #d3e5d5;
            margin: 0.8rem 0;
        }

        .quiz-result-box h4 { margin: 0 0 0.3rem; color: var(--forest); }
        .quiz-result-box p { margin: 0; color: #53675f; font-size: 0.9rem; }

        .journal-entry {
            border-left: 3px solid var(--sage-mid);
            padding: 0.2rem 0 0.2rem 0.9rem;
            margin: 0.7rem 0;
        }

        .journal-entry .journal-meta { color: var(--muted); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.08em; }
        .journal-entry h4 { margin: 0.25rem 0 0.35rem; font-family: Georgia, serif; }
        .journal-entry p { color: #4d5e57; font-size: 0.88rem; line-height: 1.65; white-space: pre-wrap; }

        .badge-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.7rem;
            margin-top: 0.7rem;
        }

        .badge-card {
            border: 1px solid var(--line);
            border-radius: 1rem;
            padding: 0.95rem 1rem;
            background: #fffdf8;
            display: flex;
            gap: 0.75rem;
            align-items: flex-start;
            min-height: 96px;
        }

        .badge-card.earned {
            background: linear-gradient(135deg, #fff8e8, #fffdf8);
            border-color: #eddaaf;
        }

        .badge-card.locked { opacity: 0.58; filter: grayscale(0.65); }
        .badge-icon { font-size: 1.55rem; line-height: 1; }
        .badge-card strong { font-size: 0.88rem; display: block; color: var(--ink); }
        .badge-card span { display: block; color: var(--muted); font-size: 0.72rem; line-height: 1.45; margin-top: 0.15rem; }

        .activity-row {
            display: flex;
            gap: 0.7rem;
            align-items: flex-start;
            padding: 0.6rem 0;
            border-bottom: 1px solid #eee7dc;
        }

        .activity-row:last-child { border-bottom: none; }
        .activity-row .activity-icon { font-size: 1rem; }
        .activity-row .activity-text { color: #485a52; font-size: 0.86rem; line-height: 1.45; }
        .activity-row .activity-time { color: #8b9791; font-size: 0.67rem; margin-left: auto; white-space: nowrap; }

        .note-card {
            background: #fff8e8;
            border: 1px solid #f0dfba;
            border-radius: 1.2rem;
            padding: 1.4rem 1.55rem;
            position: relative;
        }

        .note-card .quote-mark {
            font-family: Georgia, serif;
            font-size: 3rem;
            line-height: 0.7;
            color: #d9b36b;
            display: block;
            margin-bottom: 0.3rem;
        }

        .note-card p { font-family: Georgia, serif; font-size: 1.07rem; line-height: 1.75; color: #4f4a3d; font-style: italic; }
        .note-card .signature { color: #8b6c36; font-size: 0.78rem; letter-spacing: 0.08em; text-transform: uppercase; font-weight: 700; }

        .week-grid {
            display: grid;
            grid-template-columns: repeat(7, minmax(0, 1fr));
            gap: 0.45rem;
            margin-top: 0.65rem;
        }

        .week-day {
            background: #fffdf8;
            border: 1px solid var(--line);
            border-radius: 0.8rem;
            padding: 0.7rem 0.65rem;
            min-height: 108px;
        }

        .week-day strong { color: var(--coral); font-size: 0.64rem; letter-spacing: 0.08em; text-transform: uppercase; }
        .week-day p { color: #586861; font-size: 0.75rem; line-height: 1.45; margin: 0.25rem 0 0; }

        .footer {
            margin-top: 3rem;
            padding-top: 1.2rem;
            border-top: 1px solid var(--line);
            color: #89938e;
            font-size: 0.72rem;
            line-height: 1.6;
            text-align: center;
        }

        .footer strong { color: #5c6d65; }

        .stAlert { border-radius: 0.9rem; }

        @media (max-width: 900px) {
            .stat-strip, .mini-stats { grid-template-columns: repeat(2, minmax(0, 1fr)); }
            .badge-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
            .week-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
            .hero { padding: 2.2rem 1.5rem; border-radius: 1.3rem; }
            .hero h1 { font-size: 2.55rem; }
        }

        @media (max-width: 560px) {
            .block-container { padding-left: 1rem; padding-right: 1rem; }
            .stat-strip, .mini-stats, .badge-grid { grid-template-columns: 1fr; }
            .week-grid { grid-template-columns: 1fr; }
            .hero h1 { font-size: 2.15rem; }
            .hero h1 span { font-size: 0.58em; }
            .page-head h1 { font-size: 2rem; }
        }
        """
        + size_rule
        + """
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar() -> None:
    with st.sidebar:
        st.markdown(
            """
            <div class="side-brand">
                <div class="side-mark">J</div>
                <div class="side-title">Jessica's<br>English Guide</div>
            </div>
            <p class="side-tagline">For students and adults of all ages.<br>Start from zero. Grow with confidence.</p>
            <div class="side-label">Your learning space</div>
            """,
            unsafe_allow_html=True,
        )
        st.radio("Navigation", PAGES, key="page", label_visibility="collapsed")

        percent = journey_percent()
        st.markdown(
            f"""
            <div class="side-progress">
                <div class="side-progress-top"><span>Your journey</span><strong>{percent}%</strong></div>
            """,
            unsafe_allow_html=True,
        )
        st.progress(percent / 100)
        st.markdown(
            f"""
                <div class="side-progress-caption">{len(st.session_state.completed_lessons)} of {len(LESSONS)} lessons · {len(st.session_state.completed_readings)} of {len(READINGS)} stories</div>
            </div>
            <div class="side-label">Reading comfort</div>
            """,
            unsafe_allow_html=True,
        )
        st.toggle("Larger text", key="large_text")
        st.caption("Progress is saved for this browser session. Download a report from My Progress any time.")
        st.markdown(
            """
            <div class="side-footer">
                Free · Self-paced · No sign-in needed<br>
                A practice companion for curious learners of every age.
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_footer() -> None:
    st.markdown(
        f"""
        <div class="footer">
            <strong>{safe(SITE_NAME)}</strong><br>
            Learn at your own pace. Practise a little, often, and be kind to yourself.<br>
            This guide supports practice; it does not replace a qualified teacher or formal assessment.
        </div>
        """,
        unsafe_allow_html=True,
    )
