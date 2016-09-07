import pygame, sys

pygame.init()

windowSize = (800, 600)

screen = pygame.display.set_mode(windowSize)

helloWorld = pygame.image.load("mario-icon.png")
helloWorldSize = helloWorld.get_size()

pygame.mouse.set_visible(False)

x, y = 0, 0
directionX, directionY = 1, 1

clock = pygame.time.Clock()

sound = pygame.mixer.Sound("punch.wav")

while True:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            x += 5
        if event.key == pygame.K_LEFT:
            x -= 5

        if event.key == pygame.K_DOWN:
            y += 5
        if event.key == pygame.K_UP:
            y -= 5

    screen.fill((0, 0, 0))

    if x + helloWorldSize[0] > 800:
        x = 800 - helloWorldSize[0]
        sound.stop()
        sound.play()

    if y + helloWorldSize[1] > 600:
        y = 600 - helloWorldSize[1]
        sound.stop()
        sound.play()

    if x <= 0:
        sound.stop()
        sound.play()
        x = 0
    if y <= 0:
        sound.stop()
        sound.play()
        y = 0

    screen.blit(helloWorld, (x, y))

    pygame.display.update()
