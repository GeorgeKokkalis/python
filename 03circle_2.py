import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Αναπήδηση κύκλου")

clock = pygame.time.Clock()
x, y, radius = 100, 100, 30
dx, dy = 4, 4  # Ταχύτητα

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += dx
    y += dy

    if x - radius <= 0 or x + radius >= 800:
        dx = -dx
    if y - radius <= 0 or y + radius >= 600:
        dy = -dy

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (0, 0, 255), (x, y), radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
