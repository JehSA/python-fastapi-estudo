from database.models import User
from database.connection import async_session

class UserService:
    async def create_user(name):
        async with async_session() as session:
            session.add(User(name=name))
            await session.commit()