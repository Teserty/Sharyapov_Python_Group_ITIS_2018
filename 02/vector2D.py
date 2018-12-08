import math
class Vector2D:
    n = 0
    @classmethod
    def whatistheclass(cls):
        return cls
    @staticmethod
    def getN():
        return
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __call__(self, *args, **kwargs):
        print("Vector was called")
    def len(self):
        return math.sqrt(math.pow(self.x, 2 )+ math.pow(self.y, 2 ))
    def __str__(self):
        return "<%s, %s>" % (self.x, self.y)
    #Math#
    def __eq__(self, v):
        return (v.x == self.x)*(v.y == self.y)
    def __add__(self, v):
        return Vector2D(self.x + v.x, self.y + v.y)
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.x * other, self.y * other)
        elif isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        raise Exception("error")