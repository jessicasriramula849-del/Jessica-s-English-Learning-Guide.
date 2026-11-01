"""Writing studio with prompts, checks, and a personal notebook."""

from __future__ import annotations

import re
from collections import Counter
from datetime import datetime

import streamlit as st

from content import LEVELS, WRITING_PROMPTS, WRITING_TIPS
from core import (
    chip,
    linked_selectbox,
    log_activity,
    page_header,
    safe,
    section_heading,
)

STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "if", "then", "that", "this", "these", "those",
    "is", "are", "was", "were", "be", "been", "being", "am", "i", "you", "he", "she", "it",
    "we", "they", "me", "my", "your", "his", "her", "its", "our", "their", "to", "of", "in",
    "on", "at", "for", "with", "from", "by", "as", "not", "no", "do", "does", "did", "have",
    "has", "had", "will", "would", "can", "could", "should", "there", "here", "so", "very",
    "just", "about", "into", "also", "because", "when", "what", "which", "who", "how",
}


def _words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", text)


def _sentences(text: str) -> list[str]:
    return [part.strip() for part in re.findall(r"[^.!?]+(?:[.!?]+|$)", text) if part.strip()]


def _paragraphs(text: str) -> list[str]:
    return [part.strip() for part in re.split(r"\n\s*\n", text.strip()) if part.strip()]


def _open_prompt(prompt_id: str) -> None:
    st.session_state.writing_level = "All levels"
    st.session_state.selected_prompt = prompt_id


def _select_prompt(prompt_id: str) -> None:
    st.session_state.selected_prompt = prompt_id


def _format_prompt(prompt_id: str) -> str:
    prompt = next(item for item in WRITING_PROMPTS if item["id"] == prompt_id)
    return f"{prompt['title']} · {prompt['level']}"


def stats_for(text: str) -> dict:
    words = _words(text)
    sentences = _sentences(text)
    paragraphs = _paragraphs(text)
    total_words = len(words)
    return {
        "words": total_words,
        "sentences": len(sentences),
        "paragraphs": len(paragraphs),
        "avg_sentence": round(total_words / max(len(sentences), 1), 1),
        "characters": len(text),
    }


def analyse_writing(text: str, target: int) -> dict:
    words = _words(text)
    sentences = _sentences(text)
    paragraphs = _paragraphs(text)
    total = len(words)
    lower_words = [word.lower() for word in words]
    unique_ratio = len(set(lower_words)) / max(total, 1)
    capitalized = sum(1 for sentence in sentences if sentence.strip()[:1].isupper())
    cap_ratio = capitalized / max(len(sentences), 1)
    ending = text.strip()[-1:] in {".", "!", "?"}
    link_words = [
        "and", "but", "because", "so", "although", "however", "first", "then", "finally",
        "also", "therefore", "while", "when", "if", "after", "before", "for example",
    ]
    links_used = sorted({word for word in link_words if re.search(rf"\b{re.escape(word)}\b", text.lower())})
    counts = Counter(
        word for word in lower_words if word not in STOP_WORDS and len(word) > 3
    )
    repeated = [(word, count) for word, count in counts.most_common(3) if count >= 4]

    if total == 0:
        ideas = 0
    elif total >= target * 0.75:
        ideas = 4
    elif total >= target * 0.5:
        ideas = 3
    elif total >= 20:
        ideas = 2
    else:
        ideas = 1

    if len(paragraphs) >= 3:
        organization = 4
    elif len(paragraphs) == 2:
        organization = 3
    elif total >= 60:
        organization = 2
    else:
        organization = 1

    if unique_ratio >= 0.58:
        word_choice = 4
    elif unique_ratio >= 0.48:
        word_choice = 3
    elif unique_ratio >= 0.36:
        word_choice = 2
    else:
        word_choice = 1

    if cap_ratio >= 0.85 and ending:
        conventions = 4
    elif cap_ratio >= 0.6 and ending:
        conventions = 3
    elif cap_ratio >= 0.4 or ending:
        conventions = 2
    else:
        conventions = 1

    total_score = ideas + organization + word_choice + conventions
    strengths = []
    next_steps = []

    if total >= target * 0.75:
        strengths.append(f"You reached a useful length ({total} words against a {target}-word target).")
    elif total == 0:
        next_steps.append("Begin with one sentence. Perfection is not the first step; a first sentence is.")
    else:
        next_steps.append(f"You have {total} words. Add a little more detail to move toward the {target}-word target.")

    if len(paragraphs) >= 2:
        strengths.append("Your ideas are divided into paragraphs, which helps a reader follow them.")
    elif total > 30:
        next_steps.append("Try splitting the draft into two paragraphs: one for your main idea and one for detail or example.")

    if links_used:
        strengths.append("You used linking words such as " + ", ".join(links_used[:5]) + " to connect ideas.")
    elif total > 30:
        next_steps.append("Add one or two linking words (because, but, so, however, then) to show how ideas connect.")

    if cap_ratio >= 0.85:
        strengths.append("Most or all of your sentences begin with a capital letter.")
    elif sentences:
        next_steps.append(f"{capitalized} of {len(sentences)} sentences begin with a capital letter. Check the rest.")

    if ending:
        strengths.append("Your draft ends with clear punctuation.")
    else:
        next_steps.append("Finish the final sentence with a full stop, question mark, or exclamation mark.")

    if len(sentences) and total / max(len(sentences), 1) > 25:
        next_steps.append("Some sentences may be long. Read the draft aloud and split any sentence that loses its way.")
    elif sentences:
        strengths.append("Your average sentence length is comfortable for a reader.")

    if repeated:
        word, count = repeated[0]
        if count >= 5:
            next_steps.append(f"You use “{word}” {count} times. Where possible, vary the wording.")
    else:
        strengths.append("Your word choice is varied; no common word is heavily repeated.")

    if not next_steps:
        next_steps.append("Read your draft aloud. Then check one small thing: a missing word, a plural, or a capital letter.")
    if not strengths:
        strengths.append("You have made a start. Even a few sentences are a real step forward.")

    return {
        "words": total,
        "sentences": len(sentences),
        "paragraphs": len(paragraphs),
        "avg_sentence": round(total / max(len(sentences), 1), 1),
        "unique_ratio": round(unique_ratio, 2),
        "links": links_used,
        "repeated": repeated,
        "rubric": {
            "Ideas & detail": ideas,
            "Structure": organization,
            "Word choice": word_choice,
            "Conventions": conventions,
        },
        "total_score": total_score,
        "percent": round(total_score / 16 * 100),
        "strengths": strengths,
        "next_steps": next_steps[:4],
    }


def _show_analysis(analysis: dict, target: int) -> None:
    st.markdown(
        f"""
        <div class="quiz-result-box">
            <h4>Practice check · {analysis["percent"]}%</h4>
            <p>{analysis["words"]} words · {analysis["sentences"]} sentences · {analysis["paragraphs"]} paragraph(s) · average sentence: {analysis["avg_sentence"]} words</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(min(analysis["percent"] / 100, 1.0))

    columns = st.columns(4)
    for col, (label, score) in zip(columns, analysis["rubric"].items()):
        with col:
            st.markdown(
                f"""
                <div class="mini-stat">
                    <strong>{score}/4</strong>
                    <span>{safe(label)}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("**What is working**")
    for item in analysis["strengths"]:
        st.success(item)

    st.markdown("**Try this next**")
    for item in analysis["next_steps"]:
        st.info(item)

    st.caption(
        "This is a practice guide, not a complete grammar or spelling checker. It looks at length, structure, "
        "capitalisation, punctuation and variety. Always trust your own reading and, when possible, ask a teacher or fluent friend for feedback."
    )


def _save_draft(prompt: dict, text: str, analysis: dict | None) -> None:
    if not text.strip():
        st.warning("Write a few words before saving. Even one sentence is a beginning.")
        return
    entries = st.session_state.writing_entries
    if entries and entries[-1].get("prompt_id") == prompt["id"] and entries[-1].get("text") == text:
        st.info("This version is already saved in your notebook.")
        return
    entries.append(
        {
            "prompt_id": prompt["id"],
            "title": prompt["title"],
            "level": prompt["level"],
            "text": text,
            "words": len(_words(text)),
            "date": datetime.now().strftime("%B %d, %Y · %I:%M %p"),
            "analysis": analysis,
        }
    )
    log_activity("✍️", f"Saved a draft for “{prompt['title']}”.")
    st.success("Saved to your notebook. You can return to it whenever you like.")


def render_write() -> None:
    page_header(
        "Writing studio",
        "Write English with a little guidance and no fear",
        "Start with a sentence. Build a paragraph. Shape an opinion. Every prompt includes a scenario, sentence starters, a model answer and a friendly practice check. Your words stay yours.",
        "✍️",
    )

    prompt_tab, toolkit_tab, notebook_tab = st.tabs(["✍️ Daily writing", "🧰 Writing toolkit", "📓 My notebook"])

    with prompt_tab:
        selector_left, selector_right = st.columns([1, 2.2])
        with selector_left:
            level = st.selectbox("Level", ["All levels"] + LEVELS, key="writing_level")
        candidates = [
            item["id"] for item in WRITING_PROMPTS if level == "All levels" or item["level"] == level
        ]
        if not candidates:
            candidates = [WRITING_PROMPTS[0]["id"]]
        if st.session_state.selected_prompt not in candidates:
            st.session_state.selected_prompt = candidates[0]
        with selector_right:
            prompt_id = linked_selectbox(
                "Prompt",
                candidates,
                state_key="selected_prompt",
                widget_key="_prompt_picker_label",
                label_fn=_format_prompt,
                help_text="Choose a prompt that feels useful today. You can return to any of them later.",
            )

        prompt = next(item for item in WRITING_PROMPTS if item["id"] == prompt_id)
        target = prompt["target"]

        instructions = "".join(f"<li>{safe(item)}</li>" for item in prompt["instructions"])
        starters = "".join(f"<li>{safe(item)}</li>" for item in prompt["starters"])
        checklist = "".join(f"<li>{safe(item)}</li>" for item in prompt["checklist"])
        st.markdown(
            f"""
            <div class="prompt-card">
                <div>{chip(prompt["level"], "sage")}{chip(prompt["kind"], "gold")}{chip(f"About {target} words", "muted")}</div>
                <h3>{safe(prompt["title"])}</h3>
                <p>{safe(prompt["scenario"])}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        write_col, guide_col = st.columns([1.65, 1])
        with write_col:
            st.markdown("#### Your draft")
            text = st.text_area(
                "Write here",
                key=f"draft_{prompt_id}",
                height=330,
                placeholder="Start with one sentence. You can revise it as many times as you like.",
                label_visibility="collapsed",
            )

            live = stats_for(text)
            st.markdown(
                f"""
                <div class="mini-stats">
                    <div class="mini-stat"><strong>{live["words"]}</strong><span>words</span></div>
                    <div class="mini-stat"><strong>{live["sentences"]}</strong><span>sentences</span></div>
                    <div class="mini-stat"><strong>{live["paragraphs"]}</strong><span>paragraphs</span></div>
                    <div class="mini-stat"><strong>{live["avg_sentence"]}</strong><span>avg. sentence</span></div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if live["words"] and live["words"] < target * 0.6:
                st.caption(f"Aim for about {target} words. You have {live['words']} — add one more detail or example.")
            elif live["words"] > target * 1.5:
                st.caption(f"This is longer than the {target}-word target, which is fine. Check whether every paragraph earns its place.")

            action_a, action_b = st.columns(2)
            with action_a:
                check_clicked = st.button(
                    "Check my writing",
                    key=f"check_button_{prompt_id}",
                    type="primary",
                    use_container_width=True,
                )
            with action_b:
                save_clicked = st.button(
                    "Save to notebook",
                    key=f"save_button_{prompt_id}",
                    use_container_width=True,
                )

            stored = st.session_state.get(f"writing_check_{prompt_id}")
            if check_clicked:
                if not text.strip():
                    st.warning("Write at least one sentence before checking. One sentence is enough to begin.")
                else:
                    stored = {"text": text, "analysis": analyse_writing(text, target)}
                    st.session_state[f"writing_check_{prompt_id}"] = stored

            if save_clicked:
                analysis = stored["analysis"] if stored and stored.get("text") == text else None
                _save_draft(prompt, text, analysis)

            if stored:
                if stored["text"] != text:
                    st.caption("This feedback is from your last check. Run the check again after your edits.")
                section_heading("Your practice check", "Encouraging, practical feedback")
                _show_analysis(stored["analysis"], target)

            if text.strip():
                st.download_button(
                    "Download this draft",
                    data=text,
                    file_name=f"{prompt_id}_draft.txt",
                    mime="text/plain",
                    key=f"download_{prompt_id}",
                )

        with guide_col:
            st.markdown(
                f"""
                <div class="tool-card">
                    <h4>Your task</h4>
                    <ul>{instructions}</ul>
                </div>
                <div class="tool-card">
                    <h4>Sentence starters</h4>
                    <ul class="starter-list">{starters}</ul>
                </div>
                <div class="tool-card">
                    <h4>Before you save</h4>
                    <ul>{checklist}</ul>
                </div>
                """,
                unsafe_allow_html=True,
            )
            with st.expander("See a model answer"):
                st.write(prompt["model"])
                st.caption("A model is an example, not a script. Borrow the structure, not the personal details.")

        with st.expander("Try another prompt at this level"):
            others = [item for item in WRITING_PROMPTS if item["id"] != prompt_id and (level == "All levels" or item["level"] == level)]
            if others:
                for item in others[:4]:
                    st.button(
                        f"{item['title']} · {item['level']}",
                        key=f"alt_prompt_{item['id']}",
                        on_click=_select_prompt,
                        args=(item["id"],),
                    )
            else:
                st.caption("Change the level selector above to see more prompts.")

    with toolkit_tab:
        st.markdown(
            """
            <div class="card" style="background:rgba(220,235,221,0.4);margin-bottom:1rem">
                <div class="card-kicker">Reference shelf</div>
                <h3 style="font-size:1.35rem">Six tools you can use in any draft</h3>
                <p>Good writing is not a mystery. It is a set of small, learnable choices. Open a tool when you need it.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        tool_cols = st.columns(2)
        for index, tip in enumerate(WRITING_TIPS):
            with tool_cols[index % 2]:
                with st.expander(f"{tip['icon']} {tip['title']}"):
                    st.markdown(tip["body"])
                    st.markdown(
                        f"<div class='tip-example'>{safe(tip['example'])}</div>",
                        unsafe_allow_html=True,
                    )

        section_heading("A five-minute revision routine", "Use it on any piece of writing")
        st.markdown(
            """
            1. **Read once for meaning.** Does the main idea arrive clearly?
            2. **Read once aloud.** Your ear will find missing words and sentences that run too long.
            3. **Check the edges.** Capital letters at the start; punctuation at the end.
            4. **Check the verbs.** Do they agree with their subjects? *She works. They work.*
            5. **Make one improvement.** Add a detail, replace a repeated word, or split a long sentence.
            """
        )

        st.markdown(
            """
            > **A note on models:** A model answer shows one possible route, not the only correct one.
            > Your experience, your voice and your examples are what make a piece of writing worth reading.
            """
        )

    with notebook_tab:
        entries = st.session_state.writing_entries
        section_heading("Your writing notebook", f"{len(entries)} saved draft(s)")

        if not entries:
            st.info(
                "Your notebook is empty for now. Choose a daily prompt, write a few sentences, and press "
                "**Save to notebook**. You can download your writing at any time."
            )
        else:
            all_text = "\n\n".join(
                f"{entry['title']}\n{entry['date']}\n\n{entry['text']}" for entry in reversed(entries)
            )
            st.download_button(
                "Download all drafts",
                data=all_text,
                file_name="jessicas_writing_notebook.txt",
                mime="text/plain",
                key="download_all_drafts",
            )
            for index in range(len(entries) - 1, -1, -1):
                entry = entries[index]
                with st.expander(f"{entry['title']} · {entry['date']} · {entry['words']} words"):
                    st.text(entry["text"])
                    if entry.get("analysis"):
                        st.caption(
                            f"Practice check at save time: {entry['analysis'].get('percent', 0)}%. "
                            "This reflects the draft when it was saved."
                        )
                    entry_col_a, entry_col_b = st.columns(2)
                    with entry_col_a:
                        st.download_button(
                            "Download this draft",
                            data=entry["text"],
                            file_name=f"{entry['prompt_id']}_saved.txt",
                            mime="text/plain",
                            key=f"download_entry_{index}",
                        )
                    with entry_col_b:
                        if st.button("Delete this draft", key=f"delete_entry_{index}", use_container_width=True):
                            entries.pop(index)
                            st.rerun()
