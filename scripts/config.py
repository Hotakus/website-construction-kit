import json5

config = ""

with open("../config.json", "r") as f:
    config = f.read()

config = config.replace("wp_db", "test")

js = json5.loads(config)

print(config)

print(js["db_options"]["use_default"])


str = "hello a"
str = str.replace('a', "world")
print(str)
