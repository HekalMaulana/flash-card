from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

random_word = None

# Read CSV File
try:
    data = pandas.read_csv("language-data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("language-data/english-indonesian.csv")
finally:
    old_dict = data.to_dict(orient="records")


def right_button_click():
    global old_dict
    old_dict.remove(random_word)

    new_data = pandas.DataFrame(old_dict)
    new_data.to_csv("./language-data/words_to_learn.csv", index=False)

    generate_random_word()


# Generate Random Word
def generate_random_word():
    # Generate random english word from new_dict
    global random_word, delay
    window.after_cancel(delay)
    random_word = random.choice(old_dict)
    english_word = random_word["English"]

    # Change canvas_front text to random english word
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=f"{english_word}", fill="black")
    canvas.itemconfig(card_image, image=old_image)

    delay = window.after(3000, flip_card)


# Flip The card after 3 sec
def flip_card():
    window.after_cancel(delay)

    # Generate random indonesian word from new_dict
    # random_indonesian_choice = random.choice(new_dict)
    indonesian_word = random_word["Indonesian"]

    # Change the card_image,card_title, and card_word
    canvas.itemconfig(card_image, image=new_image)
    canvas.itemconfig(card_title, text="Indonesian", fill="white")
    canvas.itemconfig(card_word, text=f"{indonesian_word}", fill="white")


window = Tk()
window.title("Flash-Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

delay = window.after(3000, flip_card)

# Front Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

# Create a background canvas from card_front_png
old_image = PhotoImage(file="./images/card_front.png")
new_image = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=old_image)

# Create text in canvas_front
card_title = canvas.create_text(390, 150, text="", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(390, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Wrong button
wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=generate_random_word)
wrong_button.grid(column=0, row=1)

# Right Button
right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=right_button_click)
right_button.grid(column=1, row=1)

generate_random_word()

window.mainloop()
