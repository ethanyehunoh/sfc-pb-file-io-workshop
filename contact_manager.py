import json
import io

"""
Note: This is designed to hold a list of contacts as a list of dictionaries.
An alternative approach is to build a "Contact" class to represent a contact.
If you would like to do that as a Bonus exercise, that would be good way
to practice using OOP and composition!
"""


class ContactManager:
    """Class to do CRUD operations on the list of contacts"""

    def __init__(self, file="data.json"):
        self.file = file
        self.contacts = []

    def load_contacts(self):
        """Loads contacts from a JSON file and converts them to a list of
        dictionaries     
        Bonus: What should happen if the file isn't there?
                What should happen if the file has invalid JSON in it?
        """
        with io.open(self.file, "r") as file:
            self.contacts = json.load(file)
        return self.contacts
    

    def add_contact(self, contact):
        """Adds a contact to the list, and saves the file"""
        self.contact = contact
        self.contacts.append(self.contact)

        with io.open(self.file, "w") as file:
            json.dump(self.contacts, file)

        
    def update_contact(self, contact_to_update):
        """
        Updates a contact and saves the file

        Bonus: What happens when the id doesn't exist?
        """
        updated_contacts = []
        target_id = contact_to_update["id"]
        self.contact_to_update = contact_to_update

        for contact in self.contacts:
            if contact["id"] == target_id:
                updated_contacts.append(self.contact_to_update)
            else:
                updated_contacts.append(contact)

        self.contacts = updated_contacts

        with io.open(self.file, "w") as file:
            json.dump(self.contacts, file)



    def delete_contact(self, id_to_delete):
        """
        Deletes a contact and saves the file

        Bonus: What happens when the id doesn't exist?
        """
        contacts_to_keep = []
        target_id = id_to_delete
        self.id_to_delete = id_to_delete

        for contact in self.contacts:
            if contact["id"] != target_id:
                contacts_to_keep.append(contact)

        self.contacts = contacts_to_keep

        with io.open(self.file, "w") as file:
            json.dump(self.contacts, file)


