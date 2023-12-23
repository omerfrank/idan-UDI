# import the pygame module, so you can use it
import threading
import pygame
import random
import time
import sys

position = [0, 0]
black = (0, 0, 0)
sleep_time = 1

def thread_manager():
    t1 = threading.Thread(target=draw_circle, args=([random.randrange(10, 630),random.randrange(10, 470)], random.randrange(1, 5)))
    t1.start()
    print(t1.name)
    t1.join()
    if t1.is_alive() == False:
        print(t1.name)
        

def draw_circle(position, sleep_time):

        time.sleep(sleep_time)

        # clear previous circle
        pygame.draw.circle(screen, black, position, 10, 0)

        # draw circle on a new position
        position = [random.randrange(10, 630), random.randrange(10, 470)]
        color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        pygame.draw.circle(screen, color, position, 10, 0)

        # Draws the surface object to the screen.
        pygame.display.update()


# initialize the pygame module
pygame.init()

i = int(input("how many balls? "))
pygame.display.set_caption(f"{i}")
arr = []
# create a surface on screen that has the size of 240 x 180
screen = pygame.display.set_mode((640, 480))

# define a variable to control the main loop
running = True
for i in range(i):
    t1 = threading.Thread(target=thread_manager)
    t1.start()
# main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False
    if  threading.enumerate() == False:
        running = False


pygame.quit()
sys.exit()