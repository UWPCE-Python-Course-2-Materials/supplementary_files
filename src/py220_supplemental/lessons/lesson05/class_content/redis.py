"""
    demonstrate use of Redis
"""

# code intentionally omitted - see git for complete module

try:
    log.info('Step 1: connect to Redis')
    r = src.login_database.login_redis_cloud()
    log.info('Step 2: cache some data in Redis')
    r.set('andy', 'andy@somewhere.com')

    log.info('Step 2: now I can read it')
    email = r.get('andy')
    log.info('But I must know the key')
    log.info(f'The results of r.get: {email}')

except Exception as e:
    print(f'Redis error: {e}')
