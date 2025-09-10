import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="PDF Chat with Gemini", layout="wide")
st.title("Chat with your PDF")

pdf_file = st.file_uploader("Upload a PDF", type="pdf")

if pdf_file:
    reader = PdfReader(pdf_file)
    pdf_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pdf_text += text + "\n"

    st.success("PDF Loaded Successfully!")


    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Ask something about the PDF:")

    if user_input:
       
        model = genai.GenerativeModel("gemini-2.5-flash")

        
        prompt = f"The following text is from a PDF:\n\n{pdf_text[:5000]}\n\nUser Question: {user_input}"

        
        response = model.generate_content(prompt)
        answer = response.text

        
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Gemini", answer))

   
    for sender, msg in st.session_state.chat_history:
        if sender == "You":
            st.markdown(f"**🧑 {sender}:** {msg}")
        else:
            st.markdown(f"**🤖 {sender}:** {msg}")
