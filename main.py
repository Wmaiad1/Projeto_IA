import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from openai import OpenAIError

from config import OPENAI_API_KEY


st.set_page_config(page_title="Agente de IA", page_icon="🤖")
#st.logo("logo.png", size="large")
st.title("🤖 NADIA IA")
st.caption("Agente de inteligência artificial para responder perguntas de forma concisa.")
st.caption("Converse com seu assistente de inteligência artificial.")

if not OPENAI_API_KEY:
    st.error(
        "A chave OPENAI_API_KEY não foi encontrada. "
        "Defina-a no arquivo .env ou nas variáveis de ambiente."
    )
    st.stop()


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

pergunta = st.chat_input("Digite sua pergunta...")

if pergunta:
    st.session_state.messages.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)

    mensagens = [
        SystemMessage(
            content="Responda as perguntas de forma curta, no máximo 140 caracteres."
        ),
        *[
            AIMessage(content=message["content"])
            if message["role"] == "assistant"
            else HumanMessage(content=message["content"])
            for message in st.session_state.messages
        ],
    ]

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                modelo = ChatOpenAI(
                    model="gpt-3.5-turbo",
                    api_key=OPENAI_API_KEY,
                    temperature=0.7,
                    max_tokens=150,
                )
                resposta = modelo.invoke(mensagens)
            except OpenAIError as error:
                st.error(f"Não foi possível obter uma resposta da OpenAI: {error}")
            else:
                st.markdown(resposta.content)
                st.session_state.messages.append(
                    {"role": "assistant", "content": resposta.content}
                )
