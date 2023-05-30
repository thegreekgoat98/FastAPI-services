import uvicorn
from script.config import Service
from fastapi import FastAPI
from constants.app_constants import CommonConstant
from course import router
app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app=CommonConstant.APP_KEY ,host=Service.host, port=Service.port)