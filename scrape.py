from urllib.request import urlopen
from html.parser import HTMLPArser

url_base = "http://www.theatlanticcities.com/authors/richard-florida/?page="

index_text = ''
with urlopen(url_base + '1') as index_handle:
	index_text = index_handle.read()

class MyHTMLParser(HTMLParser):
	def __init__(self):
		self.articles = dict()
    def handle_starttag(self, tag, attrs):
    	attr_dict = dict(attrs)
        if tag == 'a' and 'title' in attrs_dict:
        	self.articles[attrs_dict['title']] = attrs_dict['href']

parser = MyHTMLParser(strict=False)
parser.feed(index_text)
