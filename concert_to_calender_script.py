from urllib.request import urlopen
from bs4 import BeautifulSoup

#making the soup
concert_page = 'http://pc-pdx.com/show-guide/filter-by-tag/metal'
page = urlopen(concert_page)
soup = BeautifulSoup(page, "lxml")

#accessing data in html and assigning to variable
show_listing = soup.find_all("div", class_="show-listing")

#loop through data and append to list variable
i = 0
artist = []
detail = []

while i < len(show_listing):
	artist.append(show_listing[i].select(".second-column"))
	detail.append(show_listing[i].select(".third-column"))
	i += 1

#TODO: access the dates in the show_listing. research accessing siblings in Beautiful Soup   

#TODO: regex pattern *bug captures the first bracket*   /[^<>]+(?=[<])/g
