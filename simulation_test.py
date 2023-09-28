# import pygame
# import random
# import time

# def main():
#     n = 5  # Number of customers
#     t = 10  # Total time
#     customer = [(1,2),(2,3),(5,2),(6,1),(7,2)]

#     pygame.init()
#     screen = pygame.display.set_mode((1000, 600))
#     pygame.display.set_caption("Queue Simulation")

#     people = 450 // n
#     k = 500

#     for i in range(n + 1):
#         font = pygame.font.Font(None, 36)
#         text = font.render(str(i), True, (255, 255, 255))
#         screen.blit(text, (80, k - 5))
#         pygame.draw.line(screen, (255, 255, 255), (95, k), (105, k))
#         k -= people

#     time_interval = 850 // t
#     k = 100

#     for i in range(t + 1):
#         font = pygame.font.Font(None, 36)
#         text = font.render(str(i), True, (255, 255, 255))
#         screen.blit(text, (k, 505))
#         pygame.draw.line(screen, (255, 255, 255), (k, 495), (k, 505))
#         k += time_interval

#     x1, y1, x2, y2 = 100, 500, 100, 300
#     k = 0

#     q = []
#     init = 0
#     i = 0

#     while x1 <= 950:
#         y2 = 50 + (people * (n - len(q)))
#         pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2))

#         if k == time_interval:
#             k = 0
#             init += 1
#             print("Time:", init)
#             if q:
#                 ff, ss = q[0]
#                 if ss == 1:
#                     print(ss, "out")
#                     q.pop(0)
#                 else:
#                     q[0] = (ff, ss - 1)

#         else:
#             color = (255, 255, 255) if q else (0, 0, 0)
#             pygame.draw.line(screen, color, (x1, y1), (x2, y2))

#         if i < len(customer) and init == customer[i][0]:
#             print(customer[i][0], "in")
#             q.append(customer[i])
#             i += 1

#         k += 1
#         x1 += 1
#         x2 += 1

#         pygame.display.update()
#         time.sleep(0.01)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 return

#     pygame.quit()

# if __name__ == "__main__":
#     main()
import pygame
import random
import time

def main():
    n = 5  # Number of customers
    t = 10  # Total time
    customer = [(1,2),(2,3),(5,2),(6,1),(7,2)]

    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Queue Simulation")

    people = 450 // n
    k = 500

    # Define colors
    text_color = (255, 255, 255)  # White text
    line_color = (255, 0, 0)  # Red lines

    for i in range(n + 1):
        font = pygame.font.Font(None, 36)
        text = font.render(str(i), True, text_color)
        screen.blit(text, (80, k - 5))
        pygame.draw.line(screen, line_color, (95, k), (105, k))
        k -= people

    time_interval = 850 // t
    k = 100

    for i in range(t + 1):
        font = pygame.font.Font(None, 36)
        text = font.render(str(i), True, text_color)
        screen.blit(text, (k, 505))
        pygame.draw.line(screen, line_color, (k, 495), (k, 505))
        k += time_interval

    x1, y1, x2, y2 = 100, 500, 100, 300
    k = 0

    q = []
    init = 0
    i = 0

    while x1 <= 950:
        y2 = 50 + (people * (n - len(q)))
        pygame.draw.line(screen, line_color, (x1, y1), (x2, y2))

        if k == time_interval:
            k = 0
            init += 1
            print("Time:", init)
            if q:
                ff, ss = q[0]
                if ss == 1:
                    print(ss, "out")
                    q.pop(0)
                else:
                    q[0] = (ff, ss - 1)

        else:
            pygame.draw.line(screen, line_color, (x1, y1), (x2, y2))

        if i < len(customer) and init == customer[i][0]:
            print(customer[i][0], "in")
            q.append(customer[i])
            i += 1

        k += 1
        x1 += 1
        x2 += 1

        pygame.display.update()
        time.sleep(0.01)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

    pygame.quit()

if __name__ == "__main__":
    main()
