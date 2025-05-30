from tkinter import *
window = Tk()
window.geometry("400x300")

# Use a frame for grid-managed widgets
form_frame = Frame(window)
form_frame.pack(pady=20)

Label(form_frame, text='First Name').grid(row=0, column=0)
Label(form_frame, text='Last Name').grid(row=1, column=0)
e1 = Entry(form_frame)
e2 = Entry(form_frame)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

label = Label(window, text="Hello, Tkinter!", font=("Arial", 24))
label.pack(pady=10)

button = Button(window, text="Click Me", command=lambda: print("Button Clicked!"), width=20, height=2)
button.pack(pady=10)

window.mainloop()
