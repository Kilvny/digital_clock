from tkinter import Tk, Label


window = Tk()
window.title('Digital clock')
window.geometry("600x300")

window.mainloop()

# window.configure(bg="black")

label = Label(window, text="WELCOME!",font=("Aria Black",78,'bold'), bg='steelblue',fg='white')
label.pack()
