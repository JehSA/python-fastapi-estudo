from pydantic import BaseModel

class UserCreateInput(BaseModel):
    name: str

class UserFavoriteAddInput(BaseModel):
    user_id: int
    symbol: str

class StandardOutput(BaseModel):
    message: str

class ErrorOutput(BaseModel):
    details: str