import ttkbootstrap as ttk
import csv
import os
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from cryptography.fernet import Fernet


class ExerciseApp(ttk.Frame):
    def __init__(self, master_window):
        super().__init__(master_window, padding=(20,20))
        self.pack()

        self.input_text = ttk.StringVar(value="")
        self.input_score = ttk.IntVar(value=0)

        self.left_container = ttk.Frame(self)
        self.left_container.pack(side="left", fill=Y)
        self.database = Database()
        self.treeView = self.create_treeview()

        self.right_container = ttk.Frame(self)
        self.right_container.pack(side="left", fill=Y)

        self.label_create(self.right_container, "Name:")
        self.entry_create(self.right_container, self.input_text)
        self.label_create(self.right_container, "Score:")
        self.entry_create(self.right_container, self.input_score)
        self.button_create(self.right_container)

    def label_create(self, place, text):
        label = ttk.Label(place, text=text)
        label.pack(padx=5, pady=5)
        return

    def button_create(self, place):
        button = ttk.Button(place, text="Submit!")
        button.bind("<Button-1>" , self.on_click_button)
        button.pack(padx=5, pady=5)
        return

    def entry_create(self, place, variable):
        entry = ttk.Entry(place, textvariable=variable)
        entry.pack(padx=5, pady=5)
        return

    def create_treeview(self):
        tree = ttk.Treeview(master=self.left_container, bootstyle = "secondary", columns=["Name","Score"], show='headings')
        tree.grid_configure(row=0,column=0,columnspan=4,rowspan=5,padx=20, pady=20)

        tree.column("Name",anchor=CENTER)
        tree.column("Score", anchor=CENTER)

        tree.heading("Name", text="Name")
        tree.heading("Score", text="Score")
        for row in self.database.read_data():
            tree.insert("", 'end', values=(row[0], row[1]))
        return tree

    def on_click_button(self, args):
        self.treeView.insert("", 'end', values=(self.input_text.get(), self.input_score.get()))
        self.database.add_data(self.input_text.get(), self.input_score.get())
        toast = ToastNotification(
            title="Notification!",
            message="New element in treeview!",
            duration=1000
        )
        toast.show_toast()
        return
    
class Database():
    def __init__(self):
        self.filename="database.csv"
        self.key=b'e7Ovosmxtw7EgAxJVTaCNFjmCN0Re5NqC_iBOknMEOg='
        self.cipher_app=Fernet(self.key)

    def read_data(self):
        if not os.path.isfile(self.filename):
            with open(self.filename, 'w', newline='') as csvfile:
                pass  # Creating an empty file

        data_table=[]
        with open(self.filename, mode='r', newline='') as file:
            reader=csv.reader(file)
            for row in reader:
                decrypted_text=self.cipher_app.decrypt(row[0])
                decrypted_score=self.cipher_app.decrypt(row[1])
                data_table.append([decrypted_text.decode(), decrypted_score.decode()])
        return data_table

    def add_data(self, text, score):
        encrypted_text  =self.cipher_app.encrypt(text.encode())
        encrypted_score =self.cipher_app.encrypt(str(score).encode())
        with open(self.filename, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([encrypted_text.decode(), encrypted_score.decode()])

if __name__ == "__main__":
    app = ttk.Window(title="Zadanie 5",themename="minty")
    app.geometry("800x400")
    ExerciseApp(app)
    app.mainloop()
