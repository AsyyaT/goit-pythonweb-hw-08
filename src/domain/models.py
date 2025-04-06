from sqlalchemy import Integer, String, Date
from db import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String, unique=True)
    phone: Mapped[str] = mapped_column(String)
    birthday: Mapped[date] = mapped_column(Date)
    additional_info: Mapped[str] = mapped_column(String, nullable=True)
