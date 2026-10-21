# agent.py
import os
from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool

# 1. Definição de ferramentas (Tools) exemplo
@tool
def obter_previsao_tempo(localidade: str) -> str:
    """Retorna a previsão do tempo para uma determinada cidade ou localidade."""
    # Exemplo mockado. Em produção, chamaria uma API externa (ex: OpenWeather)
    return f"O tempo em {localidade} está ensolarado com 25°C."

# 2. Configuração do Agente
def inicializar_agente():
    # Certifique-se de ter a variável de ambiente OPENAI_API_KEY configurada
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    tools = [obter_previsao_tempo]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente virtual prestativo e focado em resolver problemas."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    agent = create_openai_functions_agent(llm, tools, prompt)
    
    # Retorna o executor do agente
    return AgentExecutor(agent=agent, tools=tools, verbose=True)

# Instância global do executor para uso no app.py
executor_agente = inicializar_agente()
