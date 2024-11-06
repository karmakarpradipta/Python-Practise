gender = input("Enter gender (male/female): ").lower()
salary = float(input("Enter salary: "))

if gender == "male":
    bonus = 0.05 * salary  
elif gender == "female":
    bonus = 0.10 * salary  
else:
    print("Invalid gender input.")
    bonus = 0

gross_salary = salary + bonus


if gross_salary > 10000:
    tax = 0.02 * gross_salary 
    net_salary = gross_salary - tax
else:
    net_salary = gross_salary

print("Net Salary after bonus and tax:", net_salary)
