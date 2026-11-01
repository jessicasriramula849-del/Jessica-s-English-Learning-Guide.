"""Practice zone: flashcards, quiz, and spelling."""

import random

import streamlit as st

from content import FLASHCARDS, QUIZ_QUESTIONS, SPELLING_WORDS
from core import (
    log_activity,
    page_header,
    safe,
    section_heading,
)


def _next_flash() -> None:
    st.session_state.flash_index += 1
    st.session_state.flash_reveal = False


def _previous_flash() -> None:
    st.session_state.flash_index -= 1
    st.session_state.flash_reveal = False


def _reveal_flash() -> None:
    st.session_state.flash_reveal = not st.session_state.flash_reveal


def render_practice() -> None:
    page_header(
        "Practice zone",
        "Small practice, repeated often, becomes confidence",
        "Flip a word card, check your spelling, or take a quick ten-question quiz. Every answer is explained, and nothing here is a formal test. Use it to notice what is growing.",
        "🎯",
    )

    flash_tab, quiz_tab, spelling_tab = st.tabs(["🃏 Vocabulary cards", "🧠 Quick quiz", "🔤 Spelling practice"])

    # ------------------------------------------------------------------
    # Flashcards
    # ------------------------------------------------------------------
    with flash_tab:
        categories = ["All words"] + sorted({card["category"] for card in FLASHCARDS})
        col_a, col_b = st.columns([1, 2.2])
        with col_a:
            category = st.selectbox("Word group", categories, key="flash_category")
        deck = [card for card in FLASHCARDS if category == "All words" or card["category"] == category]

        if st.session_state.get("_flash_last_category") != category:
            st.session_state.flash_index = 0
            st.session_state.flash_reveal = False
            st.session_state["_flash_last_category"] = category

        if not deck:
            st.info("There are no cards in this group yet.")
            return

        st.session_state.flash_index = st.session_state.flash_index % len(deck)
        card = deck[st.session_state.flash_index]
        known = card["word"] in st.session_state.flash_mastered
        known_in_deck = sum(1 for item in deck if item["word"] in st.session_state.flash_mastered)

        with col_b:
            st.caption(f"{known_in_deck} of {len(deck)} words in this group marked as known")
            st.progress(known_in_deck / len(deck))

        revealed = st.session_state.flash_reveal
        if revealed:
            meaning_html = f"""
                <div class="flash-reveal">
                    <p>{safe(card["meaning"])}</p>
                    <p><em>“{safe(card["example"])}”</em></p>
                </div>
            """
        else:
            meaning_html = "<div class='flash-hidden'>Meaning hidden · reveal it when you are ready</div>"

        st.markdown(
            f"""
            <div class="flash-card">
                <div class="flash-cat">{safe(card["category"])} · {st.session_state.flash_index + 1} of {len(deck)}</div>
                <div class="flash-word">{safe(card["word"])}</div>
                <div class="flash-pron">/{safe(card["pron"])}/</div>
                {meaning_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

        if known:
            st.success("You have marked this word as known. Reviewing it again is still useful.")

        button_a, button_b, button_c, button_d = st.columns(4)
        with button_a:
            st.button("← Previous", key="flash_prev", use_container_width=True, on_click=_previous_flash)
        with button_b:
            st.button("Reveal meaning" if not revealed else "Hide meaning", key="flash_reveal_btn", use_container_width=True, on_click=_reveal_flash)
        with button_c:
            if st.button("I know this word", key="flash_known", type="primary", use_container_width=True):
                if card["word"] not in st.session_state.flash_mastered:
                    st.session_state.flash_mastered.add(card["word"])
                    log_activity("🃏", f"Marked “{card['word']}” as a known word.")
                st.session_state.flash_index = (st.session_state.flash_index + 1) % len(deck)
                st.session_state.flash_reveal = False
                st.rerun()
        with button_d:
            st.button("Next →", key="flash_next", use_container_width=True, on_click=_next_flash)

        st.caption(
            "Reading a word aloud and saying a sentence of your own uses more memory than recognising it silently. "
            "Try the word in a sentence before you mark it known."
        )

        with st.expander("See all words in this group"):
            for item in deck:
                mark = "✅" if item["word"] in st.session_state.flash_mastered else "○"
                st.markdown(f"{mark} **{item['word']}** — {item['meaning']}")

    # ------------------------------------------------------------------
    # Quiz
    # ------------------------------------------------------------------
    with quiz_tab:
        round_number = st.session_state.quiz_round
        questions = random.Random(2026 + round_number).sample(QUIZ_QUESTIONS, 10)

        info_a, info_b = st.columns([2, 1])
        with info_a:
            st.markdown(
                f"""
                <div class="card" style="background:rgba(220,235,221,0.4)">
                    <div class="card-kicker">Ten-question check</div>
                    <h3 style="font-size:1.35rem">A friendly review of grammar, vocabulary and reading</h3>
                    <p>Answer what you can. Every result includes the correct answer and an explanation, so a wrong answer is still useful.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with info_b:
            st.metric("Personal best", f"{st.session_state.quiz_best}/10")
            st.caption(f"{st.session_state.quiz_attempts} attempt(s) so far")
            st.progress(min(st.session_state.quiz_best / 10, 1.0))

        with st.form(f"quiz_form_{round_number}"):
            for index, question in enumerate(questions, 1):
                st.markdown(f"**{index}. {question['question']}**")
                st.radio(
                    f"Answer {index}",
                    question["options"],
                    index=None,
                    key=f"quiz_answer_{round_number}_{index}",
                    label_visibility="collapsed",
                )
            submitted = st.form_submit_button("Score my quiz")

        if submitted:
            answers = [
                st.session_state.get(f"quiz_answer_{round_number}_{index}") for index in range(1, len(questions) + 1)
            ]
            score = sum(1 for q, a in zip(questions, answers) if a == q["options"][q["answer"]])
            unanswered = sum(1 for answer in answers if answer is None)
            st.session_state.quiz_attempts += 1
            st.session_state.quiz_best = max(st.session_state.quiz_best, score)
            st.session_state.quiz_result = {
                "round": round_number,
                "answers": answers,
                "score": score,
                "unanswered": unanswered,
            }
            log_activity("🧠", f"Completed a quiz with {score}/10 correct.")

        result = st.session_state.quiz_result
        if result and result.get("round") == round_number:
            score = result["score"]
            if score >= 8:
                st.success(f"**{score} out of 10.** Strong work — you are connecting the rules, not just remembering them.")
            elif score >= 5:
                st.info(f"**{score} out of 10.** A solid foundation. Read the explanations for the questions you missed, then try another round.")
            else:
                st.warning(f"**{score} out of 10.** This is information, not a verdict. Review the explanations and revisit the lesson that matches each question.")
            if result["unanswered"]:
                st.caption(f"You left {result['unanswered']} question(s) unanswered. In practice, a considered guess is better than a blank.")
            st.progress(score / 10)

            section_heading("Review your answers", "Explanations below")
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

        if st.button("Start a fresh quiz", key="new_quiz"):
            st.session_state.quiz_round += 1
            st.session_state.quiz_result = None
            st.rerun()

    # ------------------------------------------------------------------
    # Spelling
    # ------------------------------------------------------------------
    with spelling_tab:
        index = st.session_state.spell_index % len(SPELLING_WORDS)
        word = SPELLING_WORDS[index]
        solved = len(st.session_state.spelling_solved)

        st.markdown(
            f"""
            <div class="prompt-card">
                <div class="card-kicker">Spelling word {index + 1} of {len(SPELLING_WORDS)}</div>
                <h3>Can you spell this word?</h3>
                <p><strong>Meaning:</strong> {safe(word["definition"])}</p>
                <p style="margin-top:0.5rem"><strong>Pattern:</strong> <span style="font-family:monospace;letter-spacing:0.13em">{safe(word["hint"])}</span></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.progress(solved / len(SPELLING_WORDS))
        st.caption(f"{solved} of {len(SPELLING_WORDS)} words spelled correctly at least once")

        with st.form(f"spelling_form_{index}"):
            answer = st.text_input(
                "Type the word",
                key=f"spelling_input_{index}",
                placeholder="Type the complete word",
            )
            submitted = st.form_submit_button("Check my spelling")

        if submitted:
            normalised = answer.strip().lower()
            correct = normalised == word["word"].lower()
            st.session_state.spelling_attempts += 1
            if correct:
                if word["word"] not in st.session_state.spelling_solved:
                    st.session_state.spelling_solved.add(word["word"])
                    log_activity("🔤", f"Spelled “{word['word']}” correctly.")
            st.session_state.spelling_result = {
                "index": index,
                "correct": correct,
                "answer": answer.strip(),
            }

        result = st.session_state.spelling_result
        if result and result.get("index") == index:
            if result["correct"]:
                st.success(f"**Correct — {word['word']}.** {word['definition'].capitalize()}.")
            else:
                st.error(f"**Not quite.** The correct spelling is **{word['word']}**. Compare it with your answer: “{result['answer'] or 'blank'}”.")
                st.caption("Say the word aloud, split it into syllables, and try again. Spelling improves through retrieval, not just recognition.")

        nav_a, nav_b, nav_c = st.columns([1, 1.3, 1])
        with nav_a:
            if st.button("← Previous word", key="spell_prev", use_container_width=True):
                st.session_state.spell_index = (index - 1) % len(SPELLING_WORDS)
                st.session_state.spelling_result = None
                st.rerun()
        with nav_b:
            if st.button("Next word →", key="spell_next", type="primary", use_container_width=True):
                st.session_state.spell_index = (index + 1) % len(SPELLING_WORDS)
                st.session_state.spelling_result = None
                st.rerun()
        with nav_c:
            st.caption(f"Attempts: {st.session_state.spelling_attempts}")

        st.info(
            "Spelling is physical as well as visual. Write the word by hand once, cover it, and write it again from memory. "
            "Three correct recalls are worth more than reading the word ten times."
        )
