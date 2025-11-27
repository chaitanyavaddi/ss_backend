from fastapi import FastAPI
from src.employees import router as emp_router

app = FastAPI()
app.include_router(emp_router)