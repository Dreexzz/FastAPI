from fastapi import FastAPI
from apiatt.routers import api_router


app = FastAPI(title='apiatt')
app.include_router(api_router)
