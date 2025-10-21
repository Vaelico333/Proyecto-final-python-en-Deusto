import unittest
from app import create_app, db
from app.agenda.models import Contact

class AgendaTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_contact(self):
        contact = Contact(name='John Doe', phone='123456789', email='john@example.com')
        db.session.add(contact)
        db.session.commit()
        self.assertEqual(Contact.query.count(), 1)
        self.assertEqual(Contact.query.first().name, 'John Doe')

    def test_read_contact(self):
        contact = Contact(name='Jane Doe', phone='987654321', email='jane@example.com')
        db.session.add(contact)
        db.session.commit()
        retrieved_contact = Contact.query.first()
        self.assertEqual(retrieved_contact.name, 'Jane Doe')

    def test_update_contact(self):
        contact = Contact(name='John Smith', phone='123456789', email='john@example.com')
        db.session.add(contact)
        db.session.commit()
        contact.phone = '111222333'
        db.session.commit()
        updated_contact = Contact.query.first()
        self.assertEqual(updated_contact.phone, '111222333')

    def test_delete_contact(self):
        contact = Contact(name='John Doe', phone='123456789', email='john@example.com')
        db.session.add(contact)
        db.session.commit()
        db.session.delete(contact)
        db.session.commit()
        self.assertEqual(Contact.query.count(), 0)

if __name__ == '__main__':
    unittest.main()