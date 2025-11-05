import tkinter as tk  
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)#to correct blurry text and widgets
root = tk.Tk() 
bgcol="#19191a"
lbgcol="#737373"
root.configure(bg=bgcol)
root.title("Are you gay ?")
root.tk.call('tk', 'scaling', 2)
root.state('zoomed')
#===========================================================================
header=tk.Frame(root,bg=bgcol)
header.place(relx=0, rely=0, relwidth=1.0, relheight=0.1)
lb = tk.Label(header, text="Pyधुन ♬𝄞♬",font=("Segoe UI Symbol",22),anchor="center",bg=bgcol,fg="white") 
lb.pack(fill="x",pady=(10,0),padx=(10))
separator = tk.Frame(header,height=2,bg="#bfbfbf")
separator.pack(fill='x', padx=0, pady=5)

#================================================================

body=tk.Frame(root,bg=bgcol)
body.place(relx=0,rely=0.1,relheight=0.8,relwidth=1.0)

left_body=tk.Frame(body,bg=lbgcol,bd=2,relief="solid")
left_body.place(relx=0.0, rely=0, relwidth=0.2, relheight=1.0)
tk.Label(left_body,text="My Music",fg="white",bg=lbgcol,font=("Calibri",15)).pack(fill='x')
tk.Frame(left_body,height=2,bg="#bfbfbf").pack(fill='x',pady=5)

right_body=tk.Frame(body,bg=lbgcol,bd=2,relief="solid")
right_body.place(relx=0.2, rely=0, relwidth=0.8, relheight=1.0)
tk.Label(right_body,text="Queue",fg="white",bg=lbgcol,font=("Calibri",15)).pack(fill='x')
tk.Frame(right_body,height=2,bg="#bfbfbf").pack(fill='x',pady=5)

#================================================================

footer=tk.Frame(root,bg=bgcol)
footer.place(relx=0,rely=0.9,relheight=0.1,relwidth=1.0)
root.mainloop()
