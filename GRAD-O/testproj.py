from ntpath import join
import tkinter
from tkinter import *
from tkinter import ttk
from turtle import left
import customtkinter as ctk
import gradecalcu

visible = False

def toggle1():
    global visible
    visible = not visible
    if visible:
        head_label1.pack(side="left",
                         padx=10)
    else:
        head_label1.pack_forget()

#----WINDOW-----
window = Tk()
window.geometry("1980x1080")
window.minsize(1500, 1000)
window.maxsize(5000, 5000)
window.title("GRAD-O")

#----ICON----
icon = PhotoImage(file='C:\\VS Code\\Python\\GRAD-O\\icon.png')
window.iconphoto(True,icon)

#----INTERFACE----
window.configure(bg="#f5f5dc")
ribbon_photo = PhotoImage(file='C:\\VS Code\\Python\\GRAD-O\\logo.png')

#----BACKGROUND LOGO----
ribbon_photo2 = ribbon_photo
background_logo = Label(window,
                        image=ribbon_photo2,
                        width=1000,
                        height=160,
                        bg= "#f5f5dc",
                        padx=-0,
                        pady=-0
                        )
background_logo.place(relx=0.5, rely=0.5, anchor="center")

#RIBBON EDWIN
ribbon_photo1 = ribbon_photo.subsample(3, 3)
text_label = Label(window,
                     text= 'Fair Calculation, Goal-Oriented Do it With GRAD-O',
                     font= ('Titillium Web', 15, 'bold'),
                     padx= 20,
                     fg= '#000000', 
                     bg= '#fff2bb',
                     relief= (SOLID),
                     bd= 1,
                     anchor= 'w',
                     height= 100,
                     image=ribbon_photo1,
                     compound='left',
                     )

text_label.pack(side=TOP, fill=X)

# ---- SIDEBAR (SELWYN) ----

sidebar = Frame(window,
                height=300,
                width=50,
                bg="#b9c5cc",
                relief=SOLID,
                bd=1
)
sidebar.pack(side="left",
             fill="y"
)

head_label1 = Label(window, 
              text="THIS IS FROM THE WINDOW",
              bg="light blue"
              )
button1 = Button(sidebar, 
                 text="GRADE\nCALCULATOR",
                 font=("Titillium Web",15, "bold"),
                 bg="#f5f5dc",
                 fg="black",
                 relief="ridge",
                 bd=5,
                 )
button1.pack(side= TOP,
             fill= 'x',
             padx= 5,
             pady= 10,
             )

button2 = Button(sidebar,
                 text="GRADE\nPROGRESS",
                 font=("Titillium Web", 15, "bold"),
                 bg="#f5f5dc",
                 fg="black",
                 relief="ridge",
                 bd=5              
)

button2.pack(side="top",
             fill="x",
             padx=5,
             pady=10
)

button3 = Button(sidebar,
                 text="GRADE\nAVERAGE",
                 font=("Titillium Web", 15, "bold"),
                 bg="#f5f5dc",
                 fg="black",
                 relief="ridge",
                 bd=5
)
button3.pack(side="top",
             fill="x",
             padx=5,
             pady=10
)

button4 = Button(sidebar,
                 text="GRADE\nHISTORY",
                 font=("Titillium Web", 15, "bold"),
                 bg="#f5f5dc",
                 fg="black",
                 relief="ridge",
                 bd=5 
)
button4.pack(
side="top",
fill="x",
padx=5,
pady=10
)

button5 = Button(sidebar,
                 text="ABOUT\nUS",
                 font=("Titillium Web", 15, "bold"),
                 bg="#f5f5dc",
                 fg="black",
                 relief="ridge",
                 bd=5
)
button5.pack(side="top",
             fill="x",
             padx=5,
             pady=10
)

bottom_frame = Frame(sidebar,
                     bg="#b9c5cc"
)

bottom_frame.pack(side=BOTTOM,
                  fill=X,
                  padx=5,
                  pady=10
)

button6 = Button(
    bottom_frame,
    text="⚙️",
    font=("Arial", 10),
    bg="#f5f5dc",
    fg="black",
    relief="ridge",
    bd=5
)

button6.pack(
side=LEFT
)

button_frame = Frame(sidebar,
                     bg="#b9c5cc"
)

button_frame.pack(
side=BOTTOM,
anchor="e",
padx=5,
pady=10
)

button7 = Button(
bottom_frame,
text="🌙",
font=("Arial", 10),
bg="#b9c5cc",
fg="black",
relief="flat",
bd=5
)

button7.pack(
side=RIGHT,
padx=3
)

button8 = Button(
bottom_frame,
text="🔆",
font=("Arial", 10),
bg="#b9c5cc",
fg="black",
relief="flat",
bd=5
)

button8.pack(
side=RIGHT,
padx=3
)

#----GRADE COMPONENTS----
bullet_contents = "".join(( "GRADE COMPONENTS\n",
                            "• Written Works — 30%\n",
                            "• Performance Tasks — 40%\n",
                            "• Quarterly Assessment — 30%" 
                            ))                          

grade_components = Label(window,
                         text=bullet_contents,
                         font=("Titillium Web", 13, "bold"),
                         bg="#f5f5dc",
                         fg="black",
                         height = 5,
                         width = 40,
                         anchor="w",
                         padx=20,
                         pady=15,
                         relief="solid",
                         bd=5,
                        )
grade_components.config(text=bullet_contents, justify=LEFT)
grade_components.pack(side=LEFT, anchor="nw")

#----GRADE EQUIVALENCY GLOBAL SUBJECTS (Joyden)----

equivalency_glob_sub_frame = Frame(window,
                                     bg="#f5f5dc",
                                     relief="solid",
                                     bd=5)
equivalency_glob_sub_frame.place(relx=1.0,
                                 rely=0.37,
                                 anchor="ne"
                                )

equivalency_glob_sub_title_text = "".join(("GRADE EQUIVALENCY\n",
                                            "GLOBAL SUBJECTS"))

equivalency_glob_sub_title = Label(equivalency_glob_sub_frame,
                                     text=equivalency_glob_sub_title_text,
                                     font=("Titillium Web", 15, "bold"),
                                     bg="#f5f5dc",
                                     fg="black",
                                     justify="center",
                                     padx=20,
                                     pady=15)
equivalency_glob_sub_title.pack()

tabledata = [('Grade', 'Grade Point', 'Remarks'),
             ("98.00-100.00", '1.0', ""),
             ("96.00-97.99", '1.25', ""),
             ("94.00-95.99", '1.50', ""),
             ("92.00-93.99", '1.75', ""),
             ("90.00-91.99", '2.0', ""),
             ("88.00-87.99", '2.25', ""),
             ("86.00-87.99", '2.50', ""),
             ("84.00-85.99", '2.75', ""),
             ("80.00-83.99", '3.0', "Passing Grade"),
             ("0.00-79.99", '3.25', "Failing Grade")]

table_frame = Frame(equivalency_glob_sub_frame, bg="#f5f5dc"
                    )
table_frame.pack(anchor="w")

Toplevel

for i in range(11):
    for j in range(3):
        e = Entry(table_frame, width=23, fg='black', bg="#fff2bb",
                   font=('Titillium Web', 10, 'bold'))
        e.grid(row=i, column=j)
        e.insert(END, tabledata[i][j])
        e.config(state=DISABLED, disabledbackground="#fff2bb", disabledforeground="black")

#----Global Subjects----

#SUBJECT DROPDOWN (WYEN)

subject_frame= Frame(window,
    bg="#f5f5dc"
)

subject_frame.place(
    relx=1.0,
    x=20,
    y=103,
    anchor="ne",
    width=500
)

#GLOBAL NA TO

global_frame = Frame(
    subject_frame,
    bg="#f5f5dc",
    relief="solid",
    bd=2
)

global_frame.pack(
    side=LEFT,
    fill=X,
    expand=TRUE,
    anchor="n"
)

global_button = Button (
    global_frame,
    text="Global Subjects",
    font=("Arial", 10, "bold"),
    bg="#fff2bb",
    fg="black",
    relief="solid",
    bd=1
)

global_button.pack(
    side=TOP,
    fill=X
)

global_list_frame = Frame (
    global_frame,
    bg="#f5f5dc",
    height=125
)

global_list_frame.pack(
    fill=X
)

global_list_frame.pack_propagate(FALSE)

#SCROLLBAR NI NONGLOBAL

global_scrollbar = Scrollbar (
    global_list_frame,
    orient=VERTICAL,
    width=15
)

global_scrollbar.pack(
    side=LEFT,
    fill=Y
)

global_list = Listbox(
    global_list_frame,
    height=6,
    font=("Arial", 10),
    bg="#f5f5dc",
    fg="black",
    relief=FLAT,
    bd=0,
    yscrollcommand=global_scrollbar.set
)

global_list.pack(
    side=RIGHT,
    fill=BOTH,
    expand=TRUE
)   

global_scrollbar.config(
    command=global_list.yview
)

global_subjects = [
    "GEN 001",
    "GEN 002",
    "GEN 003",
    "GEN 004",
    "GEN 005",
    "GEN 006",
    "GEN 008",
    "GEN 009",
    "GEN 013",
    "GEN 014",
    "GEN 015",
    "GEN 016",
    "GEN 017",
    "GEN 018"
]

for subject in global_subjects:
    global_list.insert(
    END,
    subject
)

#PAANO SHA MAG FUNCTION NIYAN ANG DROPDOWN

def toggle_global():

    if global_list_frame.winfo_ismapped():

        global_list_frame.pack_forget()

        global_button.config(
            text="Global Subjects >"
        )

    else:

        global_list_frame.pack(
            fill=X
        )

        global_button.config(
            text="Global Subjects v"
        )

global_button.config(
    command=toggle_global
)

window.mainloop()
