import streamlit as st
import pandas as pd
from io import BytesIO
from functions.file_utils.file_info_extractor import get_file_info_dataframe

st.set_page_config(page_title="File Info Extractor", layout="centered")

st.title("📁 File Metadata Extractor")
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
                    st.dataframe(df.head(10))  # Preview first 10 rows

                    # Export to Excel
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
