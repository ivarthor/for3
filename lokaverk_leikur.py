import pygame

class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(32,32, 16, 16)

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        for veggur in veggir:
            if self.rect.colliderect(veggur.rect):
                if dx > 0:
                    self.rect.right = veggur.rect.left
                if dx < 0:
                    self.rect.left = veggur.rect.right
                if dy > 0:
                    self.rect.bottom = veggur.rect.top
                if dy < 0:
                    self.rect.top = veggur.rect.bottom

class Veggur(object):

    def __init__(self,pos):
        self.rect = pygame.Rect(pos[0],pos[1],16,16)


pygame.init()
window = pygame.display.set_mode((320,240))

klukka = pygame.time.Clock()
veggir = list()
player = Player()

# Búa til lykla og óvini
maze = ["vvvvvvvvvvvvvvvvvvvv",
        "v   v              v",
        "v   vvvvvvvvv vv   v",
        "v              v   v",
        "v   vvvv       v   v",
        "vvvvv      v   v   v",
        "v   v  v   v   v   v",
        "v      v   v       v",
        "v   v  v   v   vvvvv",
        "v   v  v           v",
        "v   v  v   vvvv vvvv",
        "v          v       v",
        "v   v      v   e   v",
        "vvvvvvvvvvvvvvvvvvvv"]

x = 0
y = 0
for i in maze:
    for a in i:
        if a == "v":
            veggir.append(Veggur((x,y)))
        if a == "e":
            endir = pygame.Rect(x,y,16,16)
        x += 16
    y += 16
    x = 0

i_gangi = True

while i_gangi:
    klukka.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    takki = pygame.key.get_pressed()
    if takki[pygame.K_LEFT]:
        player.move(-2,0)
    if takki[pygame.K_RIGHT]:
        player.move(2,0)
    if takki[pygame.K_UP]:
        player.move(0,-2)
    if takki[pygame.K_DOWN]:
        player.move(0,2)

    if player.rect.colliderect(endir):
        print("Þú vannst")
        raise SystemExit()

    window.fill((0,0,0))

    for veggur in veggir:
        pygame.draw.rect(window, (255, 255, 255), veggur.rect)

    pygame.draw.rect(window, (255, 0, 0), endir)
    pygame.draw.rect(window,(255,200,0), player)
    pygame.display.flip()
