from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import db

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }