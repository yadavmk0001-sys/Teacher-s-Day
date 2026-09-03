import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Teacher's Day!")


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CONFETTI_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
                   (255, 255, 0), (255, 105, 180), (0, 255, 255)]

# Load sprites (replace with your own PNG images)
teacher_img = pygame.image.load("t1-removebg-preview.png").convert_alpha()
student_img = pygame.image.load("s1-removebg-preview.png").convert_alpha()

# Resize sprites
teacher_img = pygame.transform.scale(teacher_img, (150, 200))
student_img = pygame.transform.scale(student_img, (150, 200))

# Sprite positions
teacher_pos = (WIDTH // 2 - 200, HEIGHT // 2)
student_pos = (WIDTH // 2 + 50, HEIGHT // 2)

# Confetti particles
confetti = []
for _ in range(100):
    x = random.randint(0, WIDTH)
    y = random.randint(-HEIGHT, 0)
    speed = random.randint(2, 5)
    color = random.choice(CONFETTI_COLORS)
    confetti.append([x, y, speed, color])

# Fonts
font = pygame.font.SysFont("Arial", 50, bold=True)

# Background
background = pygame.Surface((WIDTH, HEIGHT))
background.fill((240, 230, 255))  # light pastel background

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    screen.blit(background, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw confetti
    for c in confetti:
        pygame.draw.circle(screen, c[3], (c[0], c[1]), 5)
        c[1] += c[2]
        if c[1] > HEIGHT:
            c[1] = random.randint(-20, -5)
            c[0] = random.randint(0, WIDTH)
            c[3] = random.choice(CONFETTI_COLORS)

    # Draw sprites
    screen.blit(teacher_img, teacher_pos)
    screen.blit(student_img, student_pos)

    # Draw text
    text_surface = font.render("HAPPY TEACHER'S DAY!", True, BLACK)
    text_surfac = font.render("LOVE YOU!", True, BLACK)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 100))
    screen.blit(text_surface, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
