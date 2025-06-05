from fastapi import FastAPI
from utils import generate_text


app = FastAPI()

@app.post("/generate/")
async def generate_text_endpoint(prompt: str):
    response = generate_text(prompt)
    return {"prompt": prompt, "generated_text": response}