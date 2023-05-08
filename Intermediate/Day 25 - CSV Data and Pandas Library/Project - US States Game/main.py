import turtle
import pandas
#Requirements
#input window will update with the # of states guessed correctly out of 50, will start at 0 and increment with every state
#when a state is guessed, check if it is among available states left
#if correct, write the state's name at the corresponding coordinate and remove it from available list

# Extract states from .csv file and make a dataframe
state_data = pandas.read_csv("Intermediate\Day 25 - CSV Data and Pandas Library\Project - US States Game\states.csv")
state_df = pandas.DataFrame(state_data)

# Convert all states to lower-case, we'll convert the user's guess to lower case so it will work even if user enters as all-caps
state_df['state'] = state_df['state'].str.lower()

# Dataframe is ready to go
# Turtle UI configurations
screen = turtle.Screen()
screen.title("U.S. States Game")
background_image = "Intermediate\Day 25 - CSV Data and Pandas Library\Project - US States Game\states_img.gif"
screen.addshape(background_image)
turtle.shape(background_image)
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

# Game configurations
list_of_remaining_states = state_df["state"].to_list()
correct_guesses = 0

# Initiate game, game will continue until user guesses all 50
while correct_guesses < 50:
    # Prompt user to input a state name, default will advise to Guess the State, subsequent attempts will keep track of progress
    if correct_guesses == 0:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").lower()
    else:
        answer_state = screen.textinput(title=f"{correct_guesses}/50 correct", prompt="What's another state's name?").lower()

    # Check if guess is in list of remaining states. If so, add one to tracker and remove state from the list
    if answer_state in list_of_remaining_states:
        correct_guesses += 1
        list_of_remaining_states.remove(answer_state)
        state_row = state_df[state_df["state"] == answer_state]

        pen.goto(x=int(state_row["x"]), y=int(state_row["y"]))
        pen.write(f"{answer_state.title()}", align="left", font=("Arial", 8, "normal"))

pen.goto(x=-250, y=300)
pen.write("Congratulations! You did it!",align="left", font=("Arial", 30, "normal"))



screen.mainloop()