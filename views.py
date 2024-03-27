from fastapi import APIRouter, HTTPException
from services import UserService, FavoriteService
from schemas import (
    UserCreateInput, StandardOutput, ErrorOutput, UserFavoriteAddInput                     
)


user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')


@user_router.post('/create', description='My description test', response_model=StandardOutput, responses={400: {'model':ErrorOutput}})
async def user_create(user_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_input.name)
        return StandardOutput(message='OK')
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
    
@user_router.delete('/delete/{user_id}', response_model=StandardOutput, responses={400: {'model':ErrorOutput}})
async def user_delete(user_id: int):
    try:
        await UserService.delete_user(user_id)
        return StandardOutput(message='OK')
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
    
@user_router.post('/favorite/add', response_model=StandardOutput, responses={400: {'model':ErrorOutput}})
async def user_favorite_add(favorite_add: UserFavoriteAddInput):
    try:
        await FavoriteService.add_favorite(user_id=favorite_add.user_id, symbol=favorite_add.symbol)
        return StandardOutput(message='OK')
    except Exception as error:
        raise HTTPException(400, detail=str(error))