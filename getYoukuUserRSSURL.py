import sys
import requests
from bs4 import BeautifulSoup

url = sys.argv[1]
r = requests.get(url)
#print r.text
soup = BeautifulSoup(r.text)
try:
	cuid = soup.html.find('div',class_="YK-profile").find('div',class_="action").find('a').get('data-cuid')
	print 'http://www.youku.com/user/rss/id/'+cuid
except:
	print 'No found'