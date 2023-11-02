
import json
d = dict(name='Bob',age=20,sorce=80)
str = json.dumps(d)
print(str)
a = json.loads(str)

print(a)