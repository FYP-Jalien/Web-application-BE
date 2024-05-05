from fastapi import FastAPI
from routes import container_route, tests_route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Set to True if cookies are needed across domains
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Adding routers to the app.
app.include_router(container_route.router)
app.include_router(tests_route.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

