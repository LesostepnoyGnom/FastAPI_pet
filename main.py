from fastapi import FastAPI
from contextlib import asynccontextmanager # декоратор для контекстных менеджеров

from database import create_tables, delete_tables
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очишена")
    await create_tables() # создание таблицы при старте приложения
    print("База готова")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)


# uvicorn main:app --reload