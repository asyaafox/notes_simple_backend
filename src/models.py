import datetime, enum
from typing import Annotated

from sqlalchemy import ForeignKey, String, text
from base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[
    datetime.datetime, mapped_column(server_default=text("current_timestamp"))
]
updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("current_timestamp"),
        onupdate=text("current_timestamp"),
    ),
]


class UsersOrm(Base):
    __tablename__ = "Users"
    id: Mapped[intpk]
    name: Mapped[str]
    created_at: Mapped[created_at]
    email: Mapped[str | None] = String(128)
    password: Mapped[str] = String(128)
    notes: Mapped[list["NotesOrm"]] = relationship(back_populates="author")


class NotesOrm(Base):
    __tablename__ = "Notes"
    id: Mapped[intpk]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    name: Mapped[str]
    text: Mapped[str]
    author: Mapped["UsersOrm"] = relationship(back_populates="notes")
    author_id: Mapped[int] = mapped_column(ForeignKey("Users.id", ondelete="CASCADE"))
