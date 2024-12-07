import uvicorn
from fastapi import FastAPI

from greet.lib import greet

app = FastAPI()

@app.get("/")
async def root():
    return {"message": greet()}

if __name__ == "__main__":
    uvicorn.run(app)
