from fastapi import FastAPI, Depends
from db import get_db
from sqlalchemy.orm import Session
from schema import *
from service import *
app = FastAPI()


@app.get("/")
def health_check():
    return {"msg":"health check passed"}


@app.get("/user")
def get_user(username: str,db: Session = Depends(get_db)):
    data = get_user_from_db(username=username,db=db)
    return data


@app.post("/user")
def create_user(item: UserCreateSchema, db: Session = Depends(get_db)):
    message = create_user_in_db(data=item,db=db)
    return message

@app.put("/password")
def change_password(username: str,item:UserUpdateSchema, db: Session = Depends(get_db)):
    message = change_password_in_db(current_username = username,data=item,db=db)
    return message


@app.delete("/user")
def delete_user(item:UserDeleteSchema, db: Session = Depends(get_db)):
    message = delete_user_in_db(data=item,db=db)
    return message