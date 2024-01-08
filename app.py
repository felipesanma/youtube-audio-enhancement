import streamlit as st
from PIL import Image
import json
from audio_processing import download_youtube_video_to_audio, improve_audio_quality
import os
# SETUP ------------------------------------------------------------------------
favicon = Image.open("favicon.ico")
st.set_page_config(
    page_title="Youtube Audio Enhancement",
    page_icon=favicon,
    layout="wide",
    initial_sidebar_state="auto",
)


# Sidebar contents ------------------------------------------------------------------------
with st.sidebar:
    st.title("Youtube Audio Enhancement")
    st.markdown(
        """
    ## About
    Improve Audio Quality from youtube Video, built using:
    - [Streamlit](https://streamlit.io/)
    - pytube
    - pedalboard
    - noisereduce
    """
    )
    st.write(
        "Made with ❤️ by [Chasquilla Engineer](https://resume.chasquillaengineer.com/)"
    )


# ROW 1 ------------------------------------------------------------------------

st.header("Youtube Audio Enhancement")
st.markdown(
    "_Improve Audio Quality from Youtube video_"
)

youtube_url = st.text_input(
    "Youtube URL, sample: https://www.youtube.com/watch?v=ojQdVM-nbDg",
    key="youtube_url",
)
button1 = st.button("Get Better Audio")
if not st.session_state.get("button1"):
    st.session_state["button1"] = button1

if st.session_state["button1"]:
    if not youtube_url:
        st.warning("Youtube URL is missing")
        st.stop()

    with st.spinner("Downloading Audio from URL...."):
        st.session_state.video_id = youtube_url.split("=")[-1]
        try:
            st.session_state.is_downloaded, st.session_state.audio_file_name = download_youtube_video_to_audio(st.session_state.video_id)
        except Exception as e:
            st.error("Something went grong...")
            st.exception(e)
            st.stop()
    st.info(st.session_state.is_downloaded)
    st.info(st.session_state.audio_file_name)
    with st.spinner("Improving Audio Quality...."):
        try:
            st.session_state.improved_audio_file_name = improve_audio_quality(st.session_state.audio_file_name)
        except Exception as e:
            st.error("Something went grong...")
            st.exception(e)
            st.stop()
    st.title("Enjoy your new Audio Quality")
    st.audio(st.session_state.improved_audio_file_name, format="audio/wav")
    with open(st.session_state.improved_audio_file_name, "rb") as f:
        data = f.read()
    
    st.download_button(
    label="Download Audio",
    data=data,
    file_name="audio.wav",
    mime='audio/wav')

    os.remove(st.session_state.audio_file_name)
    st.snow()
