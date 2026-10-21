import streamlit as st 

def app():
    st.set_page_config(page_title="NADIA - Agente de IA", page_icon="🤖")
    st.header("NADIA - Agente de IA", divider=True)
    st.write(
        "Bem-vindo, sou a NADIA, seu assistente de inteligência artificial. "
        "Digite sua pergunta abaixo e receba respostas rápidas e precisas.")

    mensagem_usuario = st.chat_input("Digite sua pergunta:")
    if mensagem_usuario:
        if 'mensagens' in st.session_state:
            mensagens = st.session_state['mensagens']
        else:
            mensagens = []  
            st.session_state['mensagens'] = mensagens

        # adiciona a mensagem do usuário à lista de mensagens
        mensagens.append({"role": "user", "content": mensagem_usuario})

        # exibe a mensagem de resposta da IA - Assistente
        mensagens.append({"role": "assistant", "content": "Estou processando sua pergunta..."})
        #st.chat_message("assistant").write("Estou processando sua pergunta...")

        for mensagem in mensagens:
            # colocar a mensagem do usuario na tela
            st.chat_message(mensagem["role"]).write(mensagem["content"])
app()

