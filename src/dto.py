from pydantic import BaseModel
import datetime


class UserBase(BaseModel):
    name: str
    email: str | None


class User(UserBase):
    created_at: datetime.datetime
    notes: list["Note"]


class UserCreate(UserBase):
    password: str


class NotesBase(BaseModel):
    id: int
    name: str
    text: str
    author: int


class NoteCreate(NotesBase):
    name: str
    text: str
    author: int


class Note(NotesBase):
    created_at: datetime.datetime
    updated_at: datetime.datetime
