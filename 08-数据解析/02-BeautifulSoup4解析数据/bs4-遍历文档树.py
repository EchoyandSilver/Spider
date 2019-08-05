
from bs4 import BeautifulSoup

html = """
    <html><body><div class="separator"/>
    <div class="wiki-common-headTabBar">
        <a href="https://www.baidu.com/" nslog="normal" nslog-type="10600112" data-href="https://www.baidu.com/s?ie=utf-8&amp;fr=bks0000&amp;wd=">&#32593;&#39029;</a>
        <a href="http://news.baidu.com/" nslog="normal" nslog-type="10600112" data-href="http://news.baidu.com/ns?tn=news&amp;cl=2&amp;rn=20&amp;ct=1&amp;fr=bks0000&amp;ie=utf-8&amp;word=">&#26032;&#38395;</a>
        <a href="https://tieba.baidu.com/" nslog="normal" nslog-type="10600112" data-href="https://tieba.baidu.com/f?ie=utf-8&amp;fr=bks0000&amp;kw=">&#36148;&#21543;</a>
        <a href="https://zhidao.baidu.com/" nslog="normal" nslog-type="10600112" data-href="https://zhidao.baidu.com/search?pn=0&amp;&amp;rn=10&amp;lm=0&amp;fr=bks0000&amp;word=">&#30693;&#36947;</a>
        <a href="http://music.baidu.com/" nslog="normal" nslog-type="10600112" data-href="http://music.baidu.com/search?f=ms&amp;ct=134217728&amp;ie=utf-8&amp;rn=&amp;lm=-1&amp;pn=30&amp;fr=bks0000&amp;key=">&#38899;&#20048;</a>
        <a href="http://云打码使用.baidu.com/" nslog="normal" nslog-type="10600112" data-href="http://云打码使用.baidu.com/search/index?tn=baiduimage&amp;ct=201326592&amp;lm=-1&amp;cl=2&amp;nc=1&amp;ie=utf-8&amp;word=">&#22270;&#29255;</a>
        <a href="http://v.baidu.com/" nslog="normal" nslog-type="10600112" data-href="https://www.baidu.com/sf/vsearch?pd=video&amp;tn=vsearch&amp;ie=utf-8&amp;rsv_spt=17&amp;wd=">&#35270;&#39057;</a>
        <a href="http://map.baidu.com/" nslog="normal" nslog-type="10600112" data-href="http://map.baidu.com/m?ie=utf-8&amp;fr=bks0000&amp;word=">&#22320;&#22270;</a>
        <a href="https://wenku.baidu.com/" nslog="normal" nslog-type="10600112" data-href="https://wenku.baidu.com/search?lm=0&amp;od=0&amp;ie=utf-8&amp;fr=bks0000&amp;word=">&#25991;&#24211;</a>
        <b><!--Hey, baby. want to buy a used parser?--></b>
        <b class="baike">&#30334;&#31185;</b>
    </div>
</body></html>
"""

soup = BeautifulSoup(html)

# element list：返回字符串
# print(soup.contents)
# element list_iterator：返回生成器
# print(soup.children)
# for i in soup.strings:
#     print(i)

# 返回字符串
# print(soup.b.string)
# 返回生成器
# print(soup.b.strings)
# for string in soup.strings:
#     print(repr(string))

# 返回生成器，会去掉空白字符
print(soup.b.stripped_strings)
for string in soup.stripped_strings:
    print(repr(string))





