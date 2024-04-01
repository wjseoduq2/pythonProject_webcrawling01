import requests  # pip install requests

# https://search.naver.com/search.naver?&query=한남동날씨

from bs4 import BeautifulSoup  # pip install beautifulsoup4

weatherHtml = requests.get("https://search.naver.com/search.naver?&query=한남동날씨")
# https://search.naver.com/search.naver?&query=한남동날씨
print(weatherHtml.text)