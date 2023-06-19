from karel.stanfordkarel import *

def main():
    drawrd()
    down()
    set()
    drawld()
def drawrd():
    put_beeper()
    while front_is_clear():
        move()
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
        put_beeper()
def drawld():
    put_beeper()
    while front_is_clear():
        move()
        turn_left()
        turn_left()
        turn_left()
        move()
        turn_left()
        put_beeper()
def down():
    turn_left()
    turn_left()
    turn_left()
    while front_is_clear():
        move()
        
def set():
    turn_left()
    turn_left()
    turn_left()
    
# don't change this code
if __name__ == '__main__':
    main()