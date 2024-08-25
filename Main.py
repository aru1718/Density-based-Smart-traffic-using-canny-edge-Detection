import requests
from bs4 import BeautifulSoup

def scrape_article_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = [title.get_text() for title in soup.find_all('h2', class_='article-title')]
    return titles

# Example usage
url = 'https://news.ycombinator.com/'
article_titles = scrape_article_titles(url)
print(article_titles)

