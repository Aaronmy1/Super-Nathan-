from gamelib import*

#Game Functions-Modular Programming

game=Game(1900,1080,"Super Nathan")

city=Image("./Images/city.png",game)
city.resizeTo(game.width,game.height)

Kinder=Image("./Images/Kinder.png",game)
Kinder.resizeTo(200,200)


Nathan=Image("./Images/Nathan.png",game)
Nathan.resizeTo(200,200)
Nathan.moveTo(60,800)

NathanG=Image("./Images/NathanG.png",game)
NathanG.resizeTo(200,200)
NathanG.visible = False

NathanF=Image("./Images/NathanF.png",game)
NathanF.resizeTo(200,200)
NathanF.visible = False


Gun=Image("./Images/AK47.png",game)

bullet=Image("./Images/bullet.png",game)
bullet.resizeTo(50,50)


Zombie=Image("./Images/Zombie.png",game)
Zombie.resizeTo(200,200)
Zombie.moveTowards(Nathan,2)
Zombie.moveTo(1870,700)


Zombie2=Image("./Images/Zombie2.png",game)
Zombie2.resizeTo(200,200)
Zombie2.moveTowards(Nathan,2)


Zombie3=Image("./Images/Zombie3.png",game)
Zombie3.resizeTo(200,200)
Zombie3.moveTowards(Nathan,2)


Zombie4=Image("./Images/Zombie4.png",game)
Zombie4.resizeTo(200,200)
Zombie4.moveTowards(Nathan,2)

ZombieK=Image("./Images/Zomboss.png",game)

NathanE=Image("./Images/Nahtan.png",game)

medkit=Image("./Images/Medkit.png",game)
medkit.resizeTo(200,200)
medkit.moveTo(1000,800)

healthbar=Shape("bar",game,Nathan.health,50,green)
Nathan.health=3000
Zombie.health=100


def Nathan_control():
    healthbar.moveTo(0,20)
    healthbar.width=Nathan.health/2
    Nathan.draw()
    NathanF.moveTo(Nathan.x,Nathan.y)
    NathanG.moveTo(Nathan.x,Nathan.y)
    if keys.Pressed[K_UP]:
        Nathan.y-=4
    if keys.Pressed[K_DOWN]:
        Nathan.y+=4
    if keys.Pressed[K_LEFT]:
        Nathan.x-=4
    if keys.Pressed[K_RIGHT]:
        Nathan.x+=4


#Game 
t = 0
game.score=0
game.displaytext=game.score
Gun.visible=False
bullet.visible=False
while not game.over:
    
    game.processInput()
    city.draw()
    Kinder.draw()
    Nathan_control()
    Zombie.draw()
    medkit.draw()
    Gun.draw()
    bullet.move()

    
    Zombie.moveTowards(Nathan,3)

    t += 1
    if Nathan.health<1:
        game.over=True

    
    if mouse.LeftClick and t > 50:
        t = 0
    if not NathanG.visible:
        if t < 17:
            NathanF.visible = True
            Nathan.visible=False
        else:
            Nathan.visible=True
            NathanF.visible = False

    if Nathan.collidedWith(Gun):
        Nathan.visible=False
        NathanG.visible=True
        Gun.visible=False



    if NathanG.visible== True and t>25 and (keys.Pressed[K_LEFT] or keys.Pressed[K_RIGHT]):
        bullet.moveTo(NathanG.x-5,NathanG.y+15)

        if keys.Pressed[K_LEFT]:
            t=0
            bullet.visible=True
            bullet.setSpeed(10,90)

        if keys.Pressed[K_RIGHT]:
            t=0
            bullet.visible=True
            bullet.setSpeed(10,-90)



        
    if NathanF.collidedWith(Zombie): 
        Zombie.health-=200
        y=randint(700,1000)
        x=randint(700,1870)
        Zombie.moveTo(x,y)

    if game.score >10:
        Zombie2.draw()
        Zombie2.resizeTo(200,200)
        Zombie2.moveTowards(Nathan,3)

    if game.score >20:
        Zombie3.draw()
        Zombie4.draw()
        Zombie4.resizeTo(200,200)
        Zombie3.resizeTo(200,200)
        Zombie3.moveTowards(Nathan,3)
        Zombie4.moveTowards(Nathan,3)
        Gun.visible=True
        bullet.visible=True
      
    if Nathan.collidedWith(Zombie):
        Nathan.health-=100
        y=randint(700,1000)
        x=randint(700,1870)
        Zombie.moveTo(x,y)
    if Nathan.collidedWith(Zombie2):
        Nathan.health-=100
        y=randint(700,1000)
        x=randint(700,1870)
        Zombie2.moveTo(x,y)
    if Nathan.collidedWith(Zombie3):
        Nathan.health-=100
        y=randint(700,1000)
        x=randint(700,1870)
        Zombie3.moveTo(x,y)
    if Nathan.collidedWith(Zombie4):
        Nathan.health-=100
        y=randint(700,1000)
        x=randint(700,1870)
        Zombie4.moveTo(x,y)

    if Nathan.collidedWith(Kinder):
        Nathan.health-=10
        y=randint(700,1000)
        x=randint(700,1870)
        Kinder.moveTo(x,y)
        game.score+=1
    if Nathan.collidedWith(medkit):
        Nathan.health+=100
        y=randint(700,1000)
        x=randint(700,1870)
        medkit.moveTo(x,y)


    if NathanG.collidedWith(Zombie):
        Nathan.health-=100
        y=randint(700,1000)
        x=randint(700,1870)
        Zombie.moveTo(x,y)
    if NathanG.collidedWith(Zombie2):
        Nathan.health-=100
        y=randint(700,1000)
        x=randint(700,1870)
        Zombie2.moveTo(x,y)
    if NathanG.collidedWith(Zombie3):
        Nathan.health-=100
        y=randint(700,1000)
        x=randint(700,1870)
        Zombie3.moveTo(x,y)
    if NathanG.collidedWith(Zombie4):
        Nathan.health-=100
        y=randint(700,1000)
        x=randint(700,1870)
        Zombie4.moveTo(x,y)

    if NathanG.collidedWith(Kinder):
        Nathan.health-=10
        y=randint(700,1000)
        x=randint(700,1870)
        Kinder.moveTo(x,y)
        game.score+=20
    if NathanG.collidedWith(medkit):
        Nathan.health+=100
        y=randint(700,1000)
        x=randint(700,1870)
        medkit.moveTo(x,y)


    game.update(60)
game.quit()
