from fastapi import FastAPI
from app.routers import router


def create_table():
    from app import models
    from app.database import engine

    models.Base.metadata.create_all(bind=engine)


def get_application():
    # create_table()
    app = FastAPI()
    app.include_router(router=router, prefix="/api")
    return app


app = get_application()
