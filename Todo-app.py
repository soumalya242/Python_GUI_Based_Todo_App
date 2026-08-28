import tkinter as tk
import json

#create main window
window = tk.Tk()
window.title("My To-Do List")
window.geometry("400x500")

#tittle level
title_label = tk.Label(window, text="My To-Do List", font=("verdana", 16, "bold"))
title_label.pack(pady=10)

#Entry box for typing new task
task_entry = tk.Entry(window, width=30, font=("verdana", 12))
task_entry.pack(pady=5)


#list 
task =[]

#file save to json
FILENAME = "task.json"

def save_task():
    with open(FILENAME, "w") as f:
        json.dump(task, f)


def load_task():
    global task
    try:
        with open(FILENAME, "r") as f:
            content = f.read().strip()
            if content:
                task = json.loads(content)
            else:
                task = []
    except FileNotFoundError:
        task = []

    for t in task:
        display_text = t["task"]
        if t["done"]:
            display_text = "[x] " + display_text
        task_listbox.insert(tk.END, display_text)


#add task
def add_task():
    task_text = task_entry.get()
    if task_text.strip() !="":
        task.append({"task": task_text, "done":False})
        task_listbox.insert(tk.END, task_text)
        task_entry.delete(0, tk.END)
        save_task()


#complete task
def complete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        task[index]["done"] = True
        task_listbox.delete(index)
        task_listbox.insert(index, "[x] " + task[index]["task"])
        save_task()


#delete task
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        task.pop(index)
        task_listbox.delete(index)
        save_task()


#all clear
def clear_all():
    global task
    task = []
    task_listbox.delete(0, tk.END)
    save_task()


# Add button
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=5)

task_entry.bind("<Return>", lambda event: add_task())

#delete button
delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

#complete button
complete_button = tk.Button(window, text="Mark Complete", command=complete_task)
complete_button.pack(pady=5)

#clear button
clear_button = tk.Button(window, text="All Clear", command=clear_all)
clear_button.pack(pady=5)

#list to show the task
task_listbox = tk.Listbox(window, width=40, height=15, font=("verdada", 11))
task_listbox.pack(pady=10)

#call load
load_task()
#start window
window.mainloop()