import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            while event.key == pygame.K_DOWN:
                print("Down key pressed")
        elif event.type == pygame.KEYUP:
            while event.key ==pygame.K_UP:
                print("Up key pressed")

    
    # Fill the screen with white
    screen.fill((0, 0, 0))
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()