import pygame
import pygame.camera
from pygame.locals import *
import sys

pygame.init()
pygame.camera.init()
x=0
#create fullscreen display 640x480
screen = pygame.display.set_mode((640,480),0)

#find, open and start low-res camera
cam_list = pygame.camera.list_cameras()
print(cam_list)
webcam = pygame.camera.Camera(cam_list[x],(640,480))
webcam.start()

while True:
    #grab image, scale and blit to screen
    imagen = webcam.get_image()
    imagen = pygame.transform.scale(imagen,(640,480))
    screen.blit(imagen,(0,0))

    #draw all updates to display
    pygame.display.update()

    # check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            webcam.stop()
            pygame.quit()
            sys.exit()

