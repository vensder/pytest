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
