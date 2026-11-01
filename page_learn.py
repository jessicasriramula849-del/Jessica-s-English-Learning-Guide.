"""Lesson library and interactive lesson reader."""

import streamlit as st

from content import LESSONS, LEVEL_DETAILS, LEVELS
from core import (
    chip,
    linked_selectbox,
    log_activity,
    page_header,
    safe,
    section_heading,
)


def _select_lesson(lesson_id: str) -> None:
    st.session_state.learn_level = "All levels"
    st.session_state.selected_lesson = lesson_id


def _toggle_lesson(lesson_id: str, lesson_title: str) -> None:
    completed = st.session_state.completed_lessons
    if lesson_id in completed:
        completed.remove(lesson_id)
    else:
        completed.add(lesson_id)
        log_activity("📚", f"Completed the lesson “{lesson_title}”.")


def _format_lesson(lesson_id: str) -> str:
    index = next(i for i, item in enumerate(LESSONS, 1) if item["id"] == lesson_id)
    lesson = next(item for item in LESSONS if item["id"] == lesson_id)
    mark = " ✓" if lesson_id in st.session_state.completed_lessons else ""
    return f"{index:02d}. {lesson['title']} · {lesson['level']}{mark}"


def render_learn() -> None:
    page_header(
        "Guided lessons",
        "Learn English, one clear step at a time",
        "Sixteen lessons take you from the alphabet to confident expression. Each lesson explains one idea, shows real examples, gives you useful words, and finishes with a gentle check.",
        "📚",
    )

    # A compact level overview.
    overview = st.columns(4)
    for col, level in zip(overview, LEVELS):
        with col:
            details = LEVEL_DETAILS[level]
            done = sum(
                1 for item in LESSONS if item["level"] == level and item["id"] in st.session_state.completed_lessons
            )
            total = sum(1 for item in LESSONS if item["level"] == level)
            st.markdown(
                f"""
                <div class="card" style="padding:0.95rem 1rem">
                    <div class="card-kicker">{safe(level)}</div>
                    <h3 style="font-size:1.02rem;margin:0.3rem 0 0.15rem">{details["icon"]} {safe(details["label"])}</h3>
                    <p style="font-size:0.72rem">{done} of {total} complete</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    section_heading("Open a lesson", "Choose by level or follow the full sequence")
    selector_left, selector_right = st.columns([1, 2.2])
    with selector_left:
        level = st.selectbox("Level", ["All levels"] + LEVELS, key="learn_level")

    candidates = [item["id"] for item in LESSONS if level == "All levels" or item["level"] == level]
    if not candidates:
        candidates = [LESSONS[0]["id"]]
    if st.session_state.selected_lesson not in candidates:
        st.session_state.selected_lesson = candidates[0]

    with selector_right:
        lesson_id = linked_selectbox(
            "Lesson",
            candidates,
            state_key="selected_lesson",
            widget_key="_lesson_picker_label",
            label_fn=_format_lesson,
            help_text="Lessons build in order, but you may start anywhere that feels right.",
        )

    lesson = next(item for item in LESSONS if item["id"] == lesson_id)
    lesson_number = next(i for i, item in enumerate(LESSONS, 1) if item["id"] == lesson_id)
    is_complete = lesson_id in st.session_state.completed_lessons

    st.markdown(
        f"""
        <div class="lesson-head">
            <div class="eyebrow">{safe(lesson["level"])} · Lesson {lesson_number:02d} of {len(LESSONS)}</div>
            <h2>{safe(lesson["title"])}</h2>
            <p>{safe(lesson["subtitle"])}</p>
            <div class="meta">
                <span>⏱ {lesson["minutes"]} minutes</span>
                <span>{'✓ Completed' if is_complete else 'Self-paced'}</span>
                <span>{len(lesson["vocab"])} words to keep</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    goals_html = "".join(f"<li>{safe(goal)}</li>" for goal in lesson["goals"])
    st.markdown(
        f"""
        <div class="goal-box">
            <h4>By the end, you will be able to</h4>
            <ul>{goals_html}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption("Read slowly. There is no timer. If a sentence is unclear, read it aloud once and then read it again.")

    # Lesson body -----------------------------------------------------
    for block in lesson["sections"]:
        examples = "".join(f"<li>{safe(example)}</li>" for example in block["examples"])
        st.markdown(
            f"""
            <div class="lesson-section">
                <h3>{safe(block["heading"])}</h3>
                <p>{safe(block["body"])}</p>
                <div class="example-box">
                    <span class="example-label">See it in action</span>
                    <ul>{examples}</ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Vocabulary ------------------------------------------------------
    st.markdown("#### Words to keep")
    vocab_cols = st.columns(min(3, len(lesson["vocab"])))
    for index, word in enumerate(lesson["vocab"]):
        with vocab_cols[index % len(vocab_cols)]:
            st.markdown(
                f"""
                <div class="vocab-card">
                    <strong>{safe(word["word"])}</strong>
                    <span>{safe(word["meaning"])}</span>
                    <em>{safe(word["example"])}</em>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # Quick check -----------------------------------------------------
    section_heading("A gentle check", "One question · no penalty")
    check = lesson["check"]
    form_key = f"lesson_check_form_{lesson_id}"
    with st.form(form_key):
        answer = st.radio(
            check["question"],
            check["options"],
            index=None,
            key=f"lesson_radio_{lesson_id}",
        )
        submitted = st.form_submit_button("Check my answer")

    if submitted:
        if answer is None:
            st.warning("Choose an answer first, then check it. Guessing is a useful part of learning.")
        else:
            correct = answer == check["options"][check["answer"]]
            st.session_state[f"lesson_result_{lesson_id}"] = {
                "selected": answer,
                "correct": correct,
            }

    result = st.session_state.get(f"lesson_result_{lesson_id}")
    if result:
        if result["correct"]:
            st.success(f"**Yes — that is right.** {check['explanation']}")
        else:
            st.error(
                f"**Not quite yet.** The correct answer is **{check['options'][check['answer']]}**. {check['explanation']}"
            )

    # Completion controls --------------------------------------------
    st.write("")
    nav_left, nav_mid, nav_right = st.columns([1, 1.2, 1])
    with nav_left:
        if lesson_number > 1:
            previous = LESSONS[lesson_number - 2]
            st.button(
                "← Previous lesson",
                use_container_width=True,
                on_click=_select_lesson,
                args=(previous["id"],),
            )
        else:
            st.button("← Previous lesson", disabled=True, use_container_width=True)
    with nav_mid:
        st.button(
            "✓ Lesson complete" if not is_complete else "Completed — undo",
            type="primary" if not is_complete else "secondary",
            use_container_width=True,
            on_click=_toggle_lesson,
            args=(lesson_id, lesson["title"]),
        )
    with nav_right:
        if lesson_number < len(LESSONS):
            nxt = LESSONS[lesson_number]
            st.button(
                "Next lesson →",
                use_container_width=True,
                on_click=_select_lesson,
                args=(nxt["id"],),
            )
        else:
            st.button("Next lesson →", disabled=True, use_container_width=True)

    if is_complete:
        st.success("This lesson is marked complete. You can always come back for a second look.")

    # Full lesson map -------------------------------------------------
    with st.expander("See the full lesson map"):
        map_cols = st.columns(4)
        for col, level_name in zip(map_cols, LEVELS):
            with col:
                rows = []
                for index, item in enumerate(LESSONS, 1):
                    if item["level"] == level_name:
                        mark = "✅" if item["id"] in st.session_state.completed_lessons else "○"
                        rows.append(f"<div style='font-size:0.78rem;line-height:1.5;margin:0.3rem 0'>{mark} {index:02d}. {safe(item['title'])}</div>")
                st.markdown(
                    f"<div class='card' style='padding:0.9rem 1rem'><div class='card-kicker'>{safe(level_name)}</div>{''.join(rows)}</div>",
                    unsafe_allow_html=True,
                )

    st.info(
        "A useful habit: after each lesson, say or write two sentences of your own using the new language. "
        "Production is what turns understanding into confidence."
    )
