# from fastapi import FastAPI
# import asyncio
# import time


# app = FastAPI()

# @app.get("/async-example")
# async def async_test():
#     await asyncio.sleep(5)
#     return {"message": "This is Asynchronous"}



# @app.get("/sync-example")
# def sync_test():

#     time.sleep(5)
#     return {"message": "This is Sequential"}


##################################


from fastapi import FastAPI
import requests
import time 
import httpx

app = FastAPI()

@app.get("/sync-example")
def sync_test():
    start_time = time.perf_counter()

    for i in range(1, 5):
        response = requests.get(f"https://api.restful-api.dev/objects/{i}")
        

    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return {"message": "Sync Function", "execution_time": execution_time}

@app.get("/async-example")
async def async_test():
    async with httpx.AsyncClient() as client:
        start_time = time.perf_counter()
        for i in range(1, 5):
            response = await client.get(f"https://api.restful-api.dev/objects/{i}")
    
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        return {"message": "Async Function", "execution_time": execution_time}

