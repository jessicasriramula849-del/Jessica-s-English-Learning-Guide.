# Jessica's English Learning Guide For Students And Adults Of All Ages

A warm, self-paced Streamlit website for learning to read, write, and understand English from the very beginning. It is designed for students and adults of all ages, with clear explanations, graded stories, guided writing, practice activities, and progress tracking.

## Run the site

```powershell
pip install -r requirements.txt
streamlit run app.py
```

Then open the local address Streamlit prints in your browser (usually `http://localhost:8501`).

## What is included

- **Learn English** — 16 guided lessons across Foundation, Beginner, Growing, and Confident levels, from the alphabet and phonics to conditionals, polite email, and idioms.
- **Read English** — 8 original graded stories with glossaries, reading strategies, and explained comprehension questions.
- **Write English** — 8 writing prompts with scenarios, sentence starters, model answers, a basic practice check (length, structure, capitals, punctuation, and variety), a downloadable notebook, and a writing toolkit.
- **Practice Zone** — vocabulary flashcards, a ten-question mixed quiz with explanations, and spelling practice.
- **My Progress** — a visual dashboard, badges, recent activity, a weekly rhythm, a downloadable JSON progress report, and a reset option.
- **Reading comfort** — a larger-text toggle in the sidebar.

Progress is held in the browser session and is not connected to a database or account. Learners can download a report or their writing at any time.

## Files

| File | Purpose |
| --- | --- |
| `app.py` | Page configuration and navigation routing |
| `core.py` | Shared state, custom styling, sidebar, and layout helpers |
| `content.py` | Curriculum, stories, writing prompts, flashcards, quiz, and spelling content |
| `page_home.py` | Home page |
| `page_learn.py` | Lesson library and lesson reader |
| `page_read.py` | Graded reading room |
| `page_write.py` | Writing studio and notebook |
| `page_practice.py` | Flashcards, quiz, and spelling |
| `page_progress.py` | Progress dashboard and report |

## Note

The writing feedback is a practice guide, not a complete grammar checker. The site is a learning companion, not a replacement for a qualified teacher or formal assessment.
