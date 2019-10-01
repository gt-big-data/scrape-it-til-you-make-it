# Where code shall walk in green pastures

from bs4 import BeautifulSoup

wonderland = open("wonderland.html", "r")
soup = BeautifulSoup(wonderland, 'html.parser')

for i in soup.find_all('li'):
    print(i.text)
