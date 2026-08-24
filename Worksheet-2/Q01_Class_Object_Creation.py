class Student:
    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)

student1 = Student()
student1.name = "Gowtham"
student1.roll_number = 10
student1.marks = 100

student2 = Student()
student2.name = "Raju"
student2.roll_number = 15
student2.marks = 100

student1.display_details()
print()
student2.display_details()
