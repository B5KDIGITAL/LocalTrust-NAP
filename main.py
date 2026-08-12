import logging
from fastapi import FastAPI
from core.config import settings
from api.routers import health, injection

# Configure logging
logging.basicConfig(level=logging.INFO)

app = FastAPI(title=settings.app_name)

app.include_router(health.router)
app.include_router(injection.router)

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.app_name} API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
