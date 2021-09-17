from flask import Flask
import requests
import re
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.miniproject

app = Flask(__name__)
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/running/current.naver?order=reserve',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#크롤링으로 데이터 가져오기
lis = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')
for li in lis:
    a_tag = li.select_one('dl > dt > a')
    title = a_tag.text
    stars = li.select_one('dl > dd.star > dl.info_star > dd').text[2:6]
    desc = li.select_one('dl > dd:nth-child(3) > dl > dd:nth-child(2) > span.link_txt').text
    desc2 = ''.join(desc.split()).strip()
    image = li.select_one('div')
    image2 = image.img['src']
    url = li.select_one('dl > dt > a')['href']

    urls = requests.get('https://movie.naver.com/movie' + url)
    soups = BeautifulSoup(urls.text, 'html.parser')
    story = soups.select('#content > div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div.story_area > p')
    storys = str(story)
    storys = re.sub('<.+?>', '', storys, 0)
    image3 = soups.select_one('#content > div.article > div.mv_info_area > div.poster > a')
    image4 = image3.img['src']

#데이터 DB저장하기
    doc = {'title': title, 'stars': stars, 'genre': desc2, 'image': image2, 'story': storys, 'url': 'https://movie.naver.com' + url,
           'big_image': image4, 'sad_count': 0, 'heal_count': 0, 'itchy_count': 0, 'thrill_count': 0, 'baby_count': 0, 'spicy_count': 0}
    db.moodtheater.insert_one(doc)
