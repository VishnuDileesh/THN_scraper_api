import nltk
from requests_html import HTMLSession
from newspaper import Article
from tinydb import TinyDB

db = TinyDB('./db.json')

table = db.table('thn')

session = HTMLSession()

baseURL = 'https://thehackernews.com/search/label/'

categories = [{
    'name': 'Data Breach',
    'slug': 'data%20breach'
}, {
    'name': 'Cyber Attack',
    'slug': 'Cyber%20Attack'
}, {
    'name': 'Vulnerability',
    'slug': 'Vulnerability'
}, {
    'name': 'Malware',
    'slug': 'Malware'
}]

nltk.download('punkt')


class CategoryScrape():

    catURL = ''

    r = ''

    categoryname = ''

    categoryslug = ''

    def __init__(self, catURL, categoryName, categorySlug):

        # print(f'Scraping starting on Category : {category} \n')

        self.categoryname = categoryName

        self.categoryslug = categorySlug

        self.catURL = catURL

        self.r = session.get(self.catURL)

    def scrapeArticle(self):

        blog_posts = self.r.html.find('.body-post')

        for blog in blog_posts:

            storyLink = blog.find('.story-link', first=True).attrs['href']

            storyTitle = blog.find('.home-title', first=True).text

            new_data = {
                'title': f'{storyTitle}',
                'link': f'{storyLink}',
                'categoryname': f'{self.categoryname}',
                'categoryslug': f'{self.categoryslug}',
            }

            id = table.insert(new_data)

            article = Article(f'{storyLink}')

            article.download()

            article.parse()

            article.nlp()

            summary = article.summary

            table.update({'summary': f'{summary}'}, doc_ids=[id])


def scrapeData():

    table.truncate()

    for category in categories:

        categorySlug = category['slug']
        categoryName = category['name']

        category = CategoryScrape(f"{baseURL}{categorySlug}", categoryName,
                                  categorySlug)

        category.scrapeArticle()


def getCategories():

    return [category for category in categories]
