import traceback
import ast

def describe_error(e, args, kwargs):

    # stack trace
    stack_trace_list = traceback.format_exc().split("\n")

    for i, line in enumerate(stack_trace_list):
        if line.startswith("  File"):
            # open file
            file_name = line.split(",")[0].split('"')[1]
            print(file_name)
            with open(file_name, 'r') as f:
                tree = ast.parse(f.read())
                print(type(tree))

            # get line number


    # print("An error occurred: " + str(e) + "\n" + "\n".join(stack_trace_list))

