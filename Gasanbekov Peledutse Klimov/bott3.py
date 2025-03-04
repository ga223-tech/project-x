import pygame
import random


pygame.init()


screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Змейка")


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)


snake_block = 20


clock = pygame.time.Clock()
snake_speed = 15
try:
    background_image = pygame.image.load("food.jpg").convert() # 
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height)) 
except pygame.error as e:
    print(f"Ошибка загрузки фонового изображения: {e}")
    pygame.quit()
    quit()
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

def your_score(score):
    value = font_style.render("Очки: " + str(score), True, white)
    screen.blit(value, [0, 0])

font_style = pygame.font.SysFont(None, 30)



def game_loop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close == True:
            screen.fill(black)
            message = font_style.render("Капец ты лох! ESC - выйти, \n С - начать сначала", True, red)
            screen.blit(message, [screen_width / 6, screen_height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.blit(background_image, (0, 0)) # Отображение фонового изображения
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        your_score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
