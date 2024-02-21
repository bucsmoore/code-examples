import pygame

pygame.init()
screen = pygame.display.set_mode()
width, height = pygame.display.get_window_size()


shapes = []
num_shapes = 3
offset = 10 # to give a little room between each shape
diameter = (width/num_circles) - offset
radius = diameter/2

while True: #required for event logic

    # 1. handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # event.pos
            # rect.pointcollide(pos)
            # for each shape
            #    if point collides
            #        del shape
            
    # 2. redraw the screen

    screen.fill("white")

    # Draw the shapes on screen using a loop
    # NOTE: You need to save the shape objects in a list to interact with them in the event loop

    pygame.display.flip()