from openai import OpenAI
import streamlit as st

#Reading the openai key and setting up the client
f = open("keys/OpenAI Key.txt")
key = f.read()
client = OpenAI(api_key=key)
#the titl for the app
st.title("GenAI App: Code Debugger App")
st.subheader("Find the bugs in your python code and make it corrected by this app")

#Taking user input and generating the required response

prompt = st.text_area("Enter the code snippet")
if st.button("Fix the Code") == True:

    response = client.chat.completions.create(
        model = "gpt-3.5-turbo-0613",
        messages=[
             {"role": "system","content": """ you are a helpful AI Assistant. 
             Given a python code review it for the bugs it contains and mention the bugs and generate the correct code snippet for same code"""},

            {"role":"user", "content":prompt}
        ]
    )  

#Printing the response generated
    st.write(response.choices[0].message.content)

