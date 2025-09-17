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
    fileobj.seek(0)
    while True:
        data = fileobj.read(block_size)
        if not data:
            break
        if isinstance(data, str):
            data = data.encode("utf-8")
        h.update(data)
    fileobj.seek(0)
    return h.hexdigest()


def compute_hash_from_path(path: str, algo: str = "sha256", block_size: int = 65536) -> str:
    if algo not in SUPPORTED_ALGOS:
        raise ValueError("Unsupported algorithm")
    h = hashlib.new(algo)
    with open(path, "rb") as f:
        while True:
            chunk = f.read(block_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

# ---------------------- Integrity check helpers ----------------------

def verify_digest(expected: str, actual: str) -> Tuple[bool, str]:
    ok = hmac.compare_digest(expected, actual)
    msg = "MATCH" if ok else "MISMATCH"
    return ok, msg

# ---------------------- Streamlit UI ----------------------

def main():
    st.set_page_config(page_title="Secure File Integrity Checker", layout="wide")
    st.title("🔒 Secure File Integrity Check")

    with st.sidebar:
        st.header("Settings")
        algo = st.selectbox("Hash algorithm", SUPPORTED_ALGOS, index=0)
        secret_key = None
        st.markdown("---")
        st.write("App by: Anuj & Elroy")

    col1, col2 = st.columns([1, 1])
    digest = ""
    # print("digest value::: ",len(digest))

    with col1:
        st.subheader("Quick tools")
        st.write("Compute hash for arbitrary uploaded file")
        uploaded = st.file_uploader("Quick compute: upload file", key="quick_compute")
        if uploaded is not None and uploaded.size > 0:
            digest = compute_hash_from_fileobj(uploaded, algo=algo)
            st.code(f"{algo} digest: {digest}")

    with col2:
        st.write("Verify a file against the provided digest.")
        uploaded = st.file_uploader("Upload file to verify", accept_multiple_files=False, key="verify_upload")
        # st.markdown("**Select reference**")

        if uploaded is not None and uploaded.size > 0:
            actual = compute_hash_from_fileobj(uploaded, algo=algo)
            st.info(f"Computed {algo}: {actual}")

        st.markdown("---")
        st.write("Or verify a file against a raw digest (paste below)")
        raw_digest = st.text_input("Raw digest to compare against", disabled=digest != "")
        if digest or raw_digest:
            source = None
            if uploaded is not None and uploaded.size > 0:
                source = compute_hash_from_fileobj(uploaded, algo=algo)
            if source:
                if digest:
                    ok, msg = verify_digest(digest.strip(), source)
                    if ok:
                        st.success(f"Quick digest verify: {msg}")
                    else:
                        st.error(f"Quick digest verify: {msg}")

                if raw_digest:
                    ok, msg = verify_digest(raw_digest.strip(), source)
                    # print("Message::: ",msg)
                    if ok:
                        st.success(f"Raw digest verify: {msg}")
                    else:
                        st.error(f"Raw digest verify: {msg}")

# ---------------------- Run ----------------------

if __name__ == "__main__":
    main()
