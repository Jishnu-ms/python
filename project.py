from tkinter import *
window=Tk()
window.geometry("400x300")
button=Button(window, text="Click Me", command=lambda: print("Button Clicked!"),width=20, height=5)
label=Label(window, text="Hello, Tkinter!", font=("Arial", 24))
label.pack()

button.pack()
window.mainloop()
