import random as rand

mapping =  {
    1:"Rock",
    2:"Paper",
    3:"Scissor",
}

random_guess = rand.randint(1,4)
#print(random_guess)

user_input= int(input("start the game take the guess"))

if random_guess == user_input:
    print(f"yeah so its a draw u chhose {mapping[user_input]} and sysstem chhose : {mapping[random_guess]}")
elif random_guess == 1:
    if user_input == 2:
        print(f"user win user choose {mapping[user_input]} and system choice was {mapping[1]}")
    else: 
        print("moye moye")

elif random_guess == 2 :
    if user_input == 3:
        print(f"user win user choose {mapping[user_input]} and system choice was {mapping[2]}")
    else: 
        print("moye moye")

elif random_guess == 3 :
    if user_input == 1:
        print(f"user win user choose {mapping[user_input]} and system choice was {mapping[3]}")
    else: 
        print("moye moye")





















































