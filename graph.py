from email import message
import tkinter as tk


# def button_press(text = 'No Text to Display'):
#     print(text)

def writeLabel(display):
    if display:
        display = display
    else:
        display = 'No Text to Display'
    label1 = tk.Label(lower_frame, bg='white', text= display)
    label1.place(relwidth=1, relheight=1)

root = tk.Tk()

canvas = tk.Canvas(root, height=600, width= 900)
canvas.pack()

frame = tk.Frame(root, bg = '#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight= 0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Execute", font=40, bg='#008080' ,command=lambda: writeLabel(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame= tk.Frame(root, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.5, anchor='n')

# label1 = tk.Label(lower_frame, bg='white', text= lambda: lambda: button_press(entry.get()))
# label1.place(relwidth=1, relheight=1)

last_frame= tk.Frame(root, bd=5)
last_frame.place(relx=0.5, rely=0.8, relwidth=0.8, relheight=0.1, anchor='n')

button2 = tk.Button(last_frame, text="Exit", font=40, bg='#ff3300', command=root.destroy)
button2.place(relx=0.7, relheight=1, relwidth=0.3)

root.mainloop()
