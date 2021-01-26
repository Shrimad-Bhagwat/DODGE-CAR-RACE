import pygame
WHITE = (255,255,255)
import random
class Car(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    def __init__(self, color, width, height,car_name):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.car_name = car_name

        # Draw the car (a rectangle!)
        # pygame.draw.rect(self.image, color, [0, 0, width, height])
    
        # Instead we could load a proper pciture of a car...
        self.image = pygame.image.load(car_name).convert_alpha()
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y -= self.speed * speed / 20
 
    def moveBackward(self, speed):
        self.rect.y += self.speed * speed / 20
 
    def changeSpeed(self, speed):
        self.speed = speed
 
    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

    def continuous_move(self,speed):
        self.rect.y += self.speed * speed / 20

class Bush(pygame.sprite.Sprite):
    def __init__(self,bush_x,bush_y):
        
        super().__init__()
        self.bush_x = bush_x
        self.bush_y = bush_y
        self.image = pygame.image.load('images/bush.png').convert_alpha()
        self.rect = self.image.get_rect()

    def changeSpeed(self, speed):
        self.speed = speed

    def continuous_move(self,speed):
        self.rect.y += self.speed * speed / 20