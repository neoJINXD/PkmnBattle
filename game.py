'''
Anik Patel
May 16th, 2018
R. Vincent, instructor
Final Project - PyGame game
'''

import sys, pygame, random
from characters import Player, Enemy

#Initializes all the pygame modules so they can be used
pygame.init()

#Based on the pygame beginner tutorial code-------------------------
#Sets up the size of the window
size = width, height = 1024, 576

#Resizes and prints the background image
background = pygame.image.load('media/images/stadium.jpg')
background = pygame.transform.scale(background, [1024,576])
screen = pygame.display.set_mode(size)

#-------------------------------------------------------------------

#Sets up RGB code for colours
black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0
red = 255, 0, 0
yellow = 255, 215, 0
glow = 47, 79, 79


#Text display helper function from https://pythonprogramming.net/displaying-text-pygame-screen/
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


#Tuples with the stats, character names, and all the attack names for the characters
charlist = ('Charizard', 'Feraligatr', 'Sceptile')
atckph = (84, 105, 85)
atcksp = (109, 79, 105)
defense = (82, 92, 75)
speed = ('100', '78', '120')
pkmtype = ('Fire', 'Water', 'Grass')
phymoves = ('Slash','Crunch','Dragon Claw')
specmoves = ('Flamethrower','Surf','Energy Ball')
healmov = ('Roost','Eat Berry','Synthesis')
#Sets up and sets player and enemy id and stats
playerid = None
enemyid = None

#Sets up characters based on the classes made in the character.py file
cId = random.randint(0, 2)
if playerid == None:
    playerid = cId
    playername = charlist[cId]
    playerph = atckph[cId]
    playersp = atcksp[cId]
    playerd = defense[cId]
    playerspd = speed[cId]
    playertype = pkmtype[cId]
eId = random.randint(0, 2)
if enemyid == None:
    enemyid = eId
    enemyname = charlist[eId]
    enemyph = atckph[eId]
    enemysp = atcksp[eId]
    enemyd = defense[eId]
    enemyspd = speed[eId]
    enemytype = pkmtype[eId]
print(playerid, playertype, playername, enemyid, enemytype, enemyname)

player = Player(playername, playerid, playerph, playersp, playerd, playerspd, playertype)
enemy = Enemy(enemyname, enemyid, enemyph, enemysp, enemyd, enemyspd, enemytype)

#Sets up and resizes the character sprites
playersprite = pygame.image.load('media/images/'+player.name+'P.png')
playersprite = pygame.transform.scale(playersprite, [128,128])
enemysprite = pygame.image.load('media/images/'+enemy.name+'E.png')
enemysprite = pygame.transform.scale(enemysprite, [128,128])





def hpcolour(health):
    '''Defines the colour for the health bars, regular is green, less than 50%
    goes to yellow, and less than 25% goes to red'''
    if health < 25:
        return red
    elif health < 50:
        return yellow
    else:
        return green

font = pygame.font.Font('pokemon.ttf', 16)

#Setting up the enemys attack--------------

def enemyatt():
    '''Makes the enemy attack your character based on random chance, increases
    the chance of healign when health is lower than 50%'''
    chance = random.randrange(98)
    if enemy.health < 50:
        if chance < 20:
            enemy.physical(player)
            txtattSurface, txtattRect = text_objects(charlist[enemy.id]+'   used   '+phymoves[enemy.id], font)
            txtattRect.center = ((1024*(3/4)),(550+(26//2)))
            screen.blit(txtattSurface, txtattRect)
            pygame.display.update(txtattRect)
            #pygame.time.Clock().tick(3)
            pygame.draw.rect(background, white, (0, 550, 1024, 26))
            
        elif chance < 40:
            txtattSurface, txtattRect = text_objects(charlist[enemy.id]+'   used   '+specmoves[enemy.id], font)
            txtattRect.center = ((1024*(3/4)),(550+(26//2)))
            screen.blit(txtattSurface, txtattRect)
            pygame.display.update(txtattRect)
            #pygame.time.Clock().tick(3)
            pygame.draw.rect(background, white, (0, 550, 1024, 26))
        else:
            enemy.heal()
            txtattSurface, txtattRect = text_objects(charlist[enemy.id]+'   used   '+healmov[enemy.id], font)
            txtattRect.center = ((1024*(3/4)),(550+(26//2)))
            screen.blit(txtattSurface, txtattRect)
            pygame.display.update(txtattRect)
            #pygame.time.Clock().tick(3)
            pygame.draw.rect(background, white, (0, 550, 1024, 26))
    else:
        if chance < 53:
            enemy.physical(player)
            txtattSurface, txtattRect = text_objects(charlist[enemy.id]+'   used   '+phymoves[enemy.id], font)
            txtattRect.center = ((1024*(3/4)),(550+(26//2)))
            screen.blit(txtattSurface, txtattRect)
            pygame.display.update(txtattRect)
            #pygame.time.Clock().tick(3)
            pygame.draw.rect(background, white, (0, 550, 1024, 26))
        elif chance < 86:
            enemy.special(player)
            txtattSurface, txtattRect = text_objects(charlist[enemy.id]+'   used   '+specmoves[enemy.id], font)
            txtattRect.center = ((1024*(3/4)),(550+(26//2)))
            screen.blit(txtattSurface, txtattRect)
            pygame.display.update(txtattRect)
            #pygame.time.Clock().tick(3)
            pygame.draw.rect(background, white, (0, 550, 1024, 26))
        else:
            enemy.heal()
            txtattSurface, txtattRect = text_objects(charlist[enemy.id]+'   used   '+healmov[enemy.id], font)
            txtattRect.center = ((1024*(3/4)),(550+(26//2)))
            screen.blit(txtattSurface, txtattRect)
            pygame.display.update(txtattRect)
            #pygame.time.Clock().tick(3)
            pygame.draw.rect(background, white, (0, 550, 1024, 26))



#------------------------------------------



#Based on the button function in sentdex's youtube guide on pygame development (https://pythonprogramming.net/pygame-button-function-events/)
def Button(msg, posx, posy, width, height, inactive, active, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if posx + width > mouse[0] > posx and posy+height > mouse[1] > posy:
        pygame.draw.rect(background, active, (posx, posy, width, height))
        if click[0] == 1 and action != None:
            if action == 'Physical attack':
                physattack()
                enemyatt()
                pygame.time.delay(2000)
            elif action == 'Special attack':
                speattack()
                enemyatt()
                pygame.time.delay(2000)
            elif action == 'Heal':
                healmove()
                enemyatt()
                pygame.time.delay(2000)
    else:
        pygame.draw.rect(background, inactive, (posx, posy, width, height))

    txtSurface, txtRect = text_objects(msg, font)
    txtRect.center = ((posx+(width//2)),(posy+(height//2)))
    screen.blit(txtSurface, txtRect)
    


def physattack():
    '''Initiates the players regular physical'''
    player.physical(enemy)
    #Prints the text of the move used on the white bar
    txtattSurface, txtattRect = text_objects(charlist[player.id]+'   used   '+phymoves[player.id], font)
    txtattRect.center = ((1024//4),(550+(26//2)))
    screen.blit(txtattSurface, txtattRect)
    pygame.display.update(txtattRect)
    #pygame.time.Clock().tick(3)


def speattack():
    '''Initiates the players special move, that has type effectiveness'''
    player.special(enemy)
    #Prints the text of the move used on the white bar
    txtattSurface, txtattRect = text_objects(charlist[player.id]+'   used   '+specmoves[player.id], font)
    txtattRect.center = ((1024//4),(550+(26//2)))
    screen.blit(txtattSurface, txtattRect)
    pygame.display.update(txtattRect)
    #pygame.time.Clock().tick(3)


def healmove():
    '''Initiates the players heal based on the method'''
    player.heal()
    #Prints the text of the move used on the white bar
    txtattSurface, txtattRect = text_objects(charlist[player.id]+'   used   '+healmov[player.id], font)
    txtattRect.center = ((1024//4),(550+(26//2)))
    screen.blit(txtattSurface, txtattRect)
    pygame.display.update(txtattRect)
    #pygame.time.Clock().tick(3)




#------Music----------loops when song is finished------------------------------
def music():
    '''Plays the music file that gets open'''
    playlist = list()
    playlist.append('media/sfx/battle.mp3')
    pygame.mixer.music.load(playlist[0])
    pygame.mixer.music.play(-1)

#-----------song from: https://www.youtube.com/watch?v=Jxk9DqdYsJ4--------------

#------Health Bars---------------------------------------------------
def hpbar():
    '''Defines the health bars postitions and their colour'''
    pygame.draw.rect(background, hpcolour(player.health), (153, 200, 275 , 25))
    pygame.draw.rect(background, hpcolour(enemy.health), (600, 200, 275 , 25))

    #Display the current hp for player and enemy health bars
    playerhpSurf, playerhpRect = text_objects(str(player.health), font)
    playerhpRect.center = (((153+(275//2))),((200+(25//2))))
    screen.blit(playerhpSurf, playerhpRect)

    enemyhpSurf, enemyhpRect = text_objects(str(enemy.health), font)
    enemyhpRect.center = ((600+(275//2)),(200+(25//2)))
    screen.blit(enemyhpSurf, enemyhpRect)



#--------------------------------------------------------------------



if __name__ == '__main__':
    music()
    while True:
        #Creates the condition where pressing the 'x' button on the window closes the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #Gets the information of if the mouse has been clicked
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(background, white, (0, 550, 1024, 26))
        #Sets up the background arena picture, setting at 0,0 starting at top left
        screen.blit(background, [0,0])
        #Draws rectangles for health bars of player and oposing characters
        hpbar()

        #Draws the randomly selected character sprites
        screen.blit(playersprite, [300,275])
        screen.blit(enemysprite, [600,275])
        #Sets up attack buttons

        Button('Physical', 153, 475, 150, 50, black, glow, 'Physical attack')
        Button('Special', 425, 475, 150, 50, black, glow, 'Special attack')
        Button('Heal', 700, 475, 150, 50, black, glow, 'Heal')


        #Goes through the turn and attack selection
        print('Player: ' + str(player.health))
        print('Enemy: ' + str(enemy.health))

        #Sets up the win/lose condition, when hp is 0
        if enemy.health <= 0:
            screen.fill(white)
            win = pygame.image.load('media/images/win.png')
            screen.blit(win, [1024/2, 576/2])
        if player.health <= 0:
            screen.fill(white)
            lose = pygame.image.load('media/images/lose.png')
            screen.blit(lose, [1024/2, 576/2])


        #Refreshes the display
        pygame.display.update()
        pygame.time.Clock().tick(10)
