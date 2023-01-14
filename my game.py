import random
import arcade

class Spaceship(arcade.Sprite):
    def __init__(self,Game):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = Game.width / 2
        self.center_y = 40
        self.width = 50
        self.height = 50
        self.speed = 8

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000,height=700,title="kiya game_test")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.my_jet = Spaceship(self)
        self.zamin1 = earth1(self)
        self.zamin2 = earth2(self)
        self.zamin3 = earth3(self)
        self.zamin4 = earth4(self)
        self.zamin5 = earth5(self)
        self.zamin6 = earth6(self)
        self.zamin7 = earth7(self)
        self.zamin8 = earth8(self)
        self.zamin9 = earth9(self)
        self.zamin10 = earth10(self)
        self.zamin11 = earth11(self)
        self.zamin12 = earth12(self)
        self.emtiaz = point(self)

    def on_draw(self):
        arcade.start_render()
        self.zamin9.draw()
        self.zamin10.draw()
        self.zamin11.draw()
        self.zamin12.draw()
        self.zamin5.draw()
        self.zamin6.draw()
        self.zamin7.draw()
        self.zamin8.draw()
        self.zamin1.draw()
        self.zamin2.draw()
        self.zamin3.draw()
        self.zamin4.draw()
        self.my_jet.draw()
        self.emtiaz.draw()


    def on_key_press(self,synbol : int,modifiers: int):
        print("dokme zad")
        print(synbol)
        # a
        if synbol == 97:
            # print("left")
            self.my_jet.center_x -= self.my_jet.speed
        # d
        if synbol == 100:
            # print("right")
            self.my_jet.center_x += self.my_jet.speed
        # w
        if synbol == 119:
            self.my_jet.center_y += self.my_jet.speed
        # s
        if synbol == 115:
            self.my_jet.center_y -= self.my_jet.speed

class earth1(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/isometric_dungeon/stone_S.png")    
        self.center_x = -170
        self.center_y = 425
        self.width = 375
        self.height = 1300
        self.angle = 45

class earth2(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/isometric_dungeon/stone_S.png")
        self.center_x = 95
        self.center_y = 425
        self.width = 375
        self.height = 1300
        self.angle = 45

class earth3(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/isometric_dungeon/stone_S.png")
        self.center_x = 360
        self.center_y = 425
        self.width = 375
        self.height = 1300
        self.angle = 45

class earth4(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/isometric_dungeon/stone_S.png")
        self.center_x = 625
        self.center_y = 425
        self.width = 375
        self.height = 1300
        self.angle = 45

class earth5(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/isometric_dungeon/stone_S.png")    
        self.center_x = -170
        self.center_y = 690
        self.width = 375
        self.height = 1300
        self.angle = 45

class earth6(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/isometric_dungeon/stone_S.png")
        self.center_x = 95
        self.center_y = 690
        self.width = 375
        self.height = 1300
        self.angle = 45

class earth7(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/isometric_dungeon/stone_S.png")
        self.center_x = 360
        self.center_y = 690
        self.width = 375
        self.height = 1300
        self.angle = 45

class earth8(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/isometric_dungeon/stone_S.png")
        self.center_x = 625
        self.center_y = 690
        self.width = 375
        self.height = 1300
        self.angle = 45

class earth9(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/isometric_dungeon/stone_S.png")    
        self.center_x = -170
        self.center_y = 955
        self.width = 375
        self.height = 1300
        self.angle = 45

class earth10(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/isometric_dungeon/stone_S.png")
        self.center_x = 95
        self.center_y = 955
        self.width = 375
        self.height = 1300
        self.angle = 45

class earth11(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/isometric_dungeon/stone_S.png")
        self.center_x = 360
        self.center_y = 955
        self.width = 375
        self.height = 1300
        self.angle = 45

class earth12(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/isometric_dungeon/stone_S.png")
        self.center_x = 625
        self.center_y = 955
        self.width = 375
        self.height = 1300
        self.angle = 45

class point(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/isometric_dungeon/stoneWallArchway_S.png")
        self.center_x = 100
        self.center_y = 400
        self.width = 200
        self.height = 600
        self.angle = 30

window = Game()

arcade.run()