import os
from dotenv import load_dotenv

def get_key(root_dir):

  # Load .env file if it exists
  dotenv_path = os.path.join(root_dir, '.env')
  print(dotenv_path)

  # get the current working directory
  root_dir = os.getcwd()
  print(root_dir)

  os.environ.clear()

  load_dotenv(dotenv_path)

  if os.getenv('OPENAI_API_KEY'):
    print("returning", os.getenv('OPENAI_API_KEY'))
    return os.getenv('OPENAI_API_KEY')
  
  key = input("Enter your OpenAI API key: ")

  with open(dotenv_path, 'a') as f:
    f.write(f"\nOPENAI_API_KEY={key}")

  print(key)
  return key
