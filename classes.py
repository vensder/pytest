class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def intersect(self, other):
        self.intersection = []
        for i in self.vals:
            if i in other.vals:
                self.intersection.append(i)
        self.intersection.sort()
        return '{' + ','.join([str(e) for e in self.intersection]) + '}'


    def __len__(self):
        return len(self.vals)
        

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

s1 = intSet()
s2 = intSet()

s1.insert(1)
s1.insert(2)

s2.insert(2)
s2.insert(3)

print(s1,s2)
print(s1.intersect(s2))
print(s1.len())
s3 = intSet()
s3.insert(5)
s3.insert(6)
s3.insert(7)
print(s3.len())
print(s1.intersect(s3))

print('++++++++++++++++++++')

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        return self.getX() == other.getX() and self.getY() == other.getY()

    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'


c = Coordinate(1,2)
d = Coordinate(1,2)
e = Coordinate(3,4)

print(c, d)
print(c == d)
print(c is d)
print(c.__repr__())
print(repr(c))
f = eval(repr(c))
print(f)
print('=============')



class intSetMy():
    def __init__(self):
        self.vals = []
    def member(self, i):
        return i in self.vals
    def insert(self, i):
        if not self.member(i):
            self.vals.append(i)
            return True
        else:
            return False
    def remove(self, i):
        if self.member(i):
            self.vals.remove(i)
            return True
        else:
            return False
    def __str__(self):
        return str(sorted(self.vals))

i = intSetMy()
print(i)
i.insert(1)
print(i)
i.insert(1)
print(i)
i.insert(2)
print(i)
i.remove(2)
print(i)
i.remove(3)
print(i)


class intSet1():
    def __init__(self):
        self.vals = []
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
    def member(self,e):
        return e in self.vals
    def remove(self, e):
        if e in self.vals:
            self.vals.remove(e)
        else:
            return False
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result += str(e) + ', '
        return '<' + result.strip(', ') + '>'

i1 = intSet1()
print(i)
i1.insert(1)
print(i1)
i1.insert(1)
print(i1)
i1.insert(2)
print(i1)
i1.remove(2)
print(i1)
i1.remove(3)
print(i1)

class fraction():
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__(self,other):
        numerNew = other.getDenom() * self.getNumer() + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    def __sub__(self,other):
        numerNew = other.getDenom() * self.getNumer() - other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    def __mul__(self, other):
        numerNew = self.getNumer() * other.getNumer()
        denomNew = self.getDenom() * other.getDenom()
        return fraction(numerNew, denomNew)
    def __truediv__(self, other):
        fracNew = fraction(other.getDenom(), other.getNumer())
        return self * fracNew
    def convert(self):
        return self.getNumer() / self.getDenom()


f1 = fraction(1,2)
f2 = fraction(3,4)
print(f1, f2)
print(f1 + f2)
print(f1 - f2)
print(f1 + f1)
print(f1 - f1)
print(f1 * f2)
print(f1 / f2)
print(f1.convert(), f2.convert())

def delta(L1,L2):
    deltas = []
    for i in range(len(L1)):
        deltas.append((L1[i] - L2[i])**2)
    return (sum(deltas))**0.5


class CoordN():
    def __init__(self, *args):
        self.coords = args
        self.dimentions = len(args)
    def __check(self, other):
        if not isinstance(other, CoordN):
            raise ValueError('Not the same type')
        else:
            if self.dimentions != other.dimentions:
               raise ValueError('Not the same dimentions')
    def distance(self, other):
        self.__check(other)
        self.deltas = ()
        for i in range(self.dimentions):
            self.deltas += ((self.coords[i] - other.coords[i])**2,)
        return (sum(self.deltas))**0.5
    def __sub__(self, other):
        self.__check(other)
        self.substraction = ()
        for i in range(self.dimentions):
            self.substraction += (self.coords[i] - other.coords[i],)
        # return eval ('CoordN' + str(self.substraction))
        return CoordN(*self.substraction)


class Coord1():
    def __init__(self, x):
        self.x = x
    def distance(self, other):
        return abs(self.x - other.x)


class Coord2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x_d = (self.x - other.x)**2
        y_d = (self.y - other.y)**2
        return (x_d + y_d)**0.5


class Coord(object):
    def __str__(self):
        return "Coord: (" + (str(self.x) + ', ' + str(self.y)) + ')'
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        if isinstance(other, Coord):
            x_d = (self.x - other.x)**2
            y_d = (self.y - other.y)**2
            return (x_d + y_d)**0.5
        else:
            raise ValueError('not the same type')
    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)

    
class coord(object):
    def __str__(self):
        return "coord"
    def __init__(self, x, y):
        self.x = x
        self.y = y

        
class Single(object):
    numbers = 0

    def __init__(self):
        if self.numbers == 0:
            pass
            
    
class Foo():
    def __init__(self):
        self.x = 5

    def makeInstanceAttribute(oops):
        oops.x += 1


class Counter(object):
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


c1 = CoordN(0,0,0)
c2 = CoordN(2,2,2)
print(c2.distance(c1))
d = c2 - c1
print(d.coords)

##c3 = CoordN(3,3)
##print(c3.distance(c1))
##d3 = c3 - c1
##print(d3.coords)
