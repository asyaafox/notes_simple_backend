import asyncio
import uvicorn
from orm import create_tables, all_users
from base import async_session_factory
from models import UsersOrm


async def test_add_users():
    async with async_session_factory() as session:
        admin = UsersOrm(name="eee", email="sussy@baka.com")
        tiii = UsersOrm(name="bebebe")
        session.add(tiii)
        session.add(admin)
        await session.flush()
        await session.commit()


async def t():
    async with async_session_factory() as session:
        await all_users(session)


async def main():
    await create_tables()
    await test_add_users()
    await t()

    # await test_add_users()


asyncio.run(main())
# uvicorn.run(app="src.main:app", reload=True)


"""
def create_fastapi_app():
    app = FastAPI(title="FastAPI")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
    )
        
    @app.get("/workers", tags=["Кандидат"])
    async def get_workers():
        workers = SyncORM.convert_workers_to_dto()
        return workers
        
    @app.get("/resumes", tags=["Резюме"])
    async def get_resumes():
        resumes = await AsyncORM.select_resumes_with_all_relationships()
        return resumes
    
    return app
    

app = create_fastapi_app()


if __name__ == "__main__":
    asyncio.run(main())
    if "--webserver" in sys.argv:
        uvicorn.run(
            app="src.main:app",
            reload=True,
        )
"""
