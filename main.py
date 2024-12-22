import random

import pygame

from file_help import read_from_file, write_in_file


def game():
    pygame.init()

    pygame.mixer.init()
    shoot_sound = pygame.mixer.Sound("fire.ogg")
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
                shoot_sound.play()


            for bullet in self.bullets:
                bullet.move()

    class Enemy:
        def __init__(self,speed,width,height,x,y,skin):
            self.texture = pygame.image.load(skin)
            self.texture = pygame.transform.scale(self.texture, [width,height])
            self.hitbox = self.texture.get_rect()
            self.hitbox.x = x
            self.hitbox.y = y
            self.speed = speed



        def draw(self,window):
            window.blit(self.texture,self.hitbox)

        def move(self):
            self.hitbox.y += self.speed



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


    def win_window(window):
        fps = pygame.time.Clock()
        win_lbl = pygame.font.Font(None, 48).render("Ти переміг",True, [0, 0,0])
        while True:
            window.fill([0, 255, 0])
            window.blit(win_lbl, [200, 200])
            pygame.display.flip()

            fps.tick(60)

    def lose_window(window):
        fps = pygame.time.Clock()
        lose_lbl = pygame.font.Font(None, 48).render("Ти програв",True, [0, 0,0])
        while True:
            window.fill([255, 0, 0])
            window.blit(lose_lbl, [200, 200])
            pygame.display.flip()

            fps.tick(60)







    galaxy_sound = pygame.mixer.Sound("space.ogg")
    galaxy_sound.play(-1)

    window = pygame.display.set_mode([700,500])
    fps = pygame.time.Clock()
    rocket = Rocket(5,65, 85,250, 400,"rocket.png")





    background = pygame.image.load("galaxy.jpg")
    background = pygame.transform.scale(background, [700,500])

    enemies = []
    y = 200
    for i in range(10):
        enemies.append(Enemy(1, 50, 50, random.randint(0, 650), y, "asteroid.png"))
        y -= 100

    data = read_from_file()
    score = data["score"]
    write_in_file(data)
    score_lbl = pygame.font.Font(None, 23).render("Score: " + str(score), True, [123,123,123])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        if score >= 500:
            win_window(window)



        if score < 0:
            lose_window(window)


        score_lbl = pygame.font.Font(None,23).render("Score: " + str(score), True, [123, 123, 123])

        for e in enemies:
            e.move()
            if e.hitbox.y > 500:
                e.hitbox.y = -100
                e.hitbox.x = random.randint(0, 650)

        for e in enemies:
            for b in rocket.bullets:
                if e.hitbox.colliderect(b.hitbox):
                    b.hitbox.x = 5000
                    rocket.bullets.remove(b)
                    e.hitbox.y = -100
                    e.hitbox.x = random.randint(0, 650)
                    
                    data = read_from_file()
                    score += 1
                    data["score"] = score
                    write_in_file(data)
                    break

        for e in enemies:
            if e.hitbox.colliderect(rocket.hitbox):
                e.hitbox.y = -100
                e.hitbox.x = random.randint(0, 650)
                score -= 1

        window.fill([123,123,123])
        window.blit(background,[0,0])
        window.blit(score_lbl, [0, 0])
        rocket.draw(window)
        rocket.move()



        for e in enemies:
            e.draw(window)

        pygame.display.flip()





        fps.tick(60)
