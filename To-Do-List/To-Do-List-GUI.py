import tkinter as tk
from tkinter import messagebox as msg


def on_text_click(event):
    text.delete("1.0", tk.END)
    text.config(fg='black')


def add_task():
    task_description = text.get("1.0", "end-1c")
    if task_description.strip() == "":
        msg.showerror("Error", "Task description cannot be empty")
        return

    checkbutton_var = tk.IntVar()

    def destroy_button():
        checkbutton.destroy()
        msg.showinfo("Task", "Task Completed")

    checkbutton = tk.Checkbutton(
        root,
        text=task_description,
        variable=checkbutton_var,
        height=2,
        width=100,
        background="#303030",
        foreground="white",
        command=destroy_button,
        activebackground="green",
        activeforeground="white"
    )
    checkbutton.pack(pady=10)


root = tk.Tk()
root.geometry("360x500")
root.title("To-Do List")
root.config(background="#303030")

text = tk.Text(root, height=2, width=30, fg='grey', font="Helvetica")
text.insert(tk.END, 'Enter your task here...')
text.bind('<FocusIn>', on_text_click)
text.pack(pady=20)

tk.Button(
    text="Submit",
    command=add_task,
    font="Helvetica",
    overrelief=tk.RIDGE,
    relief=tk.RIDGE,
    foreground="black",
    background="lightgreen"
).pack()

root.mainloop()
