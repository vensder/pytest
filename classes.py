def delta(L1,L2):
    deltas = []
    for i in range(len(L1)):
        deltas.append((L1[i] - L2[i])**2)
    return (sum(deltas))**0.5


class CoordN(object):
    Nmax = 4
    def __init__(self, *args):
        self.coords = []
        self.dimentions = len(args)
        for i in range(self.dimentions):
            self.coords.append(args[i])
    def distance(self,other):
        if isinstance(other, CoordN):
            if self.dimentions == other.dimentions:
                self.deltas = []
                for i in range(self.dimentions):
                    self.deltas.append((self.coords[i] - other.coords[i])**2)
                return (sum(self.deltas))**0.5
            else:
                raise ValueError('Not the same dimentions')
        else:
            raise ValueError('not the same type')


class Coord1(object):
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


