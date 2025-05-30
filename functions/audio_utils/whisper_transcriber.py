# import whisper
# import sys
# import os
#
# # Get absolute path to the project root
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# if project_root not in sys.path:
#     sys.path.append(project_root)
#
# from functions.utils.logger import log_function_use
# def transcribe_audio(file_path):
#     if not os.path.isfile(file_path):
#         raise FileNotFoundError(f"Audio file not found: {file_path}")
#
#     model = whisper.load_model("base")
#     result = model.transcribe(file_path)
#     log_function_use(
#         function_name="Whisper Transcription",
#         input_value=file_path,
#         result_status="Transcription successful"
#     )
#     return result["text"]
