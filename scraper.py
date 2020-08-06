import nltk
from requests_html import HTMLSession
from newspaper import Article
from tinydb import TinyDB

db = TinyDB('./db.json')

table = db.table('thn')

session = HTMLSession()

baseURL = 'https://thehackernews.com/search/label/'

categories = ['data%20breach', 'Cyber%20Attack', 'Vulnerability', 'Malware']

nltk.download('punkt')


class CategoryScrape():

    catURL = ''

    r = ''

    category = ''

    def __init__(self, catURL, category):

        # print(f'Scraping starting on Category : {category} \n')

        self.category = category

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
                'category': f'{self.category}',
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

        category = CategoryScrape(f'{baseURL}{category}', category)

        category.scrapeArticle()


def getCategories():

    categoryNames = []

    for category in categories:

        category = category.replace("%20", " ")

        categoryNames.append(category.capitalize())

    return categoryNames
