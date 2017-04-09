# encoding:utf-8
import requests
import re
from io import BytesIO
from PIL import Image
#保持cookies
s = requests.session()
#创建内存文件变量，用来保存验证码图片
img = BytesIO()
#获取VIEWSTATE地址
login_url = "http://202.119.225.34/"
#获取验证码地址
code_url = "http://202.119.225.34/CheckCode.aspx"
#请求并获取VIEWSTATE
login_html = s.get(login_url)
viewstate = re.findall('name="__VIEWSTATE" value="(.*?)" />', login_html.text)[0]

#测试
# print "viewstate :" + viewstate
# print "login_html:" + str(s.cookies)

#请求验证码地址并存在img中
code_html = s.get(code_url)

#print("code_html :" + str(s.cookies))
img.write(code_html.content)
#打开验证码图片
img = Image.open(img)
img.show()
#输入验证码
code = input("input code:")
#构造请求数据
data = {
    '__VIEWSTATE': viewstate,
    'txtUserName': 'username',
    'TextBox2': 'password',
    'txtSecretCode': code,
    'RadioButtonList1': '\321\247\311\372',
    'Button1': '',
    'lbLanguage': '',
    'hidPdrs': '',
    'hidsc': ''
}
#登陆
findname = s.post("http://202.119.225.34/default2.aspx", data=data)
# print(findname.text)
#find name
name = re.findall('<span id="xhxm">(.*?)</span>', findname.text)[0]
print(name)


# qqq
