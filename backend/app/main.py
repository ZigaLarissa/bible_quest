from fastapi import FastAPI

from routers import users

import uvicorn

app = FastAPI()

app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Bible Questions API"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)