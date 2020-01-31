import json

with open('./New_Krunker_Map_export.txt') as x:
  y = json.load(x)


# the result is a Python dictionary:
z = (y["objects"])
print(y["objects"])

for year in z:
    releases= released[year]
    print releases