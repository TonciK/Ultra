import os
import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import asyncio

# Set up the environment path for Ollama if provided
ollama_path = os.environ.get('OLLAMA_PATH')
if ollama_path:
    os.environ["PATH"] += os.pathsep + ollama_path

# Initialize the model and chain once and store in session state
if "llm" not in st.session_state:
    try:
        st.session_state.llm = Ollama(model="llama2")
        print("Model initialized successfully")
    except Exception as e:
        print(f"Model initialization failed: {e}")

if "chain" not in st.session_state:
    try:
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "You are a helpful assistant. Please respond to the questions"),
                ("user", "Question:{question}")
            ]
        )
        st.session_state.chain = prompt | st.session_state.llm
        print("Chain created successfully")
    except Exception as e:
        print(f"Chain creation failed: {e}")

# Streamlit app layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Tonci")

with col2:
    st.image("images/StreamCB.png")

st.write(" ")
st.title("Last weekend we had party in city")
st.image("images/Ultra.png")

st.write(" ")
st.write(" ")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Check this on YT...")
    st.write("ULTRA - the best music festival!")

with col2:
    st.video("https://youtu.be/0aI8GxmD5bI?si=C0ye3g2SJAB2P_-Y")

st.write(" ")
st.title("Ultra Europe Gallery")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("images/U03.jpg")
with col2:
    st.image("images/U06.jpg")
with col3:
    st.image("images/U04.jpg")

st.write(" ")
st.title("Wanna know more about Ultra?")

# Function to handle user questions asynchronously
async def get_response(input_dict):
    try:
        response = await asyncio.to_thread(st.session_state.chain.invoke, input_dict)
        return response
    except Exception as e:
        return f"Chain invocation failed: {e}"

# User interaction for asking questions
user_question = st.text_input("Ask me about electronic music festival in Split, Croatia...or anything else...")
if st.button("SEND the QUESTION", use_container_width=True):
    if user_question:
        input_dict = {"question": user_question}
        with st.spinner('Processing...'):
            response = asyncio.run(get_response(input_dict))
            st.write("Response:", response)
    else:
        st.write("Please enter a question to get a response.")

st.write(" ")
st.title("Feel Ultra 2024 in Split, Croatia")
st.slider("MUSIC", 0, 100, 50)
st.slider("ENERGY", 0, 100, 50)
st.slider("JOY", 0, 100, 50)

st.write(" ")
st.write(" ")
st.write("CONTACT")
st.title("Let's stay in contact!")
linkedin_link = f'<a href="https://www.linkedin.com/in/tonci-kaleb-7917528/" target="_blank">LinkedIn</a>'

if st.button("View my LinkedIn profile"):
    st.write(linkedin_link, unsafe_allow_html=True)
