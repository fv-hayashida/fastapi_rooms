from fastapi import FastAPI
from api.routers import user, task, done

app = FastAPI()

app.include_router(user.router)
app.include_router(task.router)
app.include_router(done.router)
