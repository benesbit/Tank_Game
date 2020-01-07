# Ben Nesbit

# Import pygame module
import pygame

# Initialize pygame module
pygame.init()

GAME_DISPLAY = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Tank Game')

CLOCK = pygame.time.Clock()



# # Define a main function
# def main():
#     # Create a surface on screen that has the size of 240 x 180
#     screen = pygame.display.set_mode((240, 180))

#     # Define a variable to control the main loop
#     running = True

#     # Main loop
#     while running:
#         # Event handling, gets all events from event queue
#         for event in pygame.event.get():
#             # Only do something if event is type QUIT
#             if event.type == pygame.QUIT:
#                 # Change running value to False, exiting main loop
#                 running = False

# # Run the main function only if this module is executed as the main script
# # (if you import this as a module then nothing is executed)
# if __name__ =="__main__":
#     # Call the main function
#     main()
