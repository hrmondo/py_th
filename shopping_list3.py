import os


# Create a new empty list named shopping_list
shopping_list = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    #Shell cannot find Clear...why??-> case sensitive 


# Create a function named and add_to_list that declare the items
def add_to_list(item):
    # Add the item to the list
    show_list()
    if len(shopping_list):
        position = input("Where should I add {}?\n"
                    "Press ENTER to add to he end of the list \n"
                    "> ".format(item))
    else:    
        position = 0

    try:
        position = abs(int(position))

    except ValueError:
        position = None

    if position is not None:
        shopping_list.insert(position-1, item)
        
    else:
        shopping_list.append(new_item)

    show_list()


    print("Added* List has {} items".format(len(shopping_list)))
    show_list()

def show_list():
    clear_screen()
    print("Here is your list:")

    #did not want to make it 0
    index = 1
    for item in shopping_list:
        print("{}. {}".format(index, item))
        index += 1

    print("-"*10)


def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove? \n") 
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()


def show_help():
    clear_screen()
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' fot this help.
Enter 'SHOW' to show current items.
Enter 'REMOVE' to delete an item from your list
""")

    
show_help()

while True:
    new_item = input("> ")
    
    if new_item.upper() == "DONE" or new_item.upper() == "QUIT":
        break
    elif new_item.upper() == "HELP":
        show_help()
        continue
    elif new_item.upper() == "SHOW":
        show_list()
        continue
    elif new_item.upper() == "REMOVE":
        remove_from_list()
        continue

    else:
    # Call add_to_list with new item as an argument
        add_to_list(new_item)