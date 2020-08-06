from fastapi import FastAPI, BackgroundTasks
from scraper import scrapeData, getCategories
from tinydb import TinyDB, Query, where

# DB section

db = TinyDB('./db.json')

table = db.table('thn')

THN_query = Query()

# API section

app = FastAPI()


@app.get("/")
async def index():
    """ index route """

    return {"docs": "go to route '/docs' to see the API documentation"}


@app.get("/api/v1/news")
async def get_data():
    """ On doing a get request to route '/api/v1/news' gives you all latest news article's titles, links & summary """
    return table.all()


@app.get("/api/v1/categories")
async def get_categories():
    """ On doing a get request to route '/api/v1/categories' gives you all the categories list """
    return getCategories()


@app.get("/api/v1/{category}/news")
async def get_category_all_news(category):
    """ On doing a get request to route '/api/v1/{category}/news' gives you all the latest articles titles & links for the partical category """
    category = category.replace(" ", "%20")

    return table.search(where('category') == category)


@app.get("/api/v1/news/{id}")
async def get_category_news(id):
    """ On doing a get request to route '/api/v1//news/{id}' gives you a partical article from the category """

    return table.get(doc_id=int(id))


@app.post("/api/v1/scrape-data")
async def scrape_data(background_tasks: BackgroundTasks):
    """ On doing a post request to route '/api/v1/scrape-data' you Activates scraping """

    background_tasks.add_task(scrapeData)

    return {"Status": "Activated Scraping"}
