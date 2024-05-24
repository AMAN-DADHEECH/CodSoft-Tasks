print(f"This program is designed for Rock, Paper and Sciessor Game with computer")
import random
while True :
    print("User Can only Command --> (R or r ) ---> Rock , (P or p) ---> Paper , (S or s) ---> Sciessors  ,  Exit --->  (E or e)")
    user = input("Enter the Choice ---> ")
    if user == 'E' or user == 'e':
        print("user has chosen to Exit ")
        break
    else :
        possible_choice = ['R', 'P', 'S', 'r', 'p' , 's']
        computer = random.choice(possible_choice)
        print(f"The Game Begins :")
        print(f"User has chosen {user}")
        print(f"Computer has chosen: {computer}")
        if (user == 'R' or user == 'r') and (computer == 'R' or computer == 'r') :
            print(f"The Match is tie ")
        elif (user == 'S' or user == 's') and (computer == 'S' or computer == 's') :
            print(f"The Match is tie ")
        elif (user == 'P' or user == 'p') and (computer == 'P' or computer == 'p') :
            print(f"The Match is tie ")
        elif (user == 'R' or user == 'r') and (computer == 'S' or computer == 's') :
            print(f"The winner is ---> user by {user}")
        elif (user == 'R' or user == 'r') and (computer == 'P' or computer == 'P') :
            print(f"The winner is ---> computer by {computer}")
        elif (user == 'P' or user == 'p') and (computer == 'R' or computer == 'r') :
            print(f"The winner is ---> user by {user}")
        elif (user == 'P' or user == 'p') and (computer == 'S' or computer == 's') :
            print(f"The winner is ---> computer by {computer}")
        elif (user == 'S' or user == 's') and (computer == 'R' or computer == 'r') :
            print(f"The winner is ---> computer by {computer}")
        elif (user == 'S' or user == 's') and (computer == 'P' or computer == 'p') :
            print(f"The winner is ---> user by {user}")
        else :
            print(f"Invalid user Input Try again !!")

