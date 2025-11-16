#Creating a student information program to calculate their average marks in a dictionary and printing it by looping thorugh it

name = input("Enter student name: ")

m1 = int(input("Enter marks for Subject 1: "))
m2 = int(input("Enter marks for Subject 2: "))
m3 = int(input("Enter marks for Subject 3: "))

#storing marks in the list
marks_list = [m1, m2, m3]

average = sum(marks_list) / len(marks_list) #calculating the average marks


if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "D"

#storing details in the dictionary
student_info = {
    "Name": name,
    "Marks": marks_list,
    "Average": average,
    "Grade": grade
}

#displaying result using the For Loop
print("\n--- Student Details ---")
for key, value in student_info.items():
    print(f"{key}: {value}")
