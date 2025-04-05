from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Setup CORS (for frontend compatibility)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health Check Endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "file-sharing-bot"}

# Root Endpoint
@app.get("/")
async def root():
    return {"message": "File Sharing Bot API is running"}

# Old-style shutdown event (compatible with FastAPI 0.95.2)
@app.on_event("shutdown")
async def shutdown_event():
    print("Server shutting down gracefully")
