# Contact Book System

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)
        print(f"Contact {name} added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts in the contact book.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    def search_contact(self):
        search_term = input("Enter name or phone number: ")
        found = False
        for contact in self.contacts:
            if contact.name == search_term or contact.phone_number == search_term:
                print(f"Contact found: Name: {contact.name}, Phone Number: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
                found = True
                break
        if not found:
            print("Contact not found.")

    def update_contact(self):
        name = input("Enter name of contact to update: ")
        for contact in self.contacts:
            if contact.name == name:
                print("Enter new details (leave blank to keep current):")
                phone_number = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                if phone_number:
                    contact.phone_number = phone_number
                if email:
                    contact.email = email
                if address:
                    contact.address = address
                print(f"Contact {name} updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self):
        name = input("Enter name of contact to delete: ")
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully!")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            contact_book.add_contact()
        elif choice == '2':
            contact_book.view_contact_list()
        elif choice == '3':
            contact_book.search_contact()
        elif choice == '4':
            contact_book.update_contact()
        elif choice == '5':
            contact_book.delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()