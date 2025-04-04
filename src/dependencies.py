from sqlalchemy.ext.asyncio import AsyncSession

from database.database import async_session


async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session