import redis

redisHost = 'localhost'
redisPort = 6379

r = redis.Redis(host=redisHost, port=redisPort, decode_responses=True)

def createNode():
    print('creating node with CREATE')

def createNoteMatch():
    print('creating node with MERGE')
