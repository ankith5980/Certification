student_mark = ()

for i in range(5):
    subject_mark = int(input(f"Enter marks for subject {i+1}: "))
    student_mark += (subject_mark,)

print(f"Student Marks: {student_mark}")

# Print the highest and lowest marks
print(f"Highest Marks: {max(student_mark)}")
print(f"Lowest Marks: {min(student_mark)}")

# Print the average marks
average_marks = sum(student_mark) / len(student_mark)
print(f"Average Marks: {average_marks}")