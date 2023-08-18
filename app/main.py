from fastapi import FastAPI
import models
from config import engine
import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# @app.get("/")
# async def root_url():
#     return {"message": "vishal prajapati"}


app.include_router(router.router, prefix="/books", tags=["book"])