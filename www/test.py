import asyncio

import orm
from models import User, Topics, Article, Message, AccessToken, AuthorizationCode, Client, RefreshToken


async def test(loop):
    await orm.create_pool(loop, user='root', password='12345678', db='murray')
    u = User(avatar='/12313123123.png', username='murray', password='123456', firstLetter='M', phone='18502346413')
    await u.save()


async def find(loop):
    await orm.create_pool(loop, user='root', password='12345678', db='murray')
    rs = await User.findAll()
    print('查找测试：%s' % rs)


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([test(loop), find(loop)]))
loop.run_forever()
