# Check correct password to make login otherwise keep asking for password 3 times.

passwd = "0xkaran"

attempt = input("Enter last password you remember: ")
attempt_count = 1

while attempt != passwd:
    attempt = input("Password does not match, try again: ")
    attempt_count = attempt_count + 1
    if attempt_count > 2:
        print("You've entered wrong password multiple times, please try again later")
        break
else:
    print("This is the correct password")
    print("Redirecting to your admin dashboard")
