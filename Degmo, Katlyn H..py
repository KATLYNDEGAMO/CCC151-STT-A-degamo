import tkinter as tk

root = tk.Tk()
root.title("Student Information System")
root.config(bg="green")
root.geometry("600x350")

students = []

def add_student():
    Name = name_entry.get()
    IdNumber = id_entry.get()
    Course = course_entry.get()
    student = {'Name': Name , 'IdNumber': IdNumber , 'Course': Course}
    students.append(student)
    name_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    
def delete_student():
    IdNumber = id_entry.get()
    for student in students:
        if student['IdNumber'] == IdNumber:
            students.remove(student)
    id_entry.delete(0, tk.END)
    
def edit_student():
    IdNumber = id_entry.get()
    for student in students:
        if student['IdNumber'] == IdNumber:
            student['Name'] = name_entry.get()
            student['Course'] = course_entry.get()
            id_entry.delete(0, tk.END)
            name_entry.delete(0, tk.END)
            course_entry.delete(0, tk.END)

def list_students():
    dataoutput.delete('1.0', tk.END)
    dataoutput.tag_configure('bold', font=('Arial', 10, 'bold'))
    dataoutput.tag_configure('center', justify='center')
    for student in students:
        Name = student["Name"]
        IdNumber = student["IdNumber"]
        Course = student["Course"]
        dataoutput.insert(tk.END, f"Name: {Name}, ID: {IdNumber}, Course: {Course}\n")

def search_students():
    query = search_entry.get()
    dataoutput.delete('1.0', tk.END)
    dataoutput.tag_configure('bold', font=('Arial', 10, 'bold'))
    dataoutput.tag_configure('center', justify='center')
    for student in students:
        Name = student["Name"]
        IdNumber = student["IdNumber"]
        Course = student["Course"]
        if query.lower() in student['Name'].lower() or query.lower() in student['IdNumber'].lower():
            dataoutput.insert(tk.END, f"Name: {Name}, ID: {IdNumber}, Course: {Course}\n")
        search_entry.delete(0,tk.END)
            
studentname = tk.Label(root, text="Name", font=("Arial 10 bold"), bg="green", fg="#fff")
studentname.grid(row=1, column=0, padx=2, pady=2)
studentname.place(x=15, y=15)

name_entry = tk.Entry(root, bd= 2, font=("Arial 9"))
name_entry.grid(row=1, column=0, padx= 2, pady=2)
name_entry.place(x=70, y=15, width= 255)

studentID = tk.Label(root, text="ID", font=("Arial 10 bold"), bg="green", fg="#fff")
studentID.grid(row=1, column=2, padx=2, pady=2)
studentID.place(x=340, y=15)

id_entry = tk.Entry(root, bd= 2, font=("Arial 9"))
id_entry.grid(row=1, column=2, padx= 2, pady=2)
id_entry.place(x=365, y=15, width= 215)

studentCourse = tk.Label(root, text="Course", font=("Arial 10 bold"), bg="green", fg="#fff")
studentCourse.grid(row=2,column=1, padx=2, pady=2)
studentCourse.place(x=15, y=55)

course_entry = tk.Entry(root, bd= 2, font=("Arial 9"))
course_entry.grid(row=2, column=1, padx= 2, pady=2)
course_entry.place(x=70, y=55, width= 250)

studentearch = tk.Label(root, text="Search", font=("Arial 10 bold"), bg="green", fg="#fff")
studentearch.grid(row=3,column=1, padx=2, pady=2)
studentearch.place(x=15, y=110)

search_entry = tk.Entry(root, bd= 2, font=("Arial 9"))
search_entry.grid(row=3,column=1, padx=2, pady=2)
search_entry.place(x=70, y=110, width= 330)

add_button = tk.Button(root, bg="white", text="Add", bd=5, font=("Arial 10"), width=7, command=add_student)
add_button.place(x = 330, y= 50)
delete_button = tk.Button(root, bg="white", text="Delete", bd=5, font=("Arial 10"), width=7, command=delete_student)
delete_button.place(x = 420, y= 50)
edit_button = tk.Button(root, bg="white", text="Edit", bd=5, font=("Arial 10"), width=7, command=edit_student)
edit_button.place(x = 510, y= 50)
search_button = tk.Button(root, bg="white", text="Search", bd=5, font=("Arial 10"), width=8, command=search_students)
search_button.place(x = 410, y= 105)
list_button = tk.Button(root, bg="white", text="List", bd=5, font=("Arial 10"), width=8, command=list_students)
list_button.grid(row=4, column=4,padx=2,pady=2)
list_button.place(x = 502, y= 105)

output = tk.Text(root, width=50, height=10, state="disabled", bg="white", font=("Arial 10"))

dataoutput = tk.Text(root, width=10, height=10, bd = 3)
dataoutput.place(x=15, y=160, height = 175, width= 565)

    

root.mainloop()