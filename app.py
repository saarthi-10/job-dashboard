import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="Job Finder", layout="wide")

st.title("💼 Product & Business Analytics Job Finder")

st.write("Paste career page URLs below (one per line)")

urls = st.text_area("Career Page Links")

keywords = ["product", "business", "analytics", "analyst", "manager"]

if st.button("Find Jobs"):
    results = []

    for url in urls.splitlines():
        try:
            page = requests.get(url, timeout=10)
            soup = BeautifulSoup(page.text, "html.parser")
            text = soup.get_text().lower()

            for k in keywords:
                if k in text:
                    results.append((url, k))
                    break
        except:
            pass

    if results:
        st.success("Jobs Found 👇")
        for r in results:
            st.write(f"✅ {r[0]}")
    else:
        st.warning("No matching jobs found.")
