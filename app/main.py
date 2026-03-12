from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.problem import router as problem_router
from app.api.submission import router as sub_router
from app.api.testcase import router as tc_router
from app.core.seed import init_seed_data
from app.db.database import SessionLocal

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时执行
    db = SessionLocal()
    init_seed_data(db=db)
    db.close()
    yield
    # 关闭时执行

app = FastAPI(title="Jimmy OJ", lifespan=lifespan)

app.include_router(problem_router)
app.include_router(sub_router)
app.include_router(tc_router)