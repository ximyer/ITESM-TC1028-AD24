students = []


def addStudent():
     global students

     # Add a Student
     newStudent = input("Enter the student's name: ")
     for value in students:
          #Check if the student exists in the database
          if value["name"] == newStudent:
               print("This student is already enrolled")
          elif value["name"] != newStudent:
               print("Let's enroll this student")
          else:
               print("Wrong data, an error occurred.")
               return
     
     #Add an ID
     newId = input("What's the student's ID? ")
     for value in students:
          #Check if that ID already exists in the database
          if value["id"] == newId:
               print("This ID already exists")
               return
     
     #Add Grades
     newStudent_grades = []
     numberOfGrades = int(input("Enter number of grades for the student: "))
     for i in range(0,numberOfGrades):
          studentGrades = float(input(f"Grade {i+1}: "))
          newStudent_grades.append(studentGrades)  

     # Add the student to the database
     students.append({
          "name": newStudent,
          "id": newId,
          "grades": newStudent_grades
     })
     
     print("Student enrolled successfully!")
     return

def listStudents():
     global students
     print("Student's List: '")
     for student in students:
          print(f"Name: {student['name']}, ID: {student['id']}, Grades: {student['grades']}")
     return

def findStudent():
     global students
     yesId = input("Please input the student's ID: ")
     for student in students:
               if student["id"] == yesId:
                    print(f"Name: {student['name']}, ID: {student['id']}, Grades: {student['grades']}")
               elif student["id"] != yesId:
                    print("This ID is not included in the database")
               else:
                    print("Not valid data, an error occurred.")
     return


def avgGradeCalc():
     global students
     #Join all the grades in a single list
     allGrades = []
     for student in students:
          allGrades.extend(student["grades"])
     #Get the average grade of all the students
     if allGrades:
          average = sum(allGrades) / len(allGrades)
          print(f"The average grade of all students is: {average:.2f}")
     else:
          print("No grades available to calculate the average.")
     return




while(True):
     #Display the menu on the screen
     print("Menu")
     print("1.- Add a student")
     print("2.- List all students")
     print("3.- Find a Student by ID")
     print("4.- Calculate all the students average grade.")
     print("5.- Exit Menu")
     print("---------------")

     #Let the user decide what's needed.
     choice = int(input("Please input your choice: "))

     if choice == 1:
          addStudent()
     elif choice == 2:
          listStudents()
     elif choice == 3:
          findStudent()
     elif choice == 4:
          avgGradeCalc()
     elif choice == 5:
          print("You reached the end.")
          break
     else:
          print("An error occurred.")