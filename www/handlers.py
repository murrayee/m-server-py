import re, time, json, logging, hashlib, base64, asyncio

from aiohttp import web

from coroweb import get, post

from apis import Page, APIValueError, APIResourceNotFoundError

from models import User

from config import configs


def get_page_index(page_str):
    p = 1
    try:
        p = int(page_str)
    except ValueError as e:
        pass
    if p < 1:
        p = 1
    return p


@get('/api/users')
async def api_get_users(*, page='1'):
    # page_index = get_page_index(page)
    # num = await User.findNumber('count(id)')
    # p = Page(num, page_index)
    # if num == 0:
    #     return dict(page=p, users=())
    # users = await User.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    # for u in users:
    #     u.password = '******'
    # return dict(page=p, users=users)
    users = await User.findAll()
    return dict(users=users)
