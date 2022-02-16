def turn_right():
    for n in range(3):
        turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
