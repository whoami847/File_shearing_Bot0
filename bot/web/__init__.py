from fastapi import FastAPI
from .config import Config
from .database import Base, engine
from .routes import router as api_router
from .protect_content import content_protection_middleware

app = FastAPI(title="Secure File Sharing API", version="1.0.0")

# Include all routers
app.include_router(api_router, prefix="/api/v1")

# Add middleware
app.middleware("http")(content_protection_middleware)

# Initialize database models
@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)

# Export the app instance for WSGI servers
__all__ = ["app"]
