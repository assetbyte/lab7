import pygame

pygame.init()

screen = pygame.display.set_mode((600,400))
screen.fill((255,255,255))

x, y = 300, 200 

running = True
while running:
    
    pygame.draw.circle(screen, 'Red', (x, y), 25)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ww and y - 25 - 20 >= 0:
                y -= 20
            elif event.key == pygame.K_s and y + 25 + 20 <= 400:
                y += 20
            elif event.key == pygame.K_a and x - 25 - 20 >= 0:
                x -= 20
            elif event.key == pygame.K_d and x + 25 + 20 <= 600:
                x += 20

    screen.fill((255,255,255)) 
