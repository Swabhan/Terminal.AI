import traceback

def describe_error(e):
    return "An error occurred: " + str(e) + "\n" + traceback.format_exc()