# This function retrieves all the events that have occurred since the last time it was called 
for event in pygame.event.get():
    # Check if the user inputted the event "QUIT" (closing the window)
    if event.type == pygame.QUIT:
        running = False  # This should close the window

# To check which keyboard keys are currently being held down
keys = pygame.key.get_pressed()
# If left arrow key is pressed
if keys[pygame.K_LEFT]:
    basket_x -= 15  # Move basket 15 pixels to the left
# If right arrow key is pressed
if keys[pygame.K_RIGHT]:
    basket_x += 15  # Move basket 15 pixels to the right

# Fill the screen with white color (refresh background)
screen.fill((255, 255, 255))

# Draw the basket using a blue arc at the bottom of the screen
pygame.draw.arc(screen, blue, (basket_x, 520, 100, 50), math.pi, 2 * math.pi, 5)

# Make sure basket stays inside screen boundaries
basket_x = max(0, min(basket_x, 900))  # 1000 (screen width) - 100 (basket width)

# Loop through each shape and draw it
for shape in shapes:
    if shape["type"] == "square":
        # Draw a green square
        pygame.draw.rect(screen, green, (shape["x"], shape["y"], 30, 30))
    elif shape["type"] == "triangle":
        # Draw a red triangle using polygon points
        points = [(shape["x"], shape["y"]), (shape["x"] + 15, shape["y"]), (shape["x"] + 30, shape["y"] + 30)]
        pygame.draw.polygon(screen, red, points)

# Move each shape downward and check for catches
for shape in shapes:
    shape["y"] += shape["speed"]  # Move shape down by its speed

    # Define bottom of shape for collision detection
    shape_bottom = shape["y"] + shape_size
    caught = False

    # Check if the shape is within the basket horizontally and just above it vertically
    if (basket_x < shape["x"] + shape_size and shape["x"] < basket_x + basket_width):
        if basket_y < shape_bottom < basket_y + 15:
            caught = True

    if shape["type"] == "square":
        if caught:
            squares_caught += 1  # Increase score
            # Reset square to top with random x and speed
            shape["x"] = random.randint(0, 970)
            shape["y"] = random.randint(-300, -30)
            shape["speed"] = random.randint(7, 9)
        elif shape["y"] > 600:
            running = False  # End game if square is missed

    elif shape["type"] == "triangle":
        if caught:
            running = False  # End game if triangle is caught
        elif shape["y"] > 600:
            # Reset triangle to top with new position and speed
            shape["x"] = random.randint(0, 970)
            shape["y"] = random.randint(-300, -30)
            shape["speed"] = random.randint(10, 18)

# Update the screen to reflect changes
pygame.display.update()

# Limit frame rate to 60 frames per second
clock.tick(60)

# End of game – exit pygame and show final score
pygame.quit()
print(f"Game Over! Squares caught: {squares_caught}")
