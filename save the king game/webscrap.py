import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=narendramodi"

search = requests.get(url)

soup = BeautifulSoup(search.text,"html.parser")
print(soup.prettify())
i  = input()
