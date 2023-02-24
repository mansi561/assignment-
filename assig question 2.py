to_do_list = []
def display_to_do():
    if len(to_do_list) == 0:
        print("No To-Do items found!")
    else:
        print("To-Do List:")
        for i, item in enumerate(to_do_list):
            print(f"{i+1}. {item}")
    print()
    def add_to_do():
            item = input("Enter a new To-Do item: ")
    to_do_list.append(item)
    print(f"'{item}' added to To-Do list.")
    print()
def delete_to_do():
    display_to_do()
    item_index = int(input("Enter the index of the To-Do item to delete: ")) - 1
    if 0 <= item_index < len(to_do_list):
        item = to_do_list.pop(item_index)
        print(f"'{item}' deleted from To-Do list.")
    else:
        print("Invalid index!")
    print()
def edit_to_do():
    display_to_do()
    item_index = int(input("Enter the index of the To-Do item to edit: ")) - 1
    if 0 <= item_index < len(to_do_list):
        new_item = input("Enter the new item: ")
        to_do_list[item_index] = new_item
        print(f"'{new_item}' replaced '{to_do_list[item_index]}' in To-Do list.")
    else:
        print("Invalid index!")
print()
print("Welcome to the To-Do List App!")
while True:
        print("Choose an option:")
        print("1. List all To-Do")
        print("2. Add a To-Do")
        print("3. Delete a To-Do"
        print("4. Edit a To-Do")    
        print("5. Quit")
    option = int(input("Enter your choice: "))
    if option == 1:
        display_to_do()
        add_to_do()
    elif option == 3:
        delete_to_do()
    elif option == 4:
        edit_to_do()
    elif option == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please choose again.")




