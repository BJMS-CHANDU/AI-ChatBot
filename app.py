import streamlit as st
import ollama

st.set_page_config(
    page_title="Friendly AI",
    page_icon="😇",
    layout="centered"
)

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 10% 20%, rgba(255,255,255,0.12) 0%, transparent 25%),
        radial-gradient(circle at 90% 80%, rgba(255,255,255,0.10) 0%, transparent 25%),
        linear-gradient(135deg, #0f172a, #1e1b4b, #312e81, #4c1d95);
    min-height: 100vh;
}

.title {
    text-align: center;
    color: #ffffff;
    font-size: 50px;
    font-weight: 800;
    margin-top: 50px;
    margin-bottom: 10px;
    text-shadow: 0 4px 15px rgba(0,0,0,0.25);
}

.subtitle {
    text-align: center;
    color: #ddd6fe;
    font-size: 20px;
    margin-bottom: 40px;
}

.info {
    text-align: center;
    color: #c4b5fd;
    font-size: 17px;
    margin-bottom: 20px;
}

.stTextInput label {
    color: #ffffff !important;
    font-size: 17px !important;
    font-weight: 600 !important;
}

.stTextInput input {
    background: rgba(255,255,255,0.10) !important;
    color: white !important;
    border: 1px solid rgba(255,255,255,0.3) !important;
    border-radius: 16px !important;
    padding: 16px !important;
    font-size: 16px !important;
    backdrop-filter: blur(10px);
}

.stTextInput input::placeholder {
    color: #c4b5fd !important;
}

.stButton {
    display: flex;
    justify-content: center;
}

.stButton button {
    background: linear-gradient(90deg, #8b5cf6, #ec4899);
    color: white;
    border: none;
    border-radius: 15px;
    padding: 12px 35px;
    font-size: 18px;
    font-weight: bold;
    box-shadow: 0 8px 20px rgba(139,92,246,0.35);
    transition: 0.3s;
}

.stButton button:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 25px rgba(236,72,153,0.4);
}

.response {
    background: rgba(255,255,255,0.95);
    padding: 25px;
    border-radius: 20px;
    border-left: 6px solid #a78bfa;
    margin-top: 30px;
    color: #29223d;
    font-size: 17px;
    line-height: 1.7;
    box-shadow: 0 10px 35px rgba(0,0,0,0.25);
}

.footer {
    text-align: center;
    color: #c4b5fd;
    margin-top: 45px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🤖 Friendly AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">💬 Your friendly AI assistant for questions, learning and ideas</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="info">✨ Ask me anything — I am here to help you!</div>',
    unsafe_allow_html=True
)

question = st.text_input(
    "💡 What would you like to know?",
    placeholder="Example: Explain Artificial Intelligence in simple words..."
)

if st.button("🚀 Ask Friendly AI"):

    if question.strip():

        with st.spinner("🤖 Friendly AI is thinking..."):

            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "system",
                        "content": """
You are Friendly AI, a kind, funny and helpful AI assistant.

Help users with:
- Study and education
- Coding and programming
- Mathematics
- Writing
- Resume and career
- Project ideas
- General knowledge
- Everyday questions

Always explain things simply, clearly and positively.
Be friendly and encouraging.
Give examples when useful.
"""
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

        answer = response["message"]["content"]

        st.markdown(
            '<div class="response">'
            '<b>🤖 Friendly AI says:</b><br><br>'
            + answer +
            '</div>',
            unsafe_allow_html=True
        )

    else:
        st.warning("😊 Please type a question first!")

st.markdown(
    '<div class="footer">💜 Friendly AI • Powered by Ollama + Llama 3.2</div>',
    unsafe_allow_html=True
)