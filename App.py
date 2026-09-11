import tkinter as tk
from formula import *

# Set-up
# root = tk.Tk()
# root.title('Automate Science Calculator')
# root.geometry('350x400')
# canvas = tk.Canvas(root,width=90,height=100)
# canvas.pack(side="left", fill="both", expand=True)
# scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
# scrollbar.pack(side="right", fill="y")
# frame = tk.Frame(canvas)
# canvas.create_window((25,0),window=frame, anchor='nw')
# canvas.configure(yscrollcommand=scrollbar.set)




class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Automate Science Calculator")
        self.geometry("400x300")
        # screen_width = self.winfo_screenwidth()
        # screen_height = self.winfo_screenheight()
        # x = (screen_width - self.winfo_reqwidth()) // 2
        # y = (screen_height - self.winfo_reqheight()) // 2
        # self.geometry(f"+{x}+{y}")

        
        # Container to hold all stacked frames
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Initialize both pages
        for PageClass in (HomePage, Move1,Move2):
            frame = PageClass(container, self)
            self.frames[PageClass] = frame
            # Put all frames in the same grid cell (stacking them)
            frame.grid(row=0, column=0, sticky="nsew")

        # Show initial page
        self.show_frame(HomePage)

    def show_frame(self, page_class):
        """Bring the specified frame to the top."""
        frame = self.frames[page_class]
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        canvas = tk.Canvas(self,width=90,height=100)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        frame = tk.Frame(canvas)
        canvas.create_window((0,0),window=frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        label = tk.Label(frame, text="Home Page", font=("Arial", 10))
        label.pack(pady=20)
        
        
        btn1 = tk.Button(
            frame, 
            text="v = u + a·t formula", 
            font = ("Arial", 20),
            command=lambda: controller.show_frame(Move1)
        )
        btn1.pack()

        btn2 = tk.Button(
            frame, 
            text="s = ((u + v) / 2) · t formula", 
            font= ("Arial", 20),
            command=lambda: controller.show_frame(Move2)
        )
        btn2.pack()

   

class Move1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="v = u + a·t", font=("Impact", 10))
        label.pack(pady=20)
        
        btn = tk.Button(
            self, 
            text="Back", 
            command=lambda: controller.show_frame(HomePage)
        )
        btn.pack()


class Move2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="s = ((u + v) / 2) · t", font=("Impact", 16))
        label.pack(pady=20)
        
        btn = tk.Button(
            self, 
            text="Back", 
            command=lambda: controller.show_frame(HomePage)
        )
        btn.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
