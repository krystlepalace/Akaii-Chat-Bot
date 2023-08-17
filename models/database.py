import redis


class Database:
    __instance = None
    
    def __init__(self, redis_url):
        self.r = redis.Redis(redis_url, charset="utf-8", decode_responses=True)

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Database, cls).__new__(cls)
        else:
            cls.__instance.__init__(*args, **kwargs)

        return cls.__instance

