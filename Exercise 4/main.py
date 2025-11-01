
"""
Implements a simple contact book with commands:
  - hello -> prints greeting
  - add <name> <phone>
  - change <name> <new_phone>
  - phone <name>
  - show_all / all
  - exit / close
"""

def parse_input(user_input: str):
    
    if not user_input:
        return None, []
    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(contacts: dict, name: str, phone_number: str):
    key = name.lower()
    contacts[key] = (name, phone_number)
    return "Contact added."


def change_contact(contacts: dict, name: str, new_phone_number: str):
    key = name.lower()
    if key in contacts:
        original_name, _ = contacts[key]
        contacts[key] = (original_name, new_phone_number)
        return("Contact updated.") 
    else:
        return("Contact was not found.")


def show_phone(contacts: dict, name: str):
    key = name.lower()
    if key in contacts:
        _, phone_number = contacts[key]
        return phone_number
    else:
        return "The contact was not found."


def show_all(contacts: dict):
    if not contacts:
        print("There are no any contacts.")
        return
    for _, (display_name, phone_number) in contacts.items():
        return (f"{display_name} : {phone_number}")



def main():
    
    contacts = {}
    print("Welcome to the assistant bot!")
    
    start_of_program = input("Please enter Hello to start: ").strip().lower()
    if start_of_program == "hello":
        print("How can I help you?")
    else:
        print("I do not understand you.") 

 
    while True:

        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command is None:
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
       
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            name, phone_number = args
            print(add_contact(contacts, name, phone_number))
        elif command == "change":
            name, phone_number = args
            print(change_contact(contacts, name, phone_number))
        elif command == "phone":
            name = args[0]
            print(show_phone(contacts, name))
        elif command == "all" or "show_all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

        

if __name__ == "__main__":
    main()
