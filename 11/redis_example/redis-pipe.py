import redis
import time


pool = redis.ConnectionPool(host='localhost')

r = redis.Redis(connection_pool=pool)

pipe = r.pipeline(transaction=True)

pipe.set('name', 'test')

time.sleep(60)

pipe.set('age', 60)

pipe.execute()

































