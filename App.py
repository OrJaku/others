import pygame
import time

class Player:
    x = 50
    y = 50
    direction = 0
    width = 10
    height = 10
    v = 1

    def update(self):
        if self.direction == 0:
            self.x = self.x + self.v
        if self.direction == 1:
            self.x = self.x - self.v
        if self.direction == 2:
            self.y = self.y + self.v
        if self.direction == 3:
            self.y = self.y + self.v

    def right(self):
        self.direction = 0

    def left(self):
        self.direction = 1

    def up(self):
        self.direction = 2

    def down(self):
        self.direction = 3


class App:
    win_h = 300
    win_w = 400
    player = 0

    def __init__(self):
        self.running = True
        self.windows = None
        self.player = Player()

    def on_init(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.win_w, self.win_h), pygame.HWSURFACE)
        pygame.display.set_caption("The Game")
        self.running = True
        pygame.draw.rect(self.window, (250, 100, 0), (self.player.x, self.player.y, self.player.width,
                                                      self.player.height))
        pygame.display.flip()


    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def on_loop(self):
        self.player.update()

    def clean(self):
        pygame.quit()

    def on_render(self):
        self.window.fill((0,0,0))
        self.window.blit(self.,(self.player.x,self.player.y))
        pygame.display.flip()

    def on_execute(self):
        self.on_init()
        if self.on_init == False:
            self.running = False
        while self.running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_RIGHT]:
                self.player.right()

            if keys[pygame.K_LEFT]:

                self.player.left()

            if keys[pygame.K_UP]:
                self.player.up()

            if keys[pygame.K_DOWN]:
                self.player.down()

            if (keys[pygame.K_ESCAPE]):
                self.running = False

            if (keys[pygame.K_a]):
                self.player.width = 70

            self.on_loop()
            self.on_render()

            time.sleep(300.0 / 1000.0)
            print("X", self.player.x)
            print("Y", self.player.y)
        self.clean()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
