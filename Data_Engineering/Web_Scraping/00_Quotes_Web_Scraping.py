import requests
from bs4 import BeautifulSoup
import csv

###### Url
url = "http://quotes.toscrape.com/"
headers = {"User-Agent": 'Mozilla/5.0',"Accepted-Language":'en-US,en;q=0.5'}

#### Scrape the data
response = requests.get(url,headers) # the output here is in byte format
print(response.status_code)

scrape_data = BeautifulSoup(response.text,'html.parser')
print(scrape_data.prettify())


#### extract the data from HTML
quotes = scrape_data.find_all("span",attrs={"class" : "text"})
print(quotes)

author = scrape_data.find_all("small",attrs={"class" : "author"})
print(author)

###### Load extracted data into an excel file
load_file = open("quotes.csv",'w')
writer = csv.writer(load_file)
writer.writerow(["quotes","Author"])

for quotes,author in zip(quotes,author):
    writer.writerow([quotes.text.strip(), author.text.strip()])

load_file.close()


