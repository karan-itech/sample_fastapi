from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(
    title="My FastAPI App",
    description="A simple FastAPI application running on AWS Lambda.",
    version="0.1.0",
)

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI on AWS Lambda!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

# Mangum handler to wrap the FastAPI app for AWS Lambda
handler = Mangum(app, lifespan="off")
