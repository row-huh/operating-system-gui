import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess

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
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=master.quit)

        self.process_menu = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Process", menu=self.process_menu)
        self.process_menu.add_command(label="Create Process", command=self.create_process)
        self.process_menu.add_command(label="Display Processes", command=self.display_processes)
        self.process_menu.add_command(label="Kill Process", command=self.kill_process)

    def create_folder(self):
        folder_name = tk.simpledialog.askstring("Create Folder", "Enter folder name:")
        if folder_name:
            try:
                subprocess.run(["mkdir", folder_name])
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

    def create_process(self):
        # Implement process creation functionality here
        pass

    def display_processes(self):
        try:
            result = subprocess.run(["ps", "aux"], capture_output=True, text=True)
            processes_info = result.stdout
            messagebox.showinfo("Processes", processes_info)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to display processes: {e}")

    def kill_process(self):
        # Implement process killing functionality here
        pass

def main():
    root = tk.Tk()
    os = OperatingSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
