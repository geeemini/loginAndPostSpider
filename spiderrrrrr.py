from selenium import webdriver
import requests
import json
import time
import random

my_headers =[
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    '''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36''',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)'
]

def getHeader():
    head = {
            'user-agent': random.choice(my_headers),
            }
    return head

driver = webdriver.Firefox()
driver.get("http://134.96.106.171:8080/oss/login")

user = 'chenqi'
password = 'test$zj123'

#清空登录框
driver.find_element_by_xpath("//*[@id='username']").clear()
#自动填入登录用户名
driver.find_element_by_xpath("//*[@id='username']").send_keys(user)
#清空密码框
driver.find_element_by_xpath("//*[@id='password']").clear()
#自动填入登录密码
driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
time.sleep(1)
#点击登录按钮进行登录
driver.find_element_by_xpath("//*[@id='btnLogin']").click()
time.sleep(3)


driver.get("http://134.96.106.171:8080/oss/reportManager/oltOutNet/home?target=6")

# 获取cookies
cookie_items = driver.get_cookies()


# 获取到的cookies是列表形式，将cookies转成json形式并存入本地名为cookie的文本中
post = {}
for cookie_item in cookie_items:
    post[cookie_item['name']] = cookie_item['value']
cookie_str = json.dumps(post)
with open('cookie.txt', 'w', encoding='utf-8') as f:
    f.write(cookie_str)
f.close()

with open('cookie.txt', 'r', encoding='utf-8') as f:
    cookie = f.read()
cookies = json.loads(cookie)

beginTime = "2019-11-11"
endTime = "2019-11-17"
params = {"timeSize":2,
          "beginTime":beginTime,
          "endTime":endTime,
          # "_search": ,
          "nd":1574220854385,
          "rows":50,
          "page":1,
          "sord":"desc"
          }
url = "http://134.96.106.171:8080/oss/reportManager/oltOutNet/getList"
# 2. 发送请求获取响应数据
response = requests.post(url,params,cookies=cookies,headers = getHeader())
response.encoding = 'utf-8'
resule = json.loads(response.text)