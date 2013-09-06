#!/usr/bin/env python

import json
import redis
import sys

if sys.argv[1] != '--list':
    sys.exit()

r = redis.Redis()
groups = dict()

for key in r.keys():
    for fact, value in r.hgetall(key).iteritems():
        group="_".join([fact, value])
        if not groups.has_key(group):
            groups[group] = []
        groups[group].append(key)

print json.dumps(groups, sort_keys=True)
