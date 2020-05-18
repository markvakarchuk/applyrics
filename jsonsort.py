import json, codecs


song_id = 3

with codecs.open('data_test.json', 'a+', 'utf8') as f:
    f.seek(0)
    data = f.read()
    obj = json.loads(data)

num_songs = len(obj)

def checkList(lst): 
    ele = lst[0] 
    chk = True
    # Comparing each element with first item  
    for item in lst: 
        if ele != item: 
            chk = False
            break; 
    return chk

def rmvlast_frm_list(lst):
    return lst[:-1]

num_versus = len(obj[song_id]['versus'])

versus = []
versus_odd = []


for i in range(num_versus):
    print(obj[song_id]['versus'][i] + "\n\n")

    versus.append(obj[song_id]['versus'][i])

    if i%2 != 0:
        versus_odd.append(obj[song_id]['versus'][i])

if checkList(versus_odd):
    print("chorus")
elif checkList(rmvlast_frm_list(versus_odd)):
    print("chorus2")