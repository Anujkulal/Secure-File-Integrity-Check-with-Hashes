import streamlit as st
import hashlib
import hmac
from typing import Tuple

SUPPORTED_ALGOS = ["sha256", "sha1", "md5"]

# ---------------------- Hashing utilities ----------------------
def compute_hash_from_fileobj(fileobj, algo: str = "sha256", block_size: int = 65536) -> str:
    if algo not in SUPPORTED_ALGOS:
        raise ValueError("Unsupported algorithm")
    h = hashlib.new(algo)
    # print(f"h value::: {h}")

    fileobj.seek(0)
    # print(f"fileobj.seek(0)::: {fileobj}")

    while True:
        data = fileobj.read(block_size)
        # print(f"Read data::: {data}")

        if not data:
            break
        if isinstance(data, str):
            data = data.encode("utf-8")
            # print(f"Encoded data::: {data}")

        h.update(data)
        # print(f"Updated hash object::: {h}")
    fileobj.seek(0)
    # print(f"fileobj.seek(0)::: {fileobj}")
    # print(f"Final hexdigest::: {h.hexdigest()}")
    return h.hexdigest()

# ---------------------- Integrity check helpers ----------------------
def verify_digest(expected: str, actual: str) -> Tuple[bool, str]:
    ok = hmac.compare_digest(expected, actual)
    msg = "MATCH" if ok else "MISMATCH"
    return ok, msg

# ---------------------- Simulation UI ----------------------
st.set_page_config(page_title="Simulation", layout="wide")
st.header("Simulation: File Integrity Checker")

algo = st.selectbox("Select Hash Algorithm", SUPPORTED_ALGOS, index=0)
col1, col2 = st.columns([1, 1])
digest = ""


with col1:
    st.subheader("Quick Hashing")
    st.write("Upload a file to compute its digest.")
    uploaded = st.file_uploader("Upload file", key="quick_compute")
    if uploaded is not None and uploaded.size > 0:
        digest = compute_hash_from_fileobj(uploaded, algo=algo)
        st.code(f"{algo} digest: {digest}")

with col2:
    st.subheader("Digest Verification")
    uploaded = st.file_uploader("Upload file to verify", key="verify_upload")
    if uploaded is not None and uploaded.size > 0:
        actual = compute_hash_from_fileobj(uploaded, algo=algo)
        st.info(f"Computed {algo}: {actual}")

    raw_digest = st.text_input("Paste reference digest", disabled=digest != "")
    if (digest or raw_digest) and uploaded is not None and uploaded.size > 0:
        source = compute_hash_from_fileobj(uploaded, algo=algo)
        if digest:
            ok, msg = verify_digest(digest.strip(), source)
            if ok:
                st.success(f"Quick digest verify: {msg}")
            else:
                st.error(f"Quick digest verify: {msg}")
            # st.success(f"Quick digest verify: {msg}") if ok else st.error(f"Quick digest verify: {msg}")
        if raw_digest:
            ok, msg = verify_digest(raw_digest.strip(), source)
            if ok:
                st.success(f"Raw digest verify: {msg}")
            else:
                st.error(f"Raw digest verify: {msg}")
            # st.success(f"Raw digest verify: {msg}") if ok else st.error(f"Raw digest verify: {msg}")
