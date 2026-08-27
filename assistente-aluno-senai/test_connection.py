import os

from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient


load_dotenv()

project_endpoint = os.getenv("PROJECT_ENDPOINT")

if not project_endpoint:
    raise ValueError(
        "A variável PROJECT_ENDPOINT não foi encontrada no arquivo .env"
    )

print("Endpoint encontrado:")
print(project_endpoint)

print("\nConectando ao Microsoft Foundry...")

project = AIProjectClient(
    endpoint=project_endpoint,
    credential=DefaultAzureCredential(),
)

print("Conexão com o projeto estabelecida com sucesso!")