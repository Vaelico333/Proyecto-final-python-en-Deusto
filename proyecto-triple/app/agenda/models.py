from app.extensions import db

class Contact(db.Model):
    __tablename__ = 'contactos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(9), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)

    def __repr__(self):
        return f'<Contact {self.name}>'