import arcade
from bullet import Bullet
from jon import Jon

class Spaceship(arcade.Sprite):
    def __init__(self,Game):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = Game.width / 2
        self.center_y = 40
        self.change_x = 0
        self.change_y = 0
        self.width = 50
        self.height = 50
        self.speed = 6
        self.Score = 0
        self.Game_width = Game.width
        self.Bullet_list = []
        self.jons = []

    def move(self):
        if self.change_x == -1:
            if self.center_x > 0:
                self.center_x -= self.speed
        elif self.change_x == 1:
            if self.center_x < self.Game_width:
                self.center_x += self.speed
                
    def fire(self):
        new_bullet = Bullet(self)
        self.Bullet_list.append(new_bullet)

    def update_jon(self):
        x = 25
        for i in range(3):
            new_jon = Jon(x)
            self.jons.append(new_jon)
            x+=30

    def sound(self):
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/error2.wav'), 0.2, 0.0,False)

