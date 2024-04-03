from fastapi import FastAPI
from routes import container_route, tests_route

app = FastAPI()

# Adding routers to the app.
app.include_router(container_route.router)
app.include_router(tests_route.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

