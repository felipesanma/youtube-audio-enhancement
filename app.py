import streamlit as st
from PIL import Image
import json
from streamlit_extras.stylable_container import stylable_container

# SETUP ------------------------------------------------------------------------
favicon = Image.open("favicon.ico")
st.set_page_config(
    page_title="Y2T - Transcription from Youtube Videos",
    page_icon=favicon,
    layout="wide",
    initial_sidebar_state="auto",
)


# Sidebar contents ------------------------------------------------------------------------
with st.sidebar:
    st.title("Y2T - Transcription from Youtube Videos")
    st.markdown(
        """
    ## About
    This app is a Youtube Video transcriptor, built using:
    - [Streamlit](https://streamlit.io/)
    - [Whisper](https://openai.com/research/whisper)
    - youtube_transcript_api
    - youtubesearchpython
    - pytube
    - tinytag
    """
    )
    st.write(
        "Made with ❤️ by [Chasquilla Engineer](https://resume.chasquillaengineer.com/)"
    )


# ROW 1 ------------------------------------------------------------------------

st.header("Transcription from Youtube Videos")
st.markdown(
    "_Get transcripts from videos even if there is no automatically generated from youtube_"
)

youtube_url = st.text_input(
    "Youtube URL, sample: https://www.youtube.com/watch?v=ojQdVM-nbDg",
    key="youtube_url",
)
button1 = st.button("Get Transcription")
if not st.session_state.get("button1"):
    st.session_state["button1"] = button1

if st.session_state["button1"]:
    if not youtube_url:
        st.warning("Youtube URL is missing")
        st.stop()