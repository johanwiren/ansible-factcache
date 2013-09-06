import redis

FACT_EXPIRATION = 86400

redis = redis.Redis()

def log(host, data):
    if type(data) == dict:
        invocation = data.pop('invocation', None)
        if invocation.get('module_name', None) != 'setup':
            return

    facts = data.get('ansible_facts', None)

    redis_pipe = redis.pipeline()
    for fact in facts:
        # Only store the basic types (strings) of facts
        if isinstance(facts[fact], basestring):
            redis_pipe.hset(host, fact, facts[fact])
    redis_pipe.expire(host, FACT_EXPIRATION)
    redis_pipe.execute()

class CallbackModule(object):
    def runner_on_ok(self, host, res):
        log(host, res)
