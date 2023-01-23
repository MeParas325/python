square = lambda x: x * x
print(square(4))

avg = lambda x, y: (x + y) / 2
print(avg(2, 5))

def apply(fx, value):
    return fx(value)

cube = lambda x: x * x * x
print(apply(cube, 4))
print(apply(lambda x: x * x * x, 5))
