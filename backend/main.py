from fastapi import FastAPI
from auth.auth import router as auth_router
from auth.resume import router as resume_router  # ✅ Import resume router
from database import engine, Base

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ Create tables only once during startup
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created!")

# ✅ Include authentication and resume routers
app.include_router(auth_router)
app.include_router(resume_router)  # ✅ Add resume router

# ✅ Test Route
@app.get("/")
def home():
    return {"message": "Backend is Running!"}
