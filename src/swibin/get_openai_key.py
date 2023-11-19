import os
from dotenv import load_dotenv

def get_key(root_dir):
  # check if key is already stored in .env

  # if not, prompt user for key and store in .env
  # return key
  dotenv_path = os.path.join(root_dir, '.env')
  load_dotenv(dotenv_path)

  if os.getenv('OPENAI_API_KEY'):
    return os.getenv('OPENAI_API_KEY')
  
  key = input("Enter your OpenAI API key: ")
  with open(dotenv_path, 'a') as f:
    f.write(f"\nOPENAI_API_KEY={key}")

  return key
