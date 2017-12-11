#coding=utf-8
# print "你好"
# raw_input("输入")

# x = 6
# y = 7
# print(x + y)
# if x == 6 :
#     print("666")
# else :
#     print("88")
#
# import sys
# print(sys.argv)
#
# #多变量赋值
# a, b, c = 5, 6, "yes"
# print(a,c,b)
# # 5 的 6 次方
# print(a ** b)
# #取整除 - 返回商的整数部分
# print(b // a)
#
#
# z = "123456789"
# print(z[4])
# #[0:4] 第一个到第四个字符
# print(z[0:4])
#
# #数组
# list = [1, 2, 3, 4, 5, 6]
# list[2] = 9
# print(list)
#
# #元组 和数组差不多，但是元组是不可以二次赋值的（就是不可以更改）
# tuple = (1, 2, 3)
# tupleNew = (8,9)
# print(tuple)
# print(tuple + tupleNew)
#
# #字典 key 也可以用 单引号
# dic = {"one": 1, "two": 3, "three": 6}
# print(dic["one"])
# print(dic.keys())
# print(dic.values())
# #清空字典 但不删除这个对象
# dic.clear()
# print(dic)
# #删除字典(对象)
# del dic
# #这里会报错了
# # print(dic)
#
# #成员运算符 in： 如果在指定的序列中找到值返回 True，否则返回 False; not in: 如果在指定的序列中没有找到值返回 True，否则返回 False。
# print(6 in list)
# print(6 not in list)
#
# #身份运算符 is: x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False; is not: x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False
# print(a is b)
# print(a is not b)
#
# a = 6
# print(a is b)
# print(a is not b)

#文件名 就是相当于swift里面的framework名称里面可以包含属性、方法、类
# import FunctionTest
# FunctionTest.funcname("test")
# Test 是 FunctionTest 模块里的类
# from FunctionTest import Test
# test = Test()
# test.test()

import urllib
import urllib2
# response = urllib2.urlopen("https://www.baidu.com")

#下面这两句是和上面注释掉的是一样的
# request = urllib2.Request("https://www.baidu.com")
# response = urllib2.urlopen(request)
# print response.read()


#post 请求示例
# values = {"username": "1016903103@qq.com", "password": "123456"}
# data = urllib.urlencode(values)
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url,data)
# response = urllib2.urlopen(request)
# print response.read()

#get 请求示例
# values = {"username": "1016903103@qq.com", "password": "123456"}
# data = urllib.urlencode(values)
# url = "http://passport.csdn.net/account/login" + "?" + data
# print(url)
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# print response.read()

#put or delete 请求示例
# request = urllib2.Request("http://www.baidu.com")
# request.get_method = lambda : 'PUT' #or 'DELETE'
# response = urllib2.urlopen(request)
# print response.read()

#DebugLog 的使用示例
# httpHandler = urllib2.HTTPHandler(debuglevel=1)
# httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
# opener = urllib2.build_opener(httpHandler, httpsHandler)
# urllib2.install_opener(opener)
# response = urllib2.urlopen(request)

#Cookie
import cookielib
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# for item in cookie:
#     print "name =" + item.name
#     print  "value =" + item.value

#保存 cooKie
# filename = "cookie.txt"
# mozillacookie = cookielib.MozillaCookieJar(filename)
# mozillacookieHandler = urllib2.HTTPCookieProcessor(mozillacookie)
# opener = urllib2.build_opener(handler, mozillacookieHandler)
# response = opener.open("http://www.baidu.com")
# mozillacookie.save(ignore_discard=True, ignore_expires=True)

#读取 保存的cookie并使用
# mozillacookie = cookielib.MozillaCookieJar()
# mozillacookie.load("cookie.txt", ignore_expires=True, ignore_discard=True)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(mozillacookie))
# request = urllib2.Request("http://www.baidu.com")
# response = opener.open(request)
# print response.read()


#使用Beautiful soup
import bs4
from bs4 import BeautifulSoup
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
soup = BeautifulSoup(html)
#格式化
text = soup.prettify()
# print soup.__class__, text.__class__, "\n" + text
#Tag soup.title = 获取第一个标签里面的内容 title是HTML里面的标签(Tag)，可以有 soup.html，soup.b等,但这些仅是获取第一个的
# print soup.title
# print soup.b
#name attrs 是Tag的两个属性 name 是标签的本身，attrs 是标签里面的包含的所有属性，是一个字典
# print soup.head.name
# print soup.head.attrs
# print soup.p.name
# print soup.p.attrs
#
# print soup.p.string
#
# print soup.a.string

#contents 将tag的子节点以列表(数组)的方式输出
# print soup.head.contents
# print soup.head.contents[0]
#children 返回的不是一个 list，不过我们可以通过遍历获取所有子节点
# print soup.head.children
# for child in soup.head.children:
#     print child


#descendants 整个html的所有子节点
# for child in soup.descendants:
#     print child.__class__,child

#爬糗事百科
# url = "https://www.qiushibaike.com"
# try:
#     user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
#     header = {"User-Agent": user_agent}
#     request = urllib2.Request(url, headers=header)
#     response = urllib2.urlopen(request)
#     html = response.read().decode("utf-8")
#     soup = BeautifulSoup(html)
#     for item in soup.find_all("div",class_="content"):
#         # print(item)
#         for content in item.contents:
#             if type(content)==bs4.element.Tag:
#                 print content.string
# except urllib2.URLError, e:
#     print(e)
# except urllib2.HTTPError, e:
#     print e

from book import Info, Author
#爬起点网站
# url = "https://www.qidian.com/finish"
# books = []
# try:
#     request = urllib2.Request(url)
#     response = urllib2.urlopen(request)
#     html = response.read().decode("utf-8")
#     soup = BeautifulSoup(html)
#     print soup.prettify()
#     for tag in soup.descendants:
#         if type(tag)==bs4.element.Tag:
#             if tag.name == "div":
#                 for book in tag.find_all(class_="book-mid-info"):
#                     # book = Info()
#                     # books.append(book)
#                     for name in book.find_all("h4"):
#                         book.name = name.string
#                     # for info in book.find_all("p"):
#                         # print info
# except urllib2.URLError, e:
#     print e

'''
<div class="book-mid-info">
          <h4>
           <a data-bid="2750457" data-eid="qd_B58" href="//book.qidian.com/info/2750457" target="_blank">
            大主宰
           </a>
          </h4>
          <p class="author">
           <img src="//qidian.gtimg.com/qd/images/ico/user.f22d3.png">
            <a class="name" data-eid="qd_B59" href="//my.qidian.com/author/1019021" target="_blank">
             天蚕土豆
            </a>
            <em>
             |
            </em>
            <a data-eid="qd_B60" href="//www.qidian.com/xuanhuan" target="_blank">
             玄幻
            </a>
            <i>
             ·
            </i>
            <a class="go-sub-type" data-eid="qd_B61" data-subtypeid="73" data-typeid="21" href="javascript:">
             异世大陆
            </a>
            <em>
             |
            </em>
            <span>
             完本
            </span>
           </img>
          </p>
          <p class="intro">
           大千世界，位面交汇，万族林立，群雄荟萃，一位位来自下位面的天之至尊，在这无尽世界，演绎着令人向往的传奇，追求着那主宰之路。无尽火域，炎帝执掌，万火焚苍穹。武境之内，武祖之威
          </p>
          <p class="update">
           <span>
            496.03万字
           </span>
          </p>
         </div>
        </li>
        <li data-rid="2">
         <div class="book-img-box">
          <a data-bid="2502372" data-eid="qd_B57" href="//book.qidian.com/info/2502372" target="_blank">
           <img src="//qidian.qpic.cn/qdbimg/349573/2502372/150"/>
          </a>
         </div>
'''
# newurl = 'http://www.biquge.com/23_23176/1983983.html'
# request = urllib2.Request(newurl)
# response = urllib2.urlopen(request)
# html = response.read().decode("utf-8")
# print(html)
# soup = BeautifulSoup(html)
# # 				<div class="bookname">
# # 					<h1> 第一千二百二十三章 破阵之法</h1>  => div.bookname > h1
# name_div = soup.select('div.bookname > h1')
# # print name_div
# # id = "content" </div> => div#content
# content = soup.select('div#content')
# if content:
#     charpter_txt = unicode(content[0])
#     print charpter_txt
# else:
#     print ValueError(u'章节小说内容不存在 ')


# url = 'http://www.biquge.com/'
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# html = response.read().decode("utf-8")
# # print html
# soup = BeautifulSoup(html)
# main = soup.select("div#main")
# a = main[0].select("a")
# for item in a:
#     # 获取标签之间的内容  <a href="/0_226/"> 网游之天谴修罗 </a>
#     print item.string # 网游之天谴修罗



#MARK: UI
from Tkinter import *
def tapbutton():
    print "Test"
    #整个程序退出并销毁
    window.quit()
window = Tk() # 创建窗口
table = Listbox(master=window) # 创建tableView
data = ["001","002","003","004","005"]
for item in data:
    # 给tableView 数据源
    table.insert(0, item)
table.pack() # 将小部件放置到主窗口中
button = Button(master=window, text = "Quit", command = tapbutton, width = 100, state = NORMAL) #tapbutton()只调用一次, tapbutton就会一直调用
button.pack()
window.mainloop() # 进入消息循环 窗口展示出来

