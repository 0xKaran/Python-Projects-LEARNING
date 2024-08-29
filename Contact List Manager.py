# Project source : https://dailypythonprojects.substack.com/p/easy-bilingual-vocabulary-with-python

# dictionary
contacts = {}

# loop until user types done
while True:
    name = input("You name or 'done: ")
    if name.lower() == "done":
        break
    phone = input("%s's phone number: " % name)
    contacts[name] = phone #saved to dictionary

# saving to txt file on machine
with open("contacts.txt", "w") as file:
    for name, phone in contacts.items():
        # file formatting (name: 977)
        file.write(f"{name}: {phone}\n")
