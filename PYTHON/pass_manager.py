import random
import string

passwords = {}

#load pass file
try:
    with open("pass.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd
except:
    pass

def generate_password():
    chars = string.ascii_letters + string.digits + "!#$%"
    pasaword= "".join(random.choice(chars)for _ in range(8))
    return pasaword

while True:
    print("\n----PASSWORD MANAGER-----")
    print("1. save pass")
    print("2. View pass")
    print("3. genrate pass")
    print("4. exit")

    choice = input("enter your choice: ")

    if choice == "1":
        site = input("enter website: ")
        pwd = input("enter passs: ")

        passwords[site] = pwd
        with open("pass.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")

            print("saved!")

    elif choice == "2":
        if not passwords:
            print("no data")
        else:
                for site, pwd in passwords.items():
                    print(site, ":", pwd)
    elif choice == "3":
            print("genereted pass" , generate_password)
        
    elif choice == "4":
        print("ok b-byeeeeeeeeeeeeee...chal futtt...")
        break

    else:
         print("invalid input")