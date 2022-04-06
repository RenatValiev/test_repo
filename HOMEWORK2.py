import re
from urllib.request import urlopen

pageString = urlopen('http://htmlbook.ru/html/div').read().decode()
tags_list = re.findall(r'<div>.+</div>|<h1>.+</h1>|<p>.+</p1>', pageString)
for el in tags_list:
    print(el)
