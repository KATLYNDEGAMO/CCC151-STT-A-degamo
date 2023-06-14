# Degamo, Katlyn H. Bs Statistics II
# Simple Student Information System (SSIS) v2 using database

import tkinter as tk
import sqlite3

root = tk.Tk()
root.title("Student Information System")
root.config(bg="white")
root.geometry("800x500")

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    ID TEXT PRIMARY KEY,
                    Name TEXT,
                    Gender TEXT,
                    Year_Level TEXT,
                    Course_Code TEXT
                 )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
                    Code TEXT PRIMARY KEY,
                    Name TEXT
                 )''')


def add_student():
    student_id = id_entry.get()
    name = name_entry.get()
    gender = gender_entry.get()
    year_level = year_entry.get()
    course_code = course_entry.get()

    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)",
                   (student_id, name, gender, year_level, course_code))
    conn.commit()

    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)


def delete_student():
    student_id = id_entry.get()
    cursor.execute("DELETE FROM students WHERE ID=?", (student_id,))
    conn.commit()
    id_entry.delete(0, tk.END)


def edit_student():
    student_id = id_entry.get()
    name = name_entry.get()
    gender = gender_entry.get()
    year_level = year_entry.get()
    course_code = course_entry.get()

    cursor.execute("UPDATE students SET Name=?, Gender=?, Year_Level=?, Course_Code=? WHERE ID=?",
                   (name, gender, year_level, course_code, student_id))
    conn.commit()

    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)


def list_students():
    cursor.execute("SELECT * FROM students")
    student_data = cursor.fetchall()

    dataoutput.delete('1.0', tk.END)
    dataoutput.tag_configure('bold', font=('Arial', 10, 'bold'))
    dataoutput.tag_configure('center', justify='center')

    for student in student_data:
        student_id = student[0]
        name = student[1]
        gender = student[2]
        year_level = student[3]
        course_code = student[4]

        dataoutput.insert(tk.END, f"ID: {student_id}, Name: {name}, Gender: {gender}, Year Level: {year_level}, Course Code: {course_code}\n")


def search_students():
    query = search_entry.get()
    cursor.execute("SELECT * FROM students WHERE ID LIKE ? OR Name LIKE ?", ('%' + query + '%', '%' + query + '%'))
    student_data = cursor.fetchall()

    dataoutput.delete('1.0', tk.END)
    dataoutput.tag_configure('bold', font=('Arial', 10, 'bold'))
    dataoutput.tag_configure('center', justify='center')

    for student in student_data:
        student_id = student[0]
        name = student[1]
        gender = student[2]
        year_level = student[3]
        course_code = student[4]

        dataoutput.insert(tk.END, f"ID: {student_id}, Name: {name}, Gender: {gender}, Year Level: {year_level}, Course Code: {course_code}\n")

    search_entry.delete(0, tk.END)


def add_course():
    course_code = code_entry.get()
    course_name = name_entry.get()

    cursor.execute("INSERT INTO courses VALUES (?, ?)", (course_code, course_name))
    conn.commit()
    code_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    list_courses()  # Refresh the displayed course list


def delete_course():
    course_code = code_entry.get()
    cursor.execute("DELETE FROM courses WHERE Code=?", (course_code,))
    conn.commit()
    code_entry.delete(0, tk.END)
    list_courses()  # Refresh the displayed course list


def edit_course():
    course_code = code_entry.get()
    course_name = name_entry.get()

    cursor.execute("UPDATE courses SET Name=? WHERE Code=?", (course_name, course_code))
    conn.commit()
    code_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    list_courses()  # Refresh the displayed course list


def list_courses():
    cursor.execute("SELECT * FROM courses")
    course_data = cursor.fetchall()

    dataoutput.delete('1.0', tk.END)
    dataoutput.tag_configure('bold', font=('Arial', 10, 'bold'))
    dataoutput.tag_configure('center', justify='center')

    for course in course_data:
        course_code = course[0]
        course_name = course[1]

        dataoutput.insert(tk.END, f"Code: {course_code}, Name: {course_name}\n")


def clear_data():
    dataoutput.delete('1.0', tk.END)
    
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

name_label = tk.Label(root, text="Name", font=("Arial", 12, "bold"), bg=bg_color, fg=fg_color)
name_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

name_entry = tk.Entry(root, bd=2, font=("Arial", 12), bg=entry_bg_color)
name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

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


# Search Frame
search_label = tk.Label(root, text="Search", font=("Arial", 12, "bold"), bg=bg_color, fg=fg_color)
search_label.grid(row=1, column=2, padx=10, pady=5, sticky="e")

search_entry = tk.Entry(root, bd=2, font=("Arial", 12), bg=entry_bg_color)
search_entry.grid(row=1, column=3, padx=10, pady=5, sticky="w")

search_button = tk.Button(root, text="Search", font=("Arial", 12, "bold"), bg=button_bg_color, fg=button_fg_color, bd=2, command=search_students)
search_button.grid(row=1, column=5, columnspan=2, padx=10, pady=5, sticky="w")


# Output Frame
output_frame = tk.Frame(root, bg="yellowgreen")
output_frame.place(relx=0.5, rely=0.2, relwidth=0.4, relheight=0.7)

output_label = tk.Label(output_frame, text="Student Data", font=("Arial", 14), bg="white")
output_label.pack(side=tk.TOP, pady=10)

scrollbar = tk.Scrollbar(output_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

dataoutput = tk.Text(output_frame, font=("Arial", 12), bg="white", yscrollcommand=scrollbar.set)
dataoutput.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.7)

scrollbar.config(command=dataoutput.yview)

list_students_btn = tk.Button(output_frame, text="List Students", font=("Arial", 12), command=list_students)
list_students_btn.place(relx=0.1, rely=0.85)

list_courses_btn = tk.Button(output_frame, text="List Courses", font=("Arial", 12), command=list_courses)
list_courses_btn.place(relx=0.5, rely=0.85)

clear_data_btn = tk.Button(root, text="Clear Data", font=("Arial 10 bold"), bg="white", fg="black", command=clear_data)
clear_data_btn.place(x=1030, y=740)

root.mainloop()
