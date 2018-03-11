import orm
from models import User, Blog, Comment
import asyncio

async def test(loop):
    db_dict = { 'user':'root', 'password':'123456', 'db':'awesome' }
    await orm.create_pool(loop= loop, **db_dict)
    u = User(name='Test', email='test@example.com', passwd='123456', image='about:blank')
    await u.save()



loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()



