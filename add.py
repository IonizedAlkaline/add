import pygame
pygame.init()
pygame.display.set_caption("My first game screen")
display = pygame.display.set_mode((640,480))
text = pygame.font.Font(None,36).render("This is black",True,pygame.Color("black"))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    display.fill((255,255,255))
    display.blit(text,text.get_rect())
    rect = pygame.Rect((640-30)//2, (480-60)//2, 30, 60)
    pygame.draw.rect(display, (0,0,255), rect)
    pygame.display.flip()

