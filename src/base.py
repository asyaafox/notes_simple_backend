from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from sqlalchemy.orm import DeclarativeBase


DATABASE_URL = "sqlite+aiosqlite:///notess.sqlite"
async_engine = create_async_engine(url=DATABASE_URL, echo=True)
async_session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):

    # / code from https://github.com/artemonsh/sqlalchemy_course
    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        """Relationships не используются в repr(), т.к. могут вести к неожиданным подгрузкам"""
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")
        return f"<{self.__class__.__name__} {', '.join(cols)}>"

    # / end
