
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.static import static_router
from app.dynamic import dynamic_router
from app.push import push_router

app = FastAPI()

app.mount(
    '/static',
    StaticFiles(directory='static'),
    name='static'
)


@app.get("/")
def root():
    a = "a"
    b = "b" + a
    return {"hello world": b}


@app.get("/sum/{num1}/{num2}")
def somar(num1: int, num2: int):
    return {"sum": num1 + num2}


app.include_router(static_router)
app.include_router(dynamic_router)
app.include_router(push_router)


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
