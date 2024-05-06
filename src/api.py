from typing import List
from fastapi import APIRouter, Depends
from base import get_session
from dto import User, UserCreate
from sqlalchemy.ext.asyncio import AsyncSession

from orm import all_users, add_user, fetch_user, delete_user, update_user

router = APIRouter(prefix="/api", tags=["Api"])


@router.get("/users", response_model=list[User])
async def get_all_users(session: AsyncSession = Depends(get_session)):
    return await all_users(session)


@router.post("/add_user", response_model=User)
async def post_add_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    return await add_user(session, user)


@router.get("/get_user", response_model=User)
async def get_user_by_id(id: int, session: AsyncSession = Depends(get_session)):
    return await fetch_user(session, id)


@router.delete("/delete_user", response_model=bool)
async def delete_user_by_id(id: int, session: AsyncSession = Depends(get_session)):
    return await delete_user(session, id)


@router.put("/update_user", response_model=User)
async def put_update_user(user: User, session: AsyncSession = Depends(get_session)):
    return await update_user(session, user)
