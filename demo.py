salary = float(input ("Enter your salary: "))
bonus = salary*0.12 if salary<10000 else 0
bonus += salary * 0.05 if input("male/female: ").lower() == "male" else salary*0.10

print(f" Salary: {salary+bonus}\n Bonus: {bonus}")
