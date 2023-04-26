import functions

todos = []


while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("What todo you want to add?: ") + "\n"
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

            print("Ok. You added", todo.strip('\n'), ".")
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            new_todos = []

            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)

            for index, todo in enumerate(new_todos):
                row = f"{index + 1}.{todo}"
                print(row)
        case 'edit':
            number = int(input("Type a number of todo to edit: "))
            new_todo = input("What todo you want to add instead?: ")
            todos[number] = new_todo
            print("Ok, success. You added", new_todo)
        case 'complete':
            """completed_todo = input("Type a todo you have completed: ")
            todos.remove(completed_todo)"""
            number_of_completed_todo = int(input("Type a number of todo you have completed: "))
            completed_todo = todos[number_of_completed_todo - 1]
            todos.remove(completed_todo)
            print("You've deleted", completed_todo)
        case 'exit':
            print("Bye!")
            break
        case _:
            print("No demanded function in program.")



