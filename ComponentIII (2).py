#Game Cell
#The Diamond
#Kanvir Singh, Gurpreet Singh, Rene Juarez San Migu
#Knight has to go and retrive the King's diamond from the devil.

from gamelib import*#import game library

#objects and initial settings
game = Game (800,600,"The Diamond")
bk = Image("castle.png",game)
bk.resizeTo(game.width, game.height)
knight = Image("knight.png",game)
re = Image("re.png",game)
re.resizeTo(game.width, game.height)
brick = Image("brick.png",game)
f = Font(red,20,yellow,"castleliar")
knight.resizeBy(-10)
knight.moveTo(625,475)
brick.resizeBy(-80)

rock = []#empty list
for index in range(100):#add the images to the list
    rock.append(Image("brick.png",game))
for index in range(100):#set each item list
    rock[index].resizeBy(-90)
    x = randint(100,700)
    y = -randint(100,10000)
    rock[index].moveTo(x,y)
    s = randint(3,8)
    rock[index].setSpeed(s,180)
    
game.over = False

#Level 1 - game loop
game.time = 60
while not game.over:
    game.processInput()
    re.draw()

    
    if keys.Pressed[K_SPACE]:
        game.over = True
    game.drawText("Press [SPACE BAR] to start the game",game.width/2-150,game.height/2+20)
    game.update(30)
    
game.over = False

while not game.over:
    game.processInput()
    #game.scrollBackground("left",2)
    bk.draw()
    knight.draw()
    for index in range(len(rock)):
       rock[index].move()
    game.displayTime(25,50,f) 
    game.update(30)
    if keys.Pressed[K_LEFT]:
        knight.x -= 10
    if keys.Pressed[K_RIGHT]:
        knight.x += 10
    brick.draw()
game.over = False
#Level 2 - game loop
while not game.over:
    game.processInput()

    #game.scrollBackground("left",2)
    bk.draw()
    knight.draw()
    
        

        
    game.update(30)

game.quit()
