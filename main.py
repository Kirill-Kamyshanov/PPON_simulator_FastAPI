from fastapi import FastAPI

from api.routes import activity, information

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Это приложение - собственность ППОНа"}


app.include_router(information.router, prefix="/api/v1")
app.include_router(activity.router, prefix="/api/v1")



