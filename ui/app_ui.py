import streamlit as st
from io import BytesIO
import sys
import os

# Get absolute path to the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.append(project_root)

from functions.file_utils.file_info_extractor import get_file_info_dataframe
def file_metadata_extractor_ui():
    st.subheader("📁 File Metadata Extractor")
    st.markdown("Scan a folder to collect file metadata and export it to Excel. PDF page counts are included.")

    folder_path = st.text_input("Enter the full path to the folder you want to scan:")

    if folder_path:
        if st.button("📊 Scan and Generate Excel"):
            try:
                with st.spinner("Scanning files..."):
                    df = get_file_info_dataframe(folder_path)

                    if df.empty:
                        st.warning("✅ No files were found or processed in the selected folder.")
                    else:
                        st.success(f"Scanned {len(df)} files.")
                        st.dataframe(df.head(10))  # Preview

                        buffer = BytesIO()
                        df.to_excel(buffer, index=False, engine='openpyxl')
                        buffer.seek(0)

                        st.download_button(
                            label="⬇️ Download Excel File",
                            data=buffer,
                            file_name="file_metadata.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        )

            except FileNotFoundError as fnf_err:
                st.error(f"Path Error: {fnf_err}")
            except Exception as e:
                st.error(f"Unexpected error: {e}")

def placeholder_function_ui():
    st.subheader("🧪 Placeholder Function")
    st.markdown("This is a placeholder for another function.")
    name = st.text_input("Enter your name:")
    if name:
        st.success(f"Hello, {name}! This is a test function.")
