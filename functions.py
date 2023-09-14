FILEPATH = "todo.txt"

def get_todos(filepath=FILEPATH):
    """This funtion returns items in a textfile divided by \n as a list"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """Write the todo item list in a textfile"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_local)
