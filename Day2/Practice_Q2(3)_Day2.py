student_name = ("Ankith", "Athul", "Akshath", "Adith", "Ayana")
print("Student Names:", student_name)

# Position of student names using index()
print("Position of student names:")
name = input("Enter name of the student :: ")
if name in student_name:
    position = student_name.index(name)
    print(f"Position of {name} is: {position}")
else:
    print(f"{name} is not found in the tuple.")

# Appearance of a name using count()
print("\nCount of a name in the tuple:")
count_name = input("Enter name to count its appearance :: ")
if count_name in student_name:
    appearance = student_name.count(count_name)
    print(f"{count_name} appears {appearance} times in the tuple.")
else:
    print(f"{count_name} is not found in the tuple.")
