# import the pygame module, so you can use it
import threading
import pygame
import random
import time
import sys
import math

pos_arr = []
def adj (b1,b2):
    dist = math.sqrt((b1[0]-b2[0])**2 + (b1[1]-b2[1])**2)
    return  dist <= circle_radius == True
def overlap():
    color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    sleep_time = random.randrange(1, 10) / 2
    lock.acquire()
    j = True
    while(j):
        pos = [random.randrange(circle_radius, 640-circle_radius), random.randrange(circle_radius, 480-circle_radius)]
        can_place = True
        for i in pos_arr:
            if adj(pos,i):
                can_place = False
        if can_place == True:
            j = False
            pos_arr.append(pos)
            lock.release()
            draw_circle(pos,sleep_time,color)
          
    

def draw_circle(pos, sleep_time, color):
        # clear previous circle
    pygame.draw.circle(screen, black, pos, circle_radius, 0)

        # draw circle on a new position
    pygame.draw.circle(screen, color, pos, circle_radius, 0)

        # Draws the surface object to the screen.
    pygame.display.update()
    time.sleep(sleep_time)

    # clear last circle
    pygame.draw.circle(screen, black, pos, circle_radius, 0)
    pygame.display.update()
    pos_arr.remove(pos)

position = [0, 0]
black = (0, 0, 0)
test = False
circle_radius = 20

num_of_threads = int(input('How many running balls would you like? '))

# initialize the pygame module
pygame.init()
pygame.display.set_caption("Running Balls")

# create a surface on screen that has the size of 240 x 180
screen = pygame.display.set_mode((640, 480))

# define a variable to control the main loop
running = True
threads_list = []
threads_flag = []
lock = threading.Lock()
for i in range(num_of_threads):
    
    t = threading.Thread(target=overlap, )
    threads_list.append(t)
    threads_flag.append(True)
    t.start()
    print(f'{t.name} Started')

# main loop
while running:

    current_running_thread = 0
    for i in range(len(threads_list)):
        if threads_list[i].is_alive():
            current_running_thread += 1
        elif threads_flag[i]:
            print(f'{threads_list[i].name} was ended')
            threads_flag[i] = False

    pygame.display.set_caption(f"{current_running_thread} Running Balls")

    if threading.active_count() == 1:
        running = False

    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False

pygame.quit()
sys.exit()