import requests
from bs4 import BeautifulSoup
from zenrows import ZenRowsClient

url = 'https://www.mastersportal.com/search/scholarships/master/computer-sciences'

client = ZenRowsClient("0cbebd78501e0afa6a8ee978b515bbbca6148ac1")
headers = {"Accept-Language":"en-US,en;q=0.9,nl;q=0.8",

            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
            
            }

response = client.get(url).text

soup = BeautifulSoup(response, 'lxml')
names = soup.find('html')
print(names.text)