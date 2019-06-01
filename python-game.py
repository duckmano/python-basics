#Dependencies
from random import randint
import math

#Display the welcome message
print("""\n
|￣￣￣￣￣￣￣￣|
| Welcome to the |
|      Number    |
|       Game     |
|＿＿＿＿＿＿＿＿|
(\__/) ||
(•ㅅ•) ||
/ 　 づ\n""")

#Print the rules of the game
print('Provide a range of numbers from 1 to your defined maximum.  Guess the number within a range of tries to win!')

#Solicit user input
#num_max = int(input("\nWhat is the upper bound you would like to set? "))


#Initialize loop for input
x = 0
while x == 0 :
    num_max_str = input("\nWhat is the upper bound you would like to set? ")

#Error checking - lets make sure this is actually a positive integer
    try:
        num_max = int(num_max_str)    
        if(num_max > 0):
            x = 1
        else:
            print("Please enter a valid positive integer\n")
            continue
    except ValueError:
        print("Please enter a valid positive integer\n")

#Generate a number of tries based on how big the boundary is set
if num_max <= 20 :
    tries = 5
else :
    tries = num_max / 10

#Lets set tries to 5 as a minimum, and round the number up if it isn't whole
if tries < 5 :
    tries = 5

tries = math.ceil(tries)

#Tell them how many tries they get
print("You will have", tries, "chances to guess correctly.")

#Generate the random number
num_ran = randint(1, num_max)

#Take a guess and compare.  Provide feedback.  Loop for five chances
#Initialize chance
chance = 1

#Main Loop
for chance in range(1,tries + 1) :
    print ('\nThis is chance number', chance)

    #Solicit user guess and make sure it is a valid positive integer
    x = 0
    while x == 0 :
        guess_str = input("'What do you think the number is? ")
        try:
            guess = int(guess_str) 
            if(guess > 0):
                x = 1
            else:
                print("Please enter a valid positive integer\n")
                continue
        except ValueError:
            print("Please enter a valid positive integer\n")
    
    if guess > num_max :
        print ('\nThat\'s not even in the range you provided!')
        continue
    
    if guess < num_ran :
        print('\nToo low!')
    
    elif guess > num_ran :
        print('\nToo high!')
    
    else :
        print ('\nBingo!!!!')
        print("""
-----------------------------------------------------
   _                             .-.
  / )  .-.    ___          __   (   )
 ( (  (   ) .'___)        (__'-._) (
  \ '._) (,'.'               '.     '-.
   '.      /  "\               '    -. '.
     )    /   \ \   .-.   ,'.   )  (  ',_)    _
   .'    (     \ \ (   \ . .' .'    )    .-. ( \\
  (  .''. '.    \ \|  .' .' ,',--, /    (   ) ) )
   \ \   ', :    \    .-'  ( (  ( (     _) (,' /
    \ \   : :    )  / _     ' .  \ \  ,'      /
  ,' ,'   : ;   /  /,' '.   /.'  / / ( (\    (
  '.'      "   (    .-'. \       ''   \_)\    \\
                \  |    \ \__             )    )
              ___\ |     \___;           /  , /
             /  ___)                    (  ( (
             '.'                         ) ;) ;
                                        (_/(_/
----------------------------------------------------
            """)
        break

    #Print a message if this was the last chance
    if chance == tries:
        print('Sorry, those are all the chances you have, thanks for playing!')