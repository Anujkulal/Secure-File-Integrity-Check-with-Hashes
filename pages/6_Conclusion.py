import streamlit as st

st.set_page_config(page_title="Conclusion", layout="wide")

st.markdown(
    """
    <h2 style="color: #117A65; font-family: 'Trebuchet MS', sans-serif;">
        Conclusion
    </h2>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
This project demonstrated the importance of **file integrity verification** using cryptographic hashing algorithms such as **SHA-256**.  

With the help of an intuitive **Streamlit-based GUI**, users can easily check whether a file has been modified or tampered with.  

---

#### **Key Takeaways:**  
- Hashing ensures file authenticity and integrity.  
- Even a small change in the file results in a completely different hash.  
- User-friendly GUIs help make security tools more accessible.  

    """
)


# ---

# This system can be extended with features like **digital signatures**, **database logging**, and **multi-file verification** for real-world applications.