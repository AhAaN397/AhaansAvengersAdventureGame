# Avengers Adventure Game
import random
import time

#Variable List
villianHealth = 90
villain = random.randint(1,3)# Randomizes the villian you get
playerHealth = random.randint(55,85) # randomizes health IronMan Gets
dodgeAttack = random.randint(1,2) # randomizes if your dodge attack works or fails.
dodgeDamage = random.randint(1,25)
                 

#Begin the Game
print("Welcome to Avengers Adventure!")
time.sleep(2)

#Get user input for character
player = input("Choose your player:\n1) Iron Man\n2) Bat Man\n3) Thor\n4) Captain America\n")
player = int(player) #This is needed to make the value for comparison

if player == 1: #Player chooses Iron Man
    damageDone = random.randint(35,75)  # randomizing damage done per player
    move = 'Laser Beam'  # changing move per player
    playerHealth = 85  # setting player health
if player == 3: #Player chooses thor
    damageDone = random.randint(55,90)
    move = 'Mjolnir'
    playerHealth = 100
    playerName = 'Thor'
    print("You have chosen " + playerName + "!")
    print("Your supper powers include: Super smart, Mjolnir.\nPress enter to continue.")
    input()
    print()
    print()
    print("Smartness level: max. Mjolnir power: max. Health = " + str(playerHealth) + ".")  
    time.sleep(3.5)
    print("Engaging in battle...")
    print("5...")
    time.sleep(1)
    print("4...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print()
    print("Choosing opponent.\n")
    time.sleep(1.2)
    print("Opponent found...\n")

if player == 4: #Player chooses Cap America
    damageDone = random.randint(65,100)
    move = 'Throw shield'
    playerHealth = 120
    playerName = 'Captain America'
    print("You have chosen " + playerName + "!")
    print("Your supper powers include: Super smart, Shield.\nPress enter to continue.")
    input()
    print()
    print()
    print("Smartness level: max. Shield power: max. Health = " + str(playerHealth) + ".")  
    damageTaken = random.randint(55,75)
    print("Engaging in battle with " + villainName + "...")  
    time.sleep(1)
    print(villainName + " super powers include: Laser Beam.")      
    time.sleep(1)
    print("Speed level: med. Smartness level: 10000000%. Health = " + str(villianHealth) + "\n")
   
# Doctor Doom
if villain == 3:
    villainName = 'Doctor Doom'
    villianHealth = 120
    damageTaken = random.randint(35,80)
    print("Engaging in battle with " + villainName + "...")  
    time.sleep(1)
    print(villainName + " super powers include: Destroy.")      
    time.sleep(1)
    print("Speed level: low. Smartness level: max. Health = " + str(villianHealth) + "\n")

# Skrull
if villain == 2:
    villainName = 'Skrull'
    villianHealth = 85
    damageTaken = random.randint(20,75)
    print("Engaging in battle with " + villainName + "...")  
    time.sleep(1)
    print(villainName + " super powers include: Shape Shifting.")      
    time.sleep(1)
    print("Speed level: low. Smartness level: max. Health = " + str(villianHealth) + "\n")

# Thanos  # keep for round three
if villain == 1:
    villainName = 'Thanos'
    villianHealth = 150
    damageTaken = random.randint(55,150)
    print("You are fighting the MEGABOSS!")
    time.sleep(1.2)
    print("Engaging in battle with " + villainName + "...")  
    time.sleep(1)
    print(villainName + " super powers include: Harnessing the powers of the infinty gauntlet.")      
    time.sleep(1)
    print("Speed level: low. Smartness level: max. Health = " + str(villianHealth) + "\n")

#Loop to check player health and engage battle
while playerHealth >= 0:                                            
    print("Choose move:\n1) Dodge\n2) " + str(move))
    #move = int(input(""))
    choice = int(input(""))
   
    dodgeAttack = random.randint(1,25)
    damageDone = random.randint(35,75)  # randomizing damage done per player
    if choice == 1 and dodgeAttack == 1:          # if statements to see if dodge attack works or fails
        print("You dodge his attack and do " + str(dodgeDamage) + " damage!\n")        
        time.sleep(1.2)
        villianHealth = villianHealth - dodgeDamage        
        print(villainName + " has " + str(villianHealth) + " health left.")
    if choice == 1 and dodgeAttack == 2:
        print("Your dodge failed...\n")
        time.sleep(1.2)
        print(villainName + " does " + str(damageTaken) + " damage!\n")
        time.sleep(1)
        print("You have " + str(playerHealth-damageTaken) + " health left\n")
        playerHealth = playerHealth - damageTaken
    if choice == 2:
        villianHealth = villianHealth - damageDone                                                
        print("You do " + str(damageDone) + " damage!\n")
        time.sleep(1.5)
        print(villainName + " has " + str(villianHealth) + " health left\n")
        time.sleep(1.2)
        if villianHealth <= 0:
            print("Congratulation!!! You have killed " + str(villainName) + "!\n")
            break
        else:
            print(villainName + " does " + str(damageTaken) + " damage!\n")
            time.sleep(1.2)
            print("You have " + str(playerHealth-damageTaken) + " health left\n")
            time.sleep(1)
            playerHealth = playerHealth - damageTaken               #Subtract the taken taken from overall health
           
if playerHealth <= 0:
    print("Sorry... You died.")

if villianHealth <= 0: # advancing to new round
    # work in progress...
    print("Test")# Avengers Adventure Game
