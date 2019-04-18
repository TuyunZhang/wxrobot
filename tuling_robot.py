# 图灵机器人
from wxpy import *
import requests
import json

# 图灵机器人免费申请地址 http://www.tuling123.com
tuling = Tuling(api_key='29b365cec8204131bc171bcbe4636660')
#
# tuling = Tuling(api_key='7c8cdb56b0dc4450a8deef30a496bd4c')


def auto_reply(msg):
    """回复消息，并返回答复文本"""
    tuling.do_reply(msg)


def text_reply(msg):
    """仅返回消息的答复文本，不会回复"""
    return tuling.reply_text(msg)


if __name__ == '__main__':
    """测试图灵机器人"""
    api_url = 'http://www.tuling123.com/openapi/api'
    # 此apikey为wxpy自带apikey，建议自己免费申请一个
    apikey = '7c8cdb56b0dc4450a8deef30a496bd4c'
    data = {'key': apikey, 'info': '你好'}
    req = requests.post(api_url, data=data).text
    replys = json.loads(req)['text']
    print(replys)