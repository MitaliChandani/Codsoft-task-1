import tkinter as tk  
from tkinter import messagebox

def add_task(event=None):
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Please enter a task.")

def remove_task():
    try:
        selected_task = task_list.get(task_list.curselection())
        task_list.delete(task_list.curselection())
        save_tasks()
        messagebox.showinfo("Task Removed", f"Task '{selected_task}' has been removed.")
    except:
        messagebox.showwarning("Please select a task to remove.")

def delete_all_tasks():
    confirmed = messagebox.askyesno("Delete All Tasks", "Are you sure you want to delete all tasks?")
    if confirmed:
        task_list.delete(0, tk.END)
        save_tasks()

def save_tasks():
    tasks = task_list.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_list.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

def exit_app():
    save_tasks()
    root.destroy()

root = tk.Tk()
root.title("To-Do List")
root.configure(bg="lightblue")  

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=20)
task_entry.bind("<Return>", add_task)

task_list = tk.Listbox(root, width=40, selectbackground="lightcyan")
task_list.pack(pady=10)

load_tasks()

remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg="salmon")
delete_all_button = tk.Button(root, text="Delete All Tasks", command=delete_all_tasks, bg="salmon")
exit_button = tk.Button(root, text="Exit", command=exit_app, bg="Red")
remove_button.pack()
delete_all_button.pack()
exit_button.pack()

root.mainloop()