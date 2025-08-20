import unittest
from src.organisation import Organisation
from src.contact import Contact

<<<<<<< HEAD
# Step 1
class TestOrganisation(unittest.TestCase):
    # test that we create a name
    def test_create_organisation(self):
        org = Organisation('NM Tafe')
        self.assertEqual(org.name, 'NM Tafe')

    def test_add_contact(self):
        # arrange
        org = Organisation('NM Tafe')
        contact = Contact('John', 'test@example.com')

        # act
        org.add_contact(contact)
        #assert
        self.assertIn(contact, org.get_contacts())

    # def test_get_contacts(self):
        

if __name__ == '__main__':
    unittest.main()
=======
from src.contact import Contact
from src.organisation import Organisation

# Create an organization
class TestOrganisation(unittest.TestCase):
    # test that we create a name
    # arrange
    def test_add_organisation(self):
        # act
        org = Organisation('Johns Org')
        # assert
        self .assertEqual(org.name, 'Johns Org')

    # pass

    # Step 3 - test can add a contact
    def test_can_add_a_contact(self):
        # Create an organisation
        org = Organisation('Johns Org')
        # Create a contact
        contact = Contact('John', 'test@example.com')
        # Add contact to organisation
        org.add_contact(contact)
        # Check if contact is added to the organisation
        self.assertIn(contact, org.contacts)
>>>>>>> upstream/2025S2
