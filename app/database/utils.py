from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.settings import Database


def get_connection_string(db: Database, async_fallback: bool = False) -> str:
    result = (
        f"postgresql+asyncpg://{db.login}:{db.password}@{db.host}:{db.port}/{db.name}"
    )
    
    if async_fallback:
        result += "?async_fallback=True"

    return result


def session_getter(db_url):
    engine = create_async_engine(db_url)
    session_factory = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async def get_db_session() -> AsyncSession:
        session: AsyncSession = session_factory()
        try:
            yield session
        finally:
            await session.close()

    return get_db_session