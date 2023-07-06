import pygame
import random

pygame.init()

width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()

paddle_width = 10
paddle_height = 60
paddle_speed = 5

paddle1_x = 20
paddle1_y = height // 2 - paddle_height // 2

paddle2_x = width - 20 - paddle_width
paddle2_y = height // 2 - paddle_height // 2

ball_size = 10
ball_speed_x = 3
ball_speed_y = 3
ball_x = width // 2 - ball_size // 2
ball_y = height // 2 - ball_size // 2

score1 = 0
score2 = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < height - paddle_height:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < height - paddle_height:
        paddle2_y += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x <= paddle1_x + paddle_width and paddle1_y <= ball_y + ball_size // 2 <= paddle1_y + paddle_height:
        ball_speed_x = abs(ball_speed_x)
    if ball_x >= paddle2_x - paddle_width and paddle2_y <= ball_y + ball_size // 2 <= paddle2_y + paddle_height:
        ball_speed_x = -abs(ball_speed_x)

    if ball_y <= 0 or ball_y >= height - ball_size:
        ball_speed_y = -ball_speed_y

    if ball_x <= 0:
        score2 += 1
        ball_x = width // 2 - ball_size // 2
        ball_y = height // 2 - ball_size // 2
        ball_speed_x = random.choice([3, -3])
        ball_speed_y = random.choice([3, -3])
    if ball_x >= width - ball_size:
        score1 += 1
        ball_x = width // 2 - ball_size // 2
        ball_y = height // 2 - ball_size // 2
        ball_speed_x = random.choice([3, -3])
        ball_speed_y = random.choice([3, -3])

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, ball_size, ball_size))

    score_text = font.render(str(score1) + " - " + str(score2), True, WHITE)
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()