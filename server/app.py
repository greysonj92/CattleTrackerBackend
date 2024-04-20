from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routes.animal import router as CattleRouter

app = FastAPI()
app.include_router(CattleRouter, tags=["Cattle"], prefix="/cattle")

origins = [
    #"http://localhost:3000"
    "*"
]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to FastAPI!"}
