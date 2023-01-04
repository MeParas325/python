def square(n):
    '''Takes number n and returns its square'''
    return n*n

print(square(4))
print(square.__doc__)

def square1(n):
    print("Inside square1")
    '''Takes number n and returns its square'''
    return n*n

print(square1(4))
print(square1.__doc__)

