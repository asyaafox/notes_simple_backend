import datetime
from typing import List
from sqlalchemy import select

from base import async_engine, Base
from models import UsersOrm
from sqlalchemy.ext.asyncio import AsyncSession
from dto import User, UserCreate

# from models import NotesOrm


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        print("Initialized the db")


async def all_users(session: AsyncSession) -> list[User]:
    query = select(UsersOrm)
    result = await session.execute(query)
    return [
        User(id=user.id, name=user.name, created_at=user.created_at)
        for user in result.scalars().all()
    ]


async def add_user(session: AsyncSession, user: UserCreate) -> User:
    new_user = UsersOrm(id=None, name=user.name, password=user.password)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return User(name=new_user.name, id=new_user.id, created_at=new_user.created_at)


async def fetch_user(session: AsyncSession, id: int) -> User:
    query = select(UsersOrm).where(UsersOrm.id == id)
    try:
        result = await session.execute(query)
        user = result.scalar_one()
        return User(id=user.id, name=user.name, created_at=user.created_at)
    except:
        return User(id=-1, name="Not found!", created_at=datetime.datetime.now())


async def delete_user(session: AsyncSession, id: int) -> bool:
    query = select(UsersOrm).where(UsersOrm.id == id)
    try:
        result = await session.execute(query)
        user = result.scalar_one()
        await session.delete(user)
        await session.commit()
        return True
    except:
        return False


async def update_user(session: AsyncSession, u: User) -> User:
    query = select(UsersOrm).where(UsersOrm.id == u.id)
    try:
        result = await session.execute(query)
        user = result.scalar_one()
        user.name = u.name
        await session.commit()
        return User(id=u.id, name=u.name, created_at=user.created_at)
    except:
        return User(id=-1, name="Not found!", created_at=datetime.datetime.now())
