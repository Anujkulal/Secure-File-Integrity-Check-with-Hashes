import streamlit as st

st.set_page_config(page_title="Theory", layout="wide")
st.header("📚 Theory")

st.write("""
### 🔑 Hashing
Hashing is the process of converting data into a fixed-length digest using a **hash function**.  
Popular algorithms include:
- **MD5**: Fast but cryptographically broken (not secure for integrity).  
- **SHA-1**: Better than MD5 but also deprecated due to vulnerabilities.  
- **SHA-256**: Secure, widely used in modern cryptographic applications.  

### 🔑 File Integrity
File integrity verification ensures that a file has not been **modified, corrupted, or tampered**.  
If the computed hash of a file matches the reference hash, the file is considered authentic.

### 🔑 HMAC (Hash-based Message Authentication Code)
HMAC provides additional security by combining a **secret key** with hashing, ensuring that only parties with the key can generate/verify the digest.
""")
