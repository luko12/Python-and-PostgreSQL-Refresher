from database import create_table, add_entry, get_entries

menu = """Please select an option:
1) add new entry
2) view entries
3) exit.

Your selection: """

welcome = "welcome to the programming diary!"


def prompt_new_entry():
    entry_content = input("what have you learned today? ")
    entry_date = input("enter the date: ")

    add_entry(entry_content, entry_date)

def view_entries(entries):
    for entry in entries:
        print(f"{entry[1]}\n{entry[0]}\n\n")

create_table()

while (user_input := input(menu)) != "3":
    # we'll deal with user input here...
    if user_input == "1":
        prompt_new_entry()
        
    elif user_input == "2":
        view_entries(get_entries())

        
    else:
        print("invalid option, please try again")
