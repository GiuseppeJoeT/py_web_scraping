import os

from bs4 import BeautifulSoup # BeautifulSoup4 package

from urllib2 import urlopen
import os

my_address = "https://docs.python.org/2/whatsnew/2.7.html"

html_page = urlopen(my_address)
html_text = html_page.read()
soup = BeautifulSoup(html_text, "lxml")
# second param tells bs which parser to use

result = soup.get_text().encode("utf-8")

text = os.linesep.join([s for s in result.splitlines() if s])

print text
