import streamlit as st
import requests

st.set_page_config(
    page_title="Plainly",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Plainly")
st.write("Turn complex text into language humans understand.")

text = st.text_area(
    "Paste complex text here",
    height=180,
    placeholder="Example: The system utilizes asynchronous event-driven architecture..."
)

mode = st.selectbox(
    "Choose simplicity mode",
    ["very_simple", "simple", "normal"]
)

if st.button("Explain"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Explaining in human language..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/explain",
                    json={
                        "text": text,
                        "mode": mode
                    },
                    timeout=30
                )

                if response.status_code == 200:
                    result = response.json()["result"]
                    st.success("Explanation")
                    st.write(result)
                else:
                    st.error(f"Backend error: {response.status_code}")

            except Exception as e:
                st.error("Could not connect to backend.")
