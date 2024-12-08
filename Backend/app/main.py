from fastapi import FastAPI
from app.routers import users, cvs, jobs, match

app = FastAPI()

# Inclure les routes
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(cvs.router, prefix="/cvs", tags=["CVs"])
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
app.include_router(match.router, prefix="/match", tags=["Match"])
