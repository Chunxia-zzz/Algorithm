from urllib import request
import requests
# 请求接口
url = "http://apis.juhe.cn/ip/ipNewV3"
params = {"ip":"220.152.251.118",
"key":"123"}
res = requests.get(url = url, params= params)

print(res.status_code)
print(res.text)