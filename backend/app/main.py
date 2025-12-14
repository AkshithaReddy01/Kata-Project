from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import init_db
from app.routers import auth, sweets, inventory

# Initialize FastAPI app
app = FastAPI(
    title="Sweet Shop Management System API",
    description="RESTful API for managing a sweet shop inventory",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
@app.on_event("startup")
async def startup_event():
    init_db()

# Include routers
app.include_router(auth.router)
app.include_router(sweets.router)
app.include_router(inventory.router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Sweet Shop Management System API",
        "docs": "/docs",
        "version": "1.0.0"
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}

