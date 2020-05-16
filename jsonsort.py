import json, codecs

with codecs.open('data2.json','a+', 'utf-8','r') as f:
    data = json.load(f[0], strict=False)

print(data)