# import streamlit as st
# import hashlib
# import hmac
# from typing import Tuple

# SUPPORTED_ALGOS = ["sha256", "sha1", "md5"]


# # ---------------------- Hashing utilities ----------------------

# def compute_hash_from_fileobj(fileobj, algo: str = "sha256", block_size: int = 65536) -> str:
#     if algo not in SUPPORTED_ALGOS:
#         raise ValueError("Unsupported algorithm")
#     h = hashlib.new(algo)

#     # print("h value:::", h)
#     fileobj.seek(0)

#     # print("File object before reading:::", fileobj)
#     while True:
#         data = fileobj.read(block_size)

#         # print("data value:::", data)
#         if not data:
#             break
#         if isinstance(data, str):
#             data = data.encode("utf-8")
#         h.update(data)

#         # print("h after update:::", h)
#     fileobj.seek(0)

#     # print("File object after seek:::", fileobj)
#     # print("Final hexdigest:::", h.hexdigest())
#     return h.hexdigest()

# # ---------------------- Integrity check helpers ----------------------

# def verify_digest(expected: str, actual: str) -> Tuple[bool, str]:
#     ok = hmac.compare_digest(expected, actual)
#     msg = "MATCH" if ok else "MISMATCH"
#     return ok, msg

# # ---------------------- Streamlit UI ----------------------

# def main():
#     st.set_page_config(page_title="Secure File Integrity Checker", layout="wide")
#     st.title("🔒 Secure File Integrity Check")

#     with st.sidebar:
#         st.header("Settings")
#         algo = st.selectbox("Hash algorithm", SUPPORTED_ALGOS, index=0)
#         secret_key = None
#         st.markdown("---")
#         st.write("App by: Anuj & Elroy")

#     col1, col2 = st.columns([1, 1])
#     digest = ""
#     # print("digest value::: ",len(digest))

#     with col1:
#         st.subheader("Quick tools")
#         st.write("Compute hash for arbitrary uploaded file")
#         uploaded = st.file_uploader("Quick compute: upload file", key="quick_compute")
#         if uploaded is not None and uploaded.size > 0:
#             digest = compute_hash_from_fileobj(uploaded, algo=algo)
#             st.code(f"{algo} digest: {digest}")

#     with col2:
#         st.write("Verify a file against the provided digest.")
#         uploaded = st.file_uploader("Upload file to verify", accept_multiple_files=False, key="verify_upload")
#         # st.markdown("**Select reference**")

#         if uploaded is not None and uploaded.size > 0:
#             actual = compute_hash_from_fileobj(uploaded, algo=algo)
#             st.info(f"Computed {algo}: {actual}")

#         st.markdown("---")
#         st.write("Or verify a file against a raw digest (paste below)")
#         raw_digest = st.text_input("Raw digest to compare against", disabled=digest != "")
#         if digest or raw_digest:
#             source = None
#             if uploaded is not None and uploaded.size > 0:
#                 source = compute_hash_from_fileobj(uploaded, algo=algo)
#             if source:
#                 if digest:
#                     ok, msg = verify_digest(digest.strip(), source)
#                     if ok:
#                         st.success(f"Quick digest verify: {msg}")
#                     else:
#                         st.error(f"Quick digest verify: {msg}")

#                 if raw_digest:
#                     ok, msg = verify_digest(raw_digest.strip(), source)
#                     # print("Message::: ",msg)
#                     if ok:
#                         st.success(f"Raw digest verify: {msg}")
#                     else:
#                         st.error(f"Raw digest verify: {msg}")

# # ---------------------- Run ----------------------

# if __name__ == "__main__":
#     main()



import streamlit as st

# Page config
st.set_page_config(page_title="Secure File Integrity Checker", page_icon="🔒", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    # .main {
    #         background-color: #222;
    #         color: #ffffff;
    #         font-family: 'Segoe UI', sans-serif;
    #     }
    #     .stApp {
    #         background-color: #222;
    #     }
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.2rem;
        text-align: center;
        color: #555;
        margin-bottom: 2rem;
    }
    .card {
        padding: 1.5rem;
        border-radius: 12px;
        background-color: #222222;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        transition: all 0.3s ease-in-out;
    }
    .card:hover {
        transform: scale(1.02);
        background-color: #222222;
    }
    ul {
        font-size: 1.1rem;
        line-height: 1.8;
    }
    .success-box {
        font-size: 1rem;
        padding: 0.8rem;
        border-radius: 8px;
        background-color: #e6f4ea;
        color: #1b5e20;
        border-left: 6px solid #2e7d32;
        margin-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title + Subtitle
st.markdown('<div class="main-title">🔒 Secure File Integrity Checker</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ensure file authenticity and protect against tampering</div>', unsafe_allow_html=True)

# Card with description
st.markdown(
    """
    <div class="card">
        <p>Welcome to the <b>Secure File Integrity Checker</b> project.</p>
        <p>Use the left sidebar to navigate through the sections:</p>
        <ul>
            <li>📖 <b>Introduction</b></li>
            <li>🎯 <b>Objective</b></li>
            <li>📚 <b>Theory</b></li>
            <li>🖥️ <b>Simulation</b></li>
            <li>📝 <b>Procedure</b></li>
            <li>🔗 <b>References</b></li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# Success box at bottom
st.markdown('<div class="success-box">✅ Navigate using the sidebar to explore each section</div>', unsafe_allow_html=True)

