import pygame

class Rocket:
    def __init__(self, speed, width, height, x, y, skin):
        self.texture = pygame.image.load(skin)
        self.texture = pygame.transform.scale(self.texture, [width,height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.bullets = []

    def draw(self,window):
        window.blit(self.texture,self.hitbox)
        for bullet in self.bullets:
            bullet.draw(window)


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.hitbox.x += self.speed
        if keys[pygame.K_DOWN]:
            self.hitbox.y += self.speed
        if keys[pygame.K_LEFT]:
            self.hitbox.x -= self.speed
        if keys[pygame.K_UP]:
            self.hitbox.y -= self.speed
        if keys[pygame.K_z]:
            self.hitbox.y -= self.speed
            self.bullets.append(Bullet(10,
                                       10,10,
                                    self.hitbox.x,self.hitbox.y,
                                       "bullet.png"))


        for bullet in self.bullets:
            bullet.move()

class UFO:
    def __init__(self,width,height,x,y,skin):
        self.texture = pygame.image.load(skin)
        self.texture = pygame.transform.scale(self.texture, [width,height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y



    def draw(self,window):
        window.blit(self.texture,self.hitbox)



class Bullet:
    def __init__(self, speed, width, height, x, y, skin):
        self.texture = pygame.image.load(skin)
        self.texture = pygame.transform.scale(self.texture, [width, height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.bullets = []
    def move(self):
       self.hitbox.y -= self.speed
    def draw(self,window):
        window.blit(self.texture,self.hitbox)



pygame.init()

window = pygame.display.set_mode([700,500])
fps = pygame.time.Clock()
rocket = Rocket(5,65, 85,250, 400,"rocket.png")





background = pygame.image.load("galaxy.jpg")
background = pygame.transform.scale(background, [700,500])

ufos = [
    UFO(50,50,10,10,"ufo.png"),
    UFO(50,50,65,10,"ufo.png"),
    UFO(50,50,120,10,"ufo.png"),
    UFO(50,50,175,10,"ufo.png"),
    UFO(50,50,230,10,"ufo.png"),
    UFO(50,50,285,10,"ufo.png"),
    UFO(50, 50, 345, 10, "ufo.png"),
    UFO(50, 50, 400, 10, "ufo.png"),
    UFO(50, 50, 455, 10, "ufo.png"),
    UFO(50, 50, 510, 10, "ufo.png"),
    UFO(50, 50, 565, 10, "ufo.png"),
    UFO(50, 50, 620, 10, "ufo.png"),



]

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            print(x,y)
    window.fill([123,123,123])
    window.blit(background,[0,0])
    rocket.draw(window)
    rocket.move()

    window.fill([123, 123, 123])
    window.blit(background, [0, 0])
    rocket.draw(window)






    pygame.display.flip()


    for ufo in ufos:
        ufo.draw(window)
    pygame.display.flip()


    fps.tick(60)
