import streamlit as st

st.set_page_config(page_title="Introduction", layout="wide")
st.header("📖 Introduction")

st.write("""
In today’s digital era, ensuring **file integrity** is of paramount importance.  
Files shared over networks or stored locally may get corrupted, tampered with, 
or maliciously altered.  

A **Secure File Integrity Checker** helps verify the originality of a file by 
comparing its computed cryptographic hash against a trusted reference hash.  

This project demonstrates how hashing algorithms such as **SHA-256, SHA-1, and MD5** 
can be used to validate file authenticity and detect changes.
""")
