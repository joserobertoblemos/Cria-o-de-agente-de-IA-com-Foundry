import os

from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient


# ==========================================
# 1. CARREGAR CONFIGURAÇÕES
# ==========================================

load_dotenv()

project_endpoint = os.getenv("PROJECT_ENDPOINT")
agent_name = os.getenv("AGENT_NAME")


if not project_endpoint:
    raise ValueError(
        "PROJECT_ENDPOINT não foi encontrado no arquivo .env"
    )

if not agent_name:
    raise ValueError(
        "AGENT_NAME não foi encontrado no arquivo .env"
    )


# ==========================================
# 2. CONECTAR AO MICROSOFT FOUNDRY
# ==========================================

print("Conectando ao Microsoft Foundry...")

project = AIProjectClient(
    endpoint=project_endpoint,
    credential=DefaultAzureCredential(),
)


# ==========================================
# 3. OBTER CLIENTE DO AGENTE
# ==========================================

print(f"Conectando ao agente: {agent_name}")

openai = project.get_openai_client(
    agent_name=agent_name
)


# ============================================================
# 4. CRIAR CONVERSA
# ============================================================

conversation = openai.conversations.create()

print("\nConversa criada com sucesso!")
print(f"Conversation ID: {conversation.id}")


# ============================================================
# 5. PRIMEIRA PERGUNTA
# ============================================================

pergunta1 = "Quais são as regras de frequência mínima para aprovação?"

print("\nAluno:")
print(pergunta1)

response1 = openai.responses.create(
    conversation=conversation.id,
    input=pergunta1
)

print("\nAssistente:")
print(response1.output_text)


# ============================================================
# 6. SEGUNDA PERGUNTA — TESTE DE MEMÓRIA
# ============================================================

pergunta2 = "E se eu faltar, como devo justificar minha ausência?"

print("\nAluno:")
print(pergunta2)

response2 = openai.responses.create(
    conversation=conversation.id,
    input=pergunta2
)

print("\nAssistente:")
print(response2.output_text)