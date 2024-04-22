import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, (task, ""))
        task_entry.delete(0, tk.END)
        save_tasks()

def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        task_listbox.delete(task_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def toggle_task_completion():
    try:
        task_index = task_listbox.curselection()[0]
        task_item = task_listbox.get(task_index)
        if isinstance(task_item, tuple):
            task, completed = task_item
            task_listbox.delete(task_index)
            if completed == "":
                completed = "Done"
            else:
                completed = ""
            task_listbox.insert(task_index, (task, completed))
            save_tasks()
        else:
            messagebox.showwarning("Warning", "This task is already marked as completed.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to toggle completion.")

def save_tasks():
    with open("D:\\Code Playground\\Projects\\Projects\\To Do app\\tasks.txt", "w") as f:
        for i in range(task_listbox.size()):
            task_item = task_listbox.get(i)
            if isinstance(task_item, tuple):
                task, completed = task_item
                f.write(task + "|" + completed + "\n")

def load_tasks():
    try:
        with open("D:\\Code Playground\\Projects\\Projects\\To Do app\\tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                task_data = task.strip().split("|")
                task = task_data[0]
                completed = task_data[1] if len(task_data) > 1 else ""
                task_listbox.insert(tk.END, (task, completed))
    except FileNotFoundError:
        return
    except IndexError:
        return

def on_closing():
    save_tasks()
    root.destroy()

root = tk.Tk()
root.title("To-Do List App")

# Styling
root.geometry("490x425")
root.maxsize(490,425)
root.minsize(490,425)
root.option_add("*Font", "Arial 12")
root.option_add("*Listbox*Font", "Arial 12")
root.option_add("*Button*Font", "Arial 12")

root.configure(bg="blueviolet")
root.tk_setPalette(background="#f0f0f0", foreground="black", activeBackground="#dddddd", activeForeground="white")

task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=2, padx=10, pady=10, sticky="W")

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=1, column=0, padx=10, pady=10, sticky="W")

toggle_button = tk.Button(root, text="Toggle Completion", command=toggle_task_completion)
toggle_button.grid(row=1, column=1, padx=10, pady=10, sticky="W")

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

load_tasks()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
