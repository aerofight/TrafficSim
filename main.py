import math
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 1280, 960

# Set up the display and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
frame_rate_cap = 120

# Create a surface for the rectangle
# Should limit speed for an object to move 10% of the screen per second
rect_surface_speed = math.sqrt(WIDTH * HEIGHT) * 0.1 / frame_rate_cap
rect_surface_width, rect_surface_height = 25, 25
rect_surface = pygame.Surface((rect_surface_width, rect_surface_height))  # width, height
rect_surface.fill((0, 0, 255))  # fill the surface with red
rect_surface_pos = pygame.Vector2(WIDTH / 2 - rect_surface_width / 2, HEIGHT / 2 - rect_surface_height / 2)

button_surface = pygame.Surface((100, 100))
button_surface.fill((255, 0, 0))

# Game loop
while True:
    # Handle exit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill('black')

    # Draw the rectangle surface onto the screen
    screen.blit(rect_surface, (rect_surface_pos.x, rect_surface_pos.y))  # x, y coordinates

    key_press = pygame.key.get_pressed()
    if key_press[pygame.K_w]:
        rect_surface_pos.y -= rect_surface_speed
    if key_press[pygame.K_s]:
        rect_surface_pos.y += rect_surface_speed
    if key_press[pygame.K_a]:
        rect_surface_pos.x -= rect_surface_speed
    if key_press[pygame.K_d]:
        rect_surface_pos.x += rect_surface_speed

    # Draw the button
    screen.blit(button_surface, (100, 100))

    # Button checks
    if (pygame.mouse.get_pos()[0] > 100 and
        pygame.mouse.get_pos()[0] < 200 and
        pygame.mouse.get_pos()[1] > 100 and
        pygame.mouse.get_pos()[1] < 200 and
        pygame.mouse.get_pressed()[0]):

        button_surface.fill((0, 255, 0))
    else:
        button_surface.fill((255, 0, 0))

    # Update the display
    pygame.display.flip()

    # limits FPS to the frame_rate_cap
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(frame_rate_cap) / 1000