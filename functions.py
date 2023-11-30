def get_todos(filename='todolist.txt'):
    """Reads the content from the text file"""
    with open(filename, 'r') as file_read:  # reads the file and the content of the file
        todos_local = file_read.readlines()
    return todos_local


def write_todos(todos_arg, filename="todolist.txt"):
    """Writes the todo list from the text file as the output"""
    with open(filename, 'w') as file_write:
        file_write.writelines(todos_arg)
        