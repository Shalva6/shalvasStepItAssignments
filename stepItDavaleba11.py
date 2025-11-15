randomList = ['Red', 'Green', 'white', 'Black', 'Pink', 'yellow']

# 1
with open("stepItDavaleba12.txt", "w") as f:
    for color in randomList:
        f.write(f"{color}\n")

# 2
counter = 0
with open("stepItDavaleba12.txt", "r") as f:
    for color in f:
        color = color.strip()
        if any(char.isupper() for char in color):
            counter += 1
print(f"There are {counter} words that have an uppercase character in them.")