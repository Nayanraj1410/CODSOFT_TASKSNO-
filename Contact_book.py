contacts = []

def show_menu():
    print("\n--- Contact Management Menu ---")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        sorted_contacts = sorted(contacts, key=lambda c: c['name'].lower())
        for i, c in enumerate(sorted_contacts, start=1):
            print(f"{i}. {c['name']} - {c['phone']}")

def search_contact():
    keyword = input("Enter name or phone number to search: ")
    found = False
    for c in contacts:
        if c['name'] == keyword or c['phone'] == keyword:
            print("\nContact Found:")
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    view_contacts()
    if not contacts:
        return
    index = int(input("Enter contact number to update: "))
    if 1 <= index <= len(contacts):
        c = contacts[index-1]
        print("Leave blank to keep existing value.")
        name = input(f"Enter new name ({c['name']}): ") or c['name']
        phone = input(f"Enter new phone ({c['phone']}): ") or c['phone']
        email = input(f"Enter new email ({c['email']}): ") or c['email']
        address = input(f"Enter new address ({c['address']}): ") or c['address']
        contacts[index-1] = {"name": name, "phone": phone, "email": email, "address": address}
        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")

def delete_contact():
    view_contacts()
    if not contacts:
        return
    index = int(input("Enter contact number to delete: "))
    if 1 <= index <= len(contacts):
        contacts.pop(index-1)
        print("Contact deleted successfully!")
    else:
        print("Invalid contact number.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting Contact Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
