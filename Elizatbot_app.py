import streamlit as st
import openai

openai.api_key = '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'

st.title('OpenAI Chatbot')

user_input = st.text_input('Olá! Sou a terapia cômica. Do que você precisa hoje?')

if st.button('Enviar'):
    persona = "Você é um chatbot de psicologia. Responda de modo cômico para as pessoas que buscam por ajuda."
    instructions = f"{persona}\nUsuário: {user_input}\nChatbot:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=instructions,
        max_tokens=200
    )

    st.text(response.choices[0].text.strip())
