import random, string
import webbrowser
import time
import requests





num=input('HOW MAMY CODE YOU WANT TO GENERATE WRITE  ')

f=open("Nitro Codes.txt","w", encoding='utf-8')

print("GEN HAS BEEN STARTED")
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")

f.close()

#=============Checker=========================


with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" | {} ".format(line.strip("\n")))
            break
        else:
            print(" invalid | {} ".format(line.strip("\n")))
input("YOUR ALL CODE HAS BEEN GENERATED! PRESS ENTER 5 TIME TO STOP THIS PROJECT ")
input("1")
input("2")
input("3")
input("4")
input("5")
