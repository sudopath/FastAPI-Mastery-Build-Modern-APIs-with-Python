from fastapi import FastAPI, Depends
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from app.security import create_access_token, verify_token, create_access_token_with_role


app = FastAPI()


# class User(BaseModel):
#     username :str
#     password : str

class User(BaseModel):
    username :str
    password : str
   

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):

    fake_user = User(username = form_data.username, password = form_data.password)

    if fake_user.username == "user" and fake_user.password == "password":
        #access_token = create_access_token(data={"sub": fake_user.username})
        access_token = create_access_token_with_role(data={"sub": fake_user.username}, role="admin")
        return {"access_token": access_token, "token_type": "bearer"}
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"}
    )


@app.get("/protected")
async def protected(token: str = Depends(verify_token)):
    return {"message": "Hello, protected endpoint!"}


