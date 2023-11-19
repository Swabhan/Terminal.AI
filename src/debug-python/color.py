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






generation_color = Fore.WHITE

is_code_block = False

def color_terminal_code_blocks(text):
    # replace all instances of ``` with green color

    for char in text:
        if char == '`':
            global is_code_block
            is_code_block = not is_code_block
            if is_code_block:
                text = text.replace('`', Fore.CYAN + '`', 1)
            else:
                text = text.replace('`', generation_color + '`', 1)

    return text
