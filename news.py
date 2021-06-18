from GoogleNews import GoogleNews as gn
import pyttsx3 as py
dec = '___________'
en = py.init()
vo = en.getProperty('rate')
en.setProperty('rate', 175)
vo = en.getProperty('voices')
en.setProperty('voice', vo[3].id)

def get_news(place, no):
    n = gn()
    n = gn('en', 'd')
    n.search(place)
    n.getpage(no)
    n.result()
    paper = set(n.gettext())
    return (list(paper))

def speak(text):
    en.say(text)
    en.runAndWait()
print(dec*10)
area = input('\nEnter the place form where you need the news (india by default) : ') or 'India'
no = int(input('Enter the number of pages( by default it is 1) : ') or 1)
paper = get_news(place = area, no = no)

speak('getting todays headlines from google news ')
print(dec*10)
print('Todays headlines are.....')
for news in paper:
    print(news)
    speak(news)
print(dec*10)