# ui.py
import streamlit as st
import requests

# Configuração da página do Streamlit
st.set_page_config(page_title="Agente IA", page_icon="🤖", layout="centered")
st.title("🤖 W Trust IA")

# URL do endpoint do FastAPI
API_URL = "http://localhost:8000/chat"

# Inicializa o histórico de mensagens na sessão do Streamlit se não existir
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe as mensagens anteriores do histórico na tela
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Captura a nova mensagem digitada pelo usuário
if prompt := st.chat_input("Como posso te ajudar hoje?"):
    
    # 1. Adiciona e exibe a mensagem do usuário na UI
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Envia a requisição para o backend FastAPI
    with st.chat_message("assistant"):
        placeholder_resposta = st.empty()
        placeholder_resposta.markdown("Thinking...")
        
        payload = {
            "mensagem": prompt,
            "historico": st.session_state.messages[:-1] # Envia o histórico sem a última mensagem inserida
        }
        
        try:
            response = requests.post(API_URL, json=payload)
            
            if response.status_code == 200:
                texto_resposta = response.json().get("resposta", "Sem resposta da API.")
                placeholder_resposta.markdown(texto_resposta)
                
                # 3. Adiciona a resposta do assistente ao histórico da sessão
                st.session_state.messages.append({"role": "assistant", "content": texto_resposta})
            else:
                placeholder_resposta.markdown(f"❌ Erro na API: Código {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            placeholder_resposta.markdown("❌ Não foi possível conectar ao servidor FastAPI. Certifique-se de que o `app.py` está rodando.")
