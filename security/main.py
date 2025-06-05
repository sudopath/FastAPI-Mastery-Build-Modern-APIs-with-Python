# from pydantic import BaseModel
# from fastapi import FastAPI, HTTPException

# class Item(BaseModel):
#     name : str
#     description : str
#     price : float
#     tax: float = None


# app = FastAPI()

# @app.post('/items/')
# async def create_item(item: Item):
#     return {"name": item.name, "description": item.description}

# @app.get('/items/{item_id}')
# async def read_item(item_id: int):
#     items_db = [1,2]
#     if item_id not in items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"items": items_db[item_id]}



from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError

app  = FastAPI()

class User(BaseModel):
    name :str
    age: int


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=400, 
        content={"message":"Custom Validation Error", "detail": exc.errors()}
        )


@app.post("/validate/")
async def create_user(data: dict):
    user = User.validate(data)
    return {"message": "User is Valid", "user":user}