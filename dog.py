from urllib import request
from nonebot import on_message
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11 import Message
from nonebot.adapters.onebot.v11.message import Message


import httpx
import json
#创建requests 并且get一个url参数
dogUrl = 'https://api.dzzui.com/api/tiangou?format=json'
#(requests.get(url=dogUrl).text)
#定义一个函数可以在messages中循环调用这个接口 不会出现输出同样内容的情况
def dog_json():
    response = httpx.get(url=dogUrl)
    diaryJson = response.text
    #解析json的方法就是 json.loads(传入json数据，字符串)并在后面加上 [json里的键]   输出的就是键对应的值
    diary = json.loads(diaryJson)['text']
    return diary
# JavaUrl = 'https://tool.runoob.com/compile2.php'
# fuzai ={'code':'','token':'4381fe197827ec87cbac9552f14ec62a','language':'8','fileext':'java'}
# requests.post(url=JavaUrl,data=fuzai)

#创建事件响应器   --------》本次使用消息类型事件响应器 on_keyword
firstMessage = on_keyword(['语音舔狗'],priority=5)
@firstMessage.handle()
async def dog_diary_handle(bot:Bot,event:Event):
    #message=requests.get(url).text  在参数列表里设置请求 可以发消息都是一个请求而不是只请求一次固定数据
    #使用cq码  输出文本转语音的功能  cq码格式 [CQ:type,key=value]   文本转语音为tts类型
    raw_cqcode = '[CQ:tts,text='+dog_json()+']'
    cqcode = Message(raw_cqcode)
    await firstMessage.finish(cqcode)
dogMessage = on_keyword(['舔狗日记','今日舔狗'],priority=5)
@dogMessage.handle()
async def dog_Message(bot:Bot,event:Event):
    await dogMessage.finish(message=dog_json())