import tkinter as tk
from tkinter import simpledialog, messagebox
import os


class OperatingSystem:
    def __init__(self, master):
        self.master = master
        master.title("GUI Operating System")

        self.main_menu = tk.Menu(master)
        master.config(menu=self.main_menu)

        # Create main menu options
        self.file_menu = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Create Folder", command=self.create_folder)
        self.file_menu.add_command(label="Create File", command=self.create_file)
        self.file_menu.add_command(label="Change File Rights", command=self.change_file_rights)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=master.quit)

        self.search_menu = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Search", menu=self.search_menu)
        self.search_menu.add_command(label="Search Files", command=self.search_files)

        self.process_menu = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Process", menu=self.process_menu)
        self.process_menu.add_command(label="Create Process", command=self.create_process)
        self.process_menu.add_command(label="Create Thread", command=self.create_thread)
        self.process_menu.add_command(label="Display Processes", command=self.display_processes)
        self.process_menu.add_command(label="Kill Process", command=self.kill_process)
        
        
        
        
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

    def change_file_rights(self):
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
        command = tk.simpledialog.askstring("Create Process", "Enter command to execute:")
        if command:
            try:
                subprocess.Popen(command, shell=True)
                messagebox.showinfo("Success", "Process created successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create process: {e}")

    def create_thread(self):
        thread_function = self.sort_array_asc
        thread = threading.Thread(target=thread_function)
        thread.start()
        messagebox.showinfo("Success", "Thread created successfully.")

    def sort_array_asc(self):
        # Example function to sort an array in ascending order
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        arr.sort()
        print("Sorted array:", arr)

    def display_processes(self):
        # ... (existing code for displaying processes)
        pass
    
    
    def kill_process(self):
        # Implement process killing functionality here
        pass


def main():
    root = tk.Tk()
    os = OperatingSystem(root)
    root.mainloop()


if __name__ == "__main__":
    main()
