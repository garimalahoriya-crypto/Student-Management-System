# Students Management System
students = {}

def add_student():
 enrollment = input("Enter Enrollment Number:")
 if enrollment in students: print("Student already exist!")
 return

name= input("Enter Name:")
branch = input("Enter Branch:")
semester= ("Enter Semester:")
marks= float(input("Enter Marks:"))

students['enrollment'] = {
   "name":name,
   "branch":branch,
   "semester":semester,
   "marks": marks}

print("Student added succesfully!")

def dispaly_students():
  if not students:
   print("No students records found.")
   return

  print("\n--Students Records---")
  for enrollment, details in students.items():
     print("Enrollment Number:",enrollment)
     print("Name:",details["name"])
     print("Branch:",details["branch"])
     print("Semester:",details["semester"])
     print("Marks:",details["marks"])
     print("------------")

def search_student():
   enrollment=input("Enter Enrollment Number to search:")

   if enrollment in students:
      details=students[enrollment]
      print("\nStudent Found!")
      print("Enrollment Number:",enrollment)
      print("Name:",details["name"])
      print("Branch:",details["branch"])
      print("Semester:",details["semester"])
      print("Marks:",details["marks"])
   else:
      print("Student not found.")

def update_student():
  enrollment= input("Enter Enrollment Number to update:")

  if enrollment not in students:print("Student not found.")
  return

print("Enter new details:")
students['enrollment']["name"]= input("Enter Name")
students['enrollment']["branch"]=input("Enter Branch:")
students['enrollment']["semester"]=input("Enter Semester:")
students['enrollment']["marks"]=float(input("Enter Marks:"))

print("Student details updated successfully!") 

def delete_student():
  enrollment = input("Enter Enrollment Number to delete:")

  if enrollment in students:del students[enrollment]
  print("Student deleted successfully!")

  print("Student not found.")


#Main Menu
while True:
  print("\n=====Student Management System====")
  print("1.Add Students")
  print("2.Display Students")
  print("3.Search Student")
  print("4.Update Student")
  print("5.Delete Student")
  print("6.Exit")

  choice=input("Enter your choice:")

  if choice=="1":
    add_student()
  elif choice=="2":
    dispaly_students()
  elif choice=="3":
     search_student()
  elif choice=="4":
     update_student()
  elif choice=="5":
    delete_student()
  elif choice=="6":
    print("Thank you!")
    break
  else:
    print("Invalid choice.Please try again.")
     
