import pygame
import sys
import Gui_Project_Extra

pygame.init()

# Creating the display
display = pygame.display.set_mode((600, 600))
running = True
# Grid specifications
width = 100
height = 100

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
burnt_orange = (204, 85, 0)
green = (0, 255, 0)

# Font Setup
font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 14)
font3 = pygame.font.Font('freesansbold.ttf', 20)

# Starting screen
start_screen = pygame.image.load('tictactoe4.jpg')
start_screen = pygame.transform.scale(start_screen, (600, 600))

# Mouse
Mouse_0x, Mouse_0y = pygame.mouse.get_pos()
x = Mouse_0x
y = Mouse_0y

# X's & O's
Xready = True
Oready = False

x_icon = []
o_icon = []
x_iconx = []
x_icony = []
o_iconx = []
o_icony = []
max_x = 6
max_o = 5
for i in range(max_x):
    x_icon.append(pygame.image.load('close.png'))

for j in range(max_o):
    o_icon.append(pygame.image.load('o.png'))

# Text Box Setup
input_box = pygame.Rect(250, 200, 140, 40)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
text = ''
input_box1 = pygame.Rect(250, 300, 140, 40)
color_inactive1 = pygame.Color('lightskyblue3')
color_active1 = pygame.Color('dodgerblue2')
color1 = color_inactive
text1 = ''

# Box Update
click = False
update = False

# Box Check
box_1 = True
box_1x = False
box_1o = False
box_2 = True
box_2x = False
box_2o = False
box_3 = True
box_3x = False
box_3o = False
box_4 = True
box_4x = False
box_4o = False
box_5 = True
box_5x = False
box_5o = False
box_6 = True
box_6x = False
box_6o = False
box_7 = True
box_7x = False
box_7o = False
box_8 = True
box_8x = False
box_8o = False
box_9 = True
box_9x = False
box_9o = False


# Function that draws the grid lines
# def drawGrid():
# block_Size = 200  # Setting the size of the grid block
# for x in range(width):
# for y in range(height):
# rect = pygame.Rect(x * block_Size, y * block_Size, 200, 200)
# pygame.draw.rect(display, white, rect, 1)


def update0():
    block_Size = 200  # Setting the size of the grid block
    for x in range(width):
        for y in range(height):
            rect = pygame.Rect(x * block_Size, y * block_Size, 200, 200)
            pygame.draw.rect(display, white, rect, 1)
    if update == True:
        box()


def box():
    if c == 1:
        display.blit(x_icon[i], (x_iconx[0], x_icony[0]))
    elif c == 2:
        display.blit(x_icon[i], (x_iconx[0], x_icony[0]))
        display.blit(o_icon[j], (o_iconx[0], o_icony[0]))

    elif c == 3:
        display.blit(x_icon[i], (x_iconx[0], x_icony[0]))
        display.blit(o_icon[j], (o_iconx[0], o_icony[0]))
        display.blit(x_icon[i], (x_iconx[1], x_icony[1]))
    elif c == 4:
        display.blit(x_icon[i], (x_iconx[0], x_icony[0]))
        display.blit(o_icon[j], (o_iconx[0], o_icony[0]))
        display.blit(x_icon[i], (x_iconx[1], x_icony[1]))
        display.blit(o_icon[j], (o_iconx[1], o_icony[1]))
    elif c == 5:
        display.blit(x_icon[i], (x_iconx[0], x_icony[0]))
        display.blit(o_icon[j], (o_iconx[0], o_icony[0]))
        display.blit(x_icon[i], (x_iconx[1], x_icony[1]))
        display.blit(o_icon[j], (o_iconx[1], o_icony[1]))
        display.blit(x_icon[i], (x_iconx[2], x_icony[2]))
    elif c == 6:
        display.blit(x_icon[i], (x_iconx[0], x_icony[0]))
        display.blit(o_icon[j], (o_iconx[0], o_icony[0]))
        display.blit(x_icon[i], (x_iconx[1], x_icony[1]))
        display.blit(o_icon[j], (o_iconx[1], o_icony[1]))
        display.blit(x_icon[i], (x_iconx[2], x_icony[2]))
        display.blit(o_icon[j], (o_iconx[2], o_icony[2]))
    elif c == 7:
        display.blit(x_icon[i], (x_iconx[0], x_icony[0]))
        display.blit(o_icon[j], (o_iconx[0], o_icony[0]))
        display.blit(x_icon[i], (x_iconx[1], x_icony[1]))
        display.blit(o_icon[j], (o_iconx[1], o_icony[1]))
        display.blit(x_icon[i], (x_iconx[2], x_icony[2]))
        display.blit(o_icon[j], (o_iconx[2], o_icony[2]))
        display.blit(x_icon[i], (x_iconx[3], x_icony[3]))
    elif c == 8:
        display.blit(x_icon[i], (x_iconx[0], x_icony[0]))
        display.blit(o_icon[j], (o_iconx[0], o_icony[0]))
        display.blit(x_icon[i], (x_iconx[1], x_icony[1]))
        display.blit(o_icon[j], (o_iconx[1], o_icony[1]))
        display.blit(x_icon[i], (x_iconx[2], x_icony[2]))
        display.blit(o_icon[j], (o_iconx[2], o_icony[2]))
        display.blit(x_icon[i], (x_iconx[3], x_icony[3]))
        display.blit(o_icon[j], (o_iconx[3], o_icony[3]))
    elif c == 9:
        display.blit(x_icon[i], (x_iconx[0], x_icony[0]))
        display.blit(o_icon[j], (o_iconx[0], o_icony[0]))
        display.blit(x_icon[i], (x_iconx[1], x_icony[1]))
        display.blit(o_icon[j], (o_iconx[1], o_icony[1]))
        display.blit(x_icon[i], (x_iconx[2], x_icony[2]))
        display.blit(o_icon[j], (o_iconx[2], o_icony[2]))
        display.blit(x_icon[i], (x_iconx[3], x_icony[3]))
        display.blit(o_icon[j], (o_iconx[3], o_icony[3]))
        display.blit(x_icon[i], (x_iconx[4], x_icony[4]))


def start():
    start_text = font.render("WELCOME TO TIC-TAC-TOE!!", True, white)
    display.blit(start_text, (75, 100))

    start2_text = font.render("Press Space to start", True, white)
    display.blit(start2_text, (150, 250))

    start2_text = font2.render("Created by: Jason Zubia", True, blue)
    display.blit(start2_text, (17, 550))


def enter():
    name_one = font.render("Player One : ", True, red)
    display.blit(name_one, (50, 200))

    name_two = font.render("Player Two : ", True, blue)
    display.blit(name_two, (50, 300))

    name_enter = font.render("Enter your names below", True, green)
    display.blit(name_enter, (110, 50))


def x_icons(x_iconx, x_icony, i):
    display.blit(x_icon[i], (x_iconx, x_icony))


def o_icons(o_iconx, o_icony, j):
    display.blit(o_icon[j], (o_iconx, o_icony))


def check_win():
    if box_1x and box_2x and box_3x == True:
            print("Player1 Wins!")
            sys.exit()
    elif box_4x and box_5x and box_6x == True:
            print("Player1 Wins!")
            sys.exit()
    elif box_7x and box_8x and box_9x == True:
            print("Player1 Wins!")
            sys.exit()
    elif box_1x and box_4x and box_7x == True:
            print("Player1 Wins!")
            sys.exit()
    elif box_2x and box_5x and box_8x == True:
            print("Player1 Wins!")
            sys.exit()
    elif box_3x and box_6x and box_9x == True:
            print("Player1 Wins!")
            sys.exit()
    elif box_1x and box_5x and box_9x == True:
            print("Player1 Wins!")
            sys.exit()
    elif box_3x and box_5x and box_7x == True:
            print("Player1 Wins!")
            sys.exit()
    elif box_1o and box_2o and box_3o == True:
            print("Player2 Wins!")
            sys.exit()
    elif box_4o and box_5o and box_6o == True:
            print("Player2 Wins!")
            sys.exit()
    elif box_7o and box_8o and box_9o == True:
            print("Player2 Wins!")
            sys.exit()
    elif box_1o and box_4o and box_7o == True:
            print("Player2 Wins!")
            sys.exit()
    elif box_2o and box_5o and box_8o == True:
            print("Player2 Wins!")
            sys.exit()
    elif box_3o and box_6o and box_9o == True:
            print("Player2 Wins!")
            sys.exit()
    elif box_1o and box_5o and box_9o == True:
            print("Player2 Wins!")
            sys.exit()
    elif box_3o and box_5o and box_7o == True:
            print("Player2 Wins!")
            sys.exit()


# Intro screen
player_input = False
running = False
while (player_input == False):
    display.fill(black)
    display.blit(start_screen, (0, 0))
    start()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_input = True
                pygame.display.flip()

    pygame.display.update()

# Player Input Screen
done = False
active = False
over = False
over1 = False
set = False
while (player_input == True and running == False):
    display.fill(black)
    enter()
    # Sets up the text box to be written in/ changes the color if it's clicked
    pygame.draw.rect(display, color, input_box, 2)
    pygame.draw.rect(display, color1, input_box1, 2)
    color = green if over else color_inactive
    color1 = green if over1 else color_inactive
    selected = green if set == True else color
    txt_surface = font.render(text, True, color)
    txt_surface1 = font.render(text1, True, color1)
    width = max(200, txt_surface.get_width() + 10)
    width1 = max(200, txt_surface1.get_width() + 10)
    input_box.w = width
    input_box1.w = width1
    display.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    display.blit(txt_surface1, (input_box1.x + 5, input_box1.y + 5))
    one_confirm = font3.render("Player One : " + str(text), True, red)
    display.blit(one_confirm, (50, 500))
    two_confirm = font3.render("Player Two : " + str(text1), True, blue)
    display.blit(two_confirm, (300, 500))
    Mouse_x, Mouse_y = pygame.mouse.get_pos()
    x = Mouse_x
    y = Mouse_y
    if x in range(250, 450):
        if y in range(200, 240):
            over = True
        elif y in range(300, 340):
            over1 = True
    else:
        over = False
        over1 = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                set = True
            elif input_box1.collidepoint(event.pos):
                set = True
            else:
                set = False

        if set:
            if over == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER:
                        print(text)
                        Gui_Project_Extra.player1(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            elif over1 == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER:
                        print(text1)
                        Gui_Project_Extra.player2(text1)
                        text1 = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text1 = text1[:-1]
                    else:
                        text1 += event.unicode

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = True

    pygame.display.update()

# Specification before game loop
i = 0
j = 0
c = 0
# Main Game Loop
while (running == True):
    display.fill(black)
    Mouse_0x, Mouse_0y = pygame.mouse.get_pos()
    x = Mouse_0x
    y = Mouse_0y
    if x in range(0, 200):
        if y in range(0, 200):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                    if click == True:
                        if Xready == True:
                            Xready = False
                            Oready = True
                            x_iconx.append(x)
                            x_icony.append(y)
                            i = i + 1
                            update = True
                            box_1x = True
                        elif Oready == True:
                            Xready = True
                            Oready = False
                            o_iconx.append(x)
                            o_icony.append(y)
                            j = j + 1
                            update = True
                            box_1o = True
    if x in range(0, 200):
        if y in range(200, 400):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                    if click == True:
                        if Xready == True:
                            Xready = False
                            Oready = True
                            x_iconx.append(x)
                            x_icony.append(y)
                            i = i + 1
                            update = True
                            box_4x = True
                        elif Oready == True:
                            Xready = True
                            Oready = False
                            o_iconx.append(x)
                            o_icony.append(y)
                            j = j + 1
                            update = True
                            box_4o = True
    if x in range(0, 200):
        if y in range(400, 600):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                    if click == True:
                        if Xready == True:
                            Xready = False
                            Oready = True
                            x_iconx.append(x)
                            x_icony.append(y)
                            i = i + 1
                            box_7x = True
                            update = True
                        elif Oready == True:
                            Xready = True
                            Oready = False
                            o_iconx.append(x)
                            o_icony.append(y)
                            j = j + 1
                            update = True
                            box_7o = True
    if x in range(200, 400):
        if y in range(0, 200):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                    if click == True:
                        if Xready == True:
                            Xready = False
                            Oready = True
                            x_iconx.append(x)
                            x_icony.append(y)
                            i = i + 1
                            update = True
                            box_2x = True
                        elif Oready == True:
                            Xready = True
                            Oready = False
                            o_iconx.append(x)
                            o_icony.append(y)
                            j = j + 1
                            update = True
                            box_2o = True
    if x in range(200, 400):
        if y in range(200, 400):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                    if click == True:
                        if Xready == True:
                            Xready = False
                            Oready = True
                            x_iconx.append(x)
                            x_icony.append(y)
                            i = i + 1
                            update = True
                            box_5x = True
                        elif Oready == True:
                            Xready = True
                            Oready = False
                            o_iconx.append(x)
                            o_icony.append(y)
                            j = j + 1
                            update = True
                            box_5o = True
    if x in range(200, 400):
        if y in range(400, 600):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                    if click == True:
                        if Xready == True:
                            Xready = False
                            Oready = True
                            x_iconx.append(x)
                            x_icony.append(y)
                            i = i + 1
                            update = True
                            box_8x = True
                        elif Oready == True:
                            Xready = True
                            Oready = False
                            o_iconx.append(x)
                            o_icony.append(y)
                            j = j + 1
                            update = True
                            box_8o = True
    if x in range(400, 600):
        if y in range(0, 200):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                    if click == True:
                        if Xready == True:
                            Xready = False
                            Oready = True
                            x_iconx.append(x)
                            x_icony.append(y)
                            i = i + 1
                            update = True
                            box_3x = True
                        elif Oready == True:
                            Xready = True
                            Oready = False
                            o_iconx.append(x)
                            o_icony.append(y)
                            j = j + 1
                            update = True
                            box_3o = True
    if x in range(400, 600):
        if y in range(200, 400):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                    if click == True:
                        if Xready == True:
                            Xready = False
                            Oready = True
                            x_iconx.append(x)
                            x_icony.append(y)
                            i = i + 1
                            update = True
                            box_6x = True
                        elif Oready == True:
                            Xready = True
                            Oready = False
                            o_iconx.append(x)
                            o_icony.append(y)
                            j = j + 1
                            update = True
                            box_6o = True
    if x in range(400, 600):
        if y in range(400, 600):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                    if click == True:
                        if Xready == True:
                            Xready = False
                            Oready = True
                            x_iconx.append(x)
                            x_icony.append(y)
                            i = i + 1
                            update = True
                            box_9x = True
                        elif Oready == True:
                            Xready = True
                            Oready = False
                            o_iconx.append(x)
                            o_icony.append(y)
                            j = j + 1
                            update = True
                            box_9o = True

    if click == True:
        c = c + 1
        click = False

    try:
        if Xready == True:
            x_icons(x, y, i)
        elif Oready == True:
            o_icons(x, y, j)
    except IndexError:
        raise sys.exit()

    check_win()
    update0()
    pygame.display.flip()
    pygame.display.update()
