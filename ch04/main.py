
# mynums = [1,2,2,3]
# for idx, val in enumerate(mynums): # range(len(mylist))
#     mynums[idx] = val * 2
#     print(val)
# print(mynums)

import pygame

pygame.init()
screen = pygame.display.set_mode()
width, height = pygame.display.get_window_size()


shapes = []
num_shapes = 3
offset = 10 # to give a little room between each shape
size = 200 

starting_pos = offset
for _ in range(num_shapes):
    shape = pygame.draw.rect(screen, "aqua", [starting_pos, height/3, size, size])
    shapes.append(shape)
    starting_pos = starting_pos + size + offset

# mainloop
while True: #required for event logic
    
    # 1. handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            # for i, shape in enumerate(shapes):
            #     if shape.collidepoint(event.pos):
            #         del shapes[i]
            for shape in shapes:
                if shape.collidepoint(event.pos):
                    shapes.remove(shape)


    # 2. Update non-event data
    # a projectile moving across screen
    
    # 3. redraw the screen
    screen.fill("white")

    for shape in shapes:
        pygame.draw.rect(screen, "aqua", shape)

    # 4. Display screen
    pygame.display.flip()



# List versus Tuples

mylist = ['a', 'b', 'c']
mytuple = ('a', 'b', 'c')