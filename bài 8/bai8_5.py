print("sv: trần nguyễn viết đức.")
print ("mssv:235752020710013")

####
import tkinter as tk

root = tk.Tk()
v = tk.IntVar()
v.set(4)

languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5),
]

def ShowChoice():
    print(v.get())

tk.Label(
    root,
    text="Choose your favourite programming language:",
    justify=tk.LEFT,
    padx=20,).pack()

for language, val in languages:
    tk.Radiobutton(
        root,
        text=language,
        padx=20,
        variable=v,
        command=ShowChoice,
        value=val,
        indicatoron=0,  # Thay đổi từ Radio Button sang Indicator
    ).pack(anchor=tk.W)

root.mainloop()
