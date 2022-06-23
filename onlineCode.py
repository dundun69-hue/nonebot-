import requests
import json
from nonebot import on_command

from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.adapters import Message
from nonebot.params import EventMessage
#响应格式  {"output":"Hello\n","errors":"\n\n"}
def cainiaobianyi(javacode):
 cainiaoUrl='https://tool.runoob.com/compile2.php'
 fuzai ={'code':javacode,'token':'4381fe197827ec87cbac9552f14ec62a','language':'8','fileext':'java'}
 response = requests.post(url = cainiaoUrl,data=fuzai)
 jieguo = json.loads(response.text)['output']
 return jieguo

onlineCode= on_command('在线编程',priority=5)
@onlineCode.handle()
# async def first_Message(bot:Bot,event:Event,args: Message = CommandArg()):
#  code_text = args.extract_plain_text()
#  await onlineCode.finish(message=cainiaobianyi(javacode=code_text))
async def first_Message(matcher: Matcher,args:Message = CommandArg()):
 Code_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/在线编程 code，则args为code
 if Code_text:
  matcher.set_arg('code',args)  # 如果用户发送了参数则直接赋值 赋值给下面的got里的参数

@onlineCode.got('code',prompt="请输入你的代码（只做了java）")
async def second_city(code: Message = Arg()):
   qqcode_text = code.extract_plain_text()
   await onlineCode.finish(cainiaobianyi(javacode=qqcode_text))