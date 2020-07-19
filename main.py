from fastapi import FastAPI
from scraper import scrapeData, getScrapedData

app = FastAPI()


@app.get("/")
def get_data():
    """ Get all scraped data as in json """

    return getScrapedData()


@app.post("/")
def scrape_data():
    """ On doing a post request to '/' you Activates scraping """

    scrapeData()

    return {"Status": "Scraping Started"}
