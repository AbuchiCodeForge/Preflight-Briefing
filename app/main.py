"""
FastAPI application.
"""

from fastapi import FastAPI

app = FastAPI(title="Flight Briefer")

@app.get("/")
def read_root():
    return {"message": "Flight Briefer API is running"}