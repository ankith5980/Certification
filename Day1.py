# This is a list
students = ["Athul", "Ankith", "Chakku", "Ayana", "Akshath", "Adith"]
print("Students in class :: ", students)

# This is a tuple
students_tuple = ("Athul", "Ankith", "Chakku", "Ayana", "Akshath", "Adith")
print("Students in class :: ", students_tuple)

# This is a dictionary
student_records = {
    "Athul" : {
        "roll no" : 5,
        "gender" : "Male",
        "age" : 23
    },
    "Ankith" :{
        "roll no" : 1,
        "gender" : "Male",
        "age" : 21 
    },
    "Ayana" : {
        "roll no" : 8,
        "gender" : "Female",
        "age" : 22
    },
    "Akshath" : {
        "roll no" : 3,
        "gender" : "Male",
        "age" : 24
    },
    "Adith" : {
        "roll no" : 6,
        "gender" : "Male",
        "age" : 23
    }
}

# Accessing elements from a list using a for loop
for student in students:
    print("Student Name :: ", student)

    # Accessing elements from a tuple using a for loop
for student in students_tuple:
    print("Student Name :: ", student)

    # Accessing elements from a dictionary using a for loop
for student, details in student_records.items():
    print("Student Name :: ", student)
    print("Roll No :: ", details["roll no"])
    print("Gender :: ", details["gender"])
    print("Age :: ", details["age"])