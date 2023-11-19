import os
from dotenv import load_dotenv

def get_key():
  # check if key is already stored
  load_dotenv()

  if os.getenv("OPENAI_API_KEY") is not None:
    return os.getenv("OPENAI_API_KEY")

  key = input("Enter your OpenAI API key: ")
  # write to text file
  with open(".env", 'w') as f:
    f.write(f"OPENAI_API_KEY={key}")

  return key
