from random import choice, randint

import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

BOARD_BACKGROUND_COLOR = (0, 0, 0)

BORDER_COLOR = (93, 216, 228)

APPLE_COLOR = (255, 0, 0)

SNAKE_COLOR = (0, 255, 0)

SPEED = 14

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()


class GameObject:
    """
    Базовый класс, который содержит позицию, цвет объекта
    и заготовку отрисовки объекта.
    """

    def __init__(self, position=None, body_color=None):
        self.position = position
        self.body_color = body_color

    def draw(self):
        """Отрисовка объекта."""
        pass


class Snake(GameObject):
    """Класс, описывающий змейку и её поведение."""

    def __init__(self):
        self.body_color = SNAKE_COLOR
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.positions = [self.position]
        self.length = 1
        self.next_direction = None
        self.last = None
        self.direction = RIGHT

    def draw(self, surface):
        """Отрисовка змейки"""
        for position in self.positions[:-1]:
            rect = (
                pygame.Rect((position[0], position[1]), (GRID_SIZE, GRID_SIZE))
            )
            pygame.draw.rect(surface, self.body_color, rect)
            pygame.draw.rect(surface, BORDER_COLOR, rect, 1)

        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.body_color, head_rect)
        pygame.draw.rect(surface, BORDER_COLOR, head_rect, 1)

        if self.last:
            last_rect = pygame.Rect(
                (self.last[0], self.last[1]),
                (GRID_SIZE, GRID_SIZE)
            )
            pygame.draw.rect(surface, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self):
        """Возвращает позицию головы змейки."""
        return self.positions[0]

    def move(self):
        """Обновляет позицию змейки."""
        head_position = self.get_head_position()
        delta_x, delta_y = self.direction

        position = (
            (head_position[0] + (delta_x * GRID_SIZE)) % SCREEN_WIDTH,
            (head_position[1] + (delta_y * GRID_SIZE)) % SCREEN_HEIGHT
        )
        if self.get_head_position() in self.positions[1:]:
            self.reset()
        else:
            self.positions.insert(0, position)
        if len(self.positions) > self.length:
            self.last = self.positions.pop()
        else:
            self.last = None

    def update_direction(self):
        """Обновляет направление движения змейки."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def reset(self):
        """
        Cбрасывает змейку в начальное состояние
        после столкновения с собой.
        """
        screen.fill(BOARD_BACKGROUND_COLOR)
        self.length = 1
        self.positions = [self.position]
        self.direction = choice([UP, RIGHT, DOWN, LEFT])


class Apple(GameObject):
    """Класс, описывающий яблоко и его свойства."""

    def __init__(self):

        self.body_color = APPLE_COLOR
        self.position = (
            randint(0, 31) * GRID_SIZE,
            randint(0, 23) * GRID_SIZE
        )

    def draw(self, surface):
        """Отрисовка яблока."""
        rect = pygame.Rect(
            (self.position[0], self.position[1]),
            (GRID_SIZE, GRID_SIZE)
        )
        pygame.draw.rect(surface, self.body_color, rect)
        pygame.draw.rect(surface, BORDER_COLOR, rect, 1)

    def randomize_position(self):
        """Устанавливает случайное положение яблока."""
        self.position = (
            randint(0, 31) * GRID_SIZE,
            randint(0, 23) * GRID_SIZE
        )


def handle_keys(game_object):
    """Обрабатывает нажатия клавиш."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    """Основной цикл игры."""
    apple = Apple()
    snake = Snake()
    screen.fill(BOARD_BACKGROUND_COLOR)

    while True:
        clock.tick(SPEED)

        handle_keys(snake)
        snake.update_direction()
        snake.move()

        if apple.position == snake.get_head_position():
            snake.length += 1

            apple.randomize_position()
            while apple.position in snake.positions:
                apple.randomize_position()

        apple.draw(screen)
        snake.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
