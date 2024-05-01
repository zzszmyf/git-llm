import logging
from openai import OpenAI
from config import LLM_API_KEY,LLM_URL,LLM_MODEL_NAME
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if __name__ == "__name__":
  if LLM_API_KEY == "" or LLM_API_KEY == None:
      logging.error("Please set the LLM_API_KEY environment variable.")
      sys.exit(1)
  if LLM_URL == "" or LLM_URL == None:
      logging.error("Please set the LLM_URL environment variable.")
      sys.exit(1)
  client = OpenAI(
    base_url=LLM_URL,
    api_key=LLM_API_KEY,
  )

  git_commit_message = sys.stdin.read()
  prompt = f"""根据我给的git commit信息:{git_commit_message},生成一个新的分支名"""

  if LLM_MODEL_NAME is None or LLM_MODEL_NAME == "":
    logging.error("LLM_MODEL_NAME is None")
    exit()
  completion = client.chat.completions.create(
    model=LLM_MODEL_NAME,
    messages=[
      {
        "role": "user",
        "content": prompt
      },
    ],
  )
  logging.info(completion.choices[0].message.content)
