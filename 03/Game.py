def validate(f):
    def wrapper(*args):
        a = 1
        for i in args:
            a = a + 1
            if not isinstance(i, int):
                raise TypeError(a)
        ret = f(*args)
        return ret
    return wrapper
@validate
def printValues(*args):
    for i in args:
        print (i)
if __name__ == '__main__':
    printValues(2, 3, 4, 5)
