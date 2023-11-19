import sys
import subprocess
from openai import OpenAI
import glob
import os
import platform

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

def explain_error_with_gpt(error_message):
    client = OpenAI(api_key='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')

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a python expert that gives specific code suggestions."},
                {"role": "user", "content": f"Understand the following exception, along with all of the associated functions. Explain what might have caused it and suggest possible fixes. Mention line numbers and function names if applicable. Be concise:\n\n{error_message}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error in contacting OpenAI API: {str(e)}"

def run_script(script_path, custom_prompt=""):
    try:
        output = subprocess.check_output([sys.executable, script_path], stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        error_output = e.output.decode()
        print(error_output)
        env_details = get_and_format_environment_details()
        all_files_contents = get_python_files_contents(script_path)
        print(all_files_contents)
        combined_input = f"{custom_prompt}\n\nError Output:\n{error_output}\n\nEnvironment Details:\n{env_details}\n\nPython Files Contents:\n{all_files_contents}"
        explanation = explain_error_with_gpt(combined_input)
        print(explanation)

def main():
    if len(sys.argv) < 2:
        print("Usage: mhacks-run <script_path>")
        sys.exit(1)

    script_path = sys.argv[1]
    custom_prompt = sys.argv[2] if len(sys.argv) > 2 else ""
    run_script(script_path, custom_prompt)
