#Created in Aryan Rekhi
import pygame

pygame.init()

win = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Battle of Saiyans : Goku v Vegeta")
# we add 3 elements in both of the lists below
''' 0: large stride
    1: small stride
    2: jump'''
walkRight = [pygame.image.load('pics\\GokuR2x.png'), pygame.image.load('pics\\GokuR3x.png'),pygame.image.load('pics\\GokuR1x.png')]
walkLeft = [pygame.image.load('pics\\GokuL2x.png'), pygame.image.load('pics\\GokuL3x.png'),pygame.image.load('pics\\GokuL1x.png')]

bg = pygame.image.load('pics\\bodybg.jpg')
stan = pygame.image.load('pics\\GokuSx.png')

Gh = pygame.image.load('pics\\gh1-modified.png')
Vh = pygame.image.load('pics\\Vh.png')

bgm = pygame.mixer.music.load("pics\\Royal Blue (Vegeta's Limit Breaker Theme) - Dragon Ball Super (Extended Version).mp3")
hitSound = pygame.mixer.Sound("pics\\kiblast.mp3")
collisionSound = pygame.mixer.Sound("pics\\punch.mp3")

pygame.mixer.music.play()



Clock = pygame.time.Clock()


class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 10
        self.isjump = False  # if it is in jumping
        self.jumpheight = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 10, self.y + 5, 80, 80) # for collision purposes
        self.health = 200 # player health

    def draw(self, win):

        if self.health >0:


            if self.walkCount + 1 > 6:  # if we exceed 6 it will show length error
                self.walkCount = 0

            if not (self.standing):

                if self.left:  # run in left w/o jumping
                    win.blit(walkLeft[self.walkCount // 2], (
                    self.x, self.y))  # divide by 2 because we are flipping two images it would be //3 for 3 images
                    self.walkCount += 1  # to flip the imgs

                elif self.right:  # run in right w/o jumping
                    win.blit(walkRight[self.walkCount // 2], (self.x, self.y))
                self.walkCount += 1  # to flip the imgs

            else:
                if self.right:
                    win.blit(pygame.image.load('pics\\GokuR1x.png'), (self.x, self.y))
                else:
                    win.blit(pygame.image.load('pics\\GokuSx.png'), (self.x, self.y))

            self.hitbox = (self.x + 10, self.y + 5, 80, 80)
            Gbar2 = pygame.draw.rect(win,(255,0,0),(80,40,210,25)) #health bar background
            Gbar = pygame.draw.rect(win,(255,255,0),(80,45,self.health,15)) #health bar
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        else:
            #Remind me to add picture here
            #text = font.render('Vegeta Wins', True, (255, 255, 255), (255, 0, 0))
            win.blit(pygame.image.load('pics\\VegetaW.jpeg'), (200,200))
            #win.blit(text, (100, 200))
            win.blit(pygame.image.load('pics\\GokuDx.png'),(self.x,self.y))

    def hit(self): #health decreasing logic
        if self.health > 0:
            self.health -= 5
            # print("Goku Damage")
        else:
            print("Goku Died")


class weapons():

    def __init__(self, x, y, width, height, facing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.facing = facing
        self.velocity = 8 * facing
        self.hitbox = (self.x, self.y, 40, 40)

    def draw(self, win):
        win.blit(pygame.image.load('pics\\Daco_2529631.png'), (self.x, self.y))  # ki blast img
        self.hitbox = (self.x, self.y, 40, 40)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


# vegeta class
class enemy():
    # loading vegeta sprites
    walkRightV = [pygame.image.load('pics\\VR2.png'), pygame.image.load('pics\\VR3.png'),pygame.image.load("pics\\VR1.png")]
    walkLeftV = [pygame.image.load('pics\\VL2cs.png'), pygame.image.load('pics\\VL3cs.png'),pygame.image.load('pics\\VL1cs.png')]

    def __init__(self, x, y, width, height, end):  # end is just to tell the enemy to flip after touching borders
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.speed = 8
        self.walkCount = 0
        self.hitbox = (self.x + 10, self.y + 5, 80, 80)
        self.health = 200

    def draw(self, win):
        self.move()

        if self.health > 0:

            if self.walkCount + 1 >= 6:
                self.walkCount = 0

            if self.speed > 0:
                win.blit(self.walkRightV[self.walkCount // 2],(self.x, self.y))  # self.walkCount is put in a list cuz we made it inside a class
                self.walkCount += 1

            else:
                win.blit(self.walkLeftV[self.walkCount // 2],(self.x, self.y))  # self.walkCount is put in a list cuz we made it inside a class
                self.walkCount += 1

            self.hitbox = (self.x + 10, self.y + 5, 80, 80)
            Vbar2 = pygame.draw.rect(win,(0,0,0),(410,40,210,25)) #health bar background
            Vbar = pygame.draw.rect(win,(255,255,0),(620, 45, -self.health, 15)) #health bar

            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        else:
            self.speed = 0
            #text = font.render('Goku Wins',True,(0,0,255),(255,100,10))
            win.blit(pygame.image.load('pics\\GokuW.jpeg'),(200,200))
            win.blit(pygame.image.load('pics\\vd1raw-removebg-preview.png'),(self.x,self.y))

    # func for enemy movement
    def move(self):

        if self.speed > 0:

            if self.x + self.speed < self.path[1]:
                self.x += self.speed
            else:
                self.speed = self.speed * -1  # in pygame multiply by 1 and -1 means going in positive and negative direction respectively
                self.walkCount = 0

        else:
            if self.x - self.speed > self.path[0]:
                self.x += self.speed

            else:
                self.speed = self.speed * -1
                self.walkCount = 0

    def hit(self):  # collison/hit purposes
        if self.health > 0:
            self.health -= 10

        else:
            print('vegeta died ')
        #print("Hit")  # so as to whenever goku n vegeta collide hit prints in our console


run = True


def Redrawgamewindow():
    win.blit(bg, (0, 0))
    goku.draw(win)
    vegeta.draw(win)
    win.blit(Gh,(10,10))
    win.blit(Vh,(600,10))

    for kiblast in kiblasts:
        kiblast.draw(win)

    pygame.display.update()  # update it shifted upwards to make the code cleaner


'''
    global left
    global right
    global walkCount '''
# globalizing the variable to update the values in the whole program

font = pygame.font.SysFont('comicsans',60,True)

goku = player(30, 400, 100, 100)
vegeta = enemy(120, 400, 100, 100, 600)
kiblasts = []
throwSpeed = 0

while run:

    ### FRAME RATE ###
    Clock.tick(25)
    #############

    # putting limits in kiblast speeds
    if throwSpeed > 0:
        throwSpeed += 1
    if throwSpeed > 3:
        throwSpeed = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if goku.health > 0 and vegeta.health > 0:
        if goku.hitbox[1] < vegeta.hitbox[1] + vegeta.hitbox[3] and goku.hitbox[1] + goku.hitbox[3] > vegeta.hitbox[1]:
            if goku.hitbox[0] + goku.hitbox[2] > vegeta.hitbox[0] and goku.hitbox[0] < vegeta.hitbox[0] + vegeta.hitbox[2]:
                goku.hit()
                collisionSound.play()

    else:
        if goku.health == 0:
            goku.speed = 0



    # making boundaries for ki blast below
    for kiblast in kiblasts:

        if vegeta.health >0:


            if kiblast.hitbox[1] + round(kiblast.hitbox[3] / 2) > vegeta.hitbox[1] and kiblast.hitbox[1] + round(kiblast.hitbox[3] / 2) < vegeta.hitbox[1] + vegeta.hitbox[3]:
                if kiblast.hitbox[0] + kiblast.hitbox[2] > vegeta.hitbox[0] and kiblast.hitbox[0] + kiblast.hitbox[2] < vegeta.hitbox[0] + vegeta.hitbox[2]:
                    vegeta.hit()  # calling hit function
                    hitSound.play() # plays ki blast sound
                    kiblasts.pop(kiblasts.index(kiblast))

        else:
            vegeta.speed = 0 #when player dies(i.e. health turns to zero) his speed turns into zero and he stops moving


        if kiblast.x < 699 and kiblast.x > 0:
            kiblast.x += kiblast.velocity

        else:
            kiblasts.pop(kiblasts.index(kiblast))

    ### KEYS ###
    keys = pygame.key.get_pressed()
    # the code after and" in the next two if conditions are used to create boundaries
    # we use the object 'goku' instead of self because we cannot use self outside the class

    ###SHOOTING###

    if keys[pygame.K_SPACE] and throwSpeed == 0:
        if goku.left == True:
            facing = -1

        else:
            facing = 1

        if len(kiblasts) < 5:
            kiblasts.append(weapons(round(goku.x + 10), round(goku.y + 30), 40, 40, facing))
        throwSpeed = 1
        # 'goku.width//2' is done so as to make the ki blast shoot from the centre of is body i.e. half of his body(//2)
        # 40,40 is the dimensions of the ki blast

    ### LEFT DIRECTION ###
    if keys[pygame.K_LEFT] and goku.x > goku.speed:
        """x > speed is a logic used to make boundary 
        in the left side of the window """
        goku.x -= goku.speed
        goku.left = True
        goku.right = False
        goku.standing = False

    ### RIGHT DIRECTION ###
    elif keys[pygame.K_RIGHT] and goku.x < 690 - goku.width - goku.speed:
        """To make the right most boundary i used  little
         different logic because pygame marks the coordinate (0,0) 
        from the top left of the window and so as to make the character stop at the boundary 
        i had to subract it with width and then speed"""
        goku.x += goku.speed
        goku.left = False
        goku.right = True
        goku.standing = False

    # For K_LEFT Left is true and right is false and vice versa for K_RIGHT

    else:
        goku.standing = True
        '''
        goku.left = False
        goku.right = False
        '''
        goku.walkCount = 0
    # this is done tp stop the legs during jump and also stop the legs when button is released
    # same is done in the code down below

    ####JUMP LOGIC ####
    if goku.isjump == False:
        if keys[pygame.K_UP]:
            goku.isjump = True
            goku.left = False
            goku.right = False
            goku.walkCount = 0  # this is done tp stop the legs during jump and also stop the legs when button is released

    else:
        if goku.jumpheight >= -10:
            neg = 1

            if goku.jumpheight < 0:
                neg = -1

            goku.y -= (goku.jumpheight ** 2) * 0.5 * neg  # eqn of y during free fall
            goku.jumpheight -= 1
        else:
            goku.isjump = False
            goku.jumpheight = 10

    # win.fill((0,0,0))
    # we wont be needing winfill as we are adding a background image
    # we will remove this rectangle because we dont need this as we are adding characters instead
    # pygame.draw.rect(win,(255,255,255),(x,y,width,height))

    Redrawgamewindow()

pygame.quit()
