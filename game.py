import pygame

# Initialize the pygame
pygame.init()


# Create the screen
screen = pygame.display.set_mode((500,500))


# Title & Icon (image: Flaticon.com)
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


#Game loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  # Red, Green & Blue
  screen.fill((0, 128, 0))
  pygame.display.update()