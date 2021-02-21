import tkinter as tk
from messages import UIMessages

msg = UIMessages("es")

class FrameNewTask(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.populate()

    def populate(self):
        self.task_label = tk.Label(self, text=msg["task"], anchor=tk.W)
        self.due_label = tk.Label(self, text=msg["duedate"], anchor=tk.W)
        self.info_label = tk.Label(self, text=msg["info"], anchor=tk.W)

        self.task_label.grid(row=0, column=0, sticky=(tk.W, tk.E))
        self.due_label.grid(row=1, column=0, sticky=(tk.W, tk.E))
        self.info_label.grid(row=2, column=0, sticky=(tk.W, tk.E))

if __name__ == "__main__":
    root = tk.Tk()
    root.title(msg["apptitle"])
    frame = FrameNewTask(root)
    frame.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
    
