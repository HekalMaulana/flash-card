from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"


window = Tk()
window.title("Flash-Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Back Canvas
# canvas_back = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
# back_image = PhotoImage(file="./images/card_back.png")
# canvas_back.create_image(400, 263, image=back_image)
# canvas_back.grid(column=0, row=0, columnspan=2)

# Front Canvas
canvas_front = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="./images/card_front.png")
canvas_front.create_image(400, 263, image=front_image)
canvas_front.create_text(390, 150, text="English", font=(FONT_NAME, 40, "italic"))
canvas_front.create_text(390, 263, text="Word", font=(FONT_NAME, 60, "bold"))
canvas_front.grid(column=0, row=0, columnspan=2)

# Wrong button
wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)

# Right Button
right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0)
right_button.grid(column=1, row=1)



window.mainloop()
