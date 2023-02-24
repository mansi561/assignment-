todos = []  
def list_todos():
    if todos:
        print("To-Do List:")
        for i, todo in enumerate(todos):
            print(f"{i+1}. {todo}")
    else:
        print("Your To-Do list is empty.")
def add_todo():
    new_todo = input("Enter a new To-Do item: ")
    todos.append(new_todo)
    print(f"'{new_todo}' has been added to your To-Do list.")
def delete_todo():
    list_todos()
    if todos:
        while True:
            try:
                todo_num = int(input("Enter the number of the To-Do item to delete: "))
                if todo_num < 1 or todo_num > len(todos):
                    print("Invalid input. Please enter a number between 1 and", len(todos))
                else:
                                        
                        break
                    except ValueError:
                print("Invalid input. Please enter a number between 1 and", len(todos))
            deleted_todo = todos.pop(todo_num - 1)
print(f"'{deleted_todo}' has been deleted from your To-Do list.")

else:

print("Your To-Do list is already empty.")
def edit_todo():
    list_todos()
    if todos:
        while True:
            try:
                todo_num = int(input("Enter the number of the To-Do item to edit: "))
                if todo_num < 1 or todo_num > len(todos):
                    print("Invalid input. Please enter a number between 1 and", len(todos))

                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and", len(todos))
        edited_todo = input(f"Enter a new value for '{todos[todo_num-1]}': ")
        todos[todo_num-1] = edited_todo
        print(f"'{edited_todo}' has replaced '{todos[todo_num-1]}' in your To-Do list.")
    else:
        print("Your To-Do list is empty.")
while True:
    print("\nWhat would you like to do? Type 'list', 'add', 'delete', 'edit', or 'quit'.")
    action = input().lower()
    if action == "list":
        list_todos()
    elif action == "add":
        add_todo()
    elif action == "delete":
        delete_todo()
        edit_todo()
    elif action == "quit":
        break
    else:
        print("Invalid input. Please try again.")

        






