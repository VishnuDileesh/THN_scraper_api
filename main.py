from fastapi import FastAPI, BackgroundTasks
from scraper import scrapeData, getScrapedData

app = FastAPI()



@app.get("/api/v1/")
async def index():
    """ index route """

    return {
        "get-data": "get request to route '/api/v1/news' to get latest news title & link",
        "scrape-data": "post request to route '/api/v1/scrape-data' activates scraping"
    }


@app.get("/api/v1/news")
async def get_data():
    """ On doing a get request to route '/api/v1/news' gives you all latest news articl's titles & links """
    return getScrapedData()


@app.post("/api/v1/scrape-data")
async def scrape_data(background_tasks: BackgroundTasks):
    """ On doing a post request to route '/api/v1/scrape-data' you Activates scraping """

    background_tasks.add_task(scrapeData)

    return {"Status": "Activated Scraping"}
