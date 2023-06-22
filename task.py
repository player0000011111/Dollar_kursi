from bs4 import BeautifulSoup
import requests


DOLLOR_UZS_LINK = 'https://www.google.com/search?q=usd+uzs&oq=usd+uzs&aqs=chrome.0.0i131i433i512j0i512l9.1032788695j0j15&sourceid=chrome&ie=UTF-8'
my_user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0'}

full_page = requests.get(DOLLOR_UZS_LINK, headers=my_user_agent)
qirqib_olish = BeautifulSoup(full_page.content,'html.parser')

natija = qirqib_olish.findAll('span',{'class':'DFlfde SwHCTb',"data-precision":2})
print(f"Bugungi kunda 1 AQSH dollori {natija[0].text}somga teng")

