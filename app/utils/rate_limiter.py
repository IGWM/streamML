from fastapi import Request
from fastapi_limiter import FastAPILimiter
import redis.asyncio as redis
import os

async def setup_limiter():
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
    r = redis.from_url(redis_url)
    await FastAPILimiter.init(r)

async def rate_limit(request: Request):
    await FastAPILimiter.redis.incr(request.scope["path"])
    return True