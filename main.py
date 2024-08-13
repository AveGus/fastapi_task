from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import *
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    print("База готова")
    yield
    print("База очищена")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)






