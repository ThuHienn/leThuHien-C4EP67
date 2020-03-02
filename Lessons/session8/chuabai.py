from pymongo import MongoCilent
cilent = MongoCilent('localhost:27017')
ort requests
from bs4 import BeautifulSoup
import pymongo

cilent = pymongo.MongoClient('mongodb://localhost:27017/')
#from pymongo import MongoCilent
#cilent = MongoCilent('localhost:27017')
db = cilent['c4e']
dantri_collection = db['dantri']
dantri_content =  requests.get('https://dantri.com.vn/')

# print(dantri_content.text)   #response [200]: thành công
soup = BeautifulSoup(dantri_content.text, 'html.parser') #'html.parser' thông báo loại dữ liệu đang truyền #xml, xhtml,... html phổ biến, hiện đại hơn
# print(soup.prettify()) xem và làm đẹp code html -> dễ đọc

div_content = soup.find('div', {'class': 'xnano'})
# print(new_content)
ul_content = div_content.find('ul', {'class': 'ul1 ulnew'})
# print(content)
li_content = ul_content.find_all('li')
for li in li_content:
    news_link = li.h4.a['href']
    news_title = str(li.h4.a.string).strip()
    new_dict ={
        'title': news_title,
        'link': news_link
    }
    dantri_collection.insert_one(new_dict) #dành cho dữ liệu ít -> code ngắn