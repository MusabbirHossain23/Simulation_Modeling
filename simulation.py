import pygame
import random
import time

class Customer:
    def __init__(self, arrival_time, service_time):
        self.arrival_time = arrival_time
        self.service_time = service_time

class QueueSimulation:
    def __init__(self, num_customers, total_time):
        self.num_customers = num_customers
        self.total_time = total_time
        self.customers = [Customer(random.randint(1, total_time), random.randint(1, total_time)) for _ in range(num_customers)]
        self.queue = []
        self.clock = pygame.time.Clock()
        self.init_pygame()

    def init_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Queue Simulation")

    def draw_grid(self):
        people = 450 // self.num_customers
        k = 500
        for i in range(self.num_customers + 1):
            font = pygame.font.Font(None, 36)
            text = font.render(str(i), True, (255, 255, 255))
            self.screen.blit(text, (80, k - 5))
            pygame.draw.line(self.screen, (255, 255, 255), (95, k), (105, k))
            k -= people

        time_interval = 850 // self.total_time
        k = 100
        for i in range(self.total_time + 1):
            font = pygame.font.Font(None, 36)
            text = font.render(str(i), True, (255, 255, 255))
            self.screen.blit(text, (k, 505))
            pygame.draw.line(self.screen, (255, 255, 255), (k, 495), (k, 505))
            k += time_interval

    def simulate(self):
        x1, y1, x2, y2 = 100, 500, 100, 300
        k = 0
        init = 0
        i = 0

        while x1 <= 950:
            y2 = 50 + (450 // self.num_customers * (self.num_customers - len(self.queue)))
            pygame.draw.line(self.screen, (255, 255, 255), (x1, y1), (x2, y2))

            if k == (850 // self.total_time):
                k = 0
                init += 1
                print("Time:", init)
                if self.queue:
                    ff, ss = self.queue[0]
                    if ss == 1:
                        print(ss, "out")
                        self.queue.pop(0)
                    else:
                        self.queue[0] = (ff, ss - 1)

            else:
                color = (255, 255, 255) if self.queue else (0, 0, 0)
                pygame.draw.line(self.screen, color, (x1, y1), (x2, y2))

            if i < len(self.customers) and init == self.customers[i].arrival_time:
                print(self.customers[i].arrival_time, "in")
                self.queue.append((self.customers[i].arrival_time, self.customers[i].service_time))
                i += 1

            k += 1
            x1 += 1
            x2 += 1

            pygame.display.update()
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

        pygame.quit()

if __name__ == "__main__":
    simulation = QueueSimulation(num_customers=5, total_time=10)
    simulation.simulate()
