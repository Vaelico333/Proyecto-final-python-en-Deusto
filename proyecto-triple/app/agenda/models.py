import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from ..models import User

class Contact(db.Model):
    __tablename__ = 'contactos'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id))
    email: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
    nombre: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
    telefono: so.Mapped[int] = so.mapped_column(sa.String(9), index=True)

    def __repr__(self):
        return f'<Contact {self.name}>'