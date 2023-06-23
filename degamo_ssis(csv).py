# Degamo, Katlyn H. Bs Statistics - II
# Simple Student Information System (SSIS) using csv

from typing import List
import tkinter as tk
import csv

students_file_path = 'students.csv'  # Replace with the desired file path

# Create an empty CSV file for students
with open(students_file_path, 'w', newline='', encoding='utf-8'):
    pass

courses_file_path = 'courses.csv'  # Replace with the desired file path

# Create an empty CSV file for courses
with open(courses_file_path, 'w', newline='', encoding='utf-8'):
    pass

root = tk.Tk()
root.title("Student Information System")
root.config(bg="green")
root.geometry("600x350")

students: List[dict] = []
courses: List[dict] = []

def add_student():
    student_id = id_entry.get()
    student_name = name_entry_student.get()
    gender = gender_entry.get()
    year_level = year_entry.get()
    course_code = course_entry.get()

    # Check if the course exists in the courses data
    course_exists = False
    for course in courses:
        if course['Course Code'] == course_code:
            course_exists = True
            break
    
    if not course_exists:
        # Display an error message if the course does not exist
        error_message = "Course does not exist."
        dataoutput.delete('1.0', tk.END)
        dataoutput.insert(tk.END, error_message)
        return

    student = {'ID': student_id, 'Name': student_name, 'Gender': gender, 'Year Level': year_level, 'Course Code': course_code}
    students.append(student)

    id_entry.delete(0, tk.END)
    name_entry_student.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)

    save_students_to_csv()


def delete_student():
    student_id = id_entry.get()
    students_copy = students.copy()
    for student in students_copy:
        if student['ID'] == student_id:
            students.remove(student)
            break
    id_entry.delete(0, tk.END)

    save_students_to_csv()


def edit_student():
    student_id = id_entry.get()
    for student in students:
        if student['ID'] == student_id:
            student['Name'] = name_entry_student.get()
            student['Gender'] = gender_entry.get()
            student['Year Level'] = year_entry.get()
            student['Course Code'] = course_entry.get()
            break
    id_entry.delete(0, tk.END)
    name_entry_student.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)

    save_students_to_csv()


def list_students():
    dataoutput.delete('1.0', tk.END)
    dataoutput.tag_configure('bold', font=('Arial', 10, 'bold'))
    dataoutput.tag_configure('center', justify='center')
    for student in students:
        student_id = student["ID"]
        student_name = student["Name"]
        gender = student["Gender"]
        year_level = student["Year Level"]
        course_code = student["Course Code"]
        dataoutput.insert(tk.END, f"ID: {student_id}, Name: {student_name}, Gender: {gender}, Year Level: {year_level}, "
                                 f"Course Code: {course_code}\n")


def search_students():
    query = search_entry.get()
    dataoutput.delete('1.0', tk.END)
    dataoutput.tag_configure('bold', font=('Arial', 10, 'bold'))
    dataoutput.tag_configure('center', justify='center')
    for student in students:
        student_id = student["ID"]
        student_name = student["Name"]
        gender = student["Gender"]
        year_level = student["Year Level"]
        course_code = student["Course Code"]
        if query.lower() in student_id.lower() or query.lower() in student_name.lower():
            dataoutput.insert(tk.END, f"ID: {student_id}, Name: {student_name}, Gender: {gender}, Year Level: {year_level}, "
                                 f"Course Code: {course_code}\n")


def add_course():
    course_code = code_entry.get()
    course_name = name_entry.get()

    course = {'Course Code': course_code, 'Course Name': course_name}
    courses.append(course)

    code_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    list_courses()  # Refresh the displayed course list

    save_courses_to_csv()


def delete_course():
    course_code = course_entry.get()
    courses_copy = courses.copy()
    for course in courses_copy:
        if course['Course Code'] == course_code:
            courses.remove(course)
            break
    course_entry.delete(0, tk.END)
    list_courses()  # Refresh the displayed course list
    save_courses_to_csv()


def edit_course():
    course_code = course_entry.get()
    course_name = name_entry.get()
    courses_copy = courses.copy()
    for course in courses_copy:
        if course['Course Code'] == course_code:
            course['Course Name'] = course_name
            break
    course_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    list_courses()  # Refresh the displayed course list

    save_courses_to_csv()


def list_courses():
    dataoutput.delete('1.0', tk.END)
    dataoutput.tag_configure('bold', font=('Arial', 10, 'bold'))
    dataoutput.tag_configure('center', justify='center')
    for course in courses:
        course_code = course["Course Code"]
        course_name = course["Course Name"]
        dataoutput.insert(tk.END, f"Course Code: {course_code}, Course Name: {course_name}\n")


def save_students_to_csv():
    with open(students_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Name', 'Gender', 'Year Level', 'Course Code'])
        for student in students:
            writer.writerow([student['ID'], student['Name'], student['Gender'], student['Year Level'],
                             student['Course Code']])


def save_courses_to_csv():
    with open(courses_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Course Code', 'Course Name'])
        for course in courses:
            writer.writerow([course['Course Code'], course['Course Name']])


def load_students_from_csv():
    with open(students_file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        students.clear()  # Clear the existing student data
        for row in reader:
            student = {
                'ID': row['ID'],
                'Name': row['Name'],
                'Gender': row['Gender'],
                'Year Level': row['Year Level'],
                'Course Code': row['Course Code']
            }
            students.append(student)

def load_courses_from_csv():
    with open(courses_file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        courses.clear()  # Clear the existing course data
        for row in reader:
            course = {
                'Course Code': row['Course Code'],
                'Course Name': row['Course Name']
            }
            courses.append(course)

def clear_data():
    dataoutput.delete('1.0', tk.END)
    
load_students_from_csv()
load_courses_from_csv()

# Styling
bg_color = "#003f00"
fg_color = "#ffffff"
entry_bg_color = "#ffffff"
button_bg_color = "#ffffff"
button_fg_color = "#000000"

root.config(bg=bg_color)

# Student Section
student_label = tk.Label(root, text="Student", font=("Arial", 16, "bold"), bg=bg_color, fg=fg_color)
student_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

id_label = tk.Label(root, text="ID", font=("Arial", 12, "bold"), bg=bg_color, fg=fg_color)
id_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

id_entry = tk.Entry(root, bd=2, font=("Arial", 12), bg=entry_bg_color)
id_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

student_name_label = tk.Label(root, text="Name", font=("Arial", 12, "bold"), bg=bg_color, fg=fg_color)
student_name_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

name_entry_student = tk.Entry(root, bd=2, font=("Arial", 12), bg=entry_bg_color)
name_entry_student.grid(row=2, column=1, padx=10, pady=5, sticky="w")

gender_label = tk.Label(root, text="Gender", font=("Arial", 12, "bold"), bg=bg_color, fg=fg_color)
gender_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

gender_entry = tk.Entry(root, bd=2, font=("Arial", 12), bg=entry_bg_color)
gender_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

year_label = tk.Label(root, text="Year Level", font=("Arial", 12, "bold"), bg=bg_color, fg=fg_color)
year_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")

year_entry = tk.Entry(root, bd=2, font=("Arial", 12), bg=entry_bg_color)
year_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

course_label = tk.Label(root, text="Course Code", font=("Arial", 12, "bold"), bg=bg_color, fg=fg_color)
course_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")

course_entry = tk.Entry(root, bd=2, font=("Arial", 12), bg=entry_bg_color)
course_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

add_button = tk.Button(root, text="Add", font=("Arial", 12, "bold"), bg=button_bg_color, fg=button_fg_color, bd=2, command=add_student)
add_button.grid(row=6, column=0, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete", font=("Arial", 12, "bold"), bg=button_bg_color, fg=button_fg_color, bd=2, command=delete_student)
delete_button.grid(row=6, column=1, padx=10, pady=10)

edit_button = tk.Button(root, text="Edit", font=("Arial", 12, "bold"), bg=button_bg_color, fg=button_fg_color, bd=2, command=edit_student)
edit_button.grid(row=6, column=2, padx=10, pady=10)

# Course Section
course_label = tk.Label(root, text="Course", font=("Arial", 16, "bold"), bg=bg_color, fg=fg_color)
course_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

course_code_label = tk.Label(root, text="Code", font=("Arial", 12, "bold"), bg=bg_color, fg=fg_color)
course_code_label.grid(row=8, column=0, padx=10, pady=5, sticky="e")

code_entry = tk.Entry(root, bd=2, font=("Arial", 12), bg=entry_bg_color)
code_entry.grid(row=8, column=1, padx=10, pady=5, sticky="w")

course_name_label = tk.Label(root, text="Name", font=("Arial", 12, "bold"), bg=bg_color, fg=fg_color)
course_name_label.grid(row=9, column=0, padx=10, pady=5, sticky="e")

name_entry = tk.Entry(root, bd=2, font=("Arial", 12), bg=entry_bg_color)
name_entry.grid(row=9, column=1, padx=10, pady=5, sticky="w")

add_course_button = tk.Button(root, text="Add", font=("Arial", 12, "bold"), bg=button_bg_color, fg=button_fg_color, bd=2, command=add_course)
add_course_button.grid(row=11, column=0, padx=10, pady=10)

delete_course_button = tk.Button(root, text="Delete", font=("Arial", 12, "bold"), bg=button_bg_color, fg=button_fg_color, bd=2, command=delete_course)
delete_course_button.grid(row=11, column=1, padx=10, pady=10)

edit_course_button = tk.Button(root, text="Edit", font=("Arial", 12, "bold"), bg=button_bg_color, fg=button_fg_color, bd=2, command=edit_course)
edit_course_button.grid(row=11, column=2, padx=10, pady=10)

list_courses_button = tk.Button(root, text="List Courses", font=("Arial", 12, "bold"), bg="white", bd=5, command=list_courses)
list_courses_button.grid(row=3, column=3, padx=10, pady=10)

# Data Section
data_label = tk.Label(root, text="Data", font=("Arial", 16, "bold"), bg=bg_color, fg=fg_color)
data_label.grid(row=0, column=2, padx=10, pady=10)

search_label = tk.Label(root, text="Search", font=("Arial", 12, "bold"), bg=bg_color, fg=fg_color)
search_label.grid(row=1, column=2, padx=10, pady=5, sticky="e")

search_entry = tk.Entry(root, bd=2, font=("Arial", 12), bg=entry_bg_color)
search_entry.grid(row=1, column=3, padx=10, pady=5, sticky="w")

search_button = tk.Button(root, text="Search", font=("Arial", 12, "bold"), bg=button_bg_color, fg=button_fg_color, bd=2, command=search_students)
search_button.grid(row=2, column=2, columnspan=2, padx=10, pady=5, sticky="w")

list_button = tk.Button(root, text="List Students", font=("Arial", 12, "bold"), bg=button_bg_color, fg=button_fg_color, bd=2, command=list_students)
list_button.grid(row=3, column=2, columnspan=2, padx=10, pady=5, sticky="w")

dataoutput = tk.Text(root, height=10, width=50, font=("Arial", 12), bg=entry_bg_color)
dataoutput.grid(row=4, column=2, columnspan=20, padx=20, pady=10)

clear_data_btn = tk.Button(root, text="Clear Data", font=("Arial", 10, "bold"), bg=button_bg_color, fg=button_fg_color, bd=2, command=clear_data)
clear_data_btn.place(x=530, y=400)

root.mainloop()