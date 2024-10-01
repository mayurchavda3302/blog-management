from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import user,blog,Authentication


models.Base.metadata.create_all(engine)
"""
here .metadata.create_all use for create modules like table,database and other things..


"""

app=FastAPI()
app.include_router(Authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
