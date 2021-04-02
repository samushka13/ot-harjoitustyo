import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import ttk

db = sqlite3.connect("test.db")
db.isolation_level = None
db.row_factory = sqlite3.Row

X = 15
Y = 10

class CustomQuestionsView:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Trivioboros')
        self.window.minsize(1280, 720)
        self.window.geometry('%dx%d+0+0' % (self.window.winfo_screenwidth(), self.window.winfo_screenheight()))
        self.window.bind_class("Button", "<Return>", self.bind_key_to_button)

        # -------------------------------------------------------------------
        # Left-side widgets start.
        # -------------------------------------------------------------------

        title = tk.Label(self.window, text="Create Custom Questions")
        title.grid(column=0, row=0, padx=X, pady=Y)

        label = tk.Label(text="Category")
        label.grid(column=0, row=1, padx=X, pady=Y)

        self.get_category_combobox()

        label = tk.Label(text="Question")
        label.grid(column=0, row=3, padx=X, pady=Y)

        self.question_entry = tk.Entry(self.window, width=50)
        self.question_entry.grid(column=0, row=4, padx=X, pady=Y)

        label = tk.Label(text="Answer")
        label.grid(column=0, row=5, padx=X, pady=Y)

        self.answer_entry = tk.Entry(self.window, width=50)
        self.answer_entry.grid(column=0, row=6, padx=X, pady=Y)

        save = tk.Button(self.window, text="Save", width=10, command=self.save_item)
        save.grid(column=0, row=7, padx=X, pady=Y)

        clear = tk.Button(self.window, text="Clear", width=10, command=self.clear_item)
        clear.grid(column=0, row=8, padx=X, pady=Y)

        # -------------------------------------------------------------------
        # Left-side widgets end.
        # -------------------------------------------------------------------
        # Right-side widgets start.
        # -------------------------------------------------------------------

        title = tk.Label(self.window, text="Browse Custom Questions")
        title.grid(column=1, row=0, columnspan=2, padx=X, pady=Y)

        self.get_listbox()

        edit = tk.Button(self.window, text="Edit", width=10, command=self.edit_item)
        edit.grid(column=1, row=8, padx=X, pady=Y)

        delete = tk.Button(self.window, text="Delete", width=10, command=self.delete_item)
        delete.grid(column=2, row=8, padx=X, pady=Y)

        delete_all = tk.Button(self.window, text="Delete all", width=10, command=self.delete_all)
        delete_all.grid(column=1, columnspan=2, row=9, padx=X, pady=Y)

        # -------------------------------------------------------------------
        # Right-side widgets end.
        # -------------------------------------------------------------------

        self.window.mainloop()

    def destroy_custom_questions_view(self):
        self.window.destroy()

    def save_item(self):
        user_id = 1
        category = self.category_combobox.get()
        question = self.question_entry.get()
        answer = self.answer_entry.get()
        db.execute("INSERT INTO Questions (user_id, category, question, answer) VALUES (?,?,?,?)", (user_id, category, question, answer))
        messagebox.showinfo("HOORAY!", "Question added successfully.")
        self.get_listbox()
        self.get_category_combobox()


    def clear_item(self):
        self.category_combobox.delete(0, 'end')
        self.question_entry.delete(0, 'end')
        self.answer_entry.delete(0, 'end')

    def edit_item(self):
        pass

    def delete_item(self):
        confirmation = messagebox.askquestion("Delete", "Are you sure you want to delete the selected question?")
        if confirmation == 'yes':
            db.execute(f"DELETE FROM Questions WHERE id='{str(self.listbox.get(self.listbox.curselection())).split(' ', 1)[0]}'")
            self.get_listbox()
            self.get_category_combobox()
            tk.messagebox.showinfo('Delete','Your question has been deleted.')

    def delete_all(self):
        confirmation = messagebox.askquestion("Delete", "Are you sure you want to delete all your questions?")
        if confirmation == 'yes':
            db.execute("DELETE FROM Questions")
            self.get_listbox()
            self.get_category_combobox()
            tk.messagebox.showinfo('Delete','Your questions have been deleted.')

        # These will be used to enable a feature,
        # where the current user can view every user's questions (in the same database),
        # but only delete (or edit) their own.
        # user_id = db.execute(f"SELECT id FROM Users WHERE username='{current_user}'").fetchone()
        # db.execute(f"DELETE FROM Questions WHERE user_id='{user_id['id']}'")

    def get_listbox(self):
        entries = []
        for row in db.execute("SELECT id, category, question, answer FROM Questions").fetchall():
            entries.append(f"{row['id']}      C: {row['category']}     Q: {row['question']}     A: {row['answer']}")
        self.listbox_entries = entries
        self.listbox = tk.Listbox(self.window, width=50, height=30)
        for entry in self.listbox_entries:
            self.listbox.insert(tk.END, entry)
            self.listbox.select_set(0)
        self.listbox.grid(column=1, row=1, columnspan=2, rowspan=7, padx=X, pady=Y)
        return self.listbox

    def get_category_combobox(self):
        self.category_combobox = ttk.Combobox(self.window, width=50, textvariable=tk.StringVar())
        values = []
        for row in db.execute("SELECT category FROM Questions GROUP BY category").fetchall():
            values.append(f"{row['category']}")
        self.category_combobox['values'] = values
        self.category_combobox.grid(column = 0, row = 2, padx=X, pady=Y)
        return self.category_combobox

    def bind_key_to_button(self, window):
        window.widget.invoke()
