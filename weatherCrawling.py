import requests  # pip install requests

# https://search.naver.com/search.naver?&query=한남동날씨

from bs4 import BeautifulSoup  # pip install beautifulsoup4

inputArea = input("날씨를 조회하려는 지역을 입력하세요:")

weatherHtml = requests.get("https://search.naver.com/search.naver?&query={inputAre}날씨")
# https://search.naver.com/search.naver?&query=한남동날씨
# print(weatherHtml.text)

weatherSoup = BeautifulSoup(weatherHtml.text, 'html.parser')
# print(weatherSoup)

areaText = weatherSoup.find("h2", {"class":"title"}).text  # tag 필요없고 text만 뽑아냄
# 날씨 지역 이름 가져오기
areaText = areaText.strip()
print(f"지역이름: {areaText}")

todayTempText = weatherSoup.find("div", {"class":"temperature_text"}).text
todayTempText = todayTempText[6:11].strip()
print(f"현재온도: {todayTempText}")
# print(todayTempText[6:11])

yesterdayTempText = weatherSoup.find("span", {"class":"temperature up"}).text
yesterdayTempText = yesterdayTempText.strip()
print(f"어제날씨비교: {yesterdayTempText}")

todayWeatherText = weatherSoup.find("span", {"class":"weather before_slash"}).text
todayWeatherText = todayWeatherText.strip()
print(f"오늘날씨: {todayWeatherText}")

senseTempText = weatherSoup.find("dd", {"class":"desc"}).text
senseTempText = senseTempText.strip()
print(f"체감온도: {senseTempText}")

todayInfoText = weatherSoup.select("ul.today_chart_list>li")  # 미세먼지, 초미세먼지, 자외선, 일몰 모두 갖고 옴
# print(todayInfoText[0:2])
dustInfo = todayInfoText[0].find("span", {"class":"txt"}).text
dustInfo = dustInfo.strip()
print(f"미세먼지: {dustInfo}")
superdustInfo = todayInfoText[1].find("span", {"class":"txt"}).text
superdustInfo = superdustInfo.strip()
print(f"초미세먼지: {superdustInfo}")
