import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)

root = tk.Tk()
root.title("Clock")

label = tk.Label(root, text="Clock", font=("Helvetica", 20), fg="white", bg='black')
label.pack()

update_time()

root.mainloop()