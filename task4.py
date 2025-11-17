def parse_input(user_input: str) -> tuple[str, list[str]]:
    """
    Розбирає введений рядок на команду та аргументи.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args: list[str], contacts: dict) -> str:
    """
    Додає новий контакт до словника.
    """
    try:
        name, phone = args
        # Використовуємо lower() для нечутливості до регістру імен
        contacts[name.lower()] = phone
        return "Contact added."
    except ValueError:
        return "Invalid command. Usage: add [name] [phone]"

def change_contact(args: list[str], contacts: dict) -> str:
    """
    Змінює існуючий контакт у словнику.
    """
    try:
        name, new_phone = args
        name_low = name.lower()
        if name_low in contacts:
            contacts[name_low] = new_phone
            return "Contact updated."
        else:
            return f"Contact '{name}' not found."
    except ValueError:
        return "Invalid command. Usage: change [name] [new_phone]"

def show_phone(args: list[str], contacts: dict) -> str:
    """
    Показує номер телефону для вказаного контакту.
    """
    try:
        name = args[0]
        name_low = name.lower()
        if name_low in contacts:
            # Повертаємо ім'я у форматі Capitalized для гарного вигляду
            return f"{name.capitalize()}'s phone: {contacts[name_low]}"
        else:
            return f"Contact '{name}' not found."
    except IndexError:
        return "Invalid command. Usage: phone [name]"

def show_all(contacts: dict) -> str:
    """
    Показує всі збережені контакти.
    """
    if not contacts:
        return "No contacts saved."
    
    # Форматуємо вивід
    output = "All contacts:\n"
    for name, phone in contacts.items():
        # Використовуємо .capitalize() для гарного відображення
        output += f"  {name.capitalize()}: {phone}\n"
    return output.strip()

def main():
    """
    Головний цикл роботи бота.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    
    # Цикл запит-відповідь
    while True:
        user_input = input("Enter a command: ").strip()
        
        # Обробка порожнього вводу
        if not user_input:
            continue
            
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()