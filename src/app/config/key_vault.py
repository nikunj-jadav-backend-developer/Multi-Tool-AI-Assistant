import os

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

KEYVAULT_URL = os.getenv("KEYVAULT_URL")

credential = DefaultAzureCredential()

client = SecretClient(
    vault_url=KEYVAULT_URL,
    credential=credential,
)


def get_secret(secret_name: str) -> str:
    return client.get_secret(secret_name).value