# 1
classroom = {
    "Student1": {
        "Name": "ანა",
        "Age": 20,
        "Grade": 9
    },

    "Student2": {
        "Name": "ნიკო",
        "Age": 22,
        "Grade": 8
    },

    "Student3": {
        "Name": "მარიამ",
        "Age": 21,
        "Grade": 10
    }
}

# ა
for i in range(1, 4):
    currentStudent = classroom["Student" + str(i)]
    print(f"Student {currentStudent["Name"]} has a grade of {currentStudent["Grade"]}")
# ბ
biggestGrade = 0
for i in range(1, 4):
    currentStudent = classroom["Student" + str(i)]
    if biggestGrade < currentStudent["Grade"]:
        biggestGrade = currentStudent["Grade"]
print(f"The biggest grade is {biggestGrade}")
# გ
classroom["Student4"] = {"Name": "შალვა", "Age": 19,"Grade": 7}
print(classroom)

# 2
text = "python is great and python is easy"
splitText = text.split()
words = []

for _ in splitText:
    if _ in words:
        continue
    else:
        words.append(_)

i = 0
while i < len(words):
    counter = 0
    for word in splitText:
        if word == words[i]:
            counter += 1
    print(f"The word '{words[i]}' exists in the text {counter} times")
    i += 1