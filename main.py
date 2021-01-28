#Importing the library
import pygame
from car import Car,Bush
import random
from pygame import mixer

pygame.init()

#define some colors
BLACK = (0,0,0,)
WHITE = (255,255,255)
GREEN = (0,255,0)
DARK_GREEN = (0,100,0)
RED = (255,0,0)
GREY = (169,169,169)
DARK_GREY = (71,71,71)
# light shade of the button 
color_light = (180,180,180) 

# dark shade of the button 
color_dark = (100,100,100)

# open a new window
size = W,H=500,700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Car Racing')  #Caption for the Game
icon = pygame.image.load('images/icon.png') # Game Icon 
pygame.display.set_icon(icon)

# stores the width of the screen into a variable 
width = screen.get_width() 

# stores the height of the screen into a variable 
height = screen.get_height() 

# Creating List of all the sprites we will use
all_sprites_list = pygame.sprite.Group()
cars = ['images/car.png','images/enemy.png','images/enemy1.png','images/enemy2.png'] #List of all cars

#All opponent cars List
all_coming_cars = pygame.sprite.Group()

#Creating a Player Car and giving its position
playerCar = Car(RED,60,96,cars[0])
playerCar.rect.x = 270
playerCar.rect.y = 500

#Adding this Player car sprite to the list of sprites
all_sprites_list.add(playerCar)

#Creating a Enemy Car and giving its position
def create_enemy():
    '''Creates a enemy Car'''
    global enemyCar
    try:
        enemyCar = Car(RED,60,96,cars[random.randint(1,3)]) # Created a Car
        lane = random.randint(0,1) # Choosing a random lane
        if lane == 0:
            enemyCar.rect.x = random.randint(100,160)
        elif lane == 1:
            enemyCar.rect.x = random.randint(260,340)

        enemyCar.rect.y = random.randint(-150,-100)
    except:
        print("Error creating an enemy.")
    #Adding this car sprite to the list of sprites
    all_sprites_list.add(enemyCar)
    all_coming_cars.add(enemyCar)

def background():
    '''Creates a background for the Game'''
    # Background    
    try:
        screen.fill(DARK_GREEN)
    except:
        print("Background fill not completed")
    # Road
    pygame.draw.rect(screen, DARK_GREY, [70, 0, 360, 700],0) 
    pygame.draw.line(screen, WHITE, [70, 0], [70, 700], 4)
    pygame.draw.line(screen, WHITE, [250, 0], [250, 700], 4)
    pygame.draw.line(screen, WHITE, [430, 0], [430, 700], 4)
    

def game_over():
    '''Game Over!'''
    mixer.music.stop()
    #Game Over Window 
    
    game_over_loop = True
    while game_over_loop:
        # Display the background
        screen.fill(GREY)
        #Game Over Message
        font = pygame.font.Font('freesansbold.ttf',50)
        status = font.render("Game Over",True,(255,0,0))
        crash = font.render("CAR CRASHED",True,(255,0,0))
        screen.blit(crash,(62,200))
        screen.blit(status,(110,270))
        score()
        pygame.display.flip() 
        
        # Exiting controls
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                add_high_score()
                pygame.quit
                quit()

def high_score():
    ''' Displays High Score'''
    # try:
    font = pygame.font.Font('freesansbold.ttf',30)
    high_score = font.render("Highscore : "+(all_scores[-1]),True,BLACK)
    screen.blit(high_score,(10,40))
    # except:
    #     print("Error displaying High Score")

def add_high_score():
    '''Adds Highscore to a file'''
    try:
        with open('highscore.txt','a') as f:
            f.write(str(score_value)+',')
    except:
        print("Error adding highscore")

def score():
    ''' Displays score'''
    global all_scores
    try:
        font = pygame.font.Font('freesansbold.ttf',30)
        score = font.render("Score : "+str(score_value),True,BLACK)
        screen.blit(score,(10,10))
    except:
        print("Error displaying Score")
    
    with open('highscore.txt','r') as f:
        x = f.read()
        all_scores = x.split(',')
        all_scores.sort()

def off_road():
    '''Displays message if car goes Off Road'''
    font = pygame.font.Font('freesansbold.ttf',30)
    score = font.render("Car going Off Road!",True,RED)
    screen.blit(score,(100,50))
def game_buttons(button_text):
    smallfont = pygame.font.SysFont('calibri',35) # button font
    quit_text = smallfont.render('Quit' , True , WHITE) # quit button text
    start_text = smallfont.render(button_text , True , WHITE) # start button text

    buttons = True
    while buttons:
        mouse = pygame.mouse.get_pos() # to get position of cursor
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                buttons = False # Terminate the loop
                pygame.quit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # quit button conditions
                if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                    pygame.quit()
                # start button conditions
                elif width/2-140 <= mouse[0] <= width/2 and height/2 <= mouse[1] <= height/2+40:
                    buttons = False
            else:
                pass
        try:
            # Quit button hover 
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
            else: 
                pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
            screen.blit(quit_text , (width/2+35,height/2+5))

            # Start butto hover
            if width/2-140 <= mouse[0] <= width/2 and height/2 <= mouse[1] <= height/2+40:
                pygame.draw.rect(screen,color_light,[(width/2)-160,(height/2),155,40]) 
            else: 
                pygame.draw.rect(screen,color_dark,[(width/2)-160,(height/2),155,40])
            screen.blit(start_text , (width/2-150,height/2+5))

            pygame.display.update() # Updates the Screen
        except:
            print("Something went Wrong")

def game_intro():
    ''' Game Starts here. This is the Landing Page of the Game.'''
    
  
    intro = True
    while intro:
        # Display the background
        screen.fill(GREY) # Creates Background 
        img = pygame.image.load("images/car main.png") # Intro Page Image
        screen.blit(img,(-90,30))
        font = pygame.font.Font('freesansbold.ttf',40) # Intro Page Text
        start = font.render("Dodge Car Racing",True,RED)
        screen.blit(start,(72,300))

        # Event Controller
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                intro = False # Terminate the loop
                pygame.quit()
        game_buttons('Start')
        intro = False
        carryOn = True
        
def create_bush():
    ''' Creates Roadside bushes'''
    global bush
    try:
        bush = Bush(50,50)
        lane_side = random.randint(0,1)
        if lane_side == 0:
            bush.rect.x = random.randint(0,30)
        elif lane_side == 1:
            bush.rect.x = random.randint(450,480)
        bush.rect.y = random.randint(-150,-100)
        #Adding this bush sprite to the list of sprites
        all_sprites_list.add(bush)
    except:
        print("Error Creating bush.")

def game_loop():
    '''Main Game loop''' 
    
    global score_value,bush
    FPS = 120 # Frame rate at which The game will Play
    score_value = 0 # the score value
    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()
    # Creating Enemies and Bushes 
    create_enemy()
    create_bush()
    
    #Game Begins
    game_intro()
    #background music
    mixer.music.load('sounds/bg-music.wav')
    mixer.music.play(-1) # -1 to play continuously

    # -------- Main Program Loop -----------
    carryOn = True
    while carryOn:
        
        try:
        # Event Handler
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    carryOn = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        carryOn = False
            keys = pygame.key.get_pressed()
            playerCar.changeSpeed(10)
            # Game Controls
            if keys[pygame.K_LEFT]:
                playerCar.moveLeft(2)
            if keys[pygame.K_RIGHT]:
                playerCar.moveRight(2)
            if keys[pygame.K_UP]:
                playerCar.moveForward(5)
            if keys[pygame.K_DOWN]:
                playerCar.moveBackward(5)
        except:
            print("Key Press not detected")
        #Check if there is a car collision
        car_collision_list = pygame.sprite.spritecollide(playerCar,all_coming_cars,False)
        for car in car_collision_list:
            print("Car crash!")

            # Crash Sound after Collision
            crash_sound = mixer.Sound('sounds/crash.wav')
            crash_sound.play()
            carryOn = False # After collision Main game loop terminates
            game_over() # Then display the Game over screen
        
        
        # Updating all the sprites that are added earlier
        all_sprites_list.update()

        #Creating Background
        background()
    
        #Draw sprites
        all_sprites_list.draw(screen)
        score() # Displaying score 
        high_score()
        speed = 8 # Setting the value of speed

        # Conditions for Game difficulty
        if score_value ==0:
            speed = 7
        if score_value > random.randint(60,100):
            speed+=2
        if score_value > random.randint(150,200):
            speed+=3

        # Setting speed and making them move for
            #Enemy
        enemyCar.changeSpeed(speed) 
        enemyCar.continuous_move(speed)
            #Bush
        bush.changeSpeed(speed)
        bush.continuous_move(speed)
    
        # Increment score if enemy car passes without collision
        if enemyCar.rect.y > 700:
            create_enemy() # Creates another enemy Car
            score_value+=10
        
        # Creates bush randomly
        if bush.rect.y > 800:
            create_bush()    

        #Conditions to check if player car is going Off Road
        if playerCar.rect.x < 70 or playerCar.rect.x > 360:
            # print("Car going off road")
            off_road() #Displays message 
        # If car gets off the road then Game ends.
        if playerCar.rect.x <60 or playerCar.rect.x>370:
            game_over()

        # Update the screen 
        pygame.display.flip()
        
        # Frames 
        clock.tick(FPS)

if __name__ == '__main__':
    game_loop()
    add_high_score()
    pygame.quit()


