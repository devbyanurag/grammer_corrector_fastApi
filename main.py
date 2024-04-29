from fastapi import FastAPI
from app.routers import content_generation_service
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(content_generation_service.router, prefix="/textGen")



@app.get("/")
async def test_api():
    return {"message": "FastAPI is working!"}