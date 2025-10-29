# 1
totalSum = 0
while True:
    newNum = input("Enter your chosen number: ")
    if newNum.lower() == "sum":
        print(f"The sum of all the inputted numbers is {totalSum}.")
        break
    newNum = int(newNum)
    if newNum < 0:
        print("Please avoid using negative numbers.")
        continue
    totalSum += newNum

# 2
totalSumTwo = 0
while True:
    newNum = int(input("Enter your chosen number (entering 0 will terminate the process): "))
    if newNum == 0:
        print(f"The sum of all numbers is {totalSumTwo}")
        break
    totalSumTwo += newNum

# 3
import random
numberToGuess = random.randint(1, 10)
while True:
    guessedNumber = int(input("Enter the number you want to guess: "))
    if guessedNumber < numberToGuess:
        print("You may need to try guessing a bigger number.")
    elif guessedNumber > numberToGuess:
        print("You may need to try guessing a lesser number.")
    else:
        print("You guessed the number correctly! Terminating game...")
        break