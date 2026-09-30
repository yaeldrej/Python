from ntpath import join
import tkinter
from tkinter import *
from tkinter import ttk
from turtle import left
import customtkinter as ctk

is_visible = False


def show_page(window):
    
#def toggle_label1():
    #global is_visible
    #if is_visible:
        #label1.grid_forget()
        #is_visible = False
    #else:
        #label1.grid(row=0,column=0)
        #is_visible = True

#def grade_calculator():

    #window
    window = Tk()
    window.geometry("1366x768")
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


    #QUOTES

    
    #RIBBON EDWIN
    ribbon_photo1 = ribbon_photo.subsample(3, 3)
    text_label = Label(window,
                     text= 'Fair Calculation, Goal-Oriented Do it With GRAD-O',
                     font= ('Titillium Web', 25, 'bold'),
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

    sidebar = Frame(
    window,
    height=800,
    width=200,
    bg="#b9c5cc",
    relief=SOLID,
    bd=1
    )

    sidebar.pack(
    side="left",
    fill="y"
    )

    label1 = Label(window, text= 'test',
               bg='light yellow')
    button1 = Button(sidebar, 
                 text="GRADE\nCALCULATOR",
                 font=("Titillium Web", 20, "bold"),
                 bg="#f5f5dc",
                 fg="black",
                 relief="ridge",
                 bd=5,
)

    button1.pack(side= TOP,
             fill= 'x',
             padx= 5,
             pady= 10
    )

    button2 = Button(
    sidebar,
    text="GRADE\nPROGRESS"
    )

    button2.config(
    font=("Titillium Web", 20, "bold")
    )

    button2.config(
    bg="#f5f5dc"
    )

    button2.config(
    fg="black"
    )

    button2.config(
    relief="ridge"
    )

    button2.config(
    bd=5
    )

    button2.pack(
    side="top",
    fill="x",
    padx=5,
    pady=10
    )

    button3 = Button(
    sidebar,
    text="GRADE\nAVERAGE"
    )

    button3.config(
    font=("Titillium Web", 20, "bold")
    )

    button3.config(
    bg="#f5f5dc"
    )

    button3.config(
    fg="black"
    )

    button3.config(
    relief="ridge"
    )

    button3.config(
    bd=5
    )

    button3.pack(
    side="top",
    fill="x",
    padx=5,
    pady=10
    )

    button4 = Button(
    sidebar,
    text="GRADE\nHISTORY"
    )

    button4.config(
    font=("Titillium Web", 20, "bold")
    )

    button4.config(
    bg="#f5f5dc"
    )

    button4.config(
    fg="black"
    )

    button4.config(
    relief="ridge"
    )

    button4.config(
    bd=5
    )

    button4.pack(
    side="top",
    fill="x",
    padx=5,
    pady=10
    )

    button5 = Button(
    sidebar,
    text="ABOUT\nUS"
    )

    button5.config(
    font=("Titillium Web", 20, "bold")
    )

    button5.config(
    bg="#f5f5dc"
    )

    button5.config(
    fg="black"
    )

    button5.config(
    relief="ridge"
    )

    button5.config(
    bd=5
    )

    button5.pack(
    side="top",
    fill="x",
    padx=5,
    pady=10
    )

    bottom_frame = Frame(
    sidebar,
    bg="#b9c5cc"
    )

    bottom_frame.pack(
    side=BOTTOM,
    fill=X,
    padx=5,
    pady=10
    )

    button6 = Button(
    bottom_frame,
    text="⚙️",
    font=("Arial", 15),
    bg="#f5f5dc",
    fg="black",
    relief="ridge",
    bd=5
    )

    button6.pack(
    side=LEFT
    )

    button_frame = Frame(
    sidebar,
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
    font=("Arial", 15),
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
    font=("Arial", 15),
    bg="#b9c5cc",
    fg="black",
    relief="flat",
    bd=5
    )

    button8.pack(
    side=RIGHT,
    padx=3
    )

    #----SUBJECT SELECTION----
    subj_selection = Frame(window,
                       width=300,
                       height=100,
                       bg="#f5f5dc",
                       relief="solid",)

    subj_selection.pack()

    #----Global Subjects----

    #SUBJECT DROPDOWN (WYEN)

    subjects_frame = Frame(window, bg="#f5f5dc", width=300,
                            height=300)
    subjects_frame.pack(side=RIGHT, anchor="ne")
    subjects_frame.pack_propagate(FALSE)


    #GLOBAL SUBJECTS

    global_frame = Frame(
    subjects_frame,
    bg="#f5f5dc",
    relief="solid",
    bd=2
    )

    global_frame.pack(side=LEFT,
                fill=BOTH,
                expand=TRUE,
                )

    global_button = Button(
    global_frame,
    text="Global Subjects v",
    font=("Titillium Web", 10, "bold",),
    bg="#fff2bb",
    fg="black",
    relief="flat",
    bd=1
    )

    global_button.pack(
    side=TOP,
    fill="x"
    )


    global_list_frame = Frame(
    global_frame,
    bg="#f5f5dc"
    )

    global_list_frame.pack(
        fill=BOTH,
        expand=TRUE
    )

    #SCROLLBAR
    global_scrollbar = Scrollbar(
        global_list_frame,
        orient=VERTICAL
    )

    global_scrollbar.pack(
        side=LEFT,
        fill=Y
    )

    global_list = Listbox(
    global_list_frame,
        height=8,
        font=("Titilium Web", 10),
        bg="#f5f5dc",
        fg="black",
        relief="flat",
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

    # Global subjects
    global_subjects = [
    "ITE 366",
    "ITE 260",
    "ITE 048",
    "ITE 186",
    "ITE 399",
    "ITE 393",
    "ITE 400",
    "ITE 314",
    "ITE 315",
    "ITE 320",
    "ITE 321",
    "ITE 322",
    "ITE 323",
    "ITE 324"
    ]

    for subject in global_subjects:
        global_list.insert(END, subject)

    #NON-GLOBAL
    nonglobal_frame = Frame(
    subjects_frame,
    bg="#f5f5dc",
    relief="solid",
    bd=2
    )

    nonglobal_frame.pack(
    side=LEFT,
    fill=BOTH,
    expand=TRUE
    )


    nonglobal_button = Button(
    nonglobal_frame,
    text="Non-Global Subjects ⌄",
    font=("Titillium Web", 10, "bold"),
    bg="#fff2bb",
    fg="black",
    relief="solid",
    bd=1
    )

    nonglobal_button.pack(
    side=TOP,
    fill=X
    )

    nonglobal_list_frame = Frame(
    nonglobal_frame,
    bg="#f5f5dc"
    )

    nonglobal_list_frame.pack(
    fill=BOTH,
    expand=TRUE
    )

    nonglobal_scrollbar = Scrollbar(
    nonglobal_list_frame,
    orient=VERTICAL
    )

    nonglobal_scrollbar.pack(
    side=LEFT,
    fill=Y
    )


    nonglobal_list = Listbox(
    nonglobal_list_frame,
    height=8,
    font=("Titillium Web", 10),
    bg="#f5f5dc",
    fg="black",
    relief=FLAT,
    bd=0,
    yscrollcommand=nonglobal_scrollbar.set
    )

    nonglobal_list.pack(
    side=RIGHT,
    fill=BOTH,
    expand=TRUE
    )


    nonglobal_scrollbar.config(
    command=nonglobal_list.yview
    )


    # Non-global subjects
    nonglobal_subjects = [
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

    for subject in nonglobal_subjects:
        nonglobal_list.insert(END, subject)


    window.mainloop()