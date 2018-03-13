import orm
from models import User, Blog, Comment
import asyncio

async def test(loop):
    db_dict = { 'host':'127.0.0.1', 'user':'www-data', 'password':'wwww-data', 'db':'awesome' }
    await orm.create_pool(loop= loop, **db_dict)
    u = User(name='Test1', email='test1@example.com', passwd='123456', image='about:blank')
    await u.save()



loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()



