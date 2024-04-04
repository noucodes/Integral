from bs4 import BeautifulSoup as pu
import requests

url = "https://www.integral-calculator.com/"
response = requests.get(url)

soup = pu(response.text, 'html.parser')


f = open("get.html", "w")
f.write(response.text)
f.close()