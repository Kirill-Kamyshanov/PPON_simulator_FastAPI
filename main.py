from fastapi import FastAPI
from api.routes import money

app = FastAPI() # создание экземпляра приложения


@app.get("/") # Определяем корневой эндпоинт
def read_root():
    return {"message": "Это приложение - собственность ППОНа"}


app.include_router(money.router)



