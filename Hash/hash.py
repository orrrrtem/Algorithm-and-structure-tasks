print("aaaaaa")
PRIME = 7717


def linkedhash_fun(c):
    ans = 0
    for x in c:
        ans = (ans + ord(x)) % m
    return ans


def openhash_linefun(ans,i):
    ans = (ans + i * step) % m
    return ans


def openhash_quadfun(ans,i):
    ans = (ans + i * i) % m
    return ans


def h2(ans):
    ans = (ans % 97) + 1
    return ans


def openhash_doublefun(ans):
    ans = (ans + h2(ans)) % m
    return ans


def openhash_insert(c):
    key = linkedhash_fun(c)
    if T[key] is -1:
        T[key] = c;
    else:
        i = 1
        while(i):
            key = openhash_linefun(key,i)
            if T[key] is -1:
                T[key] = c;
                i = -1
            i = i + 1
def quad_openhash_insert(c):
    key = linkedhash_fun(c)
    if T[key] is -1:
        T[key] = c;
    else:
        i = 1
        while(i):
            key = openhash_quadfun(key,i)
            if T[key] is -1:
                T[key] = c;
                i = -1
            i = i + 1


def double_openhash_insert(c):
    key = linkedhash_fun(c)
    if T[key] is -1:
        T[key] = c;
    else:
        i = 1
        while(i):
            key = openhash_doublefun(key)
            if T[key] is -1:
                T[key] = c;
                i = -1
            i = i + 1


def openlinehash_search(c):
    key = linkedhash_fun(c)
    if T[key] == -1:
        print('There are no', c)
    if T[key] is c:
        print("Search:", c, "corresponding key is", key)
    else:
        i = 1
        while(i > 0):
            key = openhash_linefun(key, i)
            if T[key] == -1:
                print('There are no', c)
                i = -5
            else:
                if c in T[key]:
                    print("Search:", c, "corresponding key is", key)
                    i = -5
            i = i + 1


def quad_openhash_search(c):
    key = linkedhash_fun(c)
    if T[key] == -1:
        print('There are no', c)
    if T[key] is c:
        print("Search:", c, "corresponding key is", key)
    else:
        i = 1
        while(i>0):
            key = openhash_quadfun(key, i)
            if T[key] == -1:
                print('There are no', c)
                i = -100
            else:
                if c in T[key]:
                    print("Search:", c, "corresponding key is", key)
                    i = -5
            i = i + 1

def double_openhash_search(c):
    key = linkedhash_fun(c)
    if T[key] == -1:
        print('There are no', c)
    if T[key] is c:
        print("Search:", c, "corresponding key is", key)
    else:
        i = 1
        while(i>0):
            key = openhash_doublefun(key)
            if T[key] == -1:
                print('There are no', c)
                i = -5
            else:
                if c in T[key]:
                    print("Search:", c, "corresponding key is", key)
                    i = -5
            i = i + 1



def linkedhash_mapinsert(c):
    key = linkedhash_fun(c)
    if T[key] == -1:
        T[key] = []
        T[key].append(c)
    else:
        if(c not in T[key]):
            T[key].append(c)

def init_table(T,m):
    for i in range(m):
        T.append(-1)

def linkedhash_search(c):
    key = linkedhash_fun(c)
    if T[key] == -1:
        print('There are no', c)
    else:
        if (T[key] is not list):
            if c in T[key]:
                print("Search:", c, "corresponding key is", key)
            else:
                print('There are no', c)
        else:
            for x in range(1,T[key].size):
                if T[key][x] == c:
                    print("Search:", c, "corresponding key is", key, "num in chain", x)
                else:
                    if x == T[key].size:
                        print('There are no', c)

tbb ="Assume that you have an object and you want to assign a key to it to make searching easy. To store the key/value pair, you can use a simple array like a data structure where keys (integers) can be used directly as an index to store values. However, in cases where the keys are large and cannot be used directly as an index, you should use hashing."
tr = 'a s d x c dcv xzb asn m g h j k f f fd df cxv nx nv fejfreh qwejqwe tggjtgu erfgxefrcf xjefnr bgtijbtib ewjejf dcnsdcsdn vf vfn  rfef w22 dss vtt yyh34 fer'
text = 'A hash function is any yna function that can be used to map data of arbisstrary size to data of a fixed size. The values returned by a hash function are called hash values, hash codes, digests, or simply hashes'
w = tr.split()
m = 9 * len(w)
step = 13
print(m)
T = []
init_table(T,m)
for x in w:
    linkedhash_mapinsert(x)
k = 0
print("chain's collision resolving")
print("---------------------------")
print("---------------------------")
print("---------------------------")
for x in range(0,m):
    if T[x] != -1:
        k = k + 1
        print(T[x],' with corresponding key ', x)
print("---------------------------")
j = linkedhash_fun('is')
print(j)
j = linkedhash_fun('hash')
print(j)
linkedhash_search('df')
print("---------------------------")
print("---------------------------")
print("open linear collision resolving")
print("---------------------------")
print("---------------------------")
T = []
init_table(T,m)
k = 0
for x in w:
    openhash_insert(x)
for x in range(0,m):
    if T[x] != -1:
        k = k + 1
        print(T[x],' with corresponding key ', x)



print(k)
print(len(w))
print("")

openlinehash_search('df')
print("---------------------------")
print("---------------------------")
print("open quad collision resolving")
print("---------------------------")
print("---------------------------")
T = []
init_table(T,m)
k = 0
for x in w:
    quad_openhash_insert(x)
for x in range(0,m):
    if T[x] != -1:
        k = k + 1
        print(T[x],' with corresponding key ', x)



print(k)
print(len(w))
print("")

quad_openhash_search('df')

print("---------------------------")
print("---------------------------")
print("double open  collision resolving")
print("---------------------------")
print("---------------------------")
T = []
init_table(T,m)
k = 0
for x in w:
    double_openhash_insert(x)
for x in range(0,m):
    if T[x] != -1:
        k = k + 1
        print(T[x],' with corresponding key ', x)



print(k)
print(len(w))
print("")

double_openhash_search('df')



