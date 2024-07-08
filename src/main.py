from fastapi import FastAPI
from app.utils.init_db import create_tables
from app.configs.router import router

app = FastAPI(
    debug=True,
    title="Study Python Application",
)


@app.on_event("startup")
def lifespan() -> None:
    create_tables()


app.include_router(router)
