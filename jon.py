import arcade
class Jon(arcade.Sprite):
    def __init__(self,x):
        super().__init__("Assignment 14\love.png")
        self.center_x = x
        self.center_y = 25
        self.width = 50
        self.height = 50