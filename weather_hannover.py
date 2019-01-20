# import libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen

# specify the URL
url = 'https://www.wetter.de/deutschland/wetter-hannover-18219670/wetter-uebersicht.html'

# query the URL and retrieve the HTTP response
response = urlopen(url)

# parse the HTTP response using HTML parser
soup = BeautifulSoup(response, 'html.parser')

# retrieve the tags that match the criteria and store them into lists
days = soup.findAll('div', attrs = {'class' : 'text-day'})
dates = soup.findAll('div', attrs = {'class' : 'text-date'})
min_temps = soup.findAll('span', attrs = {'class' : 'wt-color-temperature-min'})
max_temps = soup.findAll('span', attrs = {'class' : 'wt-color-temperature-max'})

# iterate over the lists and print the information
for day, date, min_temp, max_temp in zip(days, dates, min_temps, max_temps):
	print("{0:s}, {1:s} -- min: {2:>3s}, max: {3:>3s}".format(day.text, date.text, min_temp.text, max_temp.text))