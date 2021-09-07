import uvicorn, logging, os
from fastapi import FastAPI, Path
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from core.config.config import Config
from constants import LOG_DIR, CONFIG_FILE_PATH
from core.routes.profiles import router as ProfilesRouter
from core.routes.messages import router as MessagesRouter
#ToDo logging


app = FastAPI(title="Twitter miner")
app.include_router(ProfilesRouter, prefix='/api/profile', tags=["Profile"])
app.include_router(MessagesRouter, prefix='/api/message', tags=["Message"])
#! CORS

origins = [
    "http://localhost",
    "http://localhost:10000",
    "http://127.0.0.1:10000",
    "http://127.0.0.1"
]
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#! Set app config
config = Config(yaml_file=CONFIG_FILE_PATH)

#ToDo logging and connection to db  
@app.on_event("startup")
async def start_up():
    """Startup"""

@app.on_event("shutdown")
async def shut_down():
    """Shutdown"""

if __name__ == "__main__":
    uvicorn.run("main:app", port=10024, reload=True)