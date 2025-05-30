# import streamlit as st
# from io import BytesIO
# import sys
# import os
#
# # Get absolute path to the project root
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# if project_root not in sys.path:
#     sys.path.append(project_root)
#
# from functions.audio_utils.whisper_transcriber import transcribe_audio
#
# def whisper_transcription_ui():
#     st.subheader("🎙️ Whisper Audio Transcription")
#     st.markdown("Transcribe audio using OpenAI's Whisper model. Accepts formats like `.mp3`, `.wav`, `.m4a`, `.mkv`.")
#
#     audio_path = st.text_input("Enter the full path to your audio file:")
#
#     if audio_path and st.button("📝 Transcribe Audio"):
#         try:
#             with st.spinner("Transcribing... This may take a while."):
#                 text = transcribe_audio(audio_path)
#                 st.success("✅ Transcription completed.")
#                 st.text_area("📝 Transcribed Text:", text, height=300)
#
#                 st.download_button(
#                     label="⬇️ Download Transcript",
#                     data=text,
#                     file_name="transcription.txt",
#                     mime="text/plain"
#                 )
#         except FileNotFoundError as fnf_err:
#             st.error(fnf_err)
#         except Exception as e:
#             st.error(f"Unexpected error: {e}")
