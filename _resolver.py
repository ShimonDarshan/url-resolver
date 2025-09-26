import requests
from pydantic import BaseModel, HttpUrl, Field


class ResolverRequest(BaseModel):
    url: HttpUrl = Field(strict=True)



def resolve_URL(url: str):

    res = requests.get(url=url, allow_redirects=True)

    return res.url
