import asyncio
from fastapi import FastAPI
import uvicorn
from orm import create_tables, all_users
from base import async_session_factory
from models import UsersOrm
from api import router as api_router


async def test_add_users():
    async with async_session_factory() as session:
        admin = UsersOrm(name="eee", email="sussy@baka.com")
        tiii = UsersOrm(name="bebebe")
        session.add(tiii)
        session.add(admin)
        await session.flush()
        await session.commit()


# async def mainn():
#     # await test_add_users()
# asyncio.run(mainn())
# uvicorn.run(app="src.main:app", reload=True, port=8081)

"""
async def test():
    await create_tables()
    await test_add_users()
    async with async_session_factory() as session:
        await all_users(session)
asyncio.run(test())
"""

app = FastAPI(title="notes")
app.include_router(api_router)


@app.on_event("startup")
async def startup_event():
    await create_tables()
    await test_add_users()


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
