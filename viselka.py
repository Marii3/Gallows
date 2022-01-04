import random
f = open("new.txt", "r")
slovn= f.read().split("\n")
 
def visel(alphabet, lives, test):
    new_test = list(test)
    visible = len(new_test) * "*"  
    print(visible)
    while lives != 0:
        print(alphabet)
        user_choice = input("choose letter: ")
        while user_choice not in alphabet:
            user_choice = input("choose letter: ")
        alphabet= alphabet.replace(user_choice, "")    
        index = None
        for i in range(len(new_test)):
            if new_test[i] == user_choice:
                index = i 
                visible = list(visible)
                visible[index] = user_choice
                visible= "".join(visible)
                print(visible)
                print(lives)
                if visible == test:
                    print(visible, "Wy pobedili")
                    lives =0
            else:
                if i == len(new_test)-1 and index == None:
                    index = -1
                    if index == -1:
                        lives -= 1  
                        print(lives)
                        print(visible)
                        if lives == 0:
                            print(test, "wy proigrali")                
 
test = random.choice(slovn)
#print(test)
 
visel('abcdefghijklmnopqrstuvwxyz', 8, test)   