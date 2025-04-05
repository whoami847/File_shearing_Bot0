from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.on_event("shutdown")
async def shutdown_event():
    print("Web server shutting down")
