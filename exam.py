class A(object):
    def foo(self):
        print('hi')
class B(A):
    def foo(self):
        print('bye')



one = 0
two = 0

def foo_one(n):
    global one
    """ Assume n is an int >= 0 """
    answer = 1.0
    while n > 1:
        answer *= n
        n -= 1
        one +=1
    print(one)
    return answer

def foo_two(n):
    global two
    """ Assume n is an int >= 0 """
    if n <= 1: 
        return 1.0
    else:
        two += 1
        print(two)
        return n*foo_two(n-1)

print(foo_one(30))
print(foo_two(30))


def is_triangular(k):
    summa = 0
    i = 1
    while True:
        summa += i
        if summa == k:
            return True
        elif summa > k:
            return False
        i += 1
        
        
    
def getSublists(L, n):
    return [L[i:i+n] for i in range(len(L)-n+1)]

def longestRun(L):
    master = []
    longest = 0
    for i in range(len(L)+1):
        for k in getSublists(L, i):
            master.append(k)
    for h in master:
        if sorted(h) == h and len(h) >= longest:
            longest = len(h)
    return longest
