# Simple pygame program
import time
# Import and initialize the pygame library
import pygame
import random

width = 1440
height = 1080

win_prob = 0.2    # should be smaller than 0.666

case_win = {"sci":"paper", "rock":"sci", "paper":"rock"}
case_lose = {"sci":"rock", "rock":"paper", "paper":"sci"}

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
pygame.mouse.set_visible(False) 

# Set up the drawing window
screen = pygame.display.set_mode(
    (width, height),
    pygame.FULLSCREEN
)
clock = pygame.time.Clock()

def load_image(path):
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (width, height))
    # for rotated screen
    #img = pygame.transform.rotate(img, 90)
    #img = pygame.transform.scale(img, (700, height))
    return img

# Load images
background = load_image("img/background.png")
img_rock = load_image("img/rock.png")
img_paper = load_image("img/paper.png")
img_sci = load_image("img/sci.png")
img_win_left = load_image("img/win_left.png")
img_win_right = load_image("img/win_right.png")
img_draw = load_image("img/draw.png")
img_lose = load_image("img/lose.png")
numimg_list = []
for n in range(0, 12):
    img = load_image("img/"+str(n)+".png")
    numimg_list.append(img)

sound_ready1 = pygame.mixer.Sound( "sound/ready1.wav" )
sound_ready2 = pygame.mixer.Sound( "sound/ready2.wav" )
sound_go1 = pygame.mixer.Sound( "sound/go1.wav" )
sound_go2 = pygame.mixer.Sound( "sound/go2.wav" )
sound_lose = pygame.mixer.Sound( "sound/lose.wav" )
sound_win = pygame.mixer.Sound( "sound/win.wav" )
sound_roll = pygame.mixer.Sound( "sound/roll.wav" )
sound_yep = pygame.mixer.Sound( "sound/yep.wav" )


# Run until the user asks to quit
running = True
current = 'rock'
mode = 'idle'    # 'idle', 'ready', 'action', 'fever'
stage = 1
pause_time = 0
play = None
image_list = []
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE: 
                running = False
                break 
            elif event.key == pygame.K_1: 
                if mode != 'ready':
                    mode = 'ready'
                    sound_ready1.play()
            elif mode == 'ready':
                if event.key == pygame.K_LEFT: 
                    action = 'sci'
                    mode = 'action'
                    sound_ready1.stop()
                    sound_ready2.stop()
                    if stage == 1:
                        sound_go1.play()
                    elif stage == 2:
                        sound_go2.play()                   
                elif event.key == pygame.K_DOWN: 
                    action = 'rock'
                    mode = 'action'
                    sound_ready1.stop()
                    sound_ready2.stop()
                    if stage == 1:
                        sound_go1.play()
                    elif stage == 2:
                        sound_go2.play()                   
                elif event.key == pygame.K_RIGHT: 
                    action = 'paper'
                    mode = 'action'
                    sound_ready1.stop()
                    sound_ready2.stop()
                    if stage == 1:
                        sound_go1.play()
                    elif stage == 2:
                        sound_go2.play()

    image_list.append(background)

    if mode == 'idle':
        if current == 'rock':
            image_list.append(img_rock)
            current = 'paper'
        elif current == 'paper':
            image_list.append(img_paper)
            current = 'sci'
        elif current == 'sci':
            image_list.append(img_sci)
            current = 'rock'
        tick = 1

    elif mode == 'ready':
        if current == 'rock':
            image_list.append(img_rock)
            current = 'paper'
        elif current == 'paper':
            image_list.append(img_paper)
            current = 'sci'
        elif current == 'sci':
            image_list.append(img_sci)
            current = 'rock'
        tick = 20
    
    elif mode == 'fever':
        numbers = [1, 2, 7, 4, 2, 20, 1, 2, 4, 4, 2, 4]
        result = random.randint(1,12)
        for n in range(0, 25+result):
            image_list.append(background)
            if action == 'rock':
                image_list.append(img_sci)
            elif action == 'paper':
                image_list.append(img_rock)
            elif action == 'sci':
                image_list.append(img_paper)            
            image_list.append(numimg_list[n%12])
            if n%2 == 1:
                image_list.append(img_win_left)
            else:
                image_list.append(img_win_right)
            for i in image_list:
                screen.blit(i, (0, 0))
            pygame.display.flip()
            image_list.clear()
            sound_roll.play()
            clock.tick(9)
        #print('You got ' + str(numbers[result-1]))
        time.sleep(1)
        sound_yep.play()
        time.sleep(2)
        mode = 'idle'

    elif mode == 'action':
        prob = random.random()
        print(prob)
        if prob < win_prob:    # win 
            if case_win[action] == 'rock':
                image_list.append(img_rock)
            elif case_win[action] == 'paper':
                image_list.append(img_paper)
            elif case_win[action] == 'sci':
                image_list.append(img_sci)
            image_list.append(img_win_left)
            image_list.append(img_win_right)
            play = 'sound_win'
            stage = 1
            mode = 'fever'

        elif prob < win_prob+0.333:    # draw
            if action == 'rock':
                image_list.append(img_rock)
            elif action == 'paper':
                image_list.append(img_paper)
            elif action == 'sci':
                image_list.append(img_sci)
            image_list.append(img_draw)
            play = 'sound_ready2'
            stage = 2
            mode = 'ready'

        else:    # lose
            if case_lose[action] == 'rock':
                image_list.append(img_rock)
            elif case_lose[action] == 'paper':
                image_list.append(img_paper)
            elif case_lose[action] == 'sci':
                image_list.append(img_sci)        
            image_list.append(img_lose)
            play = 'sound_lose'
            stage = 1
            mode = 'idle'
        pause_time = 0.7

    # show images
    for i in image_list:
        screen.blit(i, (0, 0))
        #screen.blit(i, (500, 0))
    pygame.display.flip()
    image_list.clear()

    # sound effect after done
    if pause_time > 0:
        time.sleep(pause_time)
    if play != None:
        if play == 'sound_lose':
            sound_lose.play()
        elif play == 'sound_win':
            sound_win.play()
        elif play == 'sound_ready2':
            sound_ready2.play()
    if pause_time > 0:
        time.sleep(pause_time)

    pause_time = 0
    play = None
    clock.tick(tick)

# Done! Time to quit.
pygame.quit()