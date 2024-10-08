from models import User
from schema import *
from sqlalchemy.orm import Session
from fastapi import HTTPException
from exceptions import UserNotFoundException

def get_user_from_db(*,username: str, db: Session):
    user = db.query(User).filter(User.username==username).first()
    if not user:
        raise UserNotFoundException()
    return {"username":user.username}


def create_user_in_db(*,data: UserCreateSchema, db: Session):
    new_user = User(username=data.username,password=data.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg":"new user is created"}


def change_password_in_db(*,current_username:str,data: UserUpdateSchema,db: Session):
    is_correct_user = db.query(User).filter_by(username=current_username,password=data.password).first()
    if not is_correct_user:
        raise UserNotFoundException()
    db.query(User).update({"password":data.new_password})
    db.commit()
    return {"msg":"password is changed"}
    
def delete_user_in_db(*, data: UserDeleteSchema,db: Session):
    user_in_db = db.query(User).filter(User.username==data.username).first()
    if not user_in_db:
        raise UserNotFoundException()
    db.delete(user_in_db)
    db.commit()
    return {"msg":"user is deleted"}