import os
import subprocess
import threading
import multiprocessing
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import psutil

class MiniOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini OS")
        
        self.create_widgets()

    def create_widgets(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Create Folder", command=self.create_folder)
        file_menu.add_command(label="Create File", command=self.create_file)
        file_menu.add_command(label="Change Rights", command=self.change_rights)
        file_menu.add_command(label="Search Files", command=self.search_files)

        process_menu = tk.Menu(menu)
        menu.add_cascade(label="Processes", menu=process_menu)
        process_menu.add_command(label="Create Process", command=self.create_process)
        process_menu.add_command(label="Create Threads", command=self.create_threads)
        process_menu.add_command(label="Task Manager", command=self.task_manager)

        app_menu = tk.Menu(menu)
        menu.add_cascade(label="Applications", menu=app_menu)
        app_menu.add_command(label="Open Firefox", command=self.open_firefox)

        program_menu = tk.Menu(menu)
        menu.add_cascade(label="Programs", menu=program_menu)
        program_menu.add_command(label="Write Program", command=self.write_program)
        program_menu.add_command(label="Execute Program", command=self.execute_program)
        program_menu.add_command(label="Delete Program", command=self.delete_program)

    def create_folder(self):
            folder_name = tk.simpledialog.askstring("Create Folder", "Enter folder name:")
            if folder_name:
                try:
                    os.mkdir(folder_name)
                    messagebox.showinfo("Success", f"Folder '{folder_name}' created successfully.")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to create folder: {e}")

    def create_file(self):
        file_name = tk.simpledialog.askstring("Create File", "Enter file name:")
        if file_name:
            try:
                with open(file_name, "w") as file:
                    pass  # Create an empty file
                messagebox.showinfo("Success", f"File '{file_name}' created successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create file: {e}")

    def change_rights(self):
        file_name = tk.simpledialog.askstring("Change File Rights", "Enter file name:")
        if file_name:
            try:
                permissions = int(simpledialog.askstring("Change File Rights", "Enter permissions (e.g., 755):"), 8)
                os.chmod(file_name, permissions)
                messagebox.showinfo("Success", f"File permissions changed successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to change file permissions: {e}")


    def search_files(self):
        search_term = simpledialog.askstring("Search Files", "Enter file name (or part of it) to search:")
        if search_term:
            found_files = []
            for root, dirs, files in os.walk(os.getcwd()):
                for filename in files:
                    if search_term.lower() in filename.lower():
                        found_files.append(os.path.join(root, filename))

            if found_files:
                message = "\n".join(found_files)
                messagebox.showinfo("Search Results", f"Found files:\n{message}")
            else:
                messagebox.showinfo("Search Results", "No files found matching your criteria.")

    def create_process(self):
        array = [5, 2, 9, 1, 5, 6]
        p = multiprocessing.Process(target=sorted, args=(array,))
        p.start()
        p.join()
        messagebox.showinfo("Info", f"Process created and array sorted: {array}")

    def create_threads(self):
        def sort_array():
            array = [5, 2, 9, 1, 5, 6]
            sorted_array = sorted(array)
            messagebox.showinfo("Info", f"Thread: Array sorted: {sorted_array}")

        def solve_matrix():
            # Dummy matrix operation
            matrix = [[1, 2], [3, 4]]
            messagebox.showinfo("Info", f"Thread: Matrix operation result: {matrix}")

        t1 = threading.Thread(target=sort_array)
        t2 = threading.Thread(target=solve_matrix)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    def task_manager(self):
        process_list = psutil.pids()
        task_window = tk.Toplevel(self.root)
        task_window.title("Task Manager")

        listbox = tk.Listbox(task_window)
        listbox.pack(fill=tk.BOTH, expand=1)

        for pid in process_list:
            p = psutil.Process(pid)
            listbox.insert(tk.END, f"{pid} - {p.name()}")

        kill_button = tk.Button(task_window, text="Kill Process", command=lambda: self.kill_process(listbox))
        kill_button.pack()

    def kill_process(self, listbox):
        selection = listbox.curselection()
        if selection:
            pid = int(listbox.get(selection[0]).split(" - ")[0])
            p = psutil.Process(pid)
            p.terminate()
            messagebox.showinfo("Info", f"Process {pid} terminated")

    def open_firefox(self):
        subprocess.Popen(['firefox'])

    def write_program(self):
        program_code = simpledialog.askstring("Input", "Enter Python code:")
        if program_code:
            with open('user_program.py', 'w') as f:
                f.write(program_code)
            messagebox.showinfo("Info", "Program saved successfully")

    def execute_program(self):
        subprocess.run(['python', 'user_program.py'])
        messagebox.showinfo("Info", "Program executed successfully")

    def delete_program(self):
        if os.path.exists('user_program.py'):
            os.remove('user_program.py')
            messagebox.showinfo("Info", "Program deleted successfully")
        else:
            messagebox.showwarning("Warning", "Program file not found")

if __name__ == "__main__":
    root = tk.Tk()
    app = MiniOS(root)
    root.mainloop()
