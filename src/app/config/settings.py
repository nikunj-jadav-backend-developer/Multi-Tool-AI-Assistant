import os

from dotenv import load_dotenv

load_dotenv()

APP_ENV = os.getenv("APP_ENV", "development")

LLM_MODEL = os.getenv("LLM_MODEL", "llama-3.1-8b-instant")

TEMPERATURE = float(os.getenv("TEMPERATURE", "0.4"))

KEYVAULT_URL = os.getenv("KEYVAULT_URL")

if APP_ENV == "production":
    from app.config.key_vault import get_secret

    GROQ_API_KEY = get_secret("groq-api-key")
    OPEN_WEATHER_API_KEY = get_secret("open-weather-api-key")
    TAVILY_API_KEY = get_secret("tavily-api-key")
else:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")