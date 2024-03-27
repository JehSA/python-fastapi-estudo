from os import getenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
#import sqlalchemy.ext.asyncio as sa_async


DATABASE_URL = getenv('DATABASE_URL')


engine = create_async_engine(url=DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession)