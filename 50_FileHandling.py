f = open("Tanuja.txt", "r")

while True:
    line = f.read()
    if not line:
        print("File ended")
        break
    print(line)

f.close()