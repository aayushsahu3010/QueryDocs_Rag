# Install dependencies
!pip install streamlit requests

# Save the frontend script
frontend_code = """
import streamlit as st
import requests

API_URL = "PASTE_NGROK_URL_HERE/query"

st.title("📄 AI-Powered PDF Chatbot")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    st.success("✅ PDF uploaded successfully!")
    st.subheader("💬 Ask Questions about the PDF")
    user_query = st.text_input("Type your question:")

    if st.button("Ask"):
        files = {"file": uploaded_file}
        data = {"query": user_query}
        response = requests.post(API_URL, files=files, data=data)
        answer = response.json().get("answer", "No response from model")
        st.write(f"🤖 **AI:** {answer}")
"""

# Save as app.py
with open("app.py", "w") as f:
    f.write(frontend_code)

# Replace NGROK URL
!sed -i "s|PASTE_NGROK_URL_HERE|{public_url}|g" app.py

# Run Streamlit
!streamlit run app.py & npx localtunnel --port 8501
