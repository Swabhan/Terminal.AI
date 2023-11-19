import sys

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

def colorOutput(prompt, keywords):
    for i in keywords:
        prompt = prompt.replace(i, f"{Fore.RED}{i}{Style.RESET_ALL}")

    return prompt

keywords = ["line", "syntax", "compile time", "run time", "error"]
prompt = "On line 19, there is a syntax error causing a compile time error. To resolve this, ..."

print(colorOutput(prompt, keywords))