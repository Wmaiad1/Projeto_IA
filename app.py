# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from agent import executor_agente
import uvicorn

app = FastAPI(title="API do Agente de IA", version="1.0")

# Esquema de dados para a requisição
class ChatRequest(BaseModel):
    mensagem: str
    historico: List[Dict[str, Any]] = []  # Formato: [{"role": "user", "content": "..."}, ...]

@app.post("/chat")
async def conversar_com_agente(request: ChatRequest):
    try:
        # Converter o histórico bruto vindo do Streamlit para o formato que o LangChain espera
        # Se preferir usar LangChain nativo, mapeie para HumanMessage e AIMessage
        chat_history = []
        for msg in request.historico:
            if msg["role"] == "user":
                chat_history.append(("human", msg["content"]))
            elif msg["role"] == "assistant":
                chat_history.append(("ai", msg["content"]))

        # Executa o agente passando a entrada atual e o histórico formatado
        resposta = executor_agente.invoke({
            "input": request.mensagem,
            "chat_history": chat_history
        })
        
        return {"resposta": resposta["output"]}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # Roda o servidor na porta 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
