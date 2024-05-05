from typing import List
from fastapi import APIRouter, Depends
from base import get_session
from dto import User
from sqlalchemy.ext.asyncio import AsyncSession

from orm import all_users

router = APIRouter(prefix="/api", tags=["Api"])


@router.get("/users", response_model=list[User])
async def get_all_users(session: AsyncSession = Depends(get_session)):
    return await all_users(session)
