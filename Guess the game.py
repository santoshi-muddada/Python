import random

secret=random.randint(1,100)
guess = -1
attempts = 0
max_attempts = 5

while guess != secret and attempts < max_attempts:
    guess = int(input(f"guess your number (Attempts {attempts + 1} of {max_attempts}):"))
    attempts += 1

    if guess < secret:
        print("TO LOW ; Try Again")
    elif guess > secret:
        print("TO HIGH ; Try Again")
        
    else:
        print(f"your guess is correct",{attempts},"attempt(s)") 
else:
    print("game is over you have use all 5 attemps") 
    print("the number is :",secret)