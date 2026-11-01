"""Jessica's English Learning Guide — Streamlit application."""

import streamlit as st

from content import SITE_NAME

st.set_page_config(
    page_title=SITE_NAME,
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded",
)

from core import (  # noqa: E402
    PAGE_HOME,
    PAGES,
    inject_css,
    init_state,
    render_footer,
    render_sidebar,
)
from page_home import render_home  # noqa: E402
from page_learn import render_learn  # noqa: E402
from page_practice import render_practice  # noqa: E402
from page_progress import render_progress  # noqa: E402
from page_read import render_read  # noqa: E402
from page_write import render_write  # noqa: E402

init_state()
inject_css(st.session_state.large_text)
render_sidebar()

page = st.session_state.page
if page not in PAGES:
    st.session_state.page = PAGE_HOME

renders = {
    "🏠 Home": render_home,
    "📚 Learn English": render_learn,
    "📖 Read English": render_read,
    "✍️ Write English": render_write,
    "🎯 Practice Zone": render_practice,
    "🏅 My Progress": render_progress,
}

renders[st.session_state.page]()
render_footer()
