import requests
from bs4 import BeautifulSoup
import os
from lxml import etree
image_url = 'https://vod1eu16.128100.xyz/hls/KNhsHiD9KHw/CLS-14-v1-a1.ts?ip=38.207.137.254&exp=1722760579&hash=7d0209835c8a8bbc286ee246199b6378'
header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'connection':'keep-alive',
    'Cache-Control':'max-age=0',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'none',
    'Sec-Fetch-User':'?1',
    'Upgrade-Insecure-Requests':'1',
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",}
# 发起请求并下载图片
response = requests.get(image_url,headers=header).content
print(response)