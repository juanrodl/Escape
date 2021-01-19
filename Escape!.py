import pygame
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640,460))
screen.fill((255,255,255))
pygame.display.set_caption('Escape!')
file = 'bm.mp3'
go = pygame.image.load("gameover.png")
pygame.mixer.init()
pygame.mixer.music.load(file)
font = pygame.font.SysFont(None, 36)
level = 1
time = 60
move_left = False
move_right = False
move_up = False
move_down = False
button1use = False
button2use = False
button3use = False
enemy1 = pygame.Rect(0,150,20,20)
enemy2 = pygame.Rect(0,350,20,20)
enemy3 = pygame.Rect(390,0,20,20)
enemy4 = pygame.Rect(240,0,20,20)
player = pygame.Rect(300,400,30,30)
enemy1_speed = 1
enemy2_speed = 1
enemy3_speed = 1
enemy4_speed = 1
player_speed = 1
deaths = 0
bye = 42
obstacle = pygame.Rect(150,0,20,400)
obstacle1 = pygame.Rect(490,0,20,363)
blah = pygame.Rect(0,100,180,20)
obstacle2 = pygame.Rect(115,200,180,20)
obstaclex = pygame.Rect(160,300,20,110)
obstacle3 = pygame.Rect(280,0,20,410)
obstacle4 = pygame.Rect(0,290,210,20)
obstacle5 = pygame.Rect(385,120,20,400)
line = pygame.Rect(450,0,20,400)
wall = pygame.Rect(300,80,20,380)
wall1 = pygame.Rect(140,390,410,20)
wall2 = pygame.Rect(550,230,20,180)
wall3 = pygame.Rect(505,230,45,20)
wall4 = pygame.Rect(505,230,20,165)
wall5 = pygame.Rect(430,375,75,20)
wall6 = pygame.Rect(430,160,20,215)
wall7 = pygame.Rect(370,160,270,20)
wall8 = pygame.Rect(370,160,20,170)
wall9 = pygame.Rect(280,310,90,20)
wall10 = pygame.Rect(280,160,20,160)
wall11 = pygame.Rect(140,155,160,20)
wall12 = pygame.Rect(140,100,20,100)
wall13 = pygame.Rect(140,200,100,20)
wall14 = pygame.Rect(240,200,20,90)
wall15 = pygame.Rect(140,270,100,20)
wall16 = pygame.Rect(140,270,20,120)
wall17 = pygame.Rect(50,0,15,150)
bar1 = pygame.Rect(555,370,20,90)
bar2 = pygame.Rect(555,215,20,85)
bar3 = pygame.Rect(330,215,225,20)
bar4 = pygame.Rect(330,85,20,130)
bar5 = pygame.Rect(425,85,20,130)
bar6 = pygame.Rect(425,100,215,20)
bar7 = pygame.Rect(140,280,415,20)
bar8 = pygame.Rect(175,370,400,20)
bar9 = pygame.Rect(470,280,20,50)
bar10 = pygame.Rect(330,280,20,50)
bar11 = pygame.Rect(395,340,20,50)
bar12 = pygame.Rect(260,340,20,50)
bar13 = pygame.Rect(400,430,20,50)
bar14 = pygame.Rect(330,370,20,50)
bar15 = pygame.Rect(250,430,20,50)
bar16 = pygame.Rect(0,210,230,20)
bar17 = pygame.Rect(0,170,250,20)
bar18 = pygame.Rect(95,90,140,20)
bar19 = pygame.Rect(230,190,20,40)
bar20 = pygame.Rect(230,0,20,110)
gate4 = pygame.Rect(555,300,20,70)
gate5 = pygame.Rect(0,280,140,20)
gate6 = pygame.Rect(230,110,20,60)
gate7 = pygame.Rect(425,0,20,85)
fill6 = pygame.Rect(0,190,230,20)
button4 = pygame.Rect(460,150,40,40)
button5 = pygame.Rect(480,405,40,40)
button6 = pygame.Rect(470,237,40,40)
button7 = pygame.Rect(365,160,40,40)
enemy5 = pygame.Rect(0,370,20,20)
enemy6 = pygame.Rect(300,0,20,20)
enemy7 = pygame.Rect(520,170,20,20)
enemy8 = pygame.Rect(55,0,20,20)
button4use = False
button5use = False
button6use = False
button7use = False
enemy5_speed = 1
enemy6_speed = 2
enemy7_speed = 2
enemy8_speed = 1
fill = pygame.Rect(260,170,20,220)
fill1 = pygame.Rect(520,250,40,160)
fill2 = pygame.Rect(160,290,100,100)
fill3 = pygame.Rect(280,330,160,60)
fill4 = pygame.Rect(390,180,40,150)
fill5 = pygame.Rect(160,175,100,25)
gate1 = pygame.Rect(410,410,20,70)
gate2 = pygame.Rect(140,0,20,100)
gate3 = pygame.Rect(430,0,20,160)
button1 = pygame.Rect(458,320,40,40)
button2 = pygame.Rect(180,225,40,40)
button3 = pygame.Rect(315,250,40,40)
gate = pygame.Rect(190,290,90,20)
key = pygame.Rect(20,20,20,10)
key1 = pygame.Rect(15,30,20,10)
door = pygame.Rect(550,20,50,80)
door1 = pygame.Rect(560,10,50,130)
button = pygame.Rect(10,345,55,40)
keyhave = False
keytouch = False
buttonuse = False
timesup = False

fr = 500

main_clock = pygame.time.Clock()

def draw_text(display_string, font, surface, x, y):
    text_display = font.render(display_string, 1, (0, 0, 0))
    text_rect = text_display.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_display, text_rect)
def make_level1():
    player.x = 380
    player.y = 400
    player_speed = 1
    obstacle = pygame.Rect(150,0,20,400)
    line = pygame.Rect(450,0,20,400)
    key = pygame.Rect(20,20,20,10)
    door = pygame.Rect(550,20,50,80)
    keyhave = False
    deaths = 0
def draw_wall():
    pygame.draw.rect(screen, (255,0,0), wall)
def draw_line():
    pygame.draw.rect(screen, (255,0,0), line)
def draw_obstacle():
    pygame.draw.rect(screen, (255,0,0), obstacle)
def draw_player():
    pygame.draw.rect(screen, (0,0,0), player)
def draw_screen():
    screen.fill((160,160,160))
def draw_key():
    pygame.draw.rect(screen, (255,255,0), key)
def draw_door():
    pygame.draw.rect(screen, (102,51,0), door)

def make_level2():
    player.x = 571
    player.y = 422
    player_speed = 1
    obstacle = pygame.Rect(150,0,20,400)
    obstacle1 = pygame.Rect(490,0,20,363)
    obstacle2 = pygame.Rect(115,0,10,140)
    obstacle3 = pygame.Rect(280,0,20,410)
    obstacle4 = pygame.Rect(0,290,210,20)
    obstacle5 = pygame.Rect(405,120,20,400)
    obstaclex = pygame.Rect(160,300,20,110)
    gate = pygame.Rect(190,290,90,20)
    key1 = pygame.Rect(15,30,20,10)
    door1 = pygame.Rect(560,10,50,130)
    button = pygame.Rect(10,345,55,40)
    buttonuse = False
    deaths = 0
def draw_player():
    pygame.draw.rect(screen, (0,0,0), player)
def draw_obstacle1():
    pygame.draw.rect(screen, (255,0,0), obstacle1)
def draw_obstacle2():
    pygame.draw.rect(screen, (255,0,0), obstacle2)
def draw_obstacle3():
    pygame.draw.rect(screen, (255,0,0), obstacle3)
def draw_obstacle4():
    pygame.draw.rect(screen, (255,0,0), obstacle4)
def draw_obstacle5():
    pygame.draw.rect(screen, (255,0,0), obstacle5)
def draw_obstaclex():
    pygame.draw.rect(screen, (255,0,0), obstaclex)
def draw_blah():
    pygame.draw.rect(screen, (255,0,0), blah)
def draw_gate():
    pygame.draw.rect(screen, (51,0,102), gate)
def draw_key1():
    pygame.draw.rect(screen, (255,255,0), key1)
def draw_button():
    pygame.draw.rect(screen, (51,0,102), button)

def make_level3():
    player.x = 585
    player.y = 420
    player_speed = 1
    enemy1_speed = 1
    enemy2_speed = 1
    enemy3_speed = 1
    button1use = False
    button2use = False
    button3use= False
    enemy1.x = 0
    enemy1.y = 150
    enemy2.x = 0
    enemy2.y = 350
    enemy3.x = 390
    enemy3.y = 0
    enemy4.x = 240
    enemy4.y = 0
    deaths = 0
    wall1 = pygame.Rect(140,390,410,20)
    wall2 = pygame.Rect(550,230,20,180)
    wall3 = pygame.Rect(505,230,45,20)
    wall4 = pygame.Rect(505,230,20,165)
    wall5 = pygame.Rect(430,375,75,20)
    wall6 = pygame.Rect(430,160,20,215)
    wall7 = pygame.Rect(370,160,270,20)
    wall8 = pygame.Rect(370,160,20,170)
    wall9 = pygame.Rect(280,310,90,20)
    wall10 = pygame.Rect(280,160,20,160)
    wall11 = pygame.Rect(140,155,160,20)
    wall12 = pygame.Rect(140,100,20,100)
    wall13 = pygame.Rect(140,200,100,20)
    wall14 = pygame.Rect(240,200,20,90)
    wall15 = pygame.Rect(140,270,100,20)
    wall16 = pygame.Rect(140,270,20,120)
    fill = pygame.Rect(260,170,20,220)
    fill1 = pygame.Rect(520,250,40,160)
    fill2 = pygame.Rect(160,290,100,100)
    fill3 = pygame.Rect(280,330,160,60)
    fill4 = pygame.Rect(390,180,40,150)
    fill5 = pygame.Rect(160,175,100,25)
    gate1 = pygame.Rect(410,410,20,70)
    gate2 = pygame.Rect(140,0,20,100)
    gate3 = pygame.Rect(430,0,20,160)
    button1 = pygame.Rect(460,320,35,30)
    button2 = pygame.Rect(180,220,35,30)
    button3 = pygame.Rect(310,240,35,30)
def draw_text(display_string, font, surface, x, y):
    text_display = font.render(display_string, 1, (0, 0, 0))
    text_rect = text_display.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_display, text_rect)
def draw_wall1():
    pygame.draw.rect(screen, (255,0,0), wall1)
def draw_wall2():
    pygame.draw.rect(screen, (255,0,0), wall2)
def draw_wall3():
    pygame.draw.rect(screen, (255,0,0), wall3)
def draw_wall4():
    pygame.draw.rect(screen, (255,0,0), wall4)
def draw_wall5():
    pygame.draw.rect(screen, (255,0,0), wall5)
def draw_wall6():
    pygame.draw.rect(screen, (255,0,0), wall6)
def draw_wall7():
    pygame.draw.rect(screen, (255,0,0), wall7)
def draw_wall8():
    pygame.draw.rect(screen, (255,0,0), wall8)
def draw_wall9():
    pygame.draw.rect(screen, (255,0,0), wall9)
def draw_wall10():
    pygame.draw.rect(screen, (255,0,0), wall10)
def draw_wall11():
    pygame.draw.rect(screen, (255,0,0), wall11)
def draw_wall12():
    pygame.draw.rect(screen, (255,0,0), wall12)
def draw_wall13():
    pygame.draw.rect(screen, (255,0,0), wall13)
def draw_wall14():
    pygame.draw.rect(screen, (255,0,0), wall14)
def draw_wall15():
    pygame.draw.rect(screen, (255,0,0), wall15)
def draw_wall16():
    pygame.draw.rect(screen, (255,0,0), wall16)
def draw_wall17():
    pygame.draw.rect(screen,(255,0,0), wall17)
def draw_fill():
    pygame.draw.rect(screen,(255,0,0), fill)
def draw_fill1():
    pygame.draw.rect(screen,(255,0,0), fill1)
def draw_fill2():
    pygame.draw.rect(screen,(255,0,0), fill2)
def draw_fill3():
    pygame.draw.rect(screen,(255,0,0), fill3)
def draw_fill4():
    pygame.draw.rect(screen,(255,0,0), fill4)
def draw_fill5():
    pygame.draw.rect(screen,(255,0,0), fill5)
def draw_gate1():
    pygame.draw.rect(screen,(102,0,204), gate1)
def draw_gate2():
    pygame.draw.rect(screen,(0,255,0), gate2)
def draw_gate3():
    pygame.draw.rect(screen,(0,0,255), gate3)
def draw_button1():
    pygame.draw.rect(screen,(102,0,204), button1)
def draw_button2():
    pygame.draw.rect(screen,(0,255,0), button2)
def draw_button3():
    pygame.draw.rect(screen,(0,0,255), button3)
def draw_enemy1():
    pygame.draw.rect(screen,(255,0,0), enemy1)
def draw_enemy2():
    pygame.draw.rect(screen,(255,0,0), enemy2)
def draw_enemy3():
    pygame.draw.rect(screen,(255,0,0), enemy3)
def draw_enemy4():
    pygame.draw.rect(screen,(255,0,0), enemy4)

def make_level4():
    if level == 4:
        key.x = 170
        key.y = 30
    player.x = 590
    player.y = 400
    player_speed = 1
    bar1 = pygame.Rect(555,370,20,90)
    bar2 = pygame.Rect(555,215,20,85)
    bar3 = pygame.Rect(330,215,225,20)
    bar4 = pygame.Rect(330,85,20,130)
    bar5 = pygame.Rect(425,85,20,130)
    bar6 = pygame.Rect(425,100,215,20)
    bar7 = pygame.Rect(140,280,415,20)
    bar8 = pygame.Rect(175,370,400,20)
    bar9 = pygame.Rect(470,280,20,50)
    bar10 = pygame.Rect(330,280,20,50)
    bar11 = pygame.Rect(395,340,20,50)
    bar12 = pygame.Rect(260,340,20,50)
    bar13 = pygame.Rect(400,430,20,50)
    bar14 = pygame.Rect(330,370,20,50)
    bar15 = pygame.Rect(250,430,20,50)
    bar16 = pygame.Rect(0,210,230,20)
    bar17 = pygame.Rect(0,170,250,20)
    bar18 = pygame.Rect(95,90,140,20)
    bar19 = pygame.Rect(230,190,20,40)
    bar20 = pygame.Rect(230,0,20,110)
    gate4 = pygame.Rect(555,300,20,70)
    gate5 = pygame.Rect(0,280,140,20)
    gate6 = pygame.Rect(230,110,20,60)
    gate7 = pygame.Rect(425,0,20,85)
    button4 = pygame.Rect(460,150,40,40)
    button5 = pygame.Rect(480,405,40,40)
    button6 = pygame.Rect(470,237,40,40)
    button7 = pygame.Rect(365,160,40,40)
    enemy5 = pygame.Rect(0,370,20,20)
    enemy6 = pygame.Rect(300,0,20,20)
    enemy7 = pygame.Rect(520,170,20,20)
    button4use = False
    button5use = False
    button6use = False
    button7use = False
    enemy5_speed = 1
    enemy6_speed = 2
    enemy7_speed = 1
    enemy8_speed = 1
def draw_bar1():
    pygame.draw.rect(screen,(255,0,0), bar1)
def draw_bar2():
    pygame.draw.rect(screen,(255,0,0), bar2)
def draw_bar3():
    pygame.draw.rect(screen,(255,0,0), bar3)
def draw_bar4():
    pygame.draw.rect(screen,(255,0,0), bar4)
def draw_bar5():
    pygame.draw.rect(screen,(255,0,0), bar5)
def draw_bar6():
    pygame.draw.rect(screen,(255,0,0), bar6)
def draw_bar7():
    pygame.draw.rect(screen,(255,0,0), bar7)
def draw_bar8():
    pygame.draw.rect(screen,(255,0,0), bar8)
def draw_bar9():
    pygame.draw.rect(screen,(255,0,0), bar9)
def draw_bar10():
    pygame.draw.rect(screen,(255,0,0), bar10)
def draw_bar11():
    pygame.draw.rect(screen,(255,0,0), bar11)
def draw_bar12():
    pygame.draw.rect(screen,(255,0,0), bar12)
def draw_bar13():
    pygame.draw.rect(screen,(255,0,0), bar13)
def draw_bar14():
    pygame.draw.rect(screen,(255,0,0), bar14)
def draw_bar15():
    pygame.draw.rect(screen,(255,0,0), bar15)
def draw_bar16():
    pygame.draw.rect(screen,(255,0,0), bar16)
def draw_bar17():
    pygame.draw.rect(screen,(255,0,0), bar17)
def draw_bar18():
    pygame.draw.rect(screen,(255,0,0), bar18)
def draw_bar19():
    pygame.draw.rect(screen,(255,0,0), bar19)
def draw_bar20():
    pygame.draw.rect(screen,(255,0,0), bar20)
def draw_fill6():
    pygame.draw.rect(screen,(255,0,0), fill6)
def draw_gate4():
    pygame.draw.rect(screen,(102,0,204), gate4)
def draw_gate5():
    pygame.draw.rect(screen,(0,255,0), gate5)
def draw_gate6():
    pygame.draw.rect(screen,(204,0,204), gate6)
def draw_gate7():
    pygame.draw.rect(screen,(255,128,0), gate7)
def draw_button4():
    pygame.draw.rect(screen,(102,0,204), button4)
def draw_button5():
    pygame.draw.rect(screen,(0,255,0), button5)
def draw_button6():
    pygame.draw.rect(screen,(204,0,204), button6)
def draw_button7():
    pygame.draw.rect(screen,(255,128,0), button7)
def draw_enemy5():
    pygame.draw.rect(screen,(255,0,0), enemy5)
def draw_enemy6():
    pygame.draw.rect(screen,(255,0,0),enemy6)
def draw_enemy7():
    pygame.draw.rect(screen,(255,0,0), enemy7)
def draw_enemy8():
    pygame.draw.rect(screen,(255,0,0), enemy8)

def make_level5():
    player.x = 320
    player.y = 10
    print ("Game Over! Thanks for playing!")

print ("Collect the key while dodging all the obstacles. Once you've collected it go to the door and move on to the next level!")
print ("Controls: W to move upwards")
print ("          S to move downwards")
print ("          D to move right")
print ("          A to move left")
print ("          Hold SPACE for Bullet Time (Slow-mo).")
pygame.mixer.music.play()
pygame.mixer.music.play()
while True:
    if level == 1:
        make_level1()
    elif level == 2:
        print ("Stand on the button to open the gate in order to get the key!")
        make_level2()
        keyhave = False
        buttonuse = False
    elif level == 3:
        print ("Dodge the moving enemy guards or they'll send you back to your spawn! (Remember to use Bullet Time!)")
        make_level3()
        keyhave = False
        button1use = False
        button2use = False
        button3use = False
    elif level == 4:
        print ("This is the last level! Good luck!")
        make_level4()
        keyhave = False
        button4use = False
        button5use = False
        button6use = False
        button7use = False
    elif level == 5:
        make_level5()
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_a:
                    move_right = False
                    move_left = True
                    move_up = False
                    move_down = False
                if event.key == K_d:
                    move_left = False
                    move_right = True
                    move_up = False
                    move_down = False
                if event.key == K_w:
                    move_left = False
                    move_right = False
                    move_up = True
                    move_down = False
                if event.key == K_s:
                    move_left = False
                    move_right = False
                    move_up = False
                    move_down = True
                if event.key == K_SPACE:
                    fr = 50
            if event.type == KEYUP:
                if event.key == K_a:
                    move_left = False
                if event.key == K_d:
                    move_right = False
                if event.key == K_w:
                    move_up = False
                if event.key == K_s:
                    move_down = False
                if event.key == K_SPACE:
                    fr = 500
        if move_left and player.left > 0:
            player.x -= player_speed
        if move_right and player.right < 610:
            player.x += player_speed
        if move_up and player.y > 0:
            player.y -= player_speed
        if move_down and player.y < 430:
            player.y += player_speed

        if level == 3:
            enemy1.x += enemy1_speed
            if enemy1.x > 120 or enemy1.x < 0:
                enemy1_speed *= -1

        if level == 3:
            enemy2.x += enemy2_speed
            if enemy2.x > 120 or enemy2.x < 0:
                enemy2_speed *= -1

        if level == 3:
            enemy3.y += enemy3_speed
            if enemy3.y < 0 or enemy3.y > 150:
                enemy3_speed *= -1

        if level == 3:
            enemy4.y += enemy4_speed
            if enemy4.y < 0 or enemy3.y > 145:
                enemy4_speed *= -1

        if level == 4:
            enemy5.x += enemy5_speed
            if enemy5.x > 180 or enemy5.x < 0:
                enemy5_speed *= -1

        if level == 4:
            enemy6.y += enemy6_speed
            if enemy6.y < 0 or enemy6.y > 270:
                enemy6_speed *= -1

        if level == 4:
            enemy7.y += enemy7_speed
            if enemy7.y < 0 or enemy7.y > 200:
                enemy7_speed *= -1

        if level == 4:
            enemy8.y += enemy8_speed
            if enemy8.y < 0 or enemy8.y > 150:
                enemy8_speed *= -1


        if level == 1 and player.colliderect(obstacle):
            keyhave = False
            deaths += 1
            break

        if level == 1 and player.colliderect(wall):
            keyhave = False
            deaths += 1
            break

        if level == 1 and player.colliderect(line):
            keyhave = False
            deaths += 1
            break

        if player.colliderect(key) and not keyhave:
            keyhave = True
            print ("You have collected the key! Go and find the door to escape!")

        if player.colliderect(door):
            if keyhave == False:
                player.x = 500
                player.y = 20
                print ("You don't have the key to this door yet! Collect it and come back.")
            elif keyhave == True:
                print ("You beat this level! Next level.")
                level += 1
                keyhave = False
                break

        if level == 4 and keyhave == True and player.colliderect(door):
            print ("Game Over! Thanks for playing 'Escape!'")


        if level == 2 and player.colliderect(obstacle1):
            keyhave = False
            buttonuse = False
            deaths += 1
            break

        if level == 2 and player.colliderect(obstacle2):
            keyhave = False
            buttonuse = False
            deaths += 1
            break

        if level == 2 and player.colliderect(obstacle3):
            keyhave = False
            buttonuse = False
            deaths += 1
            break

        if level == 2 and player.colliderect(obstacle4):
            keyhave = False
            buttonuse = False
            deaths += 1
            break

        if level == 2 and player.colliderect(obstacle5):
            keyhave = False
            buttonuse = False
            deaths += 1
            break

        if level == 2 and player.colliderect(blah):
            keyhave = False
            buttonuse = False
            deaths += 1
            break

        if level == 2 and player.colliderect(obstaclex):
            keyhave = False
            buttonuse = False
            deaths += 1
            break

        if level == 2 and player.colliderect(gate) and not buttonuse:
            keyhave = False
            buttonuse = False
            deaths += 1
            break

        if level == 3 and player.colliderect(wall1):
            keyhave = False
            button1use = False
            button2use = False
            button3use = False
            deaths += 1
            break

        if level == 3 and player.colliderect(wall2):
            keyhave = False
            button1use = False
            button2use = False
            button3use = False
            deaths += 1
            break

        if level == 3 and player.colliderect(wall3):
            keyhave = False
            button1use = False
            button2use = False
            button3use = False
            deaths += 1
            break

        if level == 3 and player.colliderect(wall4):
            keyhave = False
            button1use = False
            button2use = False
            button3use = False
            deaths += 1
            break

        if level == 3 and player.colliderect(wall5):
            keyhave = False
            button1use = False
            button2use = False
            button3use = False
            deaths += 1
            break

        if level == 3 and player.colliderect(wall6):
            keyhave = False
            button1use = False
            button2use = False
            button3use = False
            deaths += 1
            break

        if level == 3 and player.colliderect(wall7):
            keyhave = False
            button1use = False
            button2use = False
            button3use = False
            deaths += 1
            break

        if level == 3 and player.colliderect(wall8):
            keyhave = False
            button1use = False
            button2use = False
            button3use = False
            deaths += 1
            break

        if level == 3 and player.colliderect(wall9):
            keyhave = False
            button1use = False
            button2use = False
            button3use = False
            deaths += 1
            break

        if level == 3 and player.colliderect(wall10):
            keyhave = False
            button1use = False
            button2use = False
            button3use = False
            deaths += 1
            break

        if level == 3 and player.colliderect(wall11):
            keyhave = False
            button1use = False
            button2use = False
            button3use = False
            deaths += 1
            break

        if level == 3 and player.colliderect(wall12):
            keyhave = False
            button1use = False
            button2use = False
            button3use = False
            deaths += 1
            break

        if level == 3 and player.colliderect(wall13):
            keyhave = False
            button1use = False
            button2use = False
            button3use = False
            deaths += 1
            break

        if level == 3 and player.colliderect(wall14):
            keyhave = False
            buttonuse1 = False
            buttonuse2 = False
            buttonuse3 = False
            deaths += 1
            break

        if level == 3 and player.colliderect(wall15):
            keyhave = False
            button1use = False
            button2use = False
            button3use = False
            deaths += 1
            break

        if level == 3 and player.colliderect(wall16):
            keyhave = False
            button1use = False
            button2use = False
            button3use = False
            deaths += 1
            break

        if level == 3 and player.colliderect(wall17):
            keyhave = False
            button1use = False
            button2use = False
            button3use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar1):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar2):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar3):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar4):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar5):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar6):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar7):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar8):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar9):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar10):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar11):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar12):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar13):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar14):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar15):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar16):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar17):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar18):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar19):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(bar20):
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if player.colliderect(button):
            buttonuse = True

        if level == 3 and player.colliderect(gate1) and not button1use:
            keyhave = False
            button1use = False
            button2use = False
            button3use = False
            deaths += 1
            break

        if level == 3 and player.colliderect(gate2) and not button2use:
            keyhave = False
            button1use = False
            button2use = False
            button3use = False
            deaths += 1
            break

        if level == 3 and player.colliderect(gate3) and not button3use:
            keyhave = False
            button1use = False
            button2use = False
            button3use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(gate4) and not button4use:
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(gate5) and not button5use:
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(gate6) and not button6use:
            keyhave = Falsew
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if level == 4 and player.colliderect(gate7) and not button7use:
            keyhave = False
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            deaths += 1
            break

        if player.colliderect(button1):
            button1use = True

        if player.colliderect(button2):
            button2use = True

        if player.colliderect(button3):
            button3use = True

        if player.colliderect(button4):
            button4use = True

        if player.colliderect(button5):
            button5use = True

        if player.colliderect(button6):
            button6use = True

        if player.colliderect(button7):
            button7use = True

        if level == 3 and player.colliderect(enemy1):
            button1use = False
            button2use = False
            button3use = False
            keyhave = False
            deaths += 1
            break

        if level == 3 and player.colliderect(enemy2):
            button1use = False
            button2use = False
            button3use = False
            keyhave = False
            deaths += 1
            break

        if level == 3 and player.colliderect(enemy3):
            button1use = False
            button2use = False
            button3use = False
            keyhave = False
            deaths += 1
            break

        if level == 3 and player.colliderect(enemy4):
            button1use = False
            button2use = False
            button3use = False
            keyhave = False
            deaths += 1
            break

        if level == 4 and player.colliderect(enemy5):
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            keyhave = False
            deaths += 1
            break


        if level == 4 and player.colliderect(enemy6):
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            keyhave = False
            deaths += 1
            break


        if level == 4 and player.colliderect(enemy7):
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            keyhave = False
            deaths += 1
            break

        if level == 4 and player.colliderect(enemy8):
            button4use = False
            button5use = False
            button6use = False
            button7use = False
            keyhave = False
            deaths += 1
            break

        main_clock.tick(fr)

        draw_screen()
        draw_player()
        draw_text('Deaths: %s' % (deaths), font, screen, 5, 430)
        draw_text('Level: %s' % (level), font, screen, 5, 400)
        if level == 1:
            draw_obstacle()
            draw_door()
            draw_wall()
            draw_line()
            if keyhave == False:
                draw_key()
        if level == 2:
            draw_obstacle1()
            draw_obstacle2()
            draw_obstacle3()
            draw_obstacle4()
            draw_obstacle5()
            draw_obstaclex()
            draw_blah()
            draw_button()
            if buttonuse == False:
                draw_gate()
            draw_door()
            if keyhave == False:
                draw_key()
        if level == 3:
            draw_wall1()
            draw_wall2()
            draw_wall3()
            draw_wall4()
            draw_wall5()
            draw_wall6()
            draw_wall7()
            draw_wall8()
            draw_wall9()
            draw_wall10()
            draw_wall11()
            draw_wall12()
            draw_wall13()
            draw_wall14()
            draw_wall15()
            draw_wall16()
            draw_wall17()
            draw_fill()
            draw_fill1()
            draw_fill2()
            draw_fill3()
            draw_fill4()
            draw_fill5()
            draw_button1()
            draw_button2()
            draw_button3()
            draw_enemy1()
            draw_enemy2()
            draw_enemy3()
            draw_enemy4()
            draw_door()
            if keyhave == False:
                draw_key()
            if button1use == False:
                draw_gate1()
            if button2use == False:
                draw_gate2()
            if button3use == False:
                draw_gate3()
        if level == 4:
            draw_bar1()
            draw_bar2()
            draw_bar3()
            draw_bar4()
            draw_bar5()
            draw_bar6()
            draw_bar7()
            draw_bar8()
            draw_bar9()
            draw_bar10()
            draw_bar11()
            draw_bar12()
            draw_bar13()
            draw_bar14()
            draw_bar15()
            draw_bar16()
            draw_bar17()
            draw_bar18()
            draw_bar19()
            draw_bar20()
            draw_fill6()
            draw_button4()
            draw_button5()
            draw_button6()
            draw_button7()
            if button4use == False:
                draw_gate4()
            if button5use == False:
                draw_gate5()
            if button6use == False:
                draw_gate6()
            if button7use == False:
                draw_gate7()
            draw_enemy5()
            draw_enemy6()
            draw_enemy7()
            draw_enemy8()
            draw_door()
            if keyhave == False:
                draw_key()
        if level == 5:
            draw_text('Game Over! Thanks for playing!', font, screen, 130,230)

        pygame.display.update()