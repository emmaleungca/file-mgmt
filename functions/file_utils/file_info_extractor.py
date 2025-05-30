import os
import pandas as pd
from datetime import datetime
from PyPDF2 import PdfReader
import sys

# Get absolute path to the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.append(project_root)

from utils.logger import log_function_use
def get_file_info(folder_path):
    file_data = []

    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder path '{folder_path}' does not exist.")

    for root, _, files in os.walk(folder_path):
        for file in files:
            try:
                print(f"Scanning file: {file}")
                file_path = os.path.join(root, file)  # Handle long file paths
                file_size = os.path.getsize(file_path)
                created_time = datetime.fromtimestamp(os.path.getctime(file_path))
                updated_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                folder_name = os.path.basename(root)
                file_name, file_extension = os.path.splitext(file)
                whole_folder_name = os.path.relpath(root, folder_path)
                whole_path = os.path.abspath(file_path)

                pdf_pages = None
                if file_extension.lower() == '.pdf':
                    try:
                        with open(file_path, "rb") as pdf_file:
                            pdf_reader = PdfReader(pdf_file)
                            pdf_pages = len(pdf_reader.pages)
                    except Exception as e:
                        pdf_pages = f"Error: {e}"

                file_data.append([
                    whole_path, whole_folder_name, folder_name, file_name, file_extension,
                    file_size, created_time, updated_time, pdf_pages
                ])
            except (FileNotFoundError, PermissionError, OSError) as e:
                print(f"Skipping {file}: {e}")
                continue

    return file_data

def get_file_info_dataframe(folder_path):
    file_info = get_file_info(folder_path)

    if not file_info:
        print("No data collected.")
    else:
        print(f"Collected {len(file_info)} entries.")

    columns = [
        "Whole Path", "Whole Folder Name", "Current Folder Name", "File Name Without Extension",
        "File Extension", "File Size (bytes)", "Created Datetime", "Updated Datetime", "Pages (if PDF)"
    ]
    df = pd.DataFrame(file_info, columns=columns)
    log_function_use(
        function_name="File Metadata Extractor",
        input_value=folder_path,
        result_status=f"{len(df)} files scanned" if not df.empty else "No files found"
    )
    return df
