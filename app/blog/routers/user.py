from fastapi import APIRouter,status,Depends,HTTPException
from sqlalchemy.orm import Session
from ..import schemas,models,database,hasing
from typing import List
from ..repository import user

router=APIRouter(   
    prefix='/user',
    tags=['User'],
)
get_db=database.get_db


@router.post('/',response_model=schemas.ShowUser)
def create_user(reqest:schemas.user,db:Session=Depends(get_db)):
     return   user.create_user(reqest,db)


@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session=Depends(get_db)):
    return user.getUser(id,db)
