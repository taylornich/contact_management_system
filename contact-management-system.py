import re

class contactSystem:

    def __init__(self):
        self.contacts = {}
# question 1 task 1
        print('''Welcome to the Contact Management System!
              Menu:
              1. Add a new contact
              2. Edit an existing contact
              3. Delete a contact
              4. Search for a contact
              5. Display all contacts
              6. Export contacts to a text file
              7. Quit''')
    
# question 1 task 2

    def add_contact(self): 
        email = input("Enter contact email address:")
        if email in self.contacts:
            print("A contact with this email already exists.")
            return
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        notes = input("Enter any additional information for this contact:")

        self.contacts[email] = {
            'Name' : name,
            'Phone number' : phone,
            'Additional information' : notes
        }
        print("Successfully added contact.")

    def edit_contact(self):
        try:
            email = input("Enter the email address of the contact you would like to edit: ")
            if email in self.contacts:
                name = input("Enter new name for this contact:")
                phone = input("Enter the new phone number for this contact: ")
                notes = input("Enter any information you would like to add to this contact: ")

                self.contacts[email] = {
                'Name' : name,
                'Phone number' : phone,
                'Additional information' : notes
                }

                print("Contact has been successfully edited.")
            else:
                print("Sorry, contact not found.")
        except Exception as UnexpectedError:
            print(f"An unexpected error occured while attempting to edit the contact: {UnexpectedError}")

    def delete_contact(self):
        try:
            email = input("Enter the email of the contact you would like to delete: ")
            if email in self.contacts:
                del self.contacts[email]
                print("Contact successfully deleted.")
            else:
                print("Sorry, contact not found.")
        except Exception as UnexpectedError:
            print(f"An unexpected error occurred while attempting to delete the contact: {UnexpectedError}")

    def contact_search(self):
        email = input("Enter the email of the contact you would like to search for: ")
        if email in self.contacts:
            contact = self.contacts[email]
            print(f"Name: {contact['Name']}, Phone: {contact['Phone number']}, Additional Information: {contact['Additional information']}.")

        else:
            print("Sorry, contact not found.")

    def display_all(self):
        try:
            if self.contacts: 
                for email, details in self.contacts.items():
                    print(f"Email: {email}, Name: {details['Name']}, Phone Number: {details['Phone number']}, Additional Information: {details['Additional information']}")
            else:
                print("No contacts found.")
        except Exception as UnexpectedError:
            print(f"An unexpected error occured whie trying to display all contact: {UnexpectedError}")

    def export_contacts(self):
        try:
            filename = input("Enter the file name to export your contacts to: ")
            with open(filename, 'w') as file:
                for email, details in self.contacts.items():
                    file.write(f"{email},{details['Name']}, {details['Phone Number']}, {details['Additional Information']}\n")
                print("Contacts exported successfully.")
        except IOError as ExportingError:
            print(f"an error occurred while exporting contacts: {ExportingError}")

# question 1 task 4
    def valid_email(self, email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email)
    
    def valid_phone_number(self, phone):
        phone_regex = r'^\+?\d{10,15}$'
        return re.match(phone_regex, phone)


    def run_program(self):
        while True:
            choice = input("What what you like to do? (Choose an option 1-7): ")

            if choice == '1':
                self.add_contact()
            elif choice =='2':
                self.edit_contact()
            elif choice =='3':
                self.delete_contact()
            elif choice == '4':
                self.contact_search()
            elif choice == '5':
                self.display_all()
            elif choice == '6':
                self.export_contacts()
            elif choice == '7':
                print("Quitting the Contact Management System. Bye!")
                break
            else:
                print("That is not a valid option choice, please choose a number between 1 and 7.")
if __name__ == "__main__":
    system_manager = contactSystem()
    system_manager.run_program()
