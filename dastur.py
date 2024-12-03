import json

num1 = int(input("Nechta odamni malumotini kiritmoqchisiz: "))
lst = []

for i in range(num1):
    name = input("Ismingizni kiriting: ")
    surname = input("Familyangizni kiriting: ")
    age = int(input("Yoshingizni kiriting: "))
    year = 2024 - age

    data = {"name": name, "surname": surname,"age": age, "year": year}
    lst.append(data)

    with open("data1.json", "w") as file:
        json.dump(lst, file, indent=4)

