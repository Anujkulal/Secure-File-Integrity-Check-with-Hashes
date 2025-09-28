import streamlit as st
import inspect
import textwrap
import hashlib, hmac

st.set_page_config(page_title="Theory", layout="wide")
st.header("Theory")

st.write("""
### Hashing
Hashing is the process of converting data into a fixed-length digest using a **hash function**.  
Popular algorithms include:
- **MD5**: Fast but cryptographically broken (not secure for integrity).  
- **SHA-1**: Better than MD5 but also deprecated due to vulnerabilities.  
- **SHA-256**: Secure, widely used in modern cryptographic applications.  

### File Integrity
File integrity verification ensures that a file has not been **modified, corrupted, or tampered**.  
If the computed hash of a file matches the reference hash, the file is considered authentic.

### HMAC (Hash-based Message Authentication Code)
HMAC provides additional security by combining a **secret key** with hashing, ensuring that only parties with the key can generate/verify the digest.
""")

st.markdown("---")

# ------------------ Function: compute_hash_from_fileobj ------------------
st.subheader("🔹 Function: `compute_hash_from_fileobj`")

# st.code(textwrap.dedent(inspect.getsource(
#     lambda fileobj=None, algo="sha256", block_size=65536: hashlib.new(algo).hexdigest()
# )).replace("<lambda>", "compute_hash_from_fileobj").strip(), language="python")

st.markdown("""
```python
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
```            
""")

st.markdown("""
**Explanation:**
- `algo`: Chooses the hashing algorithm (e.g., SHA-256).  
- `block_size`: Reads the file in chunks instead of loading the whole file into memory.  
- `fileobj.seek(0)`: Ensures the file pointer starts at the beginning.  
- `h.update(data)`: Feeds chunks of file data to the hash function.  
- Finally, `h.hexdigest()` returns the unique hash value (digest) of the file.  
This makes the function memory-efficient and works with any supported algorithm.
""")

st.markdown("---")

# ------------------ Function: verify_digest ------------------
st.subheader("🔹 Function: `verify_digest`")

# st.code(textwrap.dedent(inspect.getsource(
#     lambda expected, actual: (hmac.compare_digest(expected, actual), "MATCH" if hmac.compare_digest(expected, actual) else "MISMATCH")
# )).replace("<lambda>", "verify_digest").strip(), language="python")

st.markdown("""
```python
   def verify_digest(expected: str, actual: str) -> Tuple[bool, str]:
        ok = hmac.compare_digest(expected, actual)
        msg = "MATCH" if ok else "MISMATCH"
        return ok, msg         
```
""")

st.markdown("""
**Explanation:**
- Takes two inputs: `expected` (reference hash) and `actual` (computed hash).  
- Uses `hmac.compare_digest()` which prevents **timing attacks** by comparing securely.  
- Returns:
  - **MATCH** → if both digests are identical.  
  - **MISMATCH** → if they differ.  
This ensures file authenticity and prevents subtle timing-based vulnerabilities.
""")