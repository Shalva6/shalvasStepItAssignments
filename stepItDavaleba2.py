# 1
grade = int(input("Enter the grade of the student: "))
if grade > 100:
    print("You can't get over 100")
elif grade > 90:
    print("The student passed, and is graded A")
elif grade > 80:
    print("The student passed, and is graded B")
elif grade > 70:
    print("The student passed, and is graded C")
elif grade > 60:
    print("The student passed, and is graded D")
elif grade > 50:
    print("The student passed, and is graded E")
else:
    print("The student failed.")

# 2
n = int(input("Enter your number: "))
if n == 0:
    print(f"{n} is neither even or odd")
elif n%2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")

# 3
text = input("Please enter your text: ")
targetWords = ["small", "tall", "middle"]
text = text.split()
wordFound = False
for s in text:
    if s in targetWords:
        print(f"'{s}' was found in the text first")
        wordFound = True
        break
if wordFound == False:
    print("No words were found in the text")