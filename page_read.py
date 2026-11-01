"""Graded reading library."""

import re

import streamlit as st

from content import READINGS, LEVELS
from core import (
    linked_selectbox,
    log_activity,
    page_header,
    safe,
    section_heading,
)


def _select_reading(reading_id: str) -> None:
    st.session_state.reading_level = "All levels"
    st.session_state.selected_reading = reading_id


def _toggle_reading(reading_id: str, title: str) -> None:
    completed = st.session_state.completed_readings
    if reading_id in completed:
        completed.remove(reading_id)
    else:
        completed.add(reading_id)
        log_activity("📖", f"Finished reading “{title}”.")


def _format_reading(reading_id: str) -> str:
    story = next(item for item in READINGS if item["id"] == reading_id)
    mark = " ✓" if reading_id in st.session_state.completed_readings else ""
    return f"{story['title']} · {story['level']}{mark}"


def _word_count(story: dict) -> int:
    text = " ".join(story["paragraphs"])
    return len(re.findall(r"[A-Za-z']+", text))


def render_read() -> None:
    page_header(
        "Reading room",
        "Read stories that meet you where you are",
        "Eight original stories grow with you, from a first day at school to reading between the lines. Each one includes a glossary, a short reading toolkit, and three comprehension questions.",
        "📖",
    )

    selector_left, selector_right = st.columns([1, 2.2])
    with selector_left:
        level = st.selectbox("Level", ["All levels"] + LEVELS, key="reading_level")

    candidates = [item["id"] for item in READINGS if level == "All levels" or item["level"] == level]
    if not candidates:
        candidates = [READINGS[0]["id"]]
    if st.session_state.selected_reading not in candidates:
        st.session_state.selected_reading = candidates[0]

    with selector_right:
        reading_id = linked_selectbox(
            "Story",
            candidates,
            state_key="selected_reading",
            widget_key="_reading_picker_label",
            label_fn=_format_reading,
            help_text="Stories are graded, but curiosity is a good reason to choose any of them.",
        )

    story = next(item for item in READINGS if item["id"] == reading_id)
    is_complete = reading_id in st.session_state.completed_readings
    questions = story["questions"]

    st.markdown(
        f"""
        <div class="eyebrow">{safe(story["level"])} · {safe(story["focus"])}</div>
        <div class="story-title">{safe(story["title"])}</div>
        <div class="story-meta">{story["minutes"]} minute read · {_word_count(story)} words · {len(story["glossary"])} glossary words</div>
        <div class="story-intro">{safe(story["intro"])}</div>
        """,
        unsafe_allow_html=True,
    )

    story_col, toolkit_col = st.columns([2.15, 1])

    with story_col:
        for paragraph in story["paragraphs"]:
            st.markdown(
                f"<p class='story-paragraph'>{safe(paragraph)}</p>",
                unsafe_allow_html=True,
            )

        with st.expander("Glossary — words from this story", expanded=False):
            for word in story["glossary"]:
                st.markdown(
                    f"<div class='glossary-row'><strong>{safe(word['word'])}</strong><span>{safe(word['meaning'])}</span></div>",
                    unsafe_allow_html=True,
                )

    with toolkit_col:
        st.markdown(
            """
            <div class="tool-card">
                <h4>Before you read</h4>
                <ul>
                    <li>Read the title and introduction. What do you expect?</li>
                    <li>Choose a quiet moment. You do not need to finish quickly.</li>
                    <li>Keep the glossary closed at first. Let context help you.</li>
                </ul>
            </div>
            <div class="tool-card">
                <h4>While you read</h4>
                <ul>
                    <li>Read one paragraph at a time.</li>
                    <li>Do not stop at every unknown word. Guess, then check.</li>
                    <li>Read a difficult sentence aloud, slowly.</li>
                </ul>
            </div>
            <div class="tool-card">
                <h4>After you read</h4>
                <ul>
                    <li>Say the main idea in one sentence.</li>
                    <li>Choose one new word and write your own example.</li>
                    <li>Answer the questions without looking back first.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Comprehension ---------------------------------------------------
    section_heading("Did you understand?", "Three questions · answers explained")
    with st.form(f"reading_questions_{reading_id}"):
        for index, question in enumerate(questions, 1):
            st.markdown(f"**{index}. {question['question']}**")
            st.radio(
                f"Answer for question {index}",
                question["options"],
                index=None,
                key=f"reading_answer_{reading_id}_{index}",
                label_visibility="collapsed",
            )
        submitted = st.form_submit_button("Check my answers")

    if submitted:
        answers = [st.session_state.get(f"reading_answer_{reading_id}_{index}") for index in range(1, len(questions) + 1)]
        score = sum(1 for question, answer in zip(questions, answers) if answer == question["options"][question["answer"]])
        st.session_state[f"reading_result_{reading_id}"] = {
            "answers": answers,
            "score": score,
        }

    result = st.session_state.get(f"reading_result_{reading_id}")
    if result:
        score = result["score"]
        if score == len(questions):
            st.success(f"**{score} of {len(questions)} correct.** You read carefully and understood the whole story.")
        elif score >= 2:
            st.info(f"**{score} of {len(questions)} correct.** You caught the main ideas. Read the explanations below, then try the story once more.")
        else:
            st.warning(f"**{score} of {len(questions)} correct.** Reading slowly and checking the glossary will help. There is no penalty for trying again.")

        for index, (question, answer) in enumerate(zip(questions, result["answers"]), 1):
            if answer == question["options"][question["answer"]]:
                st.markdown(f"✅ **{index}. {question['question']}** — {question['options'][question['answer']]}")
            else:
                chosen = answer if answer is not None else "No answer chosen"
                st.markdown(
                    f"❌ **{index}. {question['question']}** — Your answer: {chosen}. "
                    f"Correct answer: **{question['options'][question['answer']]}**."
                )
            st.caption(question["explanation"])

    # Completion ------------------------------------------------------
    st.write("")
    left, mid, right = st.columns([1, 1.2, 1])
    with left:
        story_index = next(i for i, item in enumerate(READINGS) if item["id"] == reading_id)
        if story_index > 0:
            previous = READINGS[story_index - 1]
            st.button(
                "← Previous story",
                key="reading_prev",
                use_container_width=True,
                on_click=_select_reading,
                args=(previous["id"],),
            )
        else:
            st.button("← Previous story", key="reading_prev_disabled", disabled=True, use_container_width=True)
    with mid:
        st.button(
            "✓ I finished this story" if not is_complete else "Finished — undo",
            key="reading_complete",
            type="primary" if not is_complete else "secondary",
            use_container_width=True,
            on_click=_toggle_reading,
            args=(reading_id, story["title"]),
        )
    with right:
        if story_index < len(READINGS) - 1:
            nxt = READINGS[story_index + 1]
            st.button(
                "Next story →",
                key="reading_next",
                use_container_width=True,
                on_click=_select_reading,
                args=(nxt["id"],),
            )
        else:
            st.button("Next story →", key="reading_next_disabled", disabled=True, use_container_width=True)

    if is_complete:
        st.success("This story is marked as read. Rereading is one of the best ways to build fluency.")

    with st.expander("See all stories"):
        for item in READINGS:
            mark = "✅" if item["id"] in st.session_state.completed_readings else "○"
            st.markdown(
                f"{mark} **{item['title']}** · **{item['level']}** · {item['minutes']} min — *{item['focus']}*"
            )
