import traceback
import ast
import os

def describe_error(e, args, kwargs):
    print("An error occurred: " + str(e) + "\n" + "\n")
    get_project_files(e)





def get_project_files(e):
    
    # stack trace
    stack_trace_list = traceback.format_exc().split("\n")

    # get all file names in order
    file_names = []
    for i, line in enumerate(stack_trace_list):
        if line.startswith("  File"):
            file_names.append(line.split(",")[0].split('"')[1])

    # standardize file names
    for i, file_path in enumerate(file_names):
        file_names[i] = file_path.replace("\\", "/")

    project_root = "/".join(file_names[1].split("/")[0:-1])


    # get all files in directory, recursively

    all_files_text = ""

    for file_path in search_directory(project_root):

        with open(file_path, 'r') as f:

            file_name = file_path.split("/")[-1]

            all_files_text += "\n\n" + file_name + "\n" + \
                "```python\n" + f.read() + "\n```"
    

        with open("text.txt", 'w') as f:
            f.write(all_files_text)

    



# recursively go through a directory and return a generator of all files
def search_directory(directory):
    for (dirpath, dirnames, filenames) in os.walk(directory):
        for filename in filenames:
            if (filename.endswith(".py")):
                yield os.path.join(dirpath, filename)
    




    # for i, line in enumerate(stack_trace_list):
    #     if line.startswith("  File"):
    #         # open file
    #         file_name = line.split(",")[0].split('"')[1]
    #         print(file_name)
    #         with open(file_name, 'r') as f:
    #             tree = ast.parse(f.read())
    #             for node in ast.walk(tree):
    #                 if isinstance(node, ast.FunctionDef):
    #                     print(node.name)
    #                     print(node.lineno)

            # get line number


    # print("An error occurred: " + str(e) + "\n" + "\n".join(stack_trace_list))

