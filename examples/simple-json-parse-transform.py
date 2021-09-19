import json
#from arepl_dump import dump

msg = "Square Values"
print(msg)

jsonArray = json.loads(
    '[{"key":1,"value":1},{"key":2,"value":11},{"key":3,"value":44}]'
    )

for item in jsonArray:
    print(item["value"])

def square_element(x):
    return x["value"]**2

squares = list(map(square_element, jsonArray))

print(squares)