import pygame

screen_w = 500
screen_h = 500
fpsClock = pygame.time.Clock()
# init stuff
pygame.init()
pygame.font.init()
win = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Bullet and Square")

# player variables
x = 230
y = 400
w = 40
h = 50
vel = 10
tr = x+w
bl = y+h
isJump = False
JDef = 5
jumpC = JDef
Counter = 0
isDead = False
isPaused = False
BestScore = 0
DeathCount = 0


# enemy var
enemy_x = 0
enemy_vel = 10


def reset():
    global enemy_x, Counter, enemy_vel, x, y, isJump, jumpC
    enemy_x = 0
    Counter = 0
    enemy_vel = 10
    x = 230
    y = 400
    isJump = False
    jumpC = JDef


# main loop
run = True
while run:
    # enemy movement
    if not isPaused:
        enemy_x += enemy_vel
        if enemy_x > screen_w:
            enemy_x = 0
            if enemy_vel <= 30:
                enemy_vel += 1
            Counter += 1

    win.fill((0, 0, 255))

    # images
    ground = pygame.image.load(r'.\textures\ground.png')
    bullet = pygame.image.load(r'.\textures\bullet.png')
    # text
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    pointc = myfont.render('Points: '+str(Counter), False, (0, 0, 0))
    deathc = myfont.render('Deaths: '+str(DeathCount), False, (0, 0, 0))
    bestc = myfont.render('Best Score: '+str(BestScore), False, (0, 0, 0))
    pfont = pygame.font.SysFont('Comic Sans MS', 50)
    pausescreen = pfont.render('PAUSED', False, (0, 0, 0))
    win.blit(pointc, (5, 5))
    win.blit(deathc, (5, 25))
    win.blit(bestc, (5, 45))
    if isPaused:
        win.blit(pausescreen, (150, 200))
    # draw objects
    if not isDead:
        player = pygame.draw.rect(win, (255, 255, 0), (x, y, w, h))  # player
        enemy = win.blit(bullet, (enemy_x, 420))
    # pygame.draw.rect(win, (0, 255, 0), (0, 450, screen_w, 50))  # ground
    win.blit(ground, (0, 450))

    pygame.display.update()

    if player.colliderect(enemy):
        print("ok")
        DeathCount += 1
        if Counter > BestScore:
            BestScore = Counter
        print(DeathCount)
        print(BestScore)
        reset()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print('You hit "esc"!')
                if not isPaused:
                    isPaused = True
                    print("paused")
                else:
                    isPaused = False
                    print("unpaused")
    # movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        reset()
    if keys[pygame.K_a] and x > 0 and not isPaused:  # left/right
        x -= vel
    if keys[pygame.K_d] and x < screen_w-w and not isPaused:
        x += vel
    if not isJump and not isPaused:  # jumping
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpC >= -JDef and not isPaused:
            negcheck = 1
            if jumpC < 0:
                negcheck = -1
            y -= (jumpC**2)*negcheck
            jumpC -= 1
        elif not isPaused:
            isJump = False
            jumpC = JDef
            '''
    if keys[pygame.K_ESCAPE]:
        if not isPaused:
            isPaused = True
            if y != 400:
                y = 400
            print("paused")
        else:
            isPaused = False
            print("unpaused")
            '''

    fpsClock.tick(20)


pygame.quit()
