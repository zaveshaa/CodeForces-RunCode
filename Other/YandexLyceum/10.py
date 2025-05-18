from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.schema import ForeignKey

Base = declarative_base()


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    chief = Column(Integer, ForeignKey('users.id'))
    members = Column(Text)
    email = Column(String(255), unique=True, nullable=False)

    head = relationship("User", back_populates="departments_led")
