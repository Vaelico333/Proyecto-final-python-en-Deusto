from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, acceso
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash 

class User(db.Model, UserMixin):
    __tablename__ = 'usuarios'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    nombre: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=False)
    apellidos: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=False)
    telefono: so.Mapped[int] = so.mapped_column(sa.Integer(), index=True, unique=False)
    edad: so.Mapped[int] = so.mapped_column(sa.Integer(), index=True, unique=False)
    hash_contraseña: so.Mapped[str] = so.mapped_column(sa.String(256))

    def set_password(self, contraseña):
        self.hash_contraseña = generate_password_hash(contraseña)

    def check_password(self, contraseña):
        return check_password_hash(self.hash_contraseña, contraseña)
    
    def update_user(self, user_id, new):
        update = self.query.filter(self.id == user_id).update(new)
        db.session.commit()
        return update
    
    def delete(self, user_id):
        delete = db.session.query(User).filter(User.id == user_id).delete()
        db.session.commit()
        return delete
    
    def __repr__(self):
        return '<User {}>'.format(self.nombre)


@acceso.user_loader
def load_user(user_id: str):
    try:
        return db.session.get(User, int(user_id))
    except Exception:
        return None
    
