def turn_right():
    for n in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
