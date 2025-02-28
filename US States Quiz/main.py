import turtle
import pandas

# Setting up the screen with image
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Loading a file
data = pandas.read_csv("50_states.csv")
states_list = data.state.tolist()
correct_answers = []
title = "Guess the State"

# Course of the game
while len(correct_answers) < 50:
    # Guessing
    answer_state = screen.textinput(title=title, prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # Showing states to learn
        missing_states = [state for state in states_list if state not in correct_answers]
        data = pandas.Series(missing_states)
        data.to_csv("States_to_learn.csv")
        break
    if answer_state in states_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        # Writing  states in the correct places
        data_state = data[data.state == answer_state]
        t.goto(int(data_state.x.iloc[0]), int(data_state.y.iloc[0]))
        t.write(data_state.state.item())

        # Adding correct answer to the list
        correct_answers.append(answer_state)

        # Updating the title
        title = f"{len(correct_answers)}/50 States Correct"

screen.exitonclick()
