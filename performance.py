import time
import string


def search_for_elm(L,e):
    for i in L:
        if i == e:
            return True
    return False


L = 100 * list(string.ascii_lowercase)[:-1]


for l in ['a', 'z']:
    t = time.process_time()

    for i in range(10000):
        S = search_for_elm(L, l)
        
    elapsed_time = time.process_time() -t
    print(round(elapsed_time, 6), S, l)



    t = time.process_time()
    for i in range(10000):
        S = l in L
        
    elapsed_time = time.process_time() -t
    print(round(elapsed_time, 6), S, l)



def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small + extra)
    return smaller + new


L = list(string.ascii_lowercase)[0:10]

print(genSubsets(L))
