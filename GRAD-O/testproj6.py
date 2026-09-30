from ntpath import join
import tkinter
from tkinter import *
from tkinter import ttk
from turtle import left
import tkinter as tk
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        print("Successfully connected to the database!")
        return connection
    except Exception as error:
        print(f"Error connecting to database: {error}")
        return None

visible = False

def toggle1():
    global visible
    visible = not visible
    if visible:
        head_label1.pack(side="left",
                         padx=10)
    else:
        head_label1.pack_forget()

# ---- DATABASE QUERIES & HELPERS ----

def fetch_student_grades():
    """Fetch all saved subject grades from PostgreSQL."""
    conn = get_db_connection()
    if not conn:
        return []
    
    rows = []
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT subject_code, final_grade, grade_point, remarks 
            FROM student_grades 
            ORDER BY subject_code ASC;
        """)
        rows = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print(f"Error fetching grades: {e}")
    finally:
        conn.close()
    return rows

def save_calculated_grade(subject, written, quiz, exam, final_grade, grade_point, remarks):
    """Insert or Update calculated grades into PostgreSQL."""
    conn = get_db_connection()
    if not conn:
        return False
    
    try:
        cursor = conn.cursor()
        # Optional: Setup table if not existing
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS student_grades (
                subject_code VARCHAR(20) PRIMARY KEY,
                written_score NUMERIC(5,2),
                quiz_score NUMERIC(5,2),
                exam_score NUMERIC(5,2),
                final_grade NUMERIC(5,2),
                grade_point NUMERIC(3,2),
                remarks VARCHAR(50)
            );
        """)
        
        insert_query = """
            INSERT INTO student_grades 
                (subject_code, written_score, quiz_score, exam_score, final_grade, grade_point, remarks)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (subject_code) 
            DO UPDATE SET 
                written_score = EXCLUDED.written_score,
                quiz_score = EXCLUDED.quiz_score,
                exam_score = EXCLUDED.exam_score,
                final_grade = EXCLUDED.final_grade,
                grade_point = EXCLUDED.grade_point,
                remarks = EXCLUDED.remarks;
        """
        cursor.execute(insert_query, (subject, written, quiz, exam, final_grade, grade_point, remarks))
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print(f"Error saving grade: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()


#----WINDOW-----
window = Tk()
window.geometry("1280x1000")
window.minsize(1280, 1000)
window.title("GRAD-O")


# LIGHT / DARK MODE COLORS

light_mode = {
    "window": "#f5f5dc",
    "sidebar": "#b9c5cc",
    "ribbon": "#fff2bb",
    "text": "black",
    "button": "#f5f5dc",
    "table": "#fff2bb",
    "list": "#f5f5dc"
}


dark_mode = {
    "window": "#1e1e1e",
    "sidebar": "#252526",
    "ribbon": "#333333",
    "text": "white",
    "button": "#3a3a3a",
    "table": "#444444",
    "list": "#2d2d30"
}


#----ICON----
icon = PhotoImage(file='C:\\VS Code\\Python\\GRAD-O\\icon.png')
window.iconphoto(True, icon)


#----INTERFACE----
window.configure(bg=light_mode["window"])
ribbon_photo = PhotoImage(file='C:\\VS Code\\Python\\GRAD-O\\logo.png')
ribbon_photo_white1 = PhotoImage(file='C:\\VS Code\\Python\\GRAD-O\\white_logo.png')



#RIBBON EDWIN
ribbon_photo1 = ribbon_photo.subsample(3, 3)
ribbon_photo_white1 = ribbon_photo_white1.subsample(3, 3)

text_label = Label(
    window,
    text='Fair Calculation, Goal-Oriented Do it With GRAD-O',
    font=('Titillium Web', 15, 'bold'),
    padx=20,
    fg=light_mode["text"],
    bg=light_mode["ribbon"],
    relief=SOLID,
    bd=1,
    anchor='w',
    height=100,
    image=ribbon_photo1,
    compound='left',
)

text_label.pack(
    side=TOP,
    fill=X
)


# ---- SIDEBAR (SELWYN) ----

sidebar = Frame(
    window,
    height=300,
    width=50,
    bg=light_mode["sidebar"],
    relief=SOLID,
    bd=1
)

sidebar.pack(
    side="left",
    fill="y"
)


head_label1 = Label(
    window,
    text="THIS IS FROM THE WINDOW",
    bg="light blue"
)


button1 = Button(
    sidebar,
    text="HOME\nPAGE",
    font=("Titillium Web", 15, "bold"),
    bg=light_mode["button"],
    fg=light_mode["text"],
    relief="ridge",
    bd=5,
)

button1.pack(
    side=TOP,
    fill='x',
    padx=5,
    pady=10,
)


button2 = Button(
    sidebar,
    text="GRADE\nCALCULATOR",
    font=("Titillium Web", 15, "bold"),
    bg=light_mode["button"],
    fg=light_mode["text"],
    relief="ridge",
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
    text="GRADE\nPROGRESS",
    font=("Titillium Web", 15, "bold"),
    bg=light_mode["button"],
    fg=light_mode["text"],
    relief="ridge",
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
    text="GRADE\nAVERAGE",
    font=("Titillium Web", 15, "bold"),
    bg=light_mode["button"],
    fg=light_mode["text"],
    relief="ridge",
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
    text="GRADE\nHISTORY",
    font=("Titillium Web", 15, "bold"),
    bg=light_mode["button"],
    fg=light_mode["text"],
    relief="ridge",
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
    bg=light_mode["sidebar"]
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
    font=("Arial", 10),
    bg=light_mode["button"],
    fg=light_mode["text"],
    relief="ridge",
    bd=5
)

button6.pack(
    side=LEFT
)


button_frame = Frame(
    sidebar,
    bg=light_mode["sidebar"]
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
    bg=light_mode["sidebar"],
    fg=light_mode["text"],
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
    bg=light_mode["sidebar"],
    fg=light_mode["text"],
    relief="flat",
    bd=5
)

button8.pack(
    side=RIGHT,
    padx=3
)


content_frame = tk.Frame(
    window,
    bg=light_mode["window"]
)

content_frame.pack(
    side=tk.LEFT,
    fill=tk.BOTH,
    expand=True
)


#PAGES
home_page = tk.Frame(
    content_frame,
    bg=light_mode["window"]
)

calculator_page = tk.Frame(
    content_frame,
    bg=light_mode["window"]
)

progress_page = tk.Frame(
    content_frame,
    bg=light_mode["window"]
)

average_page = tk.Frame(
    content_frame,
    bg=light_mode["window"]
)

history_page = tk.Frame(
    content_frame,
    bg=light_mode["window"]
)


#----BACKGROUND LOGO----

background_logo_home = Label(
    home_page,
    image=ribbon_photo,
    width=1000,
    height=160,
    bg=light_mode["window"],
    padx=-0,
    pady=-0
)

background_logo_home.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)


background_logo_calculator = Label(
    calculator_page,
    image=ribbon_photo,
    width=1000,
    height=160,
    bg=light_mode["window"],
    padx=-0,
    pady=-0
)

background_logo_calculator.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)


background_logo_progress = Label(
    progress_page,
    image=ribbon_photo,
    width=1000,
    height=160,
    bg=light_mode["window"],
    padx=-0,
    pady=-0
)

background_logo_progress.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)


background_logo_average = Label(
    average_page,
    image=ribbon_photo,
    width=1000,
    height=160,
    bg=light_mode["window"],
    padx=-0,
    pady=-0
)

background_logo_average.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)


background_logo_history = Label(
    history_page,
    image=ribbon_photo,
    width=1000,
    height=160,
    bg=light_mode["window"],
    padx=-0,
    pady=-0
)

background_logo_history.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)


#----GRADE COMPONENTS----
bullet_contents = "".join((
    "GRADE COMPONENTS\n",
    "• Written Works — 30%\n",
    "• Performance Tasks — 40%\n",
    "• Quarterly Assessment — 30%"
))


grade_components = Label(
    home_page,
    text=bullet_contents,
    font=("Titillium Web", 13, "bold"),
    bg=light_mode["window"],
    fg=light_mode["text"],
    height=5,
    width=40,
    anchor="w",
    padx=20,
    pady=15,
    relief="solid",
    bd=5,
)

grade_components.config(
    text=bullet_contents,
    justify=LEFT
)

grade_components.place(
    relx=0.0,
    rely=0.0,
    anchor="nw"
)


#----GRADE EQUIVALENCY GLOBAL SUBJECTS (Joyden)----

equivalency_glob_sub_frame = Frame(
    home_page,
    bg=light_mode["window"],
    relief="solid",
    bd=5
)

equivalency_glob_sub_frame.place(
    relx=1.0,
    rely=0.37,
    anchor="ne"
)


equivalency_glob_sub_title_text = "".join((
    "GRADE EQUIVALENCY\n",
    "GLOBAL SUBJECTS"
))


equivalency_glob_sub_title = Label(
    equivalency_glob_sub_frame,
    text=equivalency_glob_sub_title_text,
    font=("Titillium Web", 15, "bold"),
    bg=light_mode["window"],
    fg=light_mode["text"],
    justify="center",
    padx=20,
    pady=15
)

equivalency_glob_sub_title.pack()


tabledata = [
    ('Grade', 'Grade Point', 'Remarks'),
    ("98.00-100.00", '1.0', ""),
    ("96.00-97.99", '1.25', ""),
    ("94.00-95.99", '1.50', ""),
    ("92.00-93.99", '1.75', ""),
    ("90.00-91.99", '2.0', ""),
    ("88.00-87.99", '2.25', ""),
    ("86.00-87.99", '2.50', ""),
    ("84.00-85.99", '2.75', ""),
    ("80.00-83.99", '3.0', "Passing Grade"),
    ("0.00-79.99", '3.25', "Failing Grade")
]


table_frame = Frame(
    equivalency_glob_sub_frame,
    bg=light_mode["window"]
)

table_frame.pack(
    anchor="w"
)


table_entries = []

for i in range(11):
    row_entries = []

    for j in range(3):

        e = Entry(
            table_frame,
            width=23,
            fg=light_mode["text"],
            bg=light_mode["table"],
            font=('Titillium Web', 10, 'bold')
        )

        e.grid(
            row=i,
            column=j
        )

        e.insert(
            END,
            tabledata[i][j]
        )

        e.config(
            state=DISABLED,
            disabledbackground=light_mode["table"],
            disabledforeground=light_mode["text"]
        )

        row_entries.append(e)

    table_entries.append(row_entries)


#----Global Subjects----

#SUBJECT DROPDOWN (WYEN)

subject_frame = Frame(
    home_page,
    bg=light_mode["window"]
)

subject_frame.place(
    relx=1.0,
    x=20,
    y=0,
    anchor="ne",
    width=500
)

#GLOBAL NA TO

global_frame = Frame(
    subject_frame,
    bg=light_mode["window"],
    relief="solid",
    bd=2
)

global_frame.pack(
    side=LEFT,
    fill=X,
    expand=TRUE,
    anchor="n"
)


global_button = Button(
    global_frame,
    text="Global Subjects",
    font=("Arial", 10, "bold"),
    bg=light_mode["table"],
    fg=light_mode["text"],
    relief="solid",
    bd=1
)

global_button.pack(
    side=TOP,
    fill=X
)


global_list_frame = Frame(
    global_frame,
    bg=light_mode["window"],
    height=125
)

global_list_frame.pack(
    fill=X
)

global_list_frame.pack_propagate(FALSE)


#SCROLLBAR NI GLOBAL

global_scrollbar = Scrollbar(
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
    bg=light_mode["list"],
    fg=light_mode["text"],
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


# HOME PAGE

home_title = tk.Label(
    home_page,
    font=("Titillium Web", 30, "bold"),
    bg=light_mode["window"],
    fg=light_mode["text"]
)

home_title.place(
    relx=0.5,
    rely=0.08,
    anchor="center"
)


# GRADE CALCULATOR PAGE

calculator_title = tk.Label(
    calculator_page,
    font=("Titillium Web", 30, "bold"),
    bg=light_mode["window"],
    fg=light_mode["text"]
)

calculator_title.pack(
    pady=50
)


calculator_text = tk.Label(
    calculator_page,
    font=("Titillium Web", 18),
    bg=light_mode["window"],
    fg=light_mode["text"]
)

calculator_text.pack()


# GRADE PROGRESS PAGE

progress_title = tk.Label(
    progress_page,
    font=("Titillium Web", 30, "bold"),
    bg=light_mode["window"],
    fg=light_mode["text"]
)

progress_title.pack(
    pady=50
)


progress_text = tk.Label(
    progress_page,
    font=("Titillium Web", 18),
    bg=light_mode["window"],
    fg=light_mode["text"]
)

progress_text.pack()


# GRADE AVERAGE PAGE

average_title = tk.Label(
    average_page,
    font=("Titillium Web", 30, "bold"),
    bg=light_mode["window"],
    fg=light_mode["text"]
)

average_title.pack(
    pady=50
)


average_text = tk.Label(
    average_page,
    font=("Titillium Web", 18),
    bg=light_mode["window"],
    fg=light_mode["text"]
)

average_text.pack()


# GRADE HISTORY PAGE
history_title = tk.Label(
    history_page,
    font=("Titillium Web", 30, "bold"),
    bg=light_mode["window"],
    fg=light_mode["text"]
)

history_title.pack(
    pady=50
)


history_text = tk.Label(
    history_page,
    font=("Titillium Web", 18),
    bg=light_mode["window"],
    fg=light_mode["text"]
)

history_text.pack()


# PAGE FUNCTION

def show_page(page):

    home_page.pack_forget()
    calculator_page.pack_forget()
    progress_page.pack_forget()
    average_page.pack_forget()
    history_page.pack_forget()

    page.pack(
        fill=BOTH,
        expand=True
    )

#LIGHT / DARK MODE FUNCTION

def change_theme(theme):

    # WINDOW
    window.configure(
        bg=theme["window"]
    )

    content_frame.configure(
        bg=theme["window"]
    )

    # SIDEBAR
    sidebar.configure(
        bg=theme["sidebar"]
    )

    bottom_frame.configure(
        bg=theme["sidebar"]
    )

    button_frame.configure(
        bg=theme["sidebar"]
    )

    if theme == dark_mode:
        text_label.configure(
        bg=theme["ribbon"],
        fg=theme["text"],
        image=ribbon_photo_white1
    )
    else:
        text_label.configure(
        bg=theme["ribbon"],
        fg=theme["text"],
        image=ribbon_photo1
    )
    # BACKGROUND LOGO
    if theme == dark_mode:
        background_logo_home.configure(
        bg=theme["window"],
        image=ribbon_photo_white1
    )
    else:
        background_logo_home.configure(
        bg=theme["window"],
        image=ribbon_photo
    )

    background_logo_calculator.configure(
        bg=theme["window"]
    )

    background_logo_progress.configure(
        bg=theme["window"]
    )

    background_logo_average.configure(
        bg=theme["window"]
    )

    background_logo_history.configure(
        bg=theme["window"]
    )

    # BUTTONS
    for button in (
        button1,
        button2,
        button3,
        button4,
        button5,
        button6
    ):

        button.configure(
            bg=theme["button"],
            fg=theme["text"],
            activebackground=theme["button"],
            activeforeground=theme["text"]
        )

    # LIGHT / DARK BUTTONS
    button7.configure(
        bg=theme["sidebar"],
        fg=theme["text"],
        activebackground=theme["sidebar"],
        activeforeground=theme["text"]
    )

    button8.configure(
        bg=theme["sidebar"],
        fg=theme["text"],
        activebackground=theme["sidebar"],
        activeforeground=theme["text"]
    )

    # GRADE COMPONENTS
    grade_components.configure(
        bg=theme["window"],
        fg=theme["text"]
    )

    # GRADE EQUIVALENCY
    equivalency_glob_sub_frame.configure(
        bg=theme["window"]
    )

    equivalency_glob_sub_title.configure(
        bg=theme["window"],
        fg=theme["text"]
    )

    table_frame.configure(
        bg=theme["window"]
    )

    # TABLE
    for row in table_entries:

        for entry in row:

            entry.configure(
                bg=theme["table"],
                fg=theme["text"],
                disabledbackground=theme["table"],
                disabledforeground=theme["text"]
            )

    # SUBJECT FRAME
    subject_frame.configure(
        bg=theme["window"]
    )

    global_frame.configure(
        bg=theme["window"]
    )

    global_button.configure(
        bg=theme["table"],
        fg=theme["text"],
        activebackground=theme["table"],
        activeforeground=theme["text"]
    )

    global_list_frame.configure(
        bg=theme["window"]
    )

    # GLOBAL SUBJECT LIST
    global_list.configure(
        bg=theme["list"],
        fg=theme["text"]
    )

    # GLOBAL SCROLLBAR
    global_scrollbar.configure(
        bg=theme["button"],
        activebackground=theme["table"],
        troughcolor=theme["window"]
    )

    # PAGES
    for page in (
        home_page,
        calculator_page,
        progress_page,
        average_page,
        history_page
    ):

        page.configure(
            bg=theme["window"]
        )

    # PAGE TEXT
    for label in (
        home_title,
        calculator_title,
        calculator_text,
        progress_title,
        progress_text,
        average_title,
        average_text,
        history_title,
        history_text
    ):

        label.configure(
            bg=theme["window"],
            fg=theme["text"]
        )

    #----CALCULATOR PAGE THEME----

    calculator_frame.configure(
        bg=theme["table"]
    )

    subject_label.configure(
        bg=theme["table"],
        fg=theme["text"]
    )

    below_sep.configure(
        bg=theme["window"]
    )

    enter_grades_label.configure(
        bg=theme["window"],
        fg=theme["text"]
    )

    period1.configure(
        bg=theme["list"],
        fg=theme["text"],
        insertbackground=theme["text"]
    )

    period2.configure(
        bg=theme["list"],
        fg=theme["text"],
        insertbackground=theme["text"]
    )

    period3.configure(
        bg=theme["list"],
        fg=theme["text"],
        insertbackground=theme["text"]
    )

    period1_text.configure(
        bg=theme["window"],
        fg=theme["text"]
    )

    period2_text.configure(
        bg=theme["window"],
        fg=theme["text"]
    )

    period3_text.configure(
        bg=theme["window"],
        fg=theme["text"]
    )

    below_sep2.configure(
        bg=theme["window"]
    )

    grading_components.configure(
        bg=theme["window"],
        fg=theme["text"]
    )

    written_task.configure(
        bg=theme["window"],
        fg=theme["text"]
    )

    quiz_petask.configure(
        bg=theme["window"],
        fg=theme["text"]
    )

    period_exam.configure(
        bg=theme["window"],
        fg=theme["text"]
    )

    written_ent.configure(
        bg=theme["list"],
        fg=theme["text"],
        insertbackground=theme["text"]
    )

    quiz_ent.configure(
        bg=theme["list"],
        fg=theme["text"],
        insertbackground=theme["text"]
    )

    periodexam_ent.configure(
        bg=theme["list"],
        fg=theme["text"],
        insertbackground=theme["text"]
    )

    below_sep3.configure(
        bg=theme["window"]
    )

    calculator_button.configure(
        bg=theme["table"],
        fg=theme["text"],
        activebackground=theme["sidebar"],
        activeforeground=theme["text"]
    )


    #----AVERAGE PAGE THEME----

    average_page.configure(
        bg=theme["window"]
    )

    average_top_frame.configure(
        bg=theme["table"]
    )

    average_title.configure(
        bg=theme["table"],
        fg=theme["text"]
    )

    average_value.configure(
        bg=theme["table"],
        fg=theme["text"]
    )

    average_status.configure(
        bg=theme["window"],
        fg="lime green"
    )

    component_frame.configure(
        bg=theme["table"]
    )

    component_title.configure(
        bg=theme["window"],
        fg=theme["text"]
    )

    written_label.configure(
        bg=theme["table"],
        fg=theme["text"]
    )

    quiz_label.configure(
        bg=theme["table"],
        fg=theme["text"]
    )

    exam_label.configure(
        bg=theme["table"],
        fg=theme["text"]
    )

    subjects_frame.configure(
        bg=theme["table"]
    )

    subjects_title.configure(
        bg=theme["table"],
        fg=theme["text"]
    )

    passed_label.configure(
        bg=theme["table"],
        fg=theme["text"]
    )

    failed_label.configure(
        bg=theme["table"],
        fg=theme["text"]
    )

    total_label.configure(
        bg=theme["table"],
        fg=theme["text"]
    )

    equivalency_frame.configure(
        bg=theme["table"]
    )

    equivalency_title.configure(
        bg=theme["table"],
        fg=theme["text"]
    )

    equivalency_table.configure(
        bg=theme["table"]
    )

    # AVERAGE PAGE EQUIVALENCY TABLE

    for row in equivalency_entries:

        for entry in row:

            entry.configure(
                bg=theme["table"],
                fg=theme["text"],
                disabledbackground=theme["table"],
                disabledforeground=theme["text"]
            )


    # AVERAGE PAGE SUBJECT TABLE

    style = ttk.Style()

    style.configure(
        "Treeview",
        background=theme["list"],
        foreground=theme["text"],
        fieldbackground=theme["list"]
    )

    style.configure(
        "Treeview.Heading",
        background=theme["table"],
        foreground=theme["text"]
    )

    style.map(
        "Treeview",
        background=[
            ("selected", theme["sidebar"])
        ],
        foreground=[
            ("selected", theme["text"])
        ]
    )


    # CALCULATOR COMBOBOX

    style.configure(
        "TCombobox",
        fieldbackground=theme["list"],
        background=theme["table"],
        foreground=theme["text"]
    )

    style.map(
        "TCombobox",
        fieldbackground=[
            ("readonly", theme["list"])
        ],
        foreground=[
            ("readonly", theme["text"])
        ],
        selectbackground=[
            ("readonly", theme["sidebar"])
        ],
        selectforeground=[
            ("readonly", theme["text"])
        ]
    )


# SIDEBAR BUTTON COMMANDS

button1.config(
    command=lambda: show_page(home_page)
)

button2.config(
    command=lambda: show_page(calculator_page)
)

button3.config(
    command=lambda: show_page(progress_page)
)

button4.config(
    command=lambda: show_page(average_page)
)

button5.config(
    command=lambda: show_page(history_page)
)


#----COMMANDS----

button7.config(
    command=lambda: change_theme(dark_mode)
)

button8.config(
    command=lambda: change_theme(light_mode)
)


show_page(home_page)

#----GUI CALCULATOR----
calculator_frame = Frame(
                   calculator_page,
                    bg="#fff2bb",
                    relief="solid",
                    bd=2,
                    width=500,
                    height=650,
                    )

calculator_frame.place(relx=0.02, 
                       rely=0.5, 
                       anchor="w")

subject_label = Label(
    calculator_frame,
    text="Select Subject",
    bg="#fff2bb",
    font=("Arial", 20, "bold")
)

subject_label.place(
    relx=0.25,
    rely=0.05,
    anchor="n")


subject_dropdown = ttk.Combobox(
    calculator_frame,
    values=[
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
        "GEN 018",
    ],
    state="readonly",
    width=15
)

subject_dropdown.place(relx=0.2, 
                       rely=0.10, 
                       anchor="n")

separator = Frame(
    calculator_frame,
    height=2,
    bg="#000000"
)

separator.place(
    relx=0.001,
    rely=0.2,
    relwidth=1
)

below_sep = Frame(
    calculator_frame,
    bg="#f5f5dc"
)

below_sep.place(
    relx=0,
    rely=0.203,
    relwidth=1,
    relheight=0.797
)

enter_grades_label = Label(
    below_sep,
    text="Enter Grades",
    bg="#f5f5dc",
    font=("Arial", 20, "bold")
)

enter_grades_label.place(
    relx=0.05,
    rely=0.05,
    anchor="nw"
)


period1 = Entry(below_sep, 
                width=10,
                font=("Arial", 11))
period1.place(relx=0.04, rely=0.300, height=50)

period2 = Entry(below_sep, 
                width=10,
                font=("Arial", 11))
period2.place(relx=0.38, rely=0.300, height=50)

period3 = Entry(below_sep, 
                width=10,
                font=("Arial", 11))
period3.place(relx=0.72, rely=0.300, height=50)

period1_text = Label(below_sep,
                     text='PERIOD 1',
                     bg="#f5f5dc",
                     font=('Arial', 15, 'bold'))
period1_text.place(relx=0.04, rely=0.195)

period2_text = Label(below_sep,
                     text='PERIOD 2',
                     bg="#f5f5dc",
                     font=('Arial', 15, 'bold'))
period2_text.place(relx=0.38, rely=0.195)

period3_text = Label(below_sep,
                     text='PERIOD 3',
                     bg="#f5f5dc",
                     font=('Arial', 15, 'bold'))
period3_text.place(relx=0.72, rely=0.195)

separator2 = Frame(
    calculator_frame,
    height=2,
    bg="#000000"
)

separator2.place(
    relx=0.05,
    rely=0.6,
    relwidth=0.9
)

below_sep2 = Frame(
    calculator_frame,
    bg="#f5f5dc"
)

below_sep2.place(
    relx=0,
    rely=0.603,
    relwidth=1,
    relheight=0.397
)

grading_components = Label(below_sep2,
                           text="Grading_components",
                           bg="#f5f5dc",
                           font=("Arial", 20, "bold"))
grading_components.place(relx = 0.05, rely= 0.05)

written_task = Label(below_sep2,
                    text="WRITTEN TASK",
                    bg="#f5f5dc",
                    font=("Arial", 15, "bold"))
written_task.place(relx = 0.05, rely = 0.2)

quiz_petask = Label(below_sep2,
                text="QUIZ/PERFORMANCE TASK",
                bg="#f5f5dc",
                font=("Arial", 15, "bold"))
quiz_petask.place(relx = 0.05, rely = 0.35)

period_exam = Label(below_sep2,
                text="PERIODICAL EXAM",
                bg="#f5f5dc",
                font=("Arial", 15, "bold"))
period_exam.place(relx = 0.05, rely = 0.5)

written_ent = Entry(below_sep2, 
                width=10,
                font=("Arial", 11))
written_ent.place(relx=0.75, rely=0.2, height=30)

quiz_ent = Entry(below_sep2, 
                width=10,
                font=("Arial", 11))
quiz_ent.place(relx=0.75, rely=0.35, height=30)

periodexam_ent = Entry(below_sep2, 
                width=10,
                font=("Arial", 11))
periodexam_ent.place(relx=0.75, rely=0.5, height=30)

separator3 = Frame(
    calculator_frame,
    height=2,
    bg="#000000"
)

separator3.place(
    relx=0.05,
    rely=0.90,
    relwidth=0.9
)

below_sep3 = Frame(
    calculator_frame,
    bg="#f5f5dc"
)

below_sep3.place(
    relx=0,
    rely=0.903,
    relwidth=1,
    relheight=0.097
)

calculator_button = Button(below_sep3,
                           text='🖩 CALCULATE',
                           bg='#fff2bb',
                           padx= 150,
                           pady= 18,
                           activebackground='#887b40',
                           activeforeground='black')
calculator_button.place(relx= 0.1, rely= 0.1)

# GRADE AVERAGE PAGE (SILWYN)

average_page = tk.Frame(
    content_frame,
    bg="#f5f5dc"
)


# TOP SECTION 

average_top_frame = tk.Frame(
    average_page,
    bg="#fff2bb",
    relief="solid",
    bd=1
)

average_top_frame.pack(
    fill="x",
    padx=20,
    pady=20
)

# OVERALL WEIGHTED AVERAGE

average_title = tk.Label(
    average_top_frame,
    text="OVERALL WEIGHTED AVERAGE",
    font=("Titillium Web", 15, "bold"),
    bg="#fff2bb",
    fg="black"
)

average_title.pack(
    anchor="w",
    padx=170,
    pady=(15, 0)
)


average_value = tk.Label(
    average_top_frame,
    text="1.75",
    font=("Titillium Web", 45, "bold"),
    bg="#fff2bb",
    fg="black"
)

average_value.pack(
    anchor="w",
    padx=170
)


average_status = tk.Label(
    average_top_frame,
    text="PASSED",
    font=("Titillium Web", 15),
    bg="white",
    fg="lime green",
    width=12
)

average_status.pack(
    anchor="w",
    padx=170,
    pady=(0, 20)
)


# GRADE COMPONENT 

component_frame = tk.Frame(
    average_top_frame,
    bg="#fff2bb",
    relief="solid",
    bd=1
)

component_frame.place(
    relx=0.58,
    rely=0.12,
    relwidth=0.38,
    relheight=0.75
)


component_title = tk.Label(
    component_frame,
    text="GRADE COMPONENT",
    font=("Titillium Web", 12, "bold"),
    bg="white",
    fg="black",
    anchor="w"
)

component_title.pack(
    fill="x",
    padx=10,
    pady=5
)


written_label = tk.Label(
    component_frame,
    text="WRITTEN                         30%",
    font=("Titillium Web", 11, "bold"),
    bg="#fff2bb",
    fg="black",
    anchor="w"
)

written_label.pack(
    fill="x",
    padx=10,
    pady=5
)


quiz_label = tk.Label(
    component_frame,
    text="QUIZ/PTASK                    40%",
    font=("Titillium Web", 11, "bold"),
    bg="#fff2bb",
    fg="black",
    anchor="w"
)

quiz_label.pack(
    fill="x",
    padx=10,
    pady=5
)


exam_label = tk.Label(
    component_frame,
    text="PERIODICAL EXAM          30%",
    font=("Titillium Web", 11, "bold"),
    bg="#fff2bb",
    fg="black",
    anchor="w"
)

exam_label.pack(
    fill="x",
    padx=10,
    pady=5
)

# ---- SUBJECTS ----

subjects_frame = tk.Frame(
    average_page,
    bg="#fff2bb",
    relief="solid",
    bd=1
)

subjects_frame.place(
    relx=0.02,
    rely=0.37,
    relwidth=0.62,
    relheight=0.58
)


subjects_title = tk.Label(
    subjects_frame,
    text="SUBJECTS",
    font=("Titillium Web", 17, "bold"),
    bg="#fff2bb",
    fg="black"
)

subjects_title.pack(
    anchor="w",
    padx=15,
    pady=10
)


# SUBJECT TABLE

subjects_table = ttk.Treeview(
    subjects_frame,
    columns=(
        "Subject",
        "Final Grade",
        "Grade Point",
        "Remarks"
    ),
    show="headings",
    height=7
)


subjects_table.heading(
    "Subject",
    text="SUBJECT"
)

subjects_table.heading(
    "Final Grade",
    text="FINAL GRADE"
)

subjects_table.heading(
    "Grade Point",
    text="GRADE POINT"
)

subjects_table.heading(
    "Remarks",
    text="REMARKS"
)


subjects_table.column(
    "Subject",
    width=150
)

subjects_table.column(
    "Final Grade",
    width=150
)

subjects_table.column(
    "Grade Point",
    width=150
)

subjects_table.column(
    "Remarks",
    width=150
)


subjects_table.pack(
    fill="x",
    padx=10
)


# SAMPLE SUBJECTS

subjects_table.insert(
    "",
    "end",
    values=("ITE 366", "92.00", "1.75", "Passed")
)

subjects_table.insert(
    "",
    "end",
    values=("GEN 001", "95.00", "1.50", "Passed")
)

subjects_table.insert(
    "",
    "end",
    values=("MATH 101", "88.00", "2.25", "Passed")
)

subjects_table.insert(
    "",
    "end",
    values=("ITE 260", "79.00", "3.25", "Failed")
)


# ---- PASSED / FAILED / TOTAL ----

passed_label = tk.Label(
    subjects_frame,
    text="PASSED: 3",
    font=("Titillium Web", 12, "bold"),
    bg="#fff2bb",
    fg="black"
)

passed_label.place(
    relx=0.03,
    rely=0.88
)


failed_label = tk.Label(
    subjects_frame,
    text="FAILED: 1",
    font=("Titillium Web", 12, "bold"),
    bg="#fff2bb",
    fg="black"
)

failed_label.place(
    relx=0.20,
    rely=0.88
)


total_label = tk.Label(
    subjects_frame,
    text="TOTAL SUBJECTS: 4",
    font=("Titillium Web", 12, "bold"),
    bg="#fff2bb",
    fg="black"
)

total_label.place(
    relx=0.75,
    rely=0.88
)

# GRADE EQUIVALENCY 

equivalency_frame = tk.Frame(
    average_page,
    bg="#fff2bb",
    relief="solid",
    bd=2
)

equivalency_frame.place(
    relx=0.68,
    rely=0.37,
    relwidth=0.30,
    relheight=0.58
)


equivalency_title = tk.Label(
    equivalency_frame,
    text="GRADE EQUIVALENCY\nNON - GLOBAL SUBJECTS",
    font=("Titillium Web", 16, "bold"),
    bg="#fff2bb",
    fg="black",
    justify="center"
)

equivalency_title.pack(
    pady=15
)


# EQUIVALENCY TABLE

equivalency_table = tk.Frame(
    equivalency_frame,
    bg=light_mode["table"]
)

equivalency_table.pack(
    fill="both",
    expand=True,
    padx=0,
    pady=0
)

# COLUMN SIZES

equivalency_table.grid_columnconfigure(
    0,
    weight=10
)

equivalency_table.grid_columnconfigure(
    1,
    weight=10
)

equivalency_table.grid_columnconfigure(
    2,
    weight=5
)

# EQUIVALENCY DATA

equivalency_data = [
    ("GRADE", "GRADE POINT", "REMARKS"),
    ("94.80-100.00", "1.0", ""),
    ("89.20-94.70", "1.25", ""),
    ("83.60-89.10", "1.50", ""),
    ("78.00-83.50", "1.75", ""),
    ("72.40-77.90", "2.0", ""),
    ("66.80-72.30", "2.25", ""),
    ("61.20-66.70", "2.50", ""),
    ("55.60-61.10", "2.75", ""),
    ("50.00-55.50", "3.0", "Passing Grade"),
    ("0.00-49.90", "3.25", "Failing Grade")
]


equivalency_entries = []


for i in range(len(equivalency_data)):

    row_entries = []

    equivalency_table.grid_rowconfigure(
        i,
        minsize=25
    )

    for j in range(3):

        e = tk.Entry(
            equivalency_table,
            font=("Titillium Web", 10, "bold"),
            fg="black",
            bg=light_mode["table"],
            relief="solid",
            bd=1,
            justify="left"
        )

        e.grid(
            row=i,
            column=j,
            sticky="nsew"
        )

        e.insert(
            tk.END,
            equivalency_data[i][j]
        )

        e.config(
            state=tk.DISABLED,
            disabledbackground=light_mode["table"],
            disabledforeground="black"
        )

        row_entries.append(e)

    equivalency_entries.append(row_entries)


# TTK STYLE

style = ttk.Style()

style.theme_use("clam")

style.configure(
    "TCombobox",
    fieldbackground=light_mode["list"],
    background=light_mode["table"],
    foreground=light_mode["text"]
)

style.map(
    "TCombobox",
    fieldbackground=[
        ("readonly", light_mode["list"])
    ],
    foreground=[
        ("readonly", light_mode["text"])
    ]
)

style.configure(
    "Treeview",
    background=light_mode["list"],
    foreground=light_mode["text"],
    fieldbackground=light_mode["list"]
)

style.configure(
    "Treeview.Heading",
    background=light_mode["table"],
    foreground=light_mode["text"]
)

style.map(
    "Treeview",
    background=[
        ("selected", light_mode["sidebar"])
    ],
    foreground=[
        ("selected", light_mode["text"])
    ]
)
change_theme(light_mode)
show_page(home_page)

window.mainloop()