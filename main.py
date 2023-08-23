from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import Caesar,gamming,RSA,Trans,XOR

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(Caesar.router)
app.include_router(gamming.router)
app.include_router(RSA.router)
app.include_router(XOR.router)
app.include_router(Trans.router)
