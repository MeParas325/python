def greet(func):
    def func2(*args, **kwargs):
        print("hello")
        func(*args, **kwargs)
        print("Good morning")
    return func2

@greet
def hello():
    print("Paras Verma")

@greet
def add(a, b):
    print(a + b)

hello()

add(2, 5)