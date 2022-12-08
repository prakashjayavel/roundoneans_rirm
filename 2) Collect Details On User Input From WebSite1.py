import requests
from bs4 import BeautifulSoup

url = input()
r = requests.get(url)
sm_sites = ['facebook.com','linkedin.com']
sm_sites_present = []

soup = BeautifulSoup(r.content, 'html5lib')
all_links = soup.find_all('a', href = True)


for sm_site in sm_sites:
    for link in all_links:
        if sm_site in link.attrs['href']:
            sm_sites_present.append(link.attrs['href'])

print("social Links",sm_sites_present)