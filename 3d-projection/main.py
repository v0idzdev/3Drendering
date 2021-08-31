# IMPORTS
from matrix import matrix_multiplication
from math import sin, cos
import pygame
import os

# Environment configuration
os.environ["SDL_VIDEO_CENTERED"] = '1'

# Window size
WIDTH_ = 1920
HEIGHT_ = 1080

# Colours
WHITE = (250, 250, 250)
BLACK = (25, 25, 25)

# Pygame init
pygame.init()
pygame.display.set_caption("3D Projection")
screen = pygame.display.set_mode((WIDTH_, HEIGHT_))
clock_tick = pygame.time.Clock()
fps = 60

# Shape properties
shape_pos = [WIDTH_//2, HEIGHT_//2]
angle = 0
scale = 600
speed = 0.01
points = [n for n in range(8)]

# Defining points of the cube
points[0] = [[-1], [-1], [1]]
points[1] = [[1], [-1], [1]]
points[2] = [[1], [1], [1]]
points[3] = [[-1], [1], [1]]
points[4] = [[-1], [-1], [-1]]
points[5] = [[1], [-1], [-1]]
points[6] = [[1], [1], [-1]]
points[7] = [[-1], [1], [-1]]


# Connects and draws cube points
def connect_point(i, j, k):
    a = k[i]
    b = k[j]
    pygame.draw.line(screen, WHITE, (a[0], a[1]), (b[0], b[1]), 4)


# Sets up main loop
run_simulation = True
while run_simulation:

    # Clock and colour init
    clock_tick.tick(fps)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_simulation = False

    # Sets up simulation
    index = 0
    projected_points = [j for j in range(len(points))]

    rotation_x = [[1, 0, 0],  # Rotation maths
                  [0, cos(angle), -sin(angle)],
                  [0, sin(angle), cos(angle)]]
    rotation_y = [[cos(angle), 0, -sin(angle)],
                  [0, 1, 0],
                  [sin(angle), 0, cos(angle)]]
    rotation_z = [[cos(angle), -sin(angle), 0],
                  [sin(angle), cos(angle), 0],
                  [0, 0, 1]]

    # Rotates and draws
    # cube on the screen
    for point in points:

        rotated_in_2d = matrix_multiplication(rotation_y, point)
        rotated_in_2d = matrix_multiplication(rotation_x, rotated_in_2d)
        rotated_in_2d = matrix_multiplication(rotation_z, rotated_in_2d)

        distance = 5
        z = 1/(distance - rotated_in_2d[2][0])

        projection_matrix = [[z, 0, 0],
                             [0, z, 0]]

        projected_in_2d = matrix_multiplication(
            projection_matrix, rotated_in_2d)

        x = int(projected_in_2d[0][0] * scale) + shape_pos[0]
        y = int(projected_in_2d[1][0] * scale) + shape_pos[1]

        projected_points[index] = [x, y]
        index += 1

    # Connects points
    for m in range(4):
        connect_point(m, (m+1) % 4, projected_points)
        connect_point(m+4, (m+1) % 4+4, projected_points)
        connect_point(m, m+4, projected_points)

    # Update display
    angle += speed
    pygame.display.update()

pygame.quit()
