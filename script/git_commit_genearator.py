import logging
from openai import OpenAI
from config import LLM_API_KEY,LLM_URL,LLM_MODEL_NAME
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

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

git_diff = sys.stdin.read()
prompt = f"""参考如下 git commit示例,针对我的git diff生成一个git commit，git commit 示例： 
fix(release): need to depend on latest rxjs and zone.js
The version in our package.json gets copied to the one we publish, 
and users need the latest of these.
我的git diff 如下：{git_diff}"""

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
