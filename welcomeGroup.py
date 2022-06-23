from nonebot import on_notice
from nonebot.typing import T_State

from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment,Message, GroupDecreaseNoticeEvent, GroupIncreaseNoticeEvent
welcome = on_notice()
#朋友加群
@welcome.handle()
#event:GroupIncreaseNoticeEvent  定义一个群组增加成员事件  event.get_user_id 获得增加的qq号  MessageSegment 可以发送at方法 @别人
async def _(bot: Bot, event:GroupIncreaseNoticeEvent, state: T_State):
    user = event.get_user_id()
    if(user!=bot.self_id):
        # 'file:///D:/HZY/Pictures/Saved Pictures/欢迎表情包.jpg'
     await welcome.finish(MessageSegment.at(user)+'欢迎加入本群啊！'+MessageSegment.image('file:///D:/software/QQBot/go-cqhttp/botdog/botdog/img/欢迎表情包.jpg'))
    else:
     await welcome.finish('大家好'+MessageSegment.image('file:///D:/software/QQBot/go-cqhttp/botdog/botdog/img/欢迎表情包.jpg'))
#群友退群
# @welcome.handle()
# async def _(bot: Bot, event:GroupDecreaseNoticeEvent, state: T_State):
#     user = event.get_user_id()
#     at_ = "[CQ:at,qq={}]".format(user)
#     msg = at_ + '\n' + '一位朋友离我们而去！'
#     msg = Message(msg)
#     await welcome.finish(message=msg)

# from nonebot import on_notice
# from nonebot.typing import T_State
# from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment,Message, GroupDecreaseNoticeEvent, GroupIncreaseNoticeEvent
# botHello = on_notice()
# @botHello.handle()
# async def bot_Hello(bot:Bot,event:GroupIncreaseNoticeEvent):
#     eventqq = event.user_id
#     botqq = bot.self_id
#     if(eventqq == botqq):
#         await botHello.finish('大家好')