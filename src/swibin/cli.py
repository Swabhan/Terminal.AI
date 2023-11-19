import sys
import subprocess
from openai import OpenAI
import glob
import os
import platform
from .get_openai_key import get_key
from .color import generation_color, color_terminal_code_blocks


def get_and_format_environment_details():
    python_version = sys.version
    operating_system = platform.platform()
    installed_packages = subprocess.getoutput("pip list")
    formatted_details = f"Python Version: {python_version}\n" + \
                        f"Operating System: {operating_system}\n" + \
                        f"Installed Packages:\n{installed_packages}"
    return formatted_details

def get_python_files_contents(script_path):
    script_dir = os.path.dirname(script_path)
    python_files = glob.glob(os.path.join(script_dir, '**', '*.py'), recursive=True)
    files_contents = ""
    for file in python_files:
        with open(file, 'r') as f:
            files_contents += f"\nFile: {os.path.basename(file)}\n\n"
            files_contents += f.read() + "\n"
    return files_contents


def explain_error_with_gpt(error_message, script_path):
    script_dir = os.path.dirname(script_path)
    api_key = get_key(script_dir)
    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": "You are a python expert that gives specific code suggestions."},
                {"role": "user", "content": f"{error_message}\n\nUnderstand the following exception, along with all of the associated functions. Explain what might have caused it and suggest possible fixes. Mention line numbers and include code blocks. When using line numbers. Be concise and specific."}
            ],
            stream=True
        )

        print(generation_color, end="")
        for chunk in response:
            print(color_terminal_code_blocks(chunk.choices[0].delta.content), end="")

    except Exception as e:
        print(f"Error in contacting OpenAI API: {str(e)}")



def run_script(script_path, custom_prompt=""):
    try:
        output = subprocess.check_output([sys.executable, script_path], stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        error_output = e.output.decode()

        # color red
        print("\033[91m", end="")
        print(error_output)
        env_details = get_and_format_environment_details()
        all_files_contents = get_python_files_contents(script_path)
        combined_input = f"Environment Details:\n{env_details}\n\nPython Files Contents:\n{all_files_contents}\n\nError Output:\n{error_output}\n\n{custom_prompt}"

        explain_error_with_gpt(combined_input, script_path)
        print("\033[0m")

def main():
    if len(sys.argv) < 2:
        print("Usage: mhacks-run <script_path>")
        sys.exit(1)

    script_path = sys.argv[1]
    custom_prompt = sys.argv[2] if len(sys.argv) > 2 else ""
    run_script(script_path, custom_prompt)
