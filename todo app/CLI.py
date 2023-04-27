from Modules import functions

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

        print("Ok. You added", todo.strip('\n'), ".")
    elif user_action.startswith('show'):
        todos = functions.get_todos()

        new_todos = []

        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)

        for index, todo in enumerate(new_todos):
            row = f"{index + 1}.{todo}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            todo_number = int(user_action[5:]) - 1
            new_todo = input("What todo you want to add instead?: ")
            todos = functions.get_todos()
            todos[todo_number] = new_todo
            functions.write_todos(todos)
            print("Ok, success. You added", new_todo)
        except IndexError:
            print("To-do doesn't exist.")
    elif user_action.startswith('complete'):
        try:
            completed_todo = int(user_action[9:]) - 1
            todos = functions.get_todos()
            completed_todo_name = todos[completed_todo]

            todos.pop(completed_todo)

            functions.write_todos(todos)
            print("You've deleted", completed_todo_name)
        except IndexError:
            print("To-do doesn't exist.")
    elif user_action.startswith('exit'):
        print("Bye!")
        break
    else:
        print("No demanded function in program.")



