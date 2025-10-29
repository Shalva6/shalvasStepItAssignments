# 1
enteredWord = input("Please enter your word: ")
if enteredWord[::-1].lower() == enteredWord.lower():
    print("Your chosen word is a palindrome.")
else:
    print("Your chosen word is not a palindrome.")

# 2
inputtedTxt = input("Please enter your text: ")
asciiNumbers = []
for i in inputtedTxt:
    asciiNumbers.append(ord(i))
print(asciiNumbers)

# 3
while True:
    inputtedWord = input("Please enter your word: ")
    if inputtedWord == "stop":
        break
    if inputtedWord[-3:] == "ing":
        print(f"The word would be {inputtedWord}ly")
    else:
        print(f"The word would be {inputtedWord}ing")