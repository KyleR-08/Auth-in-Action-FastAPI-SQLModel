from fastapi import FastAPI
from sqlmodel import SQLModel
app = FastAPI()
class User(SQLModel):
    username: str
    password: str

db_users = [
    User(username="admin", password="admin"),
    User(username="user", password="user"),
    User(username="guest", password="guest"),
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/login")
def login(user: User):
    for u in db_users:
        if u.username == user.username and u.password == user.password:
            return {"message": "Login successful"}
    return {"message": "Invalid username or password"}