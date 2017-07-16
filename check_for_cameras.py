import pygame
import pygame.camera

pygame.init()
pygame.camera.init()
#find, list cameras
cam_list = pygame.camera.list_cameras()
print(cam_list)
