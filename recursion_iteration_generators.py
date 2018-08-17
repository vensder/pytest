def mult_iter(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

def iterPower(base, exp):
    result = 1
    while exp > 0:
        result *= base
        exp -=1
    return result

def mult_rec(a,b):
    if b == 1:
        return a
    else:
        return a + mult_rec(a, b-1)

def recurPower(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * recurPower(base, exp -1)

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

def gcdIter(a, b):
    for gdc in range (min(a,b),0,-1):
      if a % gdc == 0 and b % gdc == 0:
        return gdc


def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

    

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        return char == aStr
    else:
        mid = len(aStr)//2
        if char == aStr[mid]:
            return True
        elif char < aStr[mid]:
            return isIn(char, aStr[:mid])
        else:
            return isIn(char, aStr[mid+1:])

def genFib():
    fib1 = 1  #  fib(n-1)
    fib2 = 0  #  fib(n -2)
    while True:
        #  fib(n) = fib(n-1) + fib(n-2)
        next = fib1 + fib2
        yield next
        fib2 = fib1
        fib1 = next


def genPrimes():
    primes = [2]
    yield primes[0]
    guess = 3
    while True:
        if all(guess%x != 0 for x in primes):
            primes.append(guess)        
        if guess == primes[-1]:
            yield primes[-1]
        guess += 2
            
    
def h(n):
    """assume n an int >= 0"""
    answer = 0
    s = str(n)
    for c in s:
        answer += int(c)
    return answer


num = 0
def lenRecur(s):
    global num
    if s == '':
        return 0
    else:
        num +=1
        print(num)
        return 1 + lenRecur(s[1:])




def isIn(a, s):
   '''
   a is a character, or, singleton string.
   s is a string, sorted in alphabetical order.
   '''
   if len(s) == 0:
      return False
   elif len(s) == 1:
      return a == s
   else:
      test = s[len(s)//2]
      if test == a:
         return True
      elif a < test:
         return isIn(a, s[:len(s)//2])
      else:
         return isIn(a, s[len(s)//2+1:])


def union(L1, L2):
   '''
   L1 & L2 are lists of the same length, n
   '''
   temp = L1[:]
   for e2 in L2:
      flag = False
      for check in temp:
         if e2 == check:
            flag = True
            break
      if not flag:
         temp.append(e2)
   return temp


