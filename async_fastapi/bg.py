import asyncio
from fastapi import FastAPI, BackgroundTasks


app = FastAPI()

async def long_task():
    for i in range(5):
        await asyncio.sleep(1)
        with open("log.txt", "a") as log_file:
            log_file.write(f"Task {i} completed\n")



@app.post("/bg-task")
async def bg_task(background_task : BackgroundTasks):
    background_task.add_task(long_task)
    return {"message": "Task scheduled"}