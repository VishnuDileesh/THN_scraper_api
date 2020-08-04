from fastapi import FastAPI, BackgroundTasks
from scraper import scrapeData, getScrapedData

app = FastAPI()



@app.get("/api/v1/")
async def index():
    """ index route """

    return {
        "get-data": "visit /get-data to get scraped data",
        "scrape-data": "visit /scrape-data to activate scraping"
    }


@app.get("/api/v1/get-data")
async def get_data():
    """ Get all scraped data as in json by visiting /get-data """
    return getScrapedData()


@app.post("/api/v1/scrape-data")
async def scrape_data(background_tasks: BackgroundTasks):
    """ On doing a get request to '/scrape-data' you Activates scraping """

    background_tasks.add_task(scrapeData)

    return {"Status": "Activated Scraping"}
