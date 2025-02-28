from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
#  Loading the data
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("german_words.csv")
to_learn = data.to_dict(orient="records")
new_word = {}

# ---------------------------- Card Functions ------------------------------- #
def new_card():
    global new_word, turn_timer
    window.after_cancel(turn_timer)
    new_word = random.choice(to_learn)
    canvas.itemconfig(language_text, text="German", fill="black")
    canvas.itemconfig(word_text, text=new_word["German"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    turn_timer = window.after(4000, func=turn_card)


def turn_card():
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=new_word["English"], fill="white")


def delete_word():
    to_learn.remove(new_word)
    new_card()
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("words_to_learn.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
turn_timer = window.after(4000, func=turn_card)

# Canvas
canvas = Canvas(width=800, height=540, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 270, image=card_front)
language_text = canvas.create_text(400, 155, text="", font=("Ariel", 35, "italic"))
word_text = canvas.create_text(400, 300, text="", font=("Ariel", 55, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_img = PhotoImage(file="./images/right.png")
right_b = Button(image=right_img, highlightthickness=0, command=delete_word)
right_b.grid(column=1, row=1)
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_b = Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_b.grid(column=0, row=1)

new_card()

window.mainloop()
