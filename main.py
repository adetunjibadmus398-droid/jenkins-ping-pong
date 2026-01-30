import pygame
pygame.init()
WIDTH, HEIGHT = 1200,600
pygame.display.set_caption("Ping Pong")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
running = True
fps = 60
clock = pygame.time.Clock()
score = 0
font = pygame.font.Font(None,38)
#pingpong = pygame.mixer.Sound("pingpong.mp3")

class Ball(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load("pingpongball.png")
        self.image=pygame.transform.scale(self.image,(80,80))
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.velocity_x = 3
        self.velocity_y = 3
    def update(self):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        if self.rect.y <= 0 or self.rect.y >= HEIGHT:
            self.velocity_y = self.velocity_y * - 1
        

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load("playerball.png")
        self.image=pygame.transform.scale(self.image,(100,100))
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.velocity = 5
        self.score = 0 
    def update(self):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                self.rect.y += self.velocity
            if event.key==pygame.K_DOWN:
                self.rect.y -= self.velocity

        


class Computer(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load("computerball.png")
        self.image=pygame.transform.scale(self.image,(100,100))
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.score = 0 
    def update(self):
        self.rect.y = ball.rect.y


ball=Ball(600,350)
player=Player(100,350)
computer=Computer(1100,350)
all_sprites=pygame.sprite.Group()
all_sprites.add(ball,player,computer)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
    screen.fill("skyblue")
    all_sprites.draw(screen)
    all_sprites.update()

    if pygame.sprite.collide_rect(ball,computer) or pygame.sprite.collide_rect(ball,player):
        ball.velocity_x = ball.velocity_x * -1 
        #pingpong.play()
    
    if ball.rect.x < 0:
        computer.score += 1
        ball.rect.center = (WIDTH/2,HEIGHT/2)
        ball.velocity_x = ball.velocity_x * -1

    if ball.rect.x > WIDTH:
        player.score += 1
        ball.rect.center = (WIDTH/2,HEIGHT/2) 
        ball.velocity_x = ball.velocity_x * -1

    playerscore_text=font.render(f"Player Score: {player.score}",True,"White")
    playerscore_rect=playerscore_text.get_rect(centerx=300,top=30)
    screen.blit(playerscore_text,playerscore_rect)
    

    compscore_text=font.render(f"Computer Score: {computer.score}",True,"Dark Blue")
    compscore_rect=compscore_text.get_rect(centerx=900,top=30)
    screen.blit(compscore_text,compscore_rect)





    pygame.display.update()
    clock.tick(fps)





pygame.quit()
