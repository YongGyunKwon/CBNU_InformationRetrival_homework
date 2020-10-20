from bs4 import BeautifulSoup
import requests

pages=requests.get("https://web.kma.go.kr/home/index.tab.now-ten.jsp?gubun=1&myPointCode=&unit=M")
soup=BeautifulSoup(pages.content,'html.parser')

links=soup.find_all(class_="weather")

print('--------------------------------------------------')


for link in links:
    img=link.find("img")
    alt=img.get("alt")

    print(link.get_text())
    print(alt)