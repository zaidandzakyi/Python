from time import sleep
import random

password_list = ['strongp4ss','secret','m1ne','dont\'know']
random_password = random.randint(0,3)
random_pick = password_list[random_password]
print(10*"=", "Mini-Program", 11*"=")
print("Hack This username = \"Username123\"")
print(35*"=")

loop = True
while loop:
    password = input("guess : secret | m1ne | dont'know | strongp4ss |  : ")
    if password == random_pick:
        for i in range (1, 101, 1):
            i /= 100
            print(f"{i:.0%}")
            sleep(0.05)
            if i == 1:
                print("\nSUCCESS...\nYou get 1000 $")
                loop = False
    else :
        for i in range (1,51,1):
            i /= 100
            print(f"{i:.0%}")
            sleep(0.05)
            if i == 0.5:
                print("\nFAILED...")
                input_again = input("\nwanna try again (yes/no) : ")
                if input_again == 'yes':
                    continue
                else :
                    print("Program failed")
                    loop = False
print("Good Bye...")