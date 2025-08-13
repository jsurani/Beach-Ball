import pgzrun
import random
WIDTH,HEIGHT = 900,800
#Create a Ball actor that moves in random directions around the screen and bounces off of the walls. 
#Use dynamic attributes to store the xspeed and yspeed of the ball. Next, add in a player-controlled Alien actor. 
#When the player uses the arrows on the keyboard, the alien should move around the screen. 
#Whenever a player collides with the ball, increase the player’s score by one, move the ball to a random location on the screen, and give the ball a new xspeed and yspeed. 
#Use a global variable to keep track of the score.
ball = Actor("beach_ball")
alien = Actor("alien")
score = 0

ball.x = random.randint(0,900)
ball.y = random.randint(0,800)
ball.xspeed = random.randint(-5,5)
ball.yspeed = random.randint(-5,5)

def draw():
  screen.clear()
  ball.draw()
  alien.draw()
  screen.draw.text("score : "+ str(score),(10,10))

def update():
  global score
  ball.x += ball.xspeed
  ball.y += ball.yspeed
  if ball.right > WIDTH:
    ball.right = WIDTH
    ball.xspeed = -ball.xspeed
  if ball.left < 0:
    ball.left = 0
    ball.xspeed = -ball.xspeed
  if ball.top < 0:
    ball.top = 0
    ball.yspeed = -ball.yspeed
  if ball.bottom > HEIGHT:
    ball.bottom = HEIGHT
    ball.yspeed = -ball.yspeed
  if(keyboard.right):
    alien.x += 10
  if(keyboard.left):
    alien.x -= 10
  if(keyboard.up):
    alien.y -= 10
  if(keyboard.down):
    alien.y += 10
  if alien.colliderect(ball):
    ball.pos= random.randint(0,WIDTH),random.randint(0,HEIGHT)
    score = score + 1
    


pgzrun.go()
