contacts = {}
while True:
    choice = input("1. Add, 2. Search, 3.List, 0. Quit: ")
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        if name not in contacts:
            contacts[name] = []
        contacts[name].append(phone)
    elif choice == "2":
        name = input("Enter name to search: ")
        print(contacts.get(name, "Contact not found."))
    elif choice == "3":
        for name in sorted(contacts):
            print(f"{name}: {', '.join(contacts[name])}")
    elif choice == "0":
        break
          