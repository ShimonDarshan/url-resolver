from fastapi import FastAPI
from fastapi.responses import JSONResponse

from _resolver import resolve_URL, ResolverRequest

api = FastAPI()


@api.post("/")
def root(req: ResolverRequest):

    resolved_url = resolve_URL(req.url)
    return JSONResponse(content={"url": resolved_url})
