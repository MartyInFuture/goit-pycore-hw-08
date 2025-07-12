from entities.address_book import AddressBook
import pickle

def main():
    book = load_data()
    print("Welcome to the assistant bot!")

    commands = {
        "add": book.add_contact,
        "add_contact": book.add_contact,

        "add_phone": book.add_phone_to_record,

        "change": book.change_phone,
        "change_phone": book.change_phone,

        "change_contact_name": book.change_contact_name,

        "phone": book.get_contact_phone_list,
        "get_phone_list": book.get_contact_phone_list,

        "get_all": book.get_all,
        "all": book.get_all,

        "get_contact": book.get_record_by_name,

        "add_birthday": book.add_birthday_to_record,
        "add-birthday": book.add_birthday_to_record,

        "show_birthday": book.show_birthday,
        "show-birthday": book.show_birthday,

        "upcoming_birthdays": book.get_upcoming_birthdays,
        "birthdays": book.get_upcoming_birthdays,
    }

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break

        elif command == "hello":
            print("How can I help you?")

        elif command in commands:
            result = commands[command](*args)
            if result is not None:
                print(result)

        else:
            print("Invalid command.")

def save_data(book, filename='address_book.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(book, file)

def load_data(filename='address_book.pkl'):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()

def parse_input(user_input):
    parts = user_input.strip().split()
    command = parts[0].lower() if parts else ""
    args = parts[1:] if len(parts) > 1 else []
    return command, *args


if __name__ == "__main__":
  main()
