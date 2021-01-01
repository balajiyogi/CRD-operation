import json

import redis

import colorama

colorama.init(autoreset=True)
r = redis.Redis()
t = {}
while True:
    print(
        "--------------------------------------------------------\nChoose the operation that you want to proceed \n1.Create\n2.Read\n3.Delete\n0.Exit\n--------------------------------------------------------")
    n = int(input())
    if n == 0:
        print("\033[1;32;40m Successfully closed.......")
        break
    elif n == 1:
        print("Do you want to give single key and value : (y/n)")
        ch = input()
        if ch == 'y':
            key = input()
            value = input()
            if key in r:
                print('\033[1;31;40m ERROR: This key is already exist. Try different key!!')
            else:
                r.set(key, value)
                print("\033[1;32;40m Successfully created.......")
                print("If you want to create Time-to-Live for keys : (y/n)")
                print("Give the key and Time-to-Live for key or keys in JSON object")
                c = input()
                if c == 'y':
                    t = json.loads(input().replace("'", ''))
                    for i in t.key():
                        if i not in r:
                            print('\033[1;31;40m ERROR: This key is not available in database. Try different key!!')
                        else:
                            print(i,t[i])
                            r.expire(i,t[i])
                            print("\033[1;32;40m Successfully created Time-to-Live value for given key or keys.......")
        else:
            kv = (input().replace("'", ''))
            kv = json.loads(kv)
            for i in kv.key():
                if i in r:
                    print('\033[1;31;40m ERROR: This key is already exist. Try different key!!')
                    break
            else:
                r.mset(kv)
                print("\033[1;32;40m Successfully created.......")
    elif n == 2:
        st = ""
        print("Enter the key that you want to read")
        key = input()
        if key not in r:
            print('\033[1;31;40m ERROR: This key is not available in database. Try different key!!')
        else:
            st += "{" + '"{}"'.format(key) + ":" + '"{}"'.format(str(r.get(key), 'utf-8')) + "}"
            st = json.loads(st)
            print(st)

    else:
        print("Enter the key that you want to delete")
        key = input()
        if key not in r:
            print('\033[1;31;40m ERROR: This key is not available in database. Try different key!!')
        else:
            r.delete(key)
            print("\033[1;32;40m Successfully deleted.......")
