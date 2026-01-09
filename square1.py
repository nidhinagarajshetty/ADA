n=float(input("enter a number:"))
guess=n/2
while(guess !=(guess+n/guess)/2):
    guess=(guess+n/guess)/2
    print("Guess:",guess)