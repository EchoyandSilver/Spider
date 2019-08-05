import re
import requests

def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    response = requests.get(url,headers)
    text = response.text
    # re.S = re.DOTALL
    # contents = re.findall(r'<div\sclass="content">.*?<span>(.*?)</span>',text,re.DOTALL)
    # contents = re.findall(r'<div.+?content">.+?<span>(.+?)</span>', text, re.DOTALL)
    contents = re.findall(r'', text, re.DOTALL)
    duanzi = []
    for content in contents:
        # x = re.sub(r'<.*?>','',content)
        # duanzi.append(x.strip())
        # print(x.strip())
        print('='*50)
        content = re.sub(r'<.+?>', "", content)
        print(content.strip())

def main():
    url = 'https://www.qiushibaike.com/text/page/{}/'
    for x in range(1,3):
        print('Current Page:%s' % x)
        url = url.format(x)
        parse_page(url)
        break

if __name__ == '__main__':
    main()