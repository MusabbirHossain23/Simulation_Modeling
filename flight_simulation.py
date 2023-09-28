import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
AIRSPEED = 1
ROTATE_SPEED = 1

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flight Simulator")

# Aircraft properties
aircraft_x, aircraft_y = WIDTH // 2, HEIGHT // 2
aircraft_width, aircraft_height = 40, 40
angle = 0

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle += ROTATE_SPEED
    if keys[pygame.K_RIGHT]:
        angle -= ROTATE_SPEED

    # Calculate the new position based on the angle
    angle_rad = math.radians(angle)
    dx = AIRSPEED * math.cos(angle_rad)
    dy = -AIRSPEED * math.sin(angle_rad)

    aircraft_x += dx
    aircraft_y += dy

    # Clear the screen
    screen.fill(BLUE)

    # Draw the aircraft (rectangle)
    rotated_aircraft = pygame.transform.rotate(pygame.Surface((aircraft_width, aircraft_height)), angle)
    rotated_aircraft_rect = rotated_aircraft.get_rect(center=(aircraft_x, aircraft_y))
    pygame.draw.rect(rotated_aircraft, WHITE, rotated_aircraft_rect)
    screen.blit(rotated_aircraft, rotated_aircraft_rect.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
