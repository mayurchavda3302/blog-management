from .. import  schemas,models,hasing
from sqlalchemy.orm import  Session
from fastapi import HTTPException,status


def create_user(reqest:schemas.user,db:Session):
     new_user= models.User(name=reqest.name,email=reqest.email,password=hasing.Hash.bcrypt(reqest.password))
     db.add(new_user)
     db.commit()
     db.refresh(new_user)
     return  new_user


def getUser(id:int,db:Session):
    user=db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} is not present in database")
    return user
