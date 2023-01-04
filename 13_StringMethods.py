name = "Paras"

print(len(name))
print(name.capitalize())
print(name.upper())
print(name.lower())

title = "What is your name?"

print(title.title())
print(title.istitle())
print(title.center(30))
print(title.isspace())

spacee = "       "
print(spacee.isspace())

friend = "Tanuja!!!"
print(friend.endswith("nja!!!"))
print(friend.islower())
print(friend.isupper())
print(friend.swapcase())

friend2 = "TANUJA"
print(friend2.islower())
print(friend2.isupper())
print(friend2.startswith("TA"))

str2 = "Welcome to my coding channel\n"
print(str2.isprintable())

str3 = "WelcomeToTheConsole12"
print(str3.isalnum())
print(str3.isalpha())
print(str3.find("ToThe"))
print(str3.endswith("To", 7, 11))
print(str3.endswith("To", 7, 9))