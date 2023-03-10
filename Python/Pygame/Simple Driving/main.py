from random import randint
import pgzrun

car = Actor("racecar")
car.pos = (700 / 2, 900 / 2)
SPEED = 4
MIN_SPEED = 1
MAX_SPEED = 6
track_count = 0
track_position = 250
track_width = 120
track_direction = False
track_left = []
track_right = []
game_status = 0

def draw():
    global game_status
    screen.fill((128, 128, 128))
    if game_status == 0:
        car.draw()
        for i in range(len(track_left)):
            track_left[i].draw()
            track_right[i].draw()
    if game_status == 1:
        screen.blit('rflag', (318, 268))
    if game_status == 2:
        screen.blit('cflag', (318, 268))

def update():
    global game_status, track_count, SPEED
    if game_status == 0:
        if keyboard.left:
            car.x -= 2
        if keyboard.right:
            car.x += 2
        if keyboard.up:
            SPEED += 1
            if SPEED > MAX_SPEED:
                SPEED = MAX_SPEED  # set to maximum speed if below it
        if keyboard.down:
            if SPEED > MIN_SPEED:
                SPEED -= 1
                for i in range(len(track_left)):
                    track_left[i].y -= SPEED
                    track_right[i].y -= SPEED  # set to minimum speed if below it
        update_track()
    if track_count > 200 :
        game_status = 2

def make_track():
    global track_count, track_left, track_right, track_position, track_width
    track_left.append(Actor("barrier", pos=(track_position - track_width, 0)))
    track_right.append(Actor("barrier", pos=(track_position + track_width, 0)))
    track_count += 1   

def update_track():
    global track_count, track_position, track_direction, track_width, game_status
    for i in range(len(track_left)):
        if car.colliderect(track_left[i]) or car.colliderect(track_right[i]):
            game_status = 1
        track_left[i].y += SPEED
        track_right[i].y += SPEED
    if track_left[-1].y > 32:
        if track_direction == False:
            track_position += 16
        else:
            track_position -= 16
        if randint(0, 4) == 1:
            track_direction = not track_direction
        if track_position > 700 - track_width:
            track_direction = True
        if track_position < track_width:
            track_direction = False
        make_track()

make_track()

pgzrun.go()