import pygame, os


class FlyingObjects(pygame.sprite.Sprite):
    # An: renamed cX and cY
    def __init__(self, img, c_x, c_y):
        # Создаем спрайт из картинки
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = self.load_image(img, -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        # Перемещаем картинку в её начальные координаты
        self.rect.x = c_x
        self.rect.y = c_y

    def load_image(self, name, colorkey=None):  # отображение картинок
        fullname = os.path.join('data', name)
        image = pygame.image.load(fullname)
        return image, image.get_rect()
