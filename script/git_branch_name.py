import logging
from openai import OpenAI
from config import LLM_API_KEY,LLM_URL,LLM_MODEL_NAME
import sys
# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
  base_url=LLM_URL,
  api_key=LLM_API_KEY,
)

# with open(sys.argv[1]) as f:
#   content = f.read()
#   content = content.replace("\n", "")
git_commit_message = sys.stdin.read()
prompt = f"""根据我给的git commit信息:{git_commit_message},生成一个新的分支名"""
# completion = client.chat.completions.create(
#   model="microsoft/wizardlm-2-8x22b",
#   messages=[
#     {
#       "role": "user",
#       "content": "帮我用python写个代码，实现ES对索引别名的管理，需要使用设计模式",
#     },
#   ],
# )
if LLM_MODEL_NAME is None:
  logging.error("LLM_MODEL_NAME is None")
completion = client.chat.completions.create(
  model=LLM_MODEL_NAME,
  messages=[
    {
      "role": "user",
      "content": prompt
    },
  ],
)
print(completion.choices[0].message.content)
