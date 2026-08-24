# Create and write student names to the file
file = open("students.txt", "w")

file.write("Gowtham\n")
file.write("Raju\n")
file.write("Anil\n")
file.write("Sita\n")
file.write("Ravi\n")

file.close()

# display student names
file = open("students.txt", "r")
students = file.readlines()
print("Student Names:")

for student in students:
    print(student.strip())

file.close()


# Count total number of students
print("Total Number of Students:", len(students))