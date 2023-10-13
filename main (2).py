class student:
 def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_student(student_list):


  sorted_student=sorted(student_list,key=lambda student:student.cgpa,reverse=True)
  return sorted_student


student=[
        student("Tom", "A123", 7.8),
        student("Jerry", "A124", 8.9),
        student("Joe", "A123", 9.1),
        student("Tem", "A123", 9.9),
        ]

sorted_student= sort_student(student)

for student in sorted_student:
   print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
student.roll_number,student.cgpa))
