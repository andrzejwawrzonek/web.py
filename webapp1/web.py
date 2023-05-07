import streamlit as st
import functions


#colors = []


#"""def color_collect():
 #   color = st.session_state["color"] + "\n"
  #  colors = functions.get_todos()
   # colors.append(color)
    #functions.write_todos(colors, filepath="colors.txt")"""


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos = functions.get_todos()
    todos.append(new_todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My todo app")
st.subheader("This list is to increase your productivity.")
st.write("Todos")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Add your todo:", placeholder="Type here...", on_change=add_todo, key="new_todo")

#st.color_picker(label="Red", key="color")

# st.session_state











