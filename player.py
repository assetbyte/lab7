import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('MP3 Player')

tracks = ['track1.mp3', 'track2.mp3']
current_track = 0

pygame.mixer.init()

def play():
    pygame.mixer.music.load(tracks[current_track])
    pygame.mixer.music.play()
    print(f"Now playing: {tracks[current_track]}")

def next_track():
    global current_track
    current_track = (current_track + 1) % len(tracks)  # Зацикливаем треки
    play()

def previous():
    global current_track
    current_track = (current_track - 1) % len(tracks)  # Зацикливаем треки
    play()

def stop():
    pygame.mixer.music.stop()

is_run = True
while is_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                previous()
            elif event.key == pygame.K_s:
                stop()

pygame.quit()
