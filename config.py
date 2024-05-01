from dotenv import load_dotenv
import os 

load_dotenv()

LLM_URL = os.getenv("LLM_URL")
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME")