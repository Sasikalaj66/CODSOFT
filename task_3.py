class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        if name not in self.contacts:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print(f"Contact '{name}' added successfully.")
        else:
            print(f"Contact '{name}' already exists. Use the update function to modify details.")

    def view_contact_list(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}")

    def search_contact(self, query):
        results = []
        for name, info in self.contacts.items():
            if query.lower() in name.lower() or query in info['phone']:
                results.append((name, info['phone'], info['email'], info['address']))

        if not results:
            print("No matching contacts found.")
        else:
            print("Search Results:")
            for name, phone, email, address in results:
                print(f"Name: {name}, Phone: {phone}, Email: {email}, Address: {address}")

    def update_contact(self, name, new_phone, new_email, new_address):
        if name in self.contacts:
            self.contacts[name]['phone'] = new_phone
            self.contacts[name]['email'] = new_email
            self.contacts[name]['address'] = new_address
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone, email, address)

        elif choice == "2":
            contact_manager.view_contact_list()

        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            contact_manager.search_contact(query)

        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email address: ")
            new_address = input("Enter new address: ")
            contact_manager.update_contact(name, new_phone, new_email, new_address)

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)

        elif choice == "6":
            print("Exiting Contact Management System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
