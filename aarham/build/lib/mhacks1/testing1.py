import sys
import subprocess
import openai
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
    openai.api_key = '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'
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Explain the following Python error and suggest possible solutions:\n\n{error_message}"}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error in contacting OpenAI API: {str(e)}"

def run_script(script_path, custom_prompt=""):
    try:
        output = subprocess.check_output([sys.executable, script_path], stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        error_output = e.output.decode()
        print("titanic")
        print(error_output)
        print("titanic")
        env_details = get_and_format_environment_details()
        all_files_contents = get_python_files_contents(script_path)
        combined_input = f"{custom_prompt}\n\nError Output:\n{error_output}\n\nEnvironment Details:\n{env_details}\n\nPython Files Contents:\n{all_files_contents}"
        explanation = explain_error_with_gpt(combined_input)
        print(explanation)
        print("titanic")

def main():
    if len(sys.argv) < 2:
        print("Usage: mhacks-run <script_path>")
        sys.exit(1)

    script_path = sys.argv[1]
    custom_prompt = sys.argv[2] if len(sys.argv) > 2 else ""
    run_script(script_path, custom_prompt)

if __name__ == "__main__":
    main()
