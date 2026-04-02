import random
import csv
import os


def get_player_infp():
    print("##==Are you a registerd player or want to play as guest==##")
    print('##== To  register urself press 2 to sign in please press 1 to play as guest presss zero==##')

    decision = int (input("choice: "))
    if decision == 1:
        name = input("whats your name: ")
        try:
            details = read_details(name)
            return details
        except:
            print("name not in database wanna try again ")
            print("you should ")
            get_player_infp()

    elif decision == 0 :
        return 0
    
    elif decision == 2:
        name = input("whats your name : ")
        record_maintian([name , 99999999 , 0 , 0 ]) #[name , high score , total games played , last score]
        print("you have been registered succesfully")
        print("sign in again to continue")
        return get_player_infp()
    
    else :
        print("not a valid input Try again")
        get_player_infp()
    


def record_maintian(data):
    with open ("data.csv",'a') as file:
        wrietr = csv.writer(file)
        wrietr.writerow(data)

def read_details(name):
    with open("data.csv", 'r') as file:
        csv_read_data = csv.reader(file)
        for i in csv_read_data:
            if i[0] == name:
                return i 
            

details = get_player_infp()

def show_details(details = details):
    if details == 0 :
        print("you playing guest mode")
    else:
        #print(details)
        print(f"you are {details[0]} || past high record {details[1]} || total game played {details[2]} || last game score {details[3]}")
        ##global current_score
        ##current_score = 0

def update_record(counter,details=details ):
    if details != 0:
        new_details = [details[0]] 
        if counter < int(details[1]):
            new_details.append(counter)
        else:
            new_details.append(details[1])
        new_details.append(int(details[2])+1)
        new_details.append(counter)
        #print(type(int(details[1])))
        #int(details[2])+=1
        #int(details[3])=counter
        #if counter<int(details[1]):
        #    details[1]=counter

        with open ('newfile.csv', 'w') as newfile:
            with open ('data.csv', 'r') as file:
                csv_file_read = csv.reader(file)
                csv_new_file_write = csv.writer(newfile)

                for i in csv_file_read:
                    if i[0]!=details[0]:
                        csv_new_file_write.writerow(i)
                    elif i[0]==details[0]:
                        csv_new_file_write.writerow(new_details)
                    else: 
                        continue

        print("record updated ")

        os.remove('data.csv')
        os.rename('newfile.csv','data.csv')
    else :
        pass


        
    

def random_gen():
    global a
    a = random.randint(1,81)

random_gen()

def get_int_guess():
    guess = int(input("guess the number: "))
    return guess

counter = 0

show_details()
while True:

    guess=get_int_guess()
    print(a)
        
    if abs(guess-a) >= 50 :
        print("far off")
    elif abs(guess -a) >= 25 and abs(guess - a) < 50 :
        print("getiin closer")
    elif abs(guess - a) >= 10 and (guess -a) < 25 :
        print("almost there")
    elif guess != a and abs(guess - a) < 10 and abs(guess - a) > 0:
        print("just bad lcuk ig")

    elif guess == a :
        print(f"you guessed it inddeed in {counter} attempts")
        update_record(counter)
        
        break

    else:
        print("idk how you manage to break the game")
        break

    counter =  counter + 1


