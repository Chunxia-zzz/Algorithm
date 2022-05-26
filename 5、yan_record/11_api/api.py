#通过网络发送信息有一个标准，名为超文本传输协议

#如果要传入一个文件，可以用post,当发起post，可以带要传入的文件
# get用来获取资源
#requests库
from urllib import request

# 调用api可以整理好读取文本，分析图片的方法，连接到第三方服务
# request.post(sddress,\
#             http_hesders,\
#             function_parameters,\
#             message_body)
#创建服务，需要 密钥，然后才能调用  
#api可以让别人用你的代码
# json是传输接口数据的一种格式