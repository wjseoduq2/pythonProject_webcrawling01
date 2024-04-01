import requests  # pip install requests

# https://search.naver.com/search.naver?&query=한남동날씨

from bs4 import BeautifulSoup  # pip install beautifulsoup4

weatherHtml = requests.get("https://search.naver.com/search.naver?&query=한남동날씨")
# https://search.naver.com/search.naver?&query=한남동날씨
print(weatherHtml.text)

weatherSoup = BeautifulSoup(weatherHtml.text, 'html.parser')
print(weatherSoup)

areaText = weatherSoup.find("h2", {"class":"title"}).text  # tag 필요없고 text만 뽑아냄
# 날씨 지역 이름 가져오기
areaText = areaText.strip()
# print(areaText)

todayTempText = weatherSoup.find("div", {"class":"temperature_text"}).text
todayTempText = todayTempText[6:11].strip()
# print(todayTempText)
# print(todayTempText[6:11])