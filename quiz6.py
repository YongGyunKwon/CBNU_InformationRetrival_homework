import wikipediaapi
import requests

wiki=wikipediaapi.Wikipedia('en')

words=['Newcastle','Judge','Customer','Market','summary','summer','winter','trust','union','response']

for i in words:
    #print("i is",i)
    page_1=wiki.page(i)
    filen= i+'.txt'
    print(page_1.summary[0:100])
    with open(filen,"w",-1,"utf-8") as f:
        f.write(page_1.summary)

