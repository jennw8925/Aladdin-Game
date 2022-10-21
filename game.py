
import gamebox
import pygame
import random

screen_width = 800
screen_height = 600
camera = gamebox.Camera(screen_width, screen_height)

# image citations
# https://freepngimg.com/thumb/disney/35990-3-aladdin-clipart.png
# https://www.pinclipart.com/picdir/middle/552-5529465_jafar-clipart-png-download.png
# https://images.pexels.com/photos/1509582/pexels-photo-1509582.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=627&w=1200
# https://toppng.com/uploads/preview/old-magic-lamp-genie-lamp-clipart-11562929502vylr65mr8l.png
# https://upload.wikimedia.org/wikipedia/en/0/0c/The_Genie_Aladdin.png
# https://pngset.com/images/star-clipart-gold-glitter-gold-star-clipart-symbol-star-symbol-transparent-png-2600158.png

aladdin = gamebox.from_image(25, 100, 'Images/aladdin.png')
aladdin.scale_by(0.27)
desert = gamebox.from_image(400, 300, 'Images/desert.jpeg')
jafar = gamebox.from_image(300, 300, 'Images/jafar.png')
jafar.scale_by(0.1)
genie = gamebox.from_image(400, 360, 'Images/genie.png')
genie.scale_by(0.3)


obstacles = [gamebox.from_color(20, -20, 'beige', 10, 130), gamebox.from_color(140, 130, 'beige', 60, 10),
             gamebox.from_color(0, 47, 'beige', 50, 10), gamebox.from_color(420, 45, 'beige', 650, 10),
             gamebox.from_color(250, 90, 'beige', 10, 80), gamebox.from_color(550, 90, 'beige', 10, 80),
             gamebox.from_color(750, 200, 'beige', 10, 320), gamebox.from_color(750, 510, 'beige', 10, 120),
             gamebox.from_color(775, 360, 'beige', 60, 10), gamebox.from_color(775, 450, 'beige', 60, 10),
             gamebox.from_color(390, 570, 'beige', 730, 10), gamebox.from_color(30, 360, 'beige', 10, 420),
             gamebox.from_color(110, 225, 'beige', 10, 60), gamebox.from_color(155, 255, 'beige', 100, 10),
             gamebox.from_color(400, 130, 'beige', 100, 10), gamebox.from_color(650, 130, 'beige', 60, 10),
             gamebox.from_color(670, 225, 'beige', 10, 60), gamebox.from_color(625, 255, 'beige', 100, 10),
             gamebox.from_color(400, 250, 'beige', 200, 10), gamebox.from_color(400, 220, 'beige', 10, 60),
             gamebox.from_color(100, 0, 'beige', 10, 100), gamebox.from_color(0, 145, 'beige', 70, 10),
             gamebox.from_color(190, 400, 'beige', 140, 10), gamebox.from_color(190, 360, 'beige', 10, 85),
             gamebox.from_color(600, 400, 'beige', 140, 10), gamebox.from_color(600, 360, 'beige', 10, 85),
             gamebox.from_color(245, 480, 'beige', 140, 10), gamebox.from_color(535, 480, 'beige', 140, 10),
             gamebox.from_color(395, 525, 'beige', 10, 100), gamebox.from_color(105, 515, 'beige', 10, 100),
             gamebox.from_color(675, 515, 'beige', 10, 100)]

instructions = [gamebox.from_text(400, 100, 'Aladdin is trying to complete a mission. He wants to collect lamps '
                                            'in order to free the Genie and be with Jasmine ', 20, 'black'),
                gamebox.from_text(400, 125, '–the princess he loves. However, the evil sorcerer Jafar, who wants '
                                            'to stop Aladdin from obtaining the lamps, chases ', 20, 'black'),
                gamebox.from_text(400, 150, 'after him in a desert maze. The goal of the game is for the first '
                                            'player (Aladdin) to collect all the lamps scattered ', 20, 'black'),
                gamebox.from_text(400, 175, 'throughout the desert maze before the second player (Jafar) catches '
                                            'up to him three times as the player has three ', 20, 'black'),
                gamebox.from_text(400, 200, 'wishes/lives. Because Aladdin\'s magic carpet often gets snagged '
                                            'throughout the maze, the genie granted Aladdin', 20, 'black'),
                gamebox.from_text(400, 225, 'an advantage by allowing him to travel through portals on the left '
                                            'and right to escape Jafar. Can Aladdin accomplish ', 20, 'black'),
                gamebox.from_text(400, 250, 'his goal? Or will Jafar carry out evil deeds? It\'s up to you!', 20,
                                            'black'),
                gamebox.from_text(400, 325, 'INSTRUCTIONS', 40, 'black', bold=True),
                gamebox.from_text(400, 375, 'This is a two player game:', 20, 'black'),
                gamebox.from_text(400, 400, 'Player 1 is Aladdin and uses the up, down, left, right keys '
                                            'for movement', 20, 'black'),
                gamebox.from_text(400, 425, 'Player 2 is Jafar and uses the W (up), S (down), A (left), D '
                                            '(right) keys for movement', 20, 'black'),
                gamebox.from_text(400, 450, 'Press the space bar to begin. Good luck!', 20, 'black')]


# Global variables
lamps = []
game_on = False
instructions_on = True
num_lives = 3


def draw_instructions():
    """
    This function writes the instructions screen with a description of the game and how to play it.
    :return: N/A
    """
    global instructions_on, instructions
    if instructions_on is True:
        box = gamebox.from_color(400, 300, 'beige', 800, 600)
        camera.draw(box)
        for instruction in instructions:
            camera.draw(instruction)


def start_game(keys):
    """
    This function allows the players to start the game with the space bar.
    :param keys: set of computer keys
    :return: N/A
    """
    global num_lives, game_on, instructions_on
    if pygame.K_SPACE in keys:
        game_on = True
        instructions_on = False


def create_lamps():
    """
    This function creates the lamps that fill the maze.
    :return: N/A
    """
    global lamps
    # methodology: put different x positions and use a for loop to create lamps with the same y position to populate a
    # row, then append it to global list lamps
    row1_x = [85, 150, 210, 296, 355, 410, 460, 510, 590, 650, 710]
    for i in range(11):
        new_lamp = gamebox.from_image(row1_x[i], 100, 'Images/lamp.png')
        new_lamp.scale_by(0.1)
        lamps.append(new_lamp)
    row2_x = [75, 150, 210, 270, 330, 390, 450, 510, 570, 630, 690]
    for i in range(11):
        new_lamp = gamebox.from_image(row2_x[i], 160, 'Images/lamp.png')
        new_lamp.scale_by(0.1)
        lamps.append(new_lamp)
    row3_x = [75, 160, 220, 280, 340, 450, 510, 570, 630, 710]
    for i in range(10):
        new_lamp = gamebox.from_image(row3_x[i], 220, 'Images/lamp.png')
        new_lamp.scale_by(0.1)
        lamps.append(new_lamp)
    row4_x = [75, 145, 205, 270, 330, 390, 450, 510, 570, 630, 690]
    for i in range(11):
        new_lamp = gamebox.from_image(row4_x[i], 285, 'Images/lamp.png')
        new_lamp.scale_by(0.1)
        lamps.append(new_lamp)
    row5_x = [75, 145, 240, 305, 490, 555, 645, 710]
    for i in range(8):
        new_lamp = gamebox.from_image(row5_x[i], 345, 'Images/lamp.png')
        new_lamp.scale_by(0.1)
        lamps.append(new_lamp)
    row6_x = [75, 150, 210, 270, 330, 390, 450, 510, 570, 630, 690]
    for i in range(11):
        new_lamp = gamebox.from_image(row6_x[i], 435, 'Images/lamp.png')
        new_lamp.scale_by(0.1)
        lamps.append(new_lamp)
    row7_x = [75, 145, 358, 438, 638, 715]
    for i in range(6):
        new_lamp = gamebox.from_image(row7_x[i], 485, 'Images/lamp.png')
        new_lamp.scale_by(0.1)
        lamps.append(new_lamp)
    row8_x = [75, 160, 220, 280, 340, 450, 510, 570, 630, 710]
    for i in range(10):
        new_lamp = gamebox.from_image(row8_x[i], 545, 'Images/lamp.png')
        new_lamp.scale_by(0.1)
        lamps.append(new_lamp)
    row9_x = [75, 320, 470, 700]
    for i in range(4):
        new_lamp = gamebox.from_image(row9_x[i], 390, 'Images/lamp.png')
        new_lamp.scale_by(0.1)
        lamps.append(new_lamp)


def restart(keys):
    """
    This function re-initiates all the variables to start over the game.
    :param keys: set of computer keys
    :return: N/A
    """
    global num_lives, instructions_on, lamps
    if pygame.K_TAB in keys and game_on is False:  # tab key restarts the game
        instructions_on = True
        aladdin.x = 25  # aladdin is placed in the top left corner
        aladdin.y = 100
        num_lives = 3  # the health bar is restored to 3 stars
        for lamp in lamps:
            lamps.remove(lamp)
        create_lamps()  # create a new set of lamps


def game_control():
    """
    This function codes for when player one wins or loses the game and the message displayed on the screen.
    :return: N/A
    """
    global game_on, lamps
    if num_lives == 0:  # if player one (aladdin) runs out of lives, they lose and player two (jafar wins)
        camera.draw(gamebox.from_color(400, 300, 'beige', 500, 300))
        camera.draw(gamebox.from_text(400, 280, 'Jafar Wins!', 60, 'black'))
        camera.draw(gamebox.from_text(400, 330, 'Press [tab] to start over', 20, 'black'))
        game_on = False
    if num_lives > 0 and len(lamps) == 0:  # if player one still has lives, and they collect all the lamps, they win
        # and player 2 loses.
        camera.draw(gamebox.from_color(400, 300, 'beige', 500, 300))
        camera.draw(gamebox.from_text(400, 280, 'Aladdin Wins!', 60, 'black'))
        camera.draw(gamebox.from_text(400, 330, 'Press [tab] to start over', 20, 'black'))
        game_on = False


def draw_lives():
    """
    This function draws the lives in the top right corner of the screen.
    :return: N/A
    """
    global num_lives
    x_loc = camera.right - 20  # code from walker_jump.py example given
    y_loc = camera.top + 20
    lives = []
    lives_text = gamebox.from_text(640, 20, 'Lives:', 30, 'beige')
    camera.draw(lives_text)
    for num in range(num_lives):
        life = gamebox.from_image(x_loc - num * 40, y_loc, 'Images/star.png')
        life.scale_by(0.07)
        lives.append(life)
    for life in lives:
        camera.draw(life)


def get_lamp():
    """
    This function codes for the disappearance of a lamp when Aladdin touches it.
    :return: N/A
    """
    global lamps
    for lamp in lamps:
        if aladdin.touches(lamp):
            lamps.remove(lamp)


def off_bounds():
    """
    This function allows Aladdin to use the portals that go off the sides of the screen to transport to another side.
    :return: N/A
    """
    if aladdin.y < 0:  # if aladdin goes off top opening
        aladdin.y = 400
        aladdin.x = 800
    if aladdin.x < 0:  # if aladdin goes off left opening
        aladdin.y = 400
        aladdin.x = 800
    if aladdin.x > 800:  # if aladdin goes off right opening
        aladdin.x = 0
        aladdin.y = 95

    if jafar.y < 0:  # prevent jafar from moving through top opening
        jafar.y = 0
    if jafar.x < 0:  # prevent jafar from moving through left opening
        jafar.x = 0
    if jafar.x > 800:  # prevent jafar from moving through right opening
        jafar.x = 800


def transport():
    """
    This function codes for Aladdin and Jafar moving to different locations after touching so that player one does not
    lose all their lives after just touching player two once.
    :return: N/A
    """
    global num_lives
    if aladdin.touches(jafar):
        num_lives -= 1
        random_loc = [[130, 200], [300, 50], [700, 80], [400, 500], [500, 100], [50, 400], [660, 550]]  # random list
        # of locations
        random_num = random.randint(0, 3)  # aladdin and jafar chose from different ranges of locations to avoid overlap
        random_num2 = random.randint(4, 6)
        aladdin_loc = random_loc[random_num]  # chose a random location from the range so the location is somewhat
        # random
        jafar_loc = random_loc[random_num2]
        jafar.x = aladdin_loc[0]
        jafar.y = aladdin_loc[1]
        aladdin.x = jafar_loc[0]
        aladdin.y = jafar_loc[1]


def tick(keys):
    """
    This function allows for user control of Aladdin, draws maze and various characters. It also contains the functions
    to operate the game.
    :param keys: set of computer keys
    :return: N/A
    """
    global aladdin, num_lives, lamps

    if game_on is True:
        if pygame.K_UP in keys:
            aladdin.y -= 5
        if pygame.K_DOWN in keys:
            aladdin.y += 5
        if pygame.K_RIGHT in keys:
            aladdin.x += 5
        if pygame.K_LEFT in keys:
            aladdin.x -= 5
        if pygame.K_w in keys:
            jafar.y -= 4
        if pygame.K_d in keys:
            jafar.x += 4
        if pygame.K_s in keys:
            jafar.y += 4
        if pygame.K_a in keys:
            jafar.x -= 4

    start_game(keys)
    restart(keys)
    camera.draw(desert)
    for obstacle in obstacles:
        aladdin.move_to_stop_overlapping(obstacle)
        jafar.move_to_stop_overlapping(obstacle)
        camera.draw(obstacle)
    get_lamp()
    for lamp in lamps:
        camera.draw(lamp)
    camera.draw(aladdin)
    camera.draw(jafar)
    jafar.move_to_stop_overlapping(genie)
    transport()
    draw_lives()
    camera.draw(genie)
    aladdin.move_to_stop_overlapping(genie)
    off_bounds()
    game_control()
    draw_instructions()
    camera.display()


create_lamps()
ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)
