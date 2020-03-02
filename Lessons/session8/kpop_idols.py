import requests
from bs4 import BeautifulSoup

kpop_idols_content = requests.get('https://dbkpop.com/db/all-k-pop-idols').text

soup = BeautifulSoup(kpop_idols_content, 'html.parser')

tbody_content = soup.find('tbody',{})

tr_content = tbody_content.find_all('tr')

td_content =[]
for tr in tr_content:
    for td in tr:
        td_content.append(td.text)
    idols = {
        'profile': td_content[0],
        'stage_name': td_content[1] 
    }

print(idols)
    
        



