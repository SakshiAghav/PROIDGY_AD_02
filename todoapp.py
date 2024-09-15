import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # List to store tasks
        self.tasks = []

        # Create UI elements
        self.task_listbox = tk.Listbox(root, height=10, width=50, font=("Arial", 14))
        self.task_listbox.pack(pady=20)

        self.add_button = tk.Button(root, text="Add Task", width=12, font=("Arial", 12), command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.edit_button = tk.Button(root, text="Edit Task", width=12, font=("Arial", 12), command=self.edit_task)
        self.edit_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(root, text="Delete Task", width=12, font=("Arial", 12), command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=10)

    def add_task(self):
        task = simpledialog.askstring("Input", "Enter new task:")
        if task:
            self.tasks.append(task)
            self.update_task_listbox()

    def edit_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            selected_task = self.tasks[selected_task_index]
            new_task = simpledialog.askstring("Edit Task", f"Edit task '{selected_task}':")
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to edit.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
