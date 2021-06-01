from tkinter import *
from PIL import ImageTk, Image
import game_2048

root = Tk()

root.iconbitmap('unnamed.ico')
root.title('2048')


bg = ImageTk.PhotoImage(Image.open("welcome.png"))

my_canvas = Canvas(root, width=780, height=550)
my_canvas.grid()

my_canvas.create_image(0, 0, image=bg, anchor=NW)

button1 = Button(root, text="New Game", fg="black", bg="#ddf0d0", padx=3,
                 pady=3, font=('Helvetica', '12', 'bold'), activebackground="#94d3c3", command=lambda: game_2048.mains(root)
                 )
button2 = Button(root, text="AI Mode", fg="black", bg="#ddf0d0",
                 padx=3, pady=3, font=('Helveica', '12', 'bold'), activebackground="#94d3c3")

button1_window = my_canvas.create_window(10, 10, anchor=NW, window=button1)
button2_window = my_canvas.create_window(120, 10, anchor=NW, window=button2)

FactsTexts = my_canvas.create_text(
    10, 400, anchor=NW, text="Fun Facts About 2048", font=(
        'Comic Sans MS', '20', 'bold'))

Facts_1 = my_canvas.create_text(
    10, 450, anchor=NW, text="- The highest score ever to be recorded in 2048 is 73,548 points.", font=(
        'Comic Sans MS', '15'))

Facts_2 = my_canvas.create_text(
    10, 480, anchor=NW, text="- 2048 is open source, meaning it can be edited and used by anyone.", font=(
        'Comic Sans MS', '15'))

Facts_3 = my_canvas.create_text(
    10, 510, anchor=NW, text="- 2048 received more that 4 million hits within a week of its launch.", font=(
        'Comic Sans MS', '15'))


root.mainloop()

# from tkinter import *
# from PIL import ImageTk, Image
# import game_2048

# root = Tk()

# root.iconbitmap('unnamed.ico')
# root.title('2048')


# bg = ImageTk.PhotoImage(Image.open("welcome.png"))

# my_canvas = Canvas(root, width=780, height=550)
# my_canvas.grid()

# my_canvas.create_image(0, 0, image=bg, anchor=NW)

# button1 = Button(root, text="New Game", fg="black", bg="#ddf0d0", padx=3,
#                  pady=3, font=('Helvetica', '12', 'bold'), activebackground="#94d3c3", command=lambda: game_2048.main()
#                  )
# button2 = Button(root, text="AI Mode", fg="black", bg="#ddf0d0",
#                  padx=3, pady=3, font=('Helveica', '12', 'bold'), activebackground="#94d3c3")

# button1_window = my_canvas.create_window(10, 10, anchor=NW, window=button1)
# button2_window = my_canvas.create_window(120, 10, anchor=NW, window=button2)

# FactsTexts = my_canvas.create_text(
#     10, 400, anchor=NW, text="Fun Facts About 2048", font=(
#         'Comic Sans MS', '20', 'bold'))

# Facts_1 = my_canvas.create_text(
#     10, 450, anchor=NW, text="- The highest score ever to be recorded in 2048 is 73,000 points.", font=(
#         'Comic Sans MS', '15'))

# Facts_2 = my_canvas.create_text(
#     10, 480, anchor=NW, text="- 2048 is open source, meaning it can be edited and used by anyone.", font=(
#         'Comic Sans MS', '15'))

# Facts_3 = my_canvas.create_text(
#     10, 510, anchor=NW, text="- 2048 received more that 4 million hits within a week of its launch.", font=(
#         'Comic Sans MS', '15'))


# root.mainloop()


# from tkinter import *
# from PIL import ImageTk, Image
# import game_2048

# root = Tk()

# root.iconbitmap('unnamed.ico')
# root.title('2048')


# bg = ImageTk.PhotoImage(Image.open("welcome.png"))

# my_canvas = Canvas(root, width=780, height=550)
# my_canvas.grid()

# my_canvas.create_image(0, 0, image=bg, anchor=NW)

# button1 = Button(root, text="New Game", fg="black", bg="#ddf0d0", padx=3,
#                  pady=3, font=('Helvetica', '12', 'bold'), activebackground="#94d3c3", command=game_2048.main()
#                  )
# button2 = Button(root, text="AI Mode", fg="black", bg="#ddf0d0",
#                  padx=3, pady=3, font=('Helveica', '12', 'bold'), activebackground="#94d3c3")

# button1_window = my_canvas.create_window(10, 10, anchor=NW, window=button1)
# button2_window = my_canvas.create_window(120, 10, anchor=NW, window=button2)

# FactsTexts = my_canvas.create_text(
#     10, 400, anchor=NW, text="Fun Facts About 2048", font=(
#         'Comic Sans MS', '20', 'bold'))

# Facts_1 = my_canvas.create_text(
#     10, 450, anchor=NW, text="- The highest score ever to be recorded in 2048 is 73,000 points.", font=(
#         'Comic Sans MS', '15'))

# Facts_2 = my_canvas.create_text(
#     10, 480, anchor=NW, text="- 2048 is open source, meaning it can be edited and used by anyone.", font=(
#         'Comic Sans MS', '15'))

# Facts_3 = my_canvas.create_text(
#     10, 510, anchor=NW, text="- 2048 received more that 4 million hits within a week of its launch.", font=(
#         'Comic Sans MS', '15'))


# root.mainloop()


# from tkinter import *
# from PIL import ImageTk, Image
# import customtkinter

# root = Tk()
# root.iconbitmap('unnamed.ico')
# root.title('2048')


# bg = ImageTk.PhotoImage(Image.open("welcome.png"))
# new_game_btn = ImageTk.PhotoImage(Image.open("image_40.png"))

# my_canvas = Canvas(root, width=780, height=550)
# my_canvas.pack()
# my_canvas.create_image(0, 0, image=bg, anchor=NW)

# button1 = Button(root, image=new_game_btn, borderwidth=00, relief=FLAT)
# button1_window = my_canvas.create_window(0, 0, anchor=NW)
# button1.pack()
# root.mainloop()
# from tkinter import *
# from PIL import ImageTk, Image

# x_pos = 100
# y_pos = 100
# width = 100
# height = 100


# def callback(event):
#     print("Canvas clicked at", event.x, event.y)
#     if (event.x > x_pos and event.x < x_pos + width):
#         if(event.y > y_pos and event.y < y_pos + height):
#             print("The button was clicked (approximately).")


# root = Tk()
# root.iconbitmap('unnamed.ico')
# root.title('2048')

# bg = ImageTk.PhotoImage(Image.open("welcome.png"))
# new_game_btn = ImageTk.PhotoImage(Image.open("image_40.png"))

# my_canvas = Canvas(root, width=780, height=550)
# my_canvas.pack()
# my_canvas.create_image(0, 0, image=bg, anchor=NW)

# my_canvas.create_image(200, 100, image=new_game_btn, anchor=NW)
# my_canvas.bind("<Button-1>", callback)

# root.mainloop()
