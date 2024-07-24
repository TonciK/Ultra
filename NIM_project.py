import os
import streamlit as st
from openai import OpenAI
import asyncio

# Read API key from the secrets file
api_key = st.secrets["NVIDIA"]["api_key"]

# Set up the NVIDIA API client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key
)


# Function to get a response from the Llama 3.1 model asynchronously
async def get_response(input_dict):
    try:
        completion = await asyncio.to_thread(
            client.chat.completions.create,
            model="meta/llama-3.1-8b-instruct",
            messages=[{"role": "user", "content": input_dict["question"]}],
            temperature=0.2,
            top_p=0.7,
            max_tokens=1024,
            stream=False
        )

        # Debugging: print the response
        # print(completion)

        # Access the content correctly
        response_message = completion.choices[0].message.content
        return response_message
    except Exception as e:
        # Debugging: print the exception message
        # print(f"API call failed: {e}")
        return f"API call failed: {e}"


# Streamlit app layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Tonci")

with col2:
    st.image("images/StreamCB.png")

st.write(" ")
st.title("2 weeks ago we had a party in city:")
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
st.title("Ask Llama about Ultra...")

# User asking questions (prompt)
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
