age = int(input("What is your age: "))
gender = input("What is your gender: ")


if gender == "f" and age < 25:
    print("You are going to law school.")

if gender == "f" and age < 18:
    print("You're still in school.")

elif gender == "f" and age > 25:
    print("Work is hard.")

if gender == "f" and age > 25:
    print("You are a lawyer.")

if gender == "m" and age < 25:
    print("You are going to STEM.")

if gender == "m" and age < 18:
    print("You're still in school.")

elif gender == "m" and age > 25:
    print("Work is hard.")

if gender == "m" and age > 25:
    print("Programming is fun.")