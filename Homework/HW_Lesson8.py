import requests
from bs4 import BeautifulSoup
from pyexcel import *
financial_report = requests.get('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn').text

soup = BeautifulSoup(financial_report,'html.parser')

table = soup.find('table', {'id': 'tableContent'})

tr_content = table.find_all('tr')
data = []
for tr in tr_content:
    td_content = tr.find_all('td')
    info_value = []
    for td in td_content:
        info_value.append((td.text).strip())     
    for info in info_value:
        if info == '':
            info_value.remove(info)
    # print(info_value)
    if   len(info_value) < 5:
        for i in range(5 - len(info_value)):
            info_value.append('')    
    for info in info_value:
        result = {
            'Danh mục': info_value[0],
            'Quý 4-2016': info_value[1],
            'Quý 1-2017': info_value[2],
            'Quý 2-2017': info_value[3],
            'Quý 3-2017': info_value[4]
        }
    data.append(result)
save_as(records=data, dest_file_name='VNM_financial_report.xls')

            

        


