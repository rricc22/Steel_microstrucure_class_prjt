import requests
from bs4 import BeautifulSoup
import os 

url = 'https://www.google.com/search?sca_esv=dcfe5edb8f188ebf&sxsrf=ACQVn0-zkDgsOl2Am4gUsap23Mx2l0k4bg:1708628433443&q=plane&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjw4s_20L-EAxVEVqQEHd84AwgQ0pQJegQIDRAB&biw=1868&bih=907&dpr=1'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.title.text)

images = soup.find_all('img')

# print(images)

for i in images:
    print(i['src'])