from fastapi.routing import APIRouter
from services.scrapy import Spider

app = APIRouter(prefix="/spiders", tags=["Spider"])


@app.get("/")
async def get_spiders():
    """returns a list of available spiders"""
    spiders = Spider().list_spiders()
    return {"spiders":spiders}


@app.get("/{spider}")
async def run_spider(spider: str):
    data = Spider().retrieve_data("azurecli")
    return data[0]
