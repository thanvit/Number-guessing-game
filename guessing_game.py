
print("Welcome to the number guessing game\nI'm thinking of a number between 1 and 100\nYou have 3,5 and 10 chances to guess the correct number based on the difficulty level.")
secret=63
guess_count=0
print("Please select a difficulty level")
print("1.Easy(10 chances)\n2.Medium(5 chances)\n3.Hard(3 chances)")
choice=int(input("Enter your choice:"))
if choice==1:
    print("Great! You have selected the Easy difficulty level.\nLet's start the game!")
    count1=10
    while guess_count<count1:                                      
        guess1=int(input("Enter your guess:"))
        guess_count+=1
        if guess1==secret:
            print(f"Congragulations! You guessed the correct number in {guess_count}.")
            break
        else:
            if guess1<63:
                print(f"Incorrect! The number is greater than {guess1}.")
            else:
                print(f"Incorrect! The number is less than {guess1}.")
       
elif choice==2:
    print("Great! You have selected the Medium difficulty level.\nLet's start the game!")
    count2=5
    while guess_count<count2:
        guess2=int(input("Enter your guess:"))
        guess_count+=1
        if guess2==secret:
            print("Congragulations! You've guessed the number correctly")
            break
        else:
            if guess2<63:
                print(f"Incorrect! The number is greater than {guess2}.")
            else:
                print(f"Incorrect! The number is less than {guess2}.")
elif choice==3:
    print("Great! You have selected the Hard difficulty level.\nLet's start the game!")
    count3=3
    while guess_count<count3:
        guess3=int(input("Enter your guess:"))
        guess_count+=1
        if guess3==secret:
            print("Congragulations! You've guessed the number correctly")
            break
        else:
           if guess3<63:
                print(f"Incorrect! The number is greater than {guess3}.")
           else:
                print(f"Incorrect! The number is less than {guess3}.")
else:
    print("The number you've entered is invalid.\nPlease enter a valid number.")
