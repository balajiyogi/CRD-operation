import json

import colorama         #please install colorama by (pip install colorama) command

colorama.init(autoreset=True)

with open('value.json','w') as d:
    json.dumps({"name":"balaji"})

with open('value.json', 'r') as d:
    del (json.load(d))["name"]

# CREATE OPERATION
def create(key, value):
    temp={}
    if len(key) <= 32:
        if len(value) <= 16777216:
            with open('value.json','r') as m:
                temp = json.load(m)
            with open('value.json', 'w') as d:
                if key not in temp:
                    t = {key:value}
                    temp.update(t)
                    if len(t) <= 1073741824:
                        json.dump(t, d)
                        print("\033[1;32;40m Successfully created.......")
                    else:
                        print('\033[1;31;40m ERROR: The size of file storing is too large. The size of file storing data must never exceed 1GB!!')
                else:
                    print('\033[1;31;40m ERROR: This key is already exist. Try different key!!')
        else:
            print('\033[1;31;40m ERROR: The value size is too large. The Value is always a JSON object at 16KB!!')
    else:
        print('\033[1;31;40m ERROR: The key size is too large. The Key is always a string-capped at 32char!!')
    return 0


# READ OPERATION
def read(key):
    st = ""
    with open('value.json', 'r') as d:
        if key not in (json.load(d)).keys():
            print('\033[1;31;40m ERROR: This key is not available in database. Try different key!!')
        else:
            st += "{" + '"{}"'.format(key) + ":" + '"{}"'.format(json.load(d)[key]) + "}"
            st = json.loads(st)
    print(st)
    return 0


# DELETE OPERATION

def delete(key):
    with open('value.json', 'r') as d:
        if key not in (json.load(d)).keys():
            print('\033[1;31;40m ERROR: This key is not available in database. Try different key!!')
        else:
            print(json.load(d).key)
            del json.load(d).key
            print("\033[1;32;40m Successfully deleted.......")
    return 0
