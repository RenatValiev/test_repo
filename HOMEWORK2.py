import re
from urllib.request import urlopen

pageString = urlopen('https://en.wikipedia.org/wiki/NCAA_Division_I').read().decode()
open_tags = re.findall(r'<div>|<h1>|<p>', pageString)
closing_tags = re.findall(r'</div>|</h1>|</p1>', pageString)
print(open_tags)
print(closing_tags)
if len(open_tags) == len(closing_tags):
    print('Valid!')
else:
    print('Invalid :(')