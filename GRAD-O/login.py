import tkinter as tk
import customtkinter as ctk
import psycopg2
import tkinter.messagebox as messagebox


class LoginFrame(ctk.CTkFrame):
    def __init__(self, root, on_login):
        super().__init__(root, corner_radius=0)
        self.root = root
        self.on_login = on_login
# Sets the title size For the Login Window
        self.root.title("QueueUP Login")
        self.pack(fill="both", expand=True)
    #Creates a centered container for the login controls
        form = ctk.CTkFrame(self, fg_color="transparent")
        form.place(relx=0.5, rely=0.5, anchor="center")

# Displays the title for login screen
        ctk.CTkLabel(
            form,
            text="QueueUP: Log-In",
            font=ctk.CTkFont(family="Trebuchet MS", size=35, weight="bold"),
        ).pack(pady=(8, 15))

# Creates a label and an input field for the username
        ctk.CTkLabel(form, text="Username").pack()
        self.username = ctk.CTkEntry(
            form,
            width=220,
            placeholder_text="Enter Username...",
            border_width=1,
            border_color=("#6FAF7A", "#6FAF7A"),
            corner_radius=4,
        )
        self.username.pack()
        self.username.bind("<Return>", self._submit_with_enter)

# Creates a label and input field for the password
# The 'show="*"' is to hide the password
        ctk.CTkLabel(form, text="Password").pack()
        self.password = ctk.CTkEntry(
            form,
            show="*",
            width=220,
            placeholder_text="Enter Password...",
            border_width=1,
            border_color=("#6FAF7A", "#6FAF7A"),    
            corner_radius=4,
        )
        self.password.pack()
        self.password.bind("<Return>", self._submit_with_enter)

# Creates a Log-in Button
        ctk.CTkButton(
            form,
            text="LOGIN",
            width=150,
            fg_color=("#8FD19E", "#3F8F50"),
            hover_color=("#72C784", "#347A42"),
            text_color=("#17351E", "#F1FBF2"),
            border_width=1,
            border_color=("#4D9B5A", "#8FD19E"),
            command=self.login,
        ).pack(pady=(16, 20))
    def _submit_with_enter(self, _event):
        self.login()
        return "break"

# Function to check and process the Log-in
    def login(self):
        username = self.username.get().strip()
        password = self.password.get()
# Checks if the username or password is empty
        if not username or not password:
            messagebox.showwarning(
                "Missing Information",
                "Enter a username and password!",
                parent=self.root,
            )
            return

        try:
            logged_in = authenticate(username, password)
        except psycopg2.Error as error:
            messagebox.showerror(
                "Database Error",
                f"Could not connect to PostgreSQL:\n{error}",
                parent=self.root,
            )
            return

        if not logged_in:
            messagebox.showerror(
                "Log-in Failed",
                "Invalid username or password!",
                parent=self.root,
            )
            return

        self.on_login()