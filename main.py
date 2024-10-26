import pygame
import sys

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Welcome to the Game")

# Prompt the user to start the game
start_game = input("Do you want to play the game? (yes/no): ").strip().lower()

# Check user input to decide whether to start the game loop
if start_game == "yes" or start_game == "y":
    print("Great! Use arrow keys to move. Press 'q' to quit.")

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_UP:
                    print("You pressed UP!")
                elif event.key == pygame.K_DOWN:
                    print("You pressed DOWN!")
                elif event.key == pygame.K_LEFT:
                    print("You pressed LEFT!")
                elif event.key == pygame.K_RIGHT:
                    print("You pressed RIGHT!")

    # Cleanup before quitting
    pygame.quit()
    sys.exit()
else:
    print("Maybe next time! Exiting the game.")
