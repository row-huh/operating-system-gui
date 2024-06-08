import os
import subprocess
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox
import psutil

#Main class
class MiniOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini OS")
        self.root.geometry("400x400")

        
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
        app_menu.add_command(label="Open Chrome", command=self.open_chrome)
        app_menu.add_command(label="Open Notepad", command=self.open_notepad)


        program_menu = tk.Menu(menu)
        menu.add_cascade(label="Programs", menu=program_menu)
        program_menu.add_command(label="Write Program", command=self.write_program)
        program_menu.add_command(label="Execute Program", command=self.execute_program)
        program_menu.add_command(label="Delete Program", command=self.delete_program)
        
                # Adding submenu for sharing data between processes
        share_data_menu = tk.Menu(process_menu)
        process_menu.add_cascade(label="Share Data Between Processes", menu=share_data_menu)
        share_data_menu.add_command(label="Select Process1", command=self.select_process1)
        share_data_menu.add_command(label="Select Process2", command=self.select_process2)
        share_data_menu.add_command(label="Link Processes", command=self.link_processes)


# 1. It allows you to create folders and files. 
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

#2. It allows you to change rights of your files. 
    def change_rights(self):
        file_name = tk.simpledialog.askstring("Change File Rights", "Enter file name:")
        if file_name:
            try:
                permissions = int(simpledialog.askstring("Change File Rights", "Enter permissions (e.g., 755):"), 8)
                os.chmod(file_name, permissions)
                messagebox.showinfo("Success", f"File permissions changed successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to change file permissions: {e}")


# 3. It can help you in searching files. 
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


# 4. Allow to create processes and threads that perform specific tasks:
    def create_process(self):
        command = tk.simpledialog.askstring("Create Process", "Enter command to execute:")
        if command:
            try:
                subprocess.Popen(command, shell=True)
                messagebox.showinfo("Success", "Process created successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create process: {e}")

    # - create a process that sorts array in ascending order
    def sort_array_asc(self):
        # Example function to sort an array in ascending order
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        arr.sort()
        print("Sorted array:", arr)
    # - create multiple threads that may help in solving matrix operations etc


    def check_process(self, process, queue):
        if process.is_alive():
            self.root.after(100, self.check_process, process, queue)
        else:
            sorted_array = queue.get()
            messagebox.showinfo("Info", f"Process created and array sorted: {sorted_array}")


    def sort_array_process(self, array, queue):
        array.sort()
        queue.put(array)

    def create_threads(self):
        t1 = threading.Thread(target=self.sort_array_thread)
        t2 = threading.Thread(target=self.solve_matrix_thread)
        t1.start()
        t2.start()
        self.root.after(100, self.check_thread, t1, "Array sorted")
        self.root.after(100, self.check_thread, t2, "Matrix operation result: [[1, 2], [3, 4]]")

    def check_thread(self, thread, message):
        if thread.is_alive():
            self.root.after(100, self.check_thread, thread, message)
        else:
            messagebox.showinfo("Info", message)

    # dummy operations
    def sort_array_thread(self):
        array = [5, 2, 9, 1, 5, 6]
        sorted_array = sorted(array)
        return sorted_array

    def solve_matrix_thread(self):
        # Dummy matrix operation
        matrix = [[1, 2], [3, 4]]
        return matrix




# 5. Allow to display processes like a task manager in windows and should allow to kill any selected process
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




# 6 Allows to open applications
    def open_chrome(self):
        # Open Google Chrome
        subprocess.call('C:/Program Files/Google/Chrome/Application/chrome.exe')


    def open_notepad(self):
        subprocess.call('notepad.exe')
    
    def open_cmd(self):
        subprocess.call('cmd.exe')
    
    
    
# 7 Allows to share data between processes

       # Variables to store the selected processes
    def select_process1(self):
        self.process1_command = simpledialog.askstring("Select Process1", "Enter command for Process1:")
        if self.process1_command:
            messagebox.showinfo("Info", f"Process1 selected: {self.process1_command}")

    def select_process2(self):
        self.process2_command = simpledialog.askstring("Select Process2", "Enter command for Process2:")
        if self.process2_command:
            messagebox.showinfo("Info", f"Process2 selected: {self.process2_command}")

    def link_processes(self):
        if hasattr(self, 'process1_command') and hasattr(self, 'process2_command'):
            output_file = "output1.txt"
            
            # Run process1
            process1 = subprocess.Popen(self.process1_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process1.communicate()
            
            if process1.returncode == 0:
                with open(output_file, 'w') as f:
                    f.write(stdout.decode())    
            else:
                messagebox.showerror("Error", f"Process 1 failed: {stderr.decode()}")
                return
            
            # Ensure file is written before starting process2
            if os.path.exists(output_file):
                # Run process2
                process2 = subprocess.Popen(f"{self.process2_command} {output_file}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process2.communicate()
                
                if process2.returncode == 0:
                    messagebox.showinfo("Info", f"Process 2 completed successfully: {stdout.decode()}")
                else:
                    messagebox.showerror("Error", f"Process 2 failed: {stderr.decode()}")
            else:
                messagebox.showerror("Error", "Output file not created by Process 1")
        else:
            messagebox.showerror("Error", "Please select both Process 1 and Process 2")
            



# 8 Allows to write python programs, provide options to execute and delete
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
