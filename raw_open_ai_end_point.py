import requests , os , streamlit as st
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
#define the API endpoint for chat completions
end_point = 'https://api.openai.com/v1/chat/completions'

#define the headers for the API request
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}
st.title("Raw OpenAI API Example")
st.write("####Author : - Kuntal")
question = st.text_input("Ask a question to OpenAI:")


#payload for the API request
payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}
    ],
    "max_tokens": 100,
    "temperature": 0.7
}

if question:
    with st.spinner("Generating response..."):
        #make the API request
        response = requests.post(end_point, headers=headers, json=payload)

        #check if the request was successful
        if response.status_code == 200:
            data = response.json()
            st.write(data['choices'][0]['message']['content'])
        else:
            st.write(f"Error: {response.status_code} - {response.text}")