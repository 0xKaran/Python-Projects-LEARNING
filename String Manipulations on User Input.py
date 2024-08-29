# Project source: https://dailypythonprojects.substack.com/p/string-manipulations-on-user-input

name = input("Please enter your full name: ")

print("\nYour name in upper case: ", name.upper())
print("Your name in lower case: ", name.lower())

print("Number of characters in your name (without spaces): ", len(name.replace(" ", "")))

print("Your name in revese order: ", name[::-1], "\n")
