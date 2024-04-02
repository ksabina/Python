import random
import math

#taking input for lower number in the range
lower = int(input("Enter the lower bound number:    "))

#taking input for lower number in the range
upper = int(input("Enter the upper bound number:    "))

#generate the random number
x= random.randint(lower,upper)

print("\n\t You have only ",
      round(math.log(upper-lower+1,2)),
      "chances to guess the integer!\n")

#initializing number of guesses
count = 0

while count< math.log(upper-lower+1,2):
    count +=1

    #Taking the guessing number as input
    guess = int(input( "Guess the number: "))

    if x == guess:
        print("congratulation great guess!\n You did  it in " , count, "try")
        break

    elif x > guess:
        print("Your guess is too low")

    elif x< guess:
        print("Your guess is too high")


if count >= math.log(upper-lower + 1,2):
    print("\n The number is %d "% x)
    print("\t Better luck next time!")
