
import requests
import re

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

def parse_page(page_url):
    print(page_url)
    resp = requests.get(page_url, headers=headers)
    html = resp.text
    houses = re.findall(r"""
        <div.+?ershoufang-list".+?<a.+?js-title.+?>(.+?)</a > # 获取房源的标题
        .+?<span>(.+?)</span> # 户型
        .+?<span>(.+?)</span> # 大小
        .+?<span>(.+?)</span> # 朝向
        .+?<span.+?last">(.+?)</span> # 精简装修
        .+?<span.+?num">(.+?)</span> # 价格
        <span.+?yue">(.+?)</span>
    """, html, re.VERBOSE | re.DOTALL)
    for house in houses:
        print(house)


def main():
    base_url = "http://cs.ganji.com/zufang/pn{}"
    for i in range(1,3):
        page_url = base_url.format(i)
        parse_page(page_url)
        break


if __name__ == '__main__':
    main()


# 总结：
# 1. 如果想要让.代表所有的字符，那么需要在函数后面加re.DOTALL来表示，否则不会代表\n，也就是换行。
# 2. 获取数据的时候，都要用非贪婪模式.
# 3. 如果正则写得不对，那么获取不到结果，程序会假死，这时候可以把你刚刚写的正则删掉，重新运行下，看下程序还会不会假死
# 如果不会假死了，说明正则写得有问题，这是就要去调整了。
# 4. 如果正则写的有问题，那么不要去钻牛角尖，去更换一个思路就可以了。






