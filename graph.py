import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
n = 5  # Number of customers
t = 10  # Total time
width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Queue Simulation")

# Colors
WHITE = (255, 255, 255)

# Initialize clock
clock = pygame.time.Clock()

# Customer data
customer = [(1, 2), (2, 3), (5, 2), (6, 1), (7, 2)]
customer.sort()

# Calculate positions
people = 450 // n
k = 500

for i in range(n + 1):
    font = pygame.font.Font(None, 36)
    text = font.render(str(i), True, WHITE)
    screen.blit(text, (80, k - 5))
    pygame.draw.line(screen, WHITE, (95, k), (105, k))
    k -= people

time_interval = 850 // t
k = 100

for i in range(t + 1):
    font = pygame.font.Font(None, 36)
    text = font.render(str(i), True, WHITE)
    screen.blit(text, (k, 505))
    pygame.draw.line(screen, WHITE, (k, 495), (k, 505))
    k += time_interval

x1, y1, x2, y2 = 100, 500, 100, 300
k = 0

customer_queue = []
init_time = 0
i = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    y2 = 50 + (people * (n - len(customer_queue)))
    pygame.draw.line(screen, WHITE, (x1, y1), (x2, y2))

    if k == time_interval:
        k = 0
        init_time += 1
        print("Time:", init_time)
        if customer_queue:
            ff, ss = customer_queue[0]
            if ss == 1:
                print(ss, "out")
                customer_queue.pop(0)
            else:
                customer_queue[0] = (ff, ss - 1)

    else:
        color = (len(customer_queue) % 16) + 7
        pygame.draw.circle(screen, (255, 255, 255), (x2, y2), 1)

    if i < len(customer) and init_time == customer[i][0]:
        print(customer[i][0], "in")
        customer_queue.append(customer[i])
        i += 1

    k += 1
    x1 += 1
    x2 += 1

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
