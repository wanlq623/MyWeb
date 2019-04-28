from urllib.parse import quote
from hashlib import md5
from http import client
import random,json

appid = '20190428000292335'
secret_key = 'vEuG6vit_c73lSqCUlYs'

#生成调用api的签名
def get_sign(salt,qurey):
    sign = appid + qurey + str(salt) + secret_key
    m = md5()
    m.update(sign.encode('utf-8'))
    return m.hexdigest()

#实现翻译功能
def trans(qurey,from_lang='zh',to_lang='en'):
    http_client = None
    salt = random.randint(32768,65536)
    sign = get_sign(salt,qurey)
    myurl = '/api/trans/vip/translate' + '?appid=' + appid + '&q=' + quote(qurey) + '&from=' + from_lang + '&to=' + to_lang + '&salt=' + str(salt) + '&sign=' + sign
    try:
        #连接API
        http_client = client.HTTPConnection('api.fanyi.baidu.com')
        #发起请求
        http_client.request('GET',myurl)
        #获取响应对象
        response = http_client.getresponse()
        #将调用API的返回结果转为字典
        content = json.loads(response.read())
        print(content)
        #返回翻译内容
        return content['trans_result'][0]['dst']
    except Exception as e:
        return e
    finally:
        if http_client:
            http_client.close()