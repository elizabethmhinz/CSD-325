import tkinter as tk
import tkinter.messagebox as msg
from tkinter import Menu

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else: 
            self.tasks = tasks

        self.tasks_canvas = tk.Canvas(self)
        
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient='vertical', command=self.tasks_canvas.yview)
        
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.title('Hinz To-Do App v2')
        self.geometry('300x400')

        self.create_menu()

        self.task_create = tk.Text(self.text_frame, height=3, bg='white', fg='black')

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0,0), window=self.tasks_frame, anchor='n')

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        todo1 = tk.Label(self.tasks_frame, text='--- Add Items Here ---  **Right Click Item to Delete**', bg='grey',fg='black', pady=10)
        todo1.bind('<Button-1>', self.remove_task)

        self.tasks.append(todo1)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        self.bind('<Return>', self.add_task)
        self.bind('<Configure>', self.on_frame_configure)
        self.bind_all('<MouseWheel>', self.mouse_scroll)
        self.bind_all('<Button-4>', self.mouse_scroll)
        self.bind_all('<Button-5>', self.mouse_scroll)
        self.tasks_canvas.bind('<Configure>', self.task_width)

        self.colour_schemes = [{'bg': 'cornflower blue', 'fg': 'black'}, {'bg': 'AntiqueWhite1', 'fg': 'black'}]

    def create_menu(self):
        menu_bar = Menu(self)
        self.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.exit_program)

        edit_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='Edit', menu=edit_menu)
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)

        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.about)

    def open_file(self):
        print("File > Open command clicked")

    def save_file(self):
        print("File > Save command clicked")

    def cut_text(self):
        print("Edit > Cut command clicked")

    def copy_text(self):
        print("Edit > Copy command clicked")

    def paste_text(self):
        print("Edit > Paste command clicked")

    def about(self):
        print("Help > About command clicked")

    def exit_program(self):
        """Exits the program."""
        self.destroy()

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0,tk.END).strip()
        
        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
                    
            self.set_task_colour(len(self.tasks), new_task)
                    
            new_task.bind('<Button-1>', self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)
                    
            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno('Really Delete?', 'Delete ' + task.cget('text') + '?'):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()
            

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)
    
    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)

        my_scheme_choice = self.colour_schemes[task_style_choice]

        task.configure(bg=my_scheme_choice['bg'])
        task.configure(fg=my_scheme_choice['fg'])
    
    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox('all'))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width = canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), 'units')
        else: 
            if event.num == 5:
                move = 1
            else:
                move = -1
            
            self.tasks_canvas.yview_scroll(move, 'units')
    def left_click(event):
        event.widget.configure(bg="green")

    def right_click(event):
        event.widget.configure(bg="red")
    
    root = tk.Tk()
    button = tk.Frame(root, width=20, height=20, background="gray")
    button.pack(padx=20, pady=20)

    button.bind("<Button-3>", right_click)

if __name__ == '__main__':
    todo = Todo()
    todo.mainloop()
                 