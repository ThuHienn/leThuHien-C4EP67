import requests
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
li_content = ul_content.find_all('li') #trả về một list chứa toàn bộ content của li -> không .find() được nữa
# print(li_content) 
# for li in li_content:
#     # print(li.h4.a.string) #.string/text: lấy tên bài báo
#     # print(li.h4.a['href']) #['']:(attribute - thuộc tính) thuộc thẻ a không phải ".": con (nội dung) của a (nằm ngay sau thẻ mở a)
#     news_link = li.h4.a['href']
#     news_title = li.h4.a.string
#     print(news_link, news_title)


data = []
for li in li_content:
    news ={
        'title': li.h4.a.string.strip(), #strip: bỏ dấu cách
        'link': li.h4.a['href']
    }
    data.append(news)
dantri.insert_many(data)