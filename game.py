#this program demonstrates a guessing game
#1.get user input
from random import randint

user_name=input("whats your name?")
print("hello there"+ user_name + "!")
#generate a random number
random_number=randint(10,50)

counter=0
while counter <5:
    user_number=eval(input("enter a number:"))
    counter += 1
    if user_number< random_number:
        print("your guess is too low")
    elif user_number > random_number: 
        print("your guess is too high")
    elif user_number == random_number:
        print("you win!")
        break       


if user_number  == random_number:
    print("you win!")
else:
    print("game over you lose! the correct number is")
    print(random_number)



#2.using a while loop
#3.get user number
#4.generate a 

#check if user input is equal to generated number

