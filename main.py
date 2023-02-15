import pandas as pd
import turtle
screen=turtle.Screen()
screen.title("U.S States Game")
image="/home/sameeranati/US States game/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
def get_mouse_click(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click)
game_on=True
i=1
correct=0
wrong=0
guessed_states=[]
states_to_learn=[]
while game_on:
    answer_state=screen.textinput(title=f"{i}/50 Guess the State",prompt="what's another state name?")
    answer_state=answer_state.title()
    data=pd.read_csv("/home/sameeranati/US States game/us-states-game-start//50_states.csv")
    all_states=data.state.to_list()
    
    # print(all_states)
    if answer_state in all_states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        guessed_states.append(answer_state)
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
        correct+=1
        
        i+=1
    if i==50:
        print(f"you answered {correct} correctly and {wrong} wrongly")
        game_on=False
    if answer_state!=all_states:
        i+=1
        wrong+=1
    if answer_state=="Exit":
        states_to_learn=[state for state in all_states if state not in guessed_states]
        # for states in all_states:
        #     if guessed_states not in all_states:
        #         states_to_learn.append(states)
        new_data=pd.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
                    
        break


