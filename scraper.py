from requests_html import HTMLSession

session = HTMLSession()

baseURL = 'https://thehackernews.com/search/label/'

categories = ['data%20breach', 'Cyber%20Attack', 'Vulnerability', 'Malware']

data = {}


class CategoryScrape():

    catURL = ''

    r = ''

    category = ''

    def __init__(self, catURL, category):

        #print(f'Scraping starting on Category : {category} \n')

        self.category = category

        self.catURL = catURL

        self.r = session.get(self.catURL)

    def scrapeArticle(self):

        data[f'{self.category}'] = []

        blog_posts = self.r.html.find('.body-post')

        for index, blog in enumerate(blog_posts):

            storyLink = blog.find('.story-link', first=True).attrs['href']

            storyTitle = blog.find('.home-title', first=True).text

            data[f'{self.category}'].append({
                'id': f'{index + 1}',
                'title': f'{storyTitle}',
                'link': f'{storyLink}'
            })


def scrapeData():

    for category in categories:

        category = CategoryScrape(f'{baseURL}{category}', category)

        category.scrapeArticle()


def getScrapedData():

    return data


def getCategories():

    categoryNames = []

    for category in categories:

        category = category.replace("%20", " ")
        categoryNames.append(category.capitalize())

    return categoryNames


def getCategoryAllNews(category):

    return data[category]


def getCategoryNews(category, id):

    dataId = int(id) - 1

    newsdata = data[category][dataId]

    return newsdata


# To Delete before pushing to git

#scrapeData()
#print(data)
