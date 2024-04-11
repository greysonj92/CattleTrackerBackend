from fastapi import FastAPI
from server.routes.animal import router as CattleRouter

app = FastAPI()
app.include_router(CattleRouter, tags=["Cattle"], prefix="/cattle")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to FastAPI!"}