import pygame

pygame.init()

screen = pygame.display.set_mode()

dimensions = screen.get_size()  # [width, and height]
print(dimensions)
starting_point = [dimensions[0] // 2, (dimensions[1] // 2) + 300]

# # draw library

# # where to draw it
# color: "red", [r,g,b]=>[0-255, 0-255, 0-255]
# starting point: [x, y]
# radius: 50

radius = 200
for _ in range(10):
    pygame.draw.circle(screen, "red", starting_point, radius)
    # move center of second circle upwards
    starting_point[1] = starting_point[1] - radius

    radius = radius // 2

    starting_point[1] = starting_point[1] - radius

pygame.display.flip()
pygame.time.wait(2000)

# pygame.draw.circle(screen, "red", starting_point, radius)
# # move center of second circle upwards
# starting_point[1] = starting_point[1] - radius

# radius = radius // 2

# pygame.display.flip()
# pygame.time.wait(2000)

# pygame.draw.circle(screen, "blue", starting_point, radius)
# # move center of second circle upwards
# starting_point[1] = starting_point[1] - radius

# radius = radius // 2

# starting_point[1] = starting_point[1] - radius

# pygame.display.flip()
# pygame.time.wait(2000)

# pygame.draw.circle(screen, "green", starting_point, radius)
# # move center of second circle upwards
# starting_point[1] = starting_point[1] - radius

# radius = radius // 2

# starting_point[1] = starting_point[1] - radius

# pygame.display.flip()
# pygame.time.wait(8000)
