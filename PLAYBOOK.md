# Playbook do Projeto de IA

## 1. Visão geral

Este projeto reúne uma interface de conversa em Streamlit, um backend em FastAPI e um agente com LangChain/OpenAI para responder perguntas de forma automatizada.

### Componentes principais
- `main.py`: interface principal do chat em Streamlit
- `app.py`: API FastAPI para receber mensagens e responder
- `agent.py`: configuração do agente e ferramentas
- `config.py`: carregamento da chave da API via variáveis de ambiente
- `UI.py`: alternativa de interface do frontend

## 2. Objetivo

Permitir que um usuário envie perguntas por uma interface web e receba respostas geradas por um agente de IA, com suporte a histórico de conversa e integração com OpenAI.

## 3. Pré-requisitos

- Python 3.11+
- Git
- Conta e chave da OpenAI
- Ambiente virtual habilitado

## 4. Setup inicial

### 4.1 Criar ambiente virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4.2 Instalar dependências

```powershell
python -m pip install --upgrade pip
python -m pip install -e .
```

### 4.3 Configurar a chave da API

Crie um arquivo `.env` na raiz do projeto com o conteúdo:

```env
OPENAI_API_KEY=sua_chave_aqui
```

> O projeto usa `python-dotenv` para carregar essa variável automaticamente.

## 5. Como executar o projeto

### 5.1 Rodar a API

No terminal, na raiz do projeto:

```powershell
python app.py
```

A API ficará disponível em:
- http://localhost:8000

### 5.2 Rodar a interface principal

Em outro terminal:

```powershell
streamlit run main.py
```

A interface abrirá no navegador em um endereço local do Streamlit.

### 5.3 Rodar a interface alternativa

Também é possível usar:

```powershell
streamlit run UI.py
```

## 6. Fluxo operacional padrão

1. Verificar se a variável `OPENAI_API_KEY` está definida.
2. Iniciar o backend com `python app.py`.
3. Iniciar a interface com `streamlit run main.py`.
4. Digitar uma pergunta na tela.
5. A aplicação envia a mensagem para a API.
6. O agente processa a pergunta e retorna a resposta.

## 7. Endpoints e uso

### 7.1 Endpoint principal

`POST /chat`

Payload esperado:

```json
{
  "mensagem": "Qual é a previsão do tempo em São Paulo?",
  "historico": [
    {"role": "user", "content": "Oi"},
    {"role": "assistant", "content": "Olá! Como posso ajudar?"}
  ]
}
```

Resposta esperada:

```json
{
  "resposta": "Resposta do agente"
}
```

## 8. Checklist de validação

Antes de entregar ou testar o projeto, confirme:

- [ ] Ambiente virtual ativado
- [ ] Dependências instaladas
- [ ] Arquivo `.env` presente
- [ ] Chave `OPENAI_API_KEY` válida
- [ ] Backend rodando sem erros
- [ ] Frontend conectado à API
- [ ] Pergunta simples respondida corretamente

## 9. Troubleshooting

### Problema: "OPENAI_API_KEY não foi encontrada"

- Verifique se o arquivo `.env` existe na raiz
- Confirme se a variável está escrita corretamente
- Reinicie o terminal após editar o `.env`

### Problema: falha ao conectar ao backend

- Confirme se `python app.py` está em execução
- Verifique se a porta 8000 está livre
- Teste o endpoint com:

```powershell
curl http://localhost:8000
```

### Problema: módulo não encontrado

Execute:

```powershell
python -m pip install -e .
```

### Problema: erro de importação do LangChain/OpenAI

- Verifique a versão do Python
- Reinstale as dependências do projeto
- Confirme que o ambiente virtual está ativo

## 10. Comandos úteis

```powershell
# ativar ambiente
.\.venv\Scripts\Activate.ps1

# instalar projeto localmente
python -m pip install -e .

# iniciar backend
python app.py

# iniciar frontend
streamlit run main.py
```

## 11. Boas práticas

- Mantenha a chave da API fora do repositório
- Use um ambiente virtual para cada projeto
- Teste a API antes de usar a interface
- Faça backups de alterações importantes em git
- Mantenha o histórico de conversa controlado para evitar prompts excessivamente longos

## 12. Observações importantes

Este projeto ainda está em evolução e há mais de uma interface e uma versão do agente na base. Para evitar conflitos em produção, mantenha uma convenção clara:

- `main.py` = interface principal
- `UI.py` = interface alternativa ou de teste
- `app.py` = backend oficial
- `agent.py` = agente principal

## 13. Próximo passo recomendado

Padronizar o projeto em um único fluxo de execução, por exemplo:

- Frontend em `main.py`
- Backend em `app.py`
- Agente em `agent.py`
- Configuração centralizada em `config.py`

Esse ajuste reduz ambiguidades entre as interfaces e facilita manutenção e operação.
