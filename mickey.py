import pygame
import sys
import math
import datetime
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Mickey Clock")

body_img = pygame.image.load("mickeyclock.jpeg").convert_alpha()
right_arm_img = pygame.image.load("mickey_right.png").convert_alpha()
left_arm_img = pygame.image.load("mickey_left.png").convert_alpha()


shoulder_pos = (800 // 2 - 20, 800 // 2)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now = datetime.datetime.now()
    minute, second = now.minute, now.second

    
    angle_minutes = -6 * minute + 90
    angle_seconds = -6 * second + 90

    
    rotated_right_arm = pygame.transform.rotate(right_arm_img, angle_minutes)
    rotated_left_arm = pygame.transform.rotate(left_arm_img, angle_seconds)

    
    screen.blit(body_img, body_img.get_rect(center=(800 // 2, 800 // 2)))
    screen.blit(rotated_right_arm, rotated_right_arm.get_rect(center=shoulder_pos))
    screen.blit(rotated_left_arm, rotated_left_arm.get_rect(center=shoulder_pos))

    pygame.display.update()
