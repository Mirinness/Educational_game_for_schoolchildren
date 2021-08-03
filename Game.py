import pygame

pygame.mixer.init()

pygame.init()
width, height = (1280, 720)
win = pygame.display.set_mode((width, height))

pygame.mixer.music.load('b_music.mp3')
pygame.mixer.music.play()

pygame.display.set_caption("Написання З і С у словах")

walkRight = [pygame.image.load('images/right_1.png'),
             pygame.image.load('images/right_2.png'),
             pygame.image.load('images/right_3.png'),
             pygame.image.load('images/right_4.png'),
             pygame.image.load('images/right_5.png'),
             pygame.image.load('images/right_6.png')]

walkStay = [pygame.image.load('images/stay_1.png'),
             pygame.image.load('images/stay_2.png'),
             pygame.image.load('images/stay_3.png'),
             pygame.image.load('images/stay_4.png'),
             pygame.image.load('images/stay_5.png')]

walkJump = [pygame.image.load('images/jump_1.png'),
            pygame.image.load('images/jump_2.png'),
            pygame.image.load('images/jump_3.png'),]

bellSound = pygame.mixer.Sound("bell.wav")
jumpSound = pygame.mixer.Sound("jump_s.wav")
okSound = pygame.mixer.Sound("ok_s.wav")
noSound = pygame.mixer.Sound("no_s.wav")

clock = pygame.time.Clock()
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)
font = pygame.font.Font(None, 50)
text1 = 'правильно'
correct = font.render(text1, True, GREEN)
text2 = 'не правильно'
wrong = font.render(text2, True, RED)
text3 = 'test'
text = font.render(text3, True, BLUE)
text4 = 'правильна відповідь'
lvl = font.render(text4, True, BLUE)
x = 0
y = 555
x1 = 0
x2 = 0
speed = 10
isJump = False
jumpcount = 10
right = False
stay = True
animcount = 0
second3 = pygame.image.load("images/second3.png")
first3 = pygame.image.load("images/first3.png")
third = pygame.image.load("images/third.png")
#--------------------
next=False
quest=""
answ=""
count=""
obj1=1300
obj2=2100
ans1=False
ans2=False
mon1 = pygame.image.load("images/z.png")
mon2 = pygame.image.load("images/s.png")
array = [[], []]


def draw_window():#------------------------------------------------------------
    global animcount, x1, x2, obj1, obj2, ans1, ans2, text3, next, count
    win.blit(third, (0, 0))
    win.blit(second3, (x2, 0))
    win.blit(first3, (x1, 0))
    win.blit(mon1, (obj1, 570))
    win.blit(mon2, (obj2, 570))
    if right or (right and isJump):
        obj1-=10
        obj2-=10
        if 75<=obj1<=85 and isJump==False:
            if count!="0":
                count=count+"0"
                bellSound.play()
        if 75<=obj1<=85 and isJump==True:
            if count!="1":
                count=count+"1"
        if 75<=obj2<=85 and isJump==False:
            if count!="2":
                count=count+"2"
                bellSound.play()
        if 75<=obj2<=85 and isJump==True:
            if count!="3":
                count=count+"3"

    win.blit(text, text.get_rect(centerx=640, centery=150))

    if ans1==True and obj2<-100 and count=="03":
        okSound.play()
        win.blit(correct, text.get_rect(centerx=640, centery=200))
    elif ans1==True and obj2<-100:
        noSound.play()
        win.blit(wrong, text.get_rect(centerx=640, centery=200))
    if -700<=obj2<=-100:
        win.blit(lvl, text.get_rect(centerx=640, centery=300))

    if ans2==True and obj2<-100 and count=="12":
        okSound.play()
        win.blit(correct, text.get_rect(centerx=640, centery=200))
    elif ans2==True and obj2<-100:
        noSound.play()
        win.blit(wrong, text.get_rect(centerx=640, centery=200))
    if -700<=obj2<=-100:
        win.blit(lvl, text.get_rect(centerx=640, centery=300))

    if obj2<-700:
        next=True

    if right:
        if x2 <= -1280:
            x2 = 0
        else:
            x2 -= 5
        if x1 <= -1280:
            x1 = 0
        else:
            x1 -= 10

    if animcount + 1 >= 30:
        animcount = 0

    if isJump:
        win.blit(walkJump[animcount // 8], (x, y-40))
        animcount += 1
    elif right:
        win.blit(walkRight[animcount // 5], (x, y))
        animcount += 1
    elif stay:
        win.blit(walkStay[animcount // 6], (x, y))
        animcount += 1



    pygame.display.update()
#-------------------------------------------------------------------------------

with open('task1.txt', encoding='utf8') as file:
    for line in file.readlines():
        array[0].append(line.strip().split(' ')[0])
        array[1].append(line.strip().split(' ')[1])
    for i in range(15):
        next=False
        quest=array[0][i]
        answ=array[1][i]
        text=font.render(quest, True, BLUE)
        obj1=1300
        obj2=2100
        count=""
        text4 = 'правильна відповідь'
        text4 = text4 + " " + answ + quest
        lvl = font.render(text4, True, BLUE)


        if answ=='з':
            ans1=True
            ans2=False
        else:
            ans1=False
            ans2=True

        while not next:
            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                right = True
            if keys[pygame.K_LEFT]:
                animcount = 0
                right = False
            if not isJump:
                if keys[pygame.K_UP]:
                    jumpSound.play()
                    animcount = 0
                    isJump = True
            else:
                if jumpcount >= -10:
                    if jumpcount < 0:
                        y += (jumpcount ** 2) / 2
                    else:
                        y -= (jumpcount ** 2) / 2
                    jumpcount -= 1
                else:
                    isJump = False
                    jumpcount = 10
            draw_window()
    pygame.quit()
