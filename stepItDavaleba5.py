# 1
import random
guessListItems = [1, 20, 30, 60, 26]
print("The numbers you can guess from is: ", end="")
for i in guessListItems:
    print(f"{i}", end=" ")
itemToGuess = guessListItems[random.randint(0, 4)]
guessedItem = int(input("\nPlease enter the number you would like to guess: "))
if guessedItem == itemToGuess:
    print("Congrats! You guessed right. Ending game.")
else:
    print("You guessed wrong. Ending game.")

# 2
myList = [43, '22', 12, 66, 210, ["hi"]]
position = 0
# # a
while position < len(myList):
    if myList[position] == 210:
        print(f"210 exists at position {position}")
    position += 1
# # b
myList[5][0] = (f"{myList[5][0]} hello")
# # c
myList.pop(2)
print(myList)
# # d
myList2 = myList[:]

# 3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transportedMatrix = [matrixLine[:] for matrixLine in matrix]
for x in range(3):
    for y in range(3):
        transportedMatrix[x][y] = matrix[y][x]
print(transportedMatrix)