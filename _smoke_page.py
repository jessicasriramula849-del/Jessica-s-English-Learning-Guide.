"""Temporary AppTest harness for one page at a time."""

import os

import streamlit as st

st.set_page_config(page_title="smoke", layout="wide")

from core import init_state, inject_css  # noqa: E402

init_state()
inject_css(False)

page = os.environ.get("TEST_PAGE", "home")
if page == "learn":
    from page_learn import render_learn
    render_learn()
elif page == "read":
    from page_read import render_read
    render_read()
elif page == "write":
    from page_write import render_write
    render_write()
elif page == "practice":
    from page_practice import render_practice
    render_practice()
elif page == "progress":
    from page_progress import render_progress
    render_progress()
