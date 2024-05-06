from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    name: str
    # email: str | None


class User(UserBase):
    id: int
    created_at: datetime
    # notes: list["Note"]


class UserCreate(UserBase):
    password: str


class NotesBase(BaseModel):
    name: str
    text: str
    author: int


class NoteCreate(NotesBase):
    name: str
    text: str
    author: int


class Note(NotesBase):
    id: int
    created_at: datetime
    updated_at: datetime
