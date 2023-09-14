import streamlit as st
import functions as f

todos = f.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"]
    existing_todos = f.get_todos()

    if new_todo + "\n" not in existing_todos:
        existing_todos.append(new_todo + "\n")
        f.write_todos(existing_todos)
    st.session_state.new_todo = ""

st.title("My-Todo App")
st.subheader("This is my todo-app")
st.write("This is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        print(todos)
        f.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
    #print(todos)
st.text_input(label="Enter a todo", placeholder="Add a new todo...", key="new_todo", on_change=add_todo)
