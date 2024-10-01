from sqlalchemy.orm import Session
from ..import models,schemas
from fastapi import HTTPException,status


def  get_all(db:Session):
      """
      here get_all use for  get all blogs from database

      para:db:Session

      db:database connection
      """
      blog=db.query(models.Blog).all()
      return  blog


def Create_blog(reqest:schemas.Blog,db:Session):
    """
    use for create  blog 

    para: reqest:schemas.Blog
      -> user need to give  blog  class

    para: db:session
     use for database connection
     
       
    """
    new_blog=models.Blog(title=reqest.title,body=reqest.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def show(id:int,  db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog for {id} is not available')
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'detail':f'blog for {id} is not available'}
        
    return  blog




def destroy(id,db:Session):
     blog=db.query(models.Blog).filter(models.Blog.id == id).first()
     if  not blog:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with {id} is not  present in database")
     
     db.delete(blog)
     db.commit()
     return {"blog deleted sucesfully"}
   

def update(id:int,reqest:schemas.Blog,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with {id} is not found")
    blog.update(reqest.dict())
    db.commit()
    return "Updated"
