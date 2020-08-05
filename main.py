from fastapi import FastAPI, BackgroundTasks
from scraper import scrapeData

app = FastAPI()


@app.get("/api/v1/")
async def index():
    """ index route """

    return {
        "get-data":
        "get request to route '/api/v1/news' to get latest news title & link",
        "scrape-data":
        "post request to route '/api/v1/scrape-data' activates scraping"
    }


@app.get("/api/v1/news")
async def get_data():
    """ On doing a get request to route '/api/v1/news' gives you all latest news articl's titles & links """
    return getScrapedData()


@app.get("/api/v1/categories")
async def get_categories():
    """ On doing a get request to route '/api/v1/categories' gives you all the categories list """
    return getCategories()


@app.get("/api/v1/{category}/news")
async def get_category_all_news(category):
    """ On doing a get request to route '/api/v1/{category}/news' gives you all the latest articles titles & links for the partical category """
    category = category.replace(" ", "%20")
    return getCategoryAllNews(category)


@app.get("/api/v1/{category}/news/{id}")
async def get_category_news(category, id):
    """ On doing a get request to route '/api/v1/{category}/news/{id}' gives you a partical article from the category """
    category = category.replace(" ", "%20")
    return getCategoryNews(category, id)


@app.post("/api/v1/scrape-data")
async def scrape_data(background_tasks: BackgroundTasks):
    """ On doing a post request to route '/api/v1/scrape-data' you Activates scraping """

    background_tasks.add_task(scrapeData)

    return {"Status": "Activated Scraping"}
