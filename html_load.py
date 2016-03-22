from urllib2 import urlopen

my_address = "https://en.wikipedia.org/wiki/Web_scraping"
html_page = urlopen(my_address)
html_text = html_page.read()
start_tag = "<title>"
end_tag = "</title>"
start_index = html_text.find(start_tag) + len(start_tag)
end_index = html_text.find(end_tag)

print html_text[start_index:end_index]
