import streamlit as st

from chatgpt_library import ChatGPT # Importando a biblioteca fictícia

 

# Inicializando a classe ou função com a chave da API

chatgpt_instance = ChatGPT(api_key="xxxxxxxx")

 

st.title("ChatGPT Interface")

 

user_input = st.text_input("Digite sua mensagem:")

 

if st.button("Enviar"):

    if user_input:

        # Fazendo a chamada à API através da biblioteca

        response = chatgpt_instance.query(user_input)

 

        # Exibindo a resposta

        st.write("Resposta do ChatGPT:", response)

    else:

        st.write("Por favor, digite uma mensagem.")




streamlit run app.py