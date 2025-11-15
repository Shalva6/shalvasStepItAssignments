# 1
exampleLst = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
newNums = []
n = 0
while n < 3:
    num = int(input("What number would you like to add?: "))
    newNums.append(num)
    n += 1
exampleLst[2] = tuple(newNums)
print(exampleLst)

# 2
randomSet = {-20, 50, 25, 10, 40, -4}
first = next(iter(randomSet))
biggestNumber = first
smallestNumber = first
for num in randomSet:
    if num > biggestNumber:
        biggestNumber = num
    if smallestNumber > num:
        smallestNumber = num
print(f"The biggest number in the set is {biggestNumber}, The smallest number in the set is {smallestNumber}")

# 3
Inputs = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
averages = []
for x in Inputs:
    sum = 0
    for y in x:
        sum += y
    averages.append(sum/len(x))
print(f"The averages for the inputted numbers are {averages}")

# აქ ცოტა დავიბენი რას ითხოვდა დავალება
outputs = [30.5, 24.25, 27.0, 23,.25]
sum = 0
for num in outputs:
    sum += num
print(f"The average of the numbers is {sum/len(outputs)}")