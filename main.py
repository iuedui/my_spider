from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import csv
import re
import time

def function_csv(url):
    # 伪装成浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/99.0.4844.51 Safari/537.36'}

    # 1. 发送HTTP请求并获取网页内容
    response = requests.get(url)
    response.encoding = 'utf-8'

    # 2. 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 3. 定位表格
    table = soup.find('table')  # 假设要爬取页面上的第一个表格

    fruits = soup.h2.get_text()
    print(fruits)
        # 5. 获取表格的表头（表格的第一行通常包含表头）
    headers = [header.text for header in table.find_all('th')]
    writer.writerow(headers)

        # 6. 获取表格的数据行
        # rows = table.find_all('tr')[1:]  # 跳过第一行，因为它是表头
    rows = list(table.tr.next_siblings)
    print(rows)
    for row in rows:
         # 从每一行中提取单元格数据
         # print(row)
        data = [cell.text for cell in row.find_all('td')]
        if row == rows[0]:
            data.insert(0, '区域')
            data.insert(0, '日期')
        else:
            data.insert(0, fruits[0:7]+"统计")
        writer.writerow(data)
            # print(data)
    # return result  # 如果需要返回结果

# 服务器地址
url = "http://fgj.wuhan.gov.cn/xxgk/xxgkml/sjfb/spzfxysydjcjb/202309/t20230906_2259587.shtml"

html = urlopen('http://fgj.wuhan.gov.cn/xxgk/xxgkml/sjfb/spzfxysydjcjb/')
allbs = BeautifulSoup(html, 'html.parser')
# print(allbs.href)
# for link in allbs.find_all(title=re.compile("2023年[1-9]月新建商品房成交统计情况")):
    # if 'href' in link.attrs:
    #     print(link.attrs['href'])
# 4. 初始化CSV文件
csv_filename = 'table_data.csv'
with open(csv_filename, 'w', encoding='gbk', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for urls in allbs.find_all(title=re.compile("2023年[0-9]*月新建商品房成交统计情况")):
        print(urls.attrs['href'])
         # 引入5秒的延迟
        time.sleep(5)
        function_csv(urls.attrs['href'])
# print(f'Table data has been scraped and saved to {csv_filename}')
