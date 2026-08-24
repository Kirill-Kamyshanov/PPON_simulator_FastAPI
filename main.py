from fastapi import FastAPI

from api.routes import activity, money

app = FastAPI() # создание экземпляра приложения


@app.get("/") # Определяем корневой эндпоинт
def read_root():
    return {"message": "Это приложение - собственность ППОНа"}


app.include_router(money.router, prefix="/api/v1")
app.include_router(activity.router, prefix="/api/v1")



