import json

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def readJson(self):
        with open("students.json", "r", encoding = "utf-8") as s:
            info = json.load(s)
            for eachStudent in info["students"]:
                print(f"Name: {eachStudent['name']}")
                print(f"Age: {eachStudent['age']}")
                print(f"Grades: {eachStudent['grades']}")
                print("\n")

    def calculateMean(self):
        with open("students.json", "r", encoding = "utf-8") as s:
            info = json.load(s)
        
        for eachPerson in info["students"]:
            result = 0
            for eachGrade in eachPerson["grades"]:
                result += eachGrade
                result = result / len(eachPerson["grades"])
            print(f"{eachPerson["name"]}: {result}")

    def addInfo(self):
        with open("students.json", "r", encoding = "utf-8") as s:
            info = json.load(s)

        info["students"].append({
            "name": self.name,
            "age": self.age,
            "grades": self.grades
        })

        with open("students.json", "w", encoding = "utf-8") as s:
            json.dump(info, s, indent = 4, ensure_ascii = False)

person = Student("Shalva", 19, [90, 100, 80])
person.readJson()
person.addInfo()
print(person.calculateMean())