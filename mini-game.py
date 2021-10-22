#Mini Game
import random
print("\n======= Mini Game =======\n")
print("--Fight the computer to win")
name = input("Input yourname : ")
player = {'Name': name,'Health' : 200,'attack':30}
computer = {'Name':"Computer",'health': 200,'attack' : 30}
options = ['attack','heal','powerup']

def start():
    input_user = input("\noptions :\n1.Heal \n2.Stats \n3.Attack \n4.increase attack\n5.Quit\nChoice : ")
    if input_user == "1":
        heal()
        check()
    elif input_user == "2":
        stats()
    elif input_user == "3":
        attack()
    elif input_user == "4":
        powerup()
    else :
        exit()

def heal():
    player["Health"] += 30
    print("\nNow yourhealth : ",player["Health"])
    c_input()
    check()
    

def attack():
    computer["health"] -= player["attack"]
    print("\nAttacking, computer health : ",computer["health"])
    c_input()
    check()
    

def stats():
    print(player)
    print(computer)
    start()

def powerup():
    player["attack"] += 30
    print("\nNow your Attack : ",player["attack"])
    c_input()
    check()
    
def check():
    if player["Health"] < 0:
        print("\nyou lose :(") 
        quit()
    if computer["health"] < 0:
        print("\nyou win :) ,good job,see you next time")
        quit()
    else :
        start()

def c_input():
    random_numbers = random.randint(0,2)
    computer_pick = options[random_numbers]
    if computer_pick == "attack":
        player["Health"] -= computer["attack"]
        print("computer attack, player health : ",player["Health"])
    elif computer_pick == "heal":
        computer["health"] += 30
        print("computer heal,computer health : ",computer["health"])
    elif computer_pick == "powerup":
        computer["attack"] += 30
        print("computer power up,computer Attack : ",computer["attack"])

def exit():
    print("\nThank You for playing,Goodbye.....")
    quit()


start()