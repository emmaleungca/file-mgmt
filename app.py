import streamlit as st
from ui.app_ui import file_metadata_extractor_ui, placeholder_function_ui
# from ui.whisper_transcriber_ui import whisper_transcription_ui
from ui.view_log_ui import view_history_ui
st.set_page_config(page_title="Tool Selector", layout="centered")

st.title("🔧 Multi-Function Tool")

function_choice = st.selectbox(
    "Choose a function to run:",
    ["File Metadata Extractor", "Placeholder Function", "Whisper Transcriber Function", "View History"]
)

if function_choice == "File Metadata Extractor":
    file_metadata_extractor_ui()
elif function_choice == "Placeholder Function":
    placeholder_function_ui()
# elif function_choice == "Whisper Transcriber Function":
#     whisper_transcription_ui()
elif function_choice == "View History":
    view_history_ui()