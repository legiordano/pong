import pygame

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

