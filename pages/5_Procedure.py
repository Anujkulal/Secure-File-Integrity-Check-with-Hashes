import streamlit as st

st.set_page_config(page_title="Procedure", layout="wide")
st.header("Procedure")

st.write("""
The steps followed in this project:

1. Select a **hash algorithm** (SHA-256, SHA-1, or MD5).  
2. Upload a file to compute its **cryptographic digest**.  
3. Upload another file (or the same file) for **verification**.  
4. Paste a **reference digest** for comparison (optional).  
5. The system will show whether the digests **MATCH** or **MISMATCH**.  

This mimics real-world file verification workflows such as verifying **ISO images, software downloads, or secure document transfers**.
""")
