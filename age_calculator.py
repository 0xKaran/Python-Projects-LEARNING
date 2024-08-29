import datetime

user_year = int(input("Enter your birth year: "))
current_year = datetime.datetime.now().year

age = current_year - user_year
print("You're %s years old" % age)
