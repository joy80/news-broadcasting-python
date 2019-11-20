import requests
from bs4 import BeautifulSoup
import pyttsx3						#windows users please check dependencies before using this package

url1 = "http://ddnews.gov.in/"
url2 = "https://indianexpress.com/todays-paper/"

def scrap(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return (soup)


news = {} 
def find_headlines(key, head_list):
    headlines = []
    temp = {}
    for x in head_list:
        headline = x.find("a").get_text()
        headlines.append(headline)
    temp = {key:headlines}
    news.update(temp)

soup1 = scrap(url1)
soup2 = scrap(url2)

news_html = soup1.find("ul", {"class":"list"})
headline_list = news_html.find_all("h3")
find_headlines("DD News", headline_list)

news_html = soup2.find("div", {"class":"l-grid l-grid--y50"})
headline_list = news_html.find_all("h2")
find_headlines("Indian Express", headline_list)

# pyttsx3 engine set up
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    if voice.languages[0] == b'\x02en-us':         # b'\x02en-us' id for english language
        engine.setProperty('voice', voice.id)
        print(voice.id)
        break

def speak(news):
    print("News Headlines")
    engine.say("News Headlines")
    engine.runAndWait()
    for k in news.keys():
        print(k +"...says")
        engine.say(k +"...says")
        engine.runAndWait()
        for v in news[k]:
            print("\t" +v)
            engine.say(v +"...")
            engine.say("...")
            engine.runAndWait()
    
    print("Thank You")
    engine.say("Thank You")
    engine.runAndWait()

speak(news)
