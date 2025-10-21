from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, acceso
from flask_login import UserMixin
from werkzeug.security import generate_password_hash as generar_hash_contraseña, check_password_hash as comprobar_hash_contr

class User(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    usuario: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    hash_contraseña: so.Mapped[str] = so.mapped_column(sa.String(256))

    def set_password(self, contraseña):
        self.hash_contraseña = generar_hash_contraseña(contraseña)

    def check_password(self, contraseña):
        return comprobar_hash_contr(self.hash_contraseña, contraseña)
    
    def __repr__(self):
        return '<User {}>'.format(self.usuario)


@acceso.user_loader
def load_user(user_id: str):
    try:
        return db.session.get(User, int(user_id))
    except Exception:
        return None
    
