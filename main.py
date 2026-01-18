import pandas
import turtle

data=pandas.read_csv("50_states.csv")
screen=turtle.Screen()
screen.screensize(600,600)
screen.bgpic("blank_states_img.gif")
draw=turtle.Turtle(visible=False)
print(data.state)
game_not_over=True

guessed=[]
state_list=data["state"].to_list()
while(game_not_over):

    guess=screen.textinput(title=f"{len(guessed)}/50",prompt="Enter a US state:")
    if(guess is None):
        game_not_over=False
    else:
        guess=guess.title()
    if(guess=="Stop" or len(guessed)==50):
        game_not_over=False
        break
    
    if((guess in state_list) and (guess not in guessed)):
        guessed.append(guess)
        x_coor=data[data["state"]==guess].x.item()
        y_coor=data[data["state"]==guess].y.item()
        draw.teleport(x_coor,y_coor)
        draw.write(guess,font=("Arial",8,"normal"),align="center")


    
screen.mainloop()


