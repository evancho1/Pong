import pygame

pygame.init()

# Constants, colours, fonts
size = (width, height) = (700, 600)
white = (255, 255, 255)
black = (0, 0, 0)
font1 = pygame.font.SysFont("Trebuchet MS", 18)
font2 = pygame.font.SysFont("Impact", 25)

# Pygame screen
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

clock=pygame.time.Clock()
fps = 30

# Player class
class Player:
    def __init__(self, xpos, ypos, width, height, colour, speed):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.colour = colour
        self.speed = speed
        self.hitbox = pygame.Rect(xpos, ypos, width, height)
        self.player = pygame.draw.rect(screen, self.colour, self.hitbox)

    def display(self):
        self.player = pygame.draw.rect(screen, self.colour, self.hitbox)

    def update(self, yDir):
        self.ypos += self.speed * yDir

        if self.ypos <= 0:
            self.ypos = 0
        elif self.ypos + self.height >= height:
            self.ypos = height - self.height

        self.hitbox = (self.xpos, self.ypos, self.width, self.height)

    def showScore(self, text, score, x, y, colour):
        text = font1.render(text + str(score), True, colour)
        screen.blit(text, (x, y))

    def getPlayer(self):
        return self.hitbox

# Ball class
class Ball:
    def __init__(self, xpos, ypos, radius, colour, speed):
        self.xpos = xpos
        self.ypos = ypos
        self.radius = radius
        self.colour = colour
        self.speed = speed
        self.xDir = 1
        self.yDir = -1
        self.ball = pygame.draw.circle(screen, self.colour, (self.xpos, self.ypos), self.radius)
        self.scored = 1

    def display(self):
        self.ball = pygame.draw.circle(screen, self.colour, (self.xpos, self.ypos), self.radius)

    def update(self):
        self.xpos += self.speed * self.xDir
        self.ypos += self.speed * self.yDir

        if self.ypos <= 0 or self.ypos >= height:
            self.yDir *= -1
        if self.xpos >= width:
            return 1
        elif self.xpos <= 0:
            return 2
        else:
            return 0

    def reset(self):
        self.xpos = width // 2
        self.ypos = height // 2
        self.xDir *= -1

    def hit(self):
        self.xDir *= -1

    def getBall(self):
        return self.ball

def main():
    run = True

    # Initialization of players and ball
    player1 = Player(20, height / 2 - 50, 10, 100, white, 8)
    player2 = Player(width - 30, height / 2 - 50, 10, 100, white, 8)
    ball = Ball(width // 2, height // 2, 10, white, 10)

    score1 = 0
    score2 = 0
    yDir1 = 0
    yDir2 = 0

    while run:
        screen.fill(black)

        # Key detection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    yDir1 = -1
                if event.key == pygame.K_s:
                    yDir1 = 1
                if event.key == pygame.K_UP:
                    yDir2 = -1
                if event.key == pygame.K_DOWN:
                    yDir2 = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    yDir1 = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    yDir2 = 0

        # Collision detection
        if pygame.Rect.colliderect(ball.getBall(), player1.getPlayer()):
            ball.hit()
        if pygame.Rect.colliderect(ball.getBall(), player2.getPlayer()):
            ball.hit()

        # Updates player and ball movement
        player1.update(yDir1)
        player2.update(yDir2)
        point = ball.update()

        # Score update
        if point == 1:
            score1 += 1
            ball.reset()
        elif point == 2:
            score2 += 1
            ball.reset()

        # Display and score update
        player1.display()
        player2.display()
        ball.display()
        player1.showScore("Player 1: ",  score1, 100, 20, white)
        player2.showScore("Player 2: ", score2, width - 200, 20, white)

        pygame.display.update()
        clock.tick(fps)

if __name__ == "__main__":
    main()
    pygame.quit()
                
                
        
        

    
