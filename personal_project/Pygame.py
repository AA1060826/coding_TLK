 #-----------------------------------------------------------------------------
 # Name: block catching pygame
 # Purpose: using pygame to create a game that catches blocks and reveakls score
 #
 # Author:Adithya Arikuti
 # Created 11-June-2025
 # Updated: 11-June-2025
 #-----------------------------------------------------------------------------





import pygame
import math
import random
pygame.init()

basket_x = 450  # Starting x-position


white = (255,255,255) #sets color
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

basket_width = 100
basket_height = 50
basket_y = 520
shape_size = 30


screen = pygame.display.set_mode((1000, 600)) # Creates a window with the given width and height
pygame.display.set_caption("Catch the falling shapes") #adds a title to the crated window


clock = pygame.time.Clock() #creates a clock object which monitors the time
running = True #ste variable running to true
squares_caught = 0
shapes = [{"type": "square", "x": 100, "y": 0, "speed": 7},{"type": "triangle", "x": 300, "y": -150, "speed": 7}]
while running: #Create the main game lop using while loop
   for event in pygame.event.get(): #This function retrieves all the events that have occurred since the last time it was called
       if event.type == pygame.QUIT: # check =s f the user inputted the event "QUIT"
           running = False  # This should close the window
   keys = pygame.key.get_pressed() #to check which keyboard keys are currently being held down.
   if keys[pygame.K_LEFT]:#if left key is pressed
       basket_x -= 15 #move basket 5 pixels to the left
   if keys[pygame.K_RIGHT]: #if right key is pressed
       basket_x += 15 #move basket 5 pixels to the right



   screen.fill((255, 255, 255)) #fills the screen with color
   pygame.draw.arc(screen, (blue), (basket_x, 520, 100, 50), math.pi, 2 * math.pi, 5) #creates an arc with the desired color
   basket_x = max(0, min(basket_x, 900))  # 1000 - basket width (approx.)


   for shape in shapes:
       if shape["type"] == "square":
           pygame.draw.rect(screen, green, (shape["x"], shape["y"], 30, 30))
       elif shape["type"] == "triangle":
           points = [(shape["x"], shape["y"] + 0), (shape["x"] + 15, shape["y"]), (shape["x"] + 30, shape["y"] + 30)]
           pygame.draw.polygon(screen, (red), points)
   for shape in shapes:
       shape["y"] += shape["speed"]

       # Detect if basket catches shape
       shape_bottom = shape["y"] + shape_size
       caught = False
       if (basket_x < shape["x"] + shape_size and shape["x"] < basket_x + basket_width):
           if basket_y < shape_bottom < basket_y + 15:
               caught = True

       if shape["type"] == "square":
           if caught:
               squares_caught += 1  # Increase counter
               # Reset square position to top with random x and speed
               shape["x"] = random.randint(0, 970)
               shape["y"] = random.randint(-300, -30)
               shape["speed"] = random.randint(7, 9)
           elif shape["y"] > 600:  # missed square
               running = False  # End game immediately

       elif shape["type"] == "triangle":
           if caught:
               running = False  # End game when catching triangle
           elif shape["y"] > 600:
               # Reset triangle to fall again
               shape["x"] = random.randint(0, 970)
               shape["y"] = random.randint(-300, -30)
               shape["speed"] = random.randint(10, 18)

   pygame.display.update() #updates the screen to notice any interactions made.
   clock.tick(60) #limits the tick speed to 60 frames
pygame.quit() #quits program

pygame.quit()  # quits program
print(f"Game Over! Squares caught: {squares_caught}")
