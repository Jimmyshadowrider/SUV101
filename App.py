import tkinter as tk
import tkinter.font as tkFont
from prog import *

# Set-up
root = tk.Tk()
root.title('Automate Science Calculator')
root.geometry('1260x960')
canvas = tk.Canvas(root,width=90,height=100)
canvas.pack(side="left", fill="both", expand=True)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
frame = tk.Frame(canvas)
canvas.create_window((550,0),window=frame, anchor='nw')
canvas.configure(yscrollcommand=scrollbar.set)


#Font
f1 = tkFont.Font(family = 'Impact', size = 25)
f2 = tkFont.Font(family='Aerial', size=15)
f3 = tkFont.Font(family='Aerial',size = 20)

# Add elements
l1 = tk.Label(frame, text = 'Choose your formula', font= f1)
b1 = tk.Button(frame, text='Movement formula 1', font=f3)
close = tk.Button(frame, text='Close', font=f2, command=root.destroy)




# Adding to window and run
l1.pack()
close.pack(padx=20,pady=20)
root.mainloop()
