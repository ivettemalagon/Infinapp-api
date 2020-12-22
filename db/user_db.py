from typing import  Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str
    
database_users = Dict[str, UserInDB]

database_users = {
    "Ivette": UserInDB(**{"username":"Ivette", 
                            "password":"root"}),
    "Brenda": UserInDB(**{"username":"Brenda", 
                            "password":"hola"}),
    "Wilson": UserInDB(**{"username":"Wilson", 
                            "password":"azul"}),
    "Sandra": UserInDB(**{"username":"Sandra", 
                            "password":"mora"}),
    "David": UserInDB(**{"username":"David", 
                            "password":"1234"}),    
}


def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else: 
        return None
    
def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db