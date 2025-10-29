# 1
finalList = {}
def funcSquare(numbers):
    for num in numbers:
        finalList.update({f"Square root of {num} is": f"{num**2}"})
    return finalList

inputtedNums = []
n = int(input("How many numbers would you like to have in the list?: "))
counter = 0
while counter < n:
    numChoice = int(input(f"Enter your desired number. {n - counter} choices remaining: "))
    inputtedNums.append(numChoice)
    counter += 1

print(funcSquare(inputtedNums))