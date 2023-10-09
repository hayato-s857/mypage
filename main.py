import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

URL = "https://eiga.com/ranking/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select("#document_16l5w5x > main > div > div > section:nth-child(4) > table > tbody > tr")

for movie in movies:
    rank = movie.select_one('span').text
    title = movie.select_one('h2 > a').text
    date = movie.select_one('.time').text
    print(rank,title,date)

client = MongoClient('mongodb+srv://sparta:<password>@cluster0.wpf2wkw.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'name':'太郎',
    'age':24
}

db.users.insert_one(doc)

