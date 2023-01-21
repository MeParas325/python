with open("Tanuja.txt", "r") as f:
    f.seek(20)
    print(f.tell())
    print(f.read(10))

with open("tanuja.txt", "w") as f:
    f.writelines("Hello world")
    f.truncate(6)
    