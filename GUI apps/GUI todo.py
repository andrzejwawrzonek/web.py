import PySimpleGUI as sg
import functions


label = sg.Text("Type a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
todos_list = sg.Listbox(values=functions.get_todos(),
                        key="todos",
                        enable_events=True,
                        size=(45, 10))

window = sg.Window("My to-do app",
                   layout = [[label, input_box], [add_button], [todos_list, edit_button]],
                   font= ("Calibri", 10),)
                   # size=(1000,2000))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"

            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)

            todos[index] = new_todo

            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSED:
            break

window.close()