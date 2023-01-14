import time
import random
import arcade
from spaceship import Spaceship
from enemy import Enemy
from jon import Jon
from bullet import Bullet

DEFAULT_FONT_SIZE = 45

class Game(arcade.Window):
    def __init__(self):
        self.w = 500
        self.h = 700
        super().__init__(self.w,self.h,title="kiya game_test")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture("Assignment 13/tamrin/start.PNG")
        self.next_enemy_time = 3
        self.game_start_time = time.time()
        self.start_time = time.time()
        self.my_jet = Spaceship(self)
        self.tir = Bullet(self.my_jet)
        self.doshmans = []
        self.my_jet.update_jon()
        self.enemy_speed = 2

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        self.my_jet.draw()

        for doshman in self.doshmans:
            doshman.draw()
        
        for jon in self.my_jet.jons:
            jon.draw()
        
        for bullet in self.my_jet.Bullet_list:
            bullet.draw()
        
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.my_jet.change_x = 0

    def on_key_press(self,synbol : int,modifiers: int):
        print("dokme zad")
        print(synbol)
        if synbol == arcade.key.A:
            print("left")
            self.my_jet.change_x = -1
        elif synbol == arcade.key.D:
            print("right")
            self.my_jet.change_x = 1
        elif synbol == arcade.key.SPACE:
            self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
            self.my_jet.fire()
            self.tir.sound()
    
    def on_update(self, delta_time):
        self.end_time = time.time()
        if self.end_time - self.start_time > self.next_enemy_time:
            self.new_doshman = Enemy(self,self.enemy_speed)
            print(self.enemy_speed)
            self.enemy_speed += 0.5
            self.doshmans.append(self.new_doshman)
            self.start_time = time.time()

        for bullet in self.my_jet.Bullet_list:
            bullet.move()

        for bullet in self.my_jet.Bullet_list:
            if bullet.center_y > 700:
                self.my_jet.Bullet_list.remove(bullet)

        for doshman in self.doshmans:
            for bullet in self.my_jet.Bullet_list:
                if arcade.check_for_collision(doshman, bullet):
                    self.doshmans.remove(doshman)
                    self.my_jet.Bullet_list.remove(bullet)
                    self.my_jet.Score += 1

        for doshman in self.doshmans:
            if doshman.center_y < 0:
                self.doshmans.remove(doshman)
                self.my_jet.jons.remove(self.my_jet.jons[0])
                if len(self.my_jet.jons) == 0:
                    self.my_jet.sound()
                    arcade.draw_text('GAME OVER', self.w//2-200, self.h//2, arcade.color.ORANGE, DEFAULT_FONT_SIZE //2, width=400, align='center')
                    print("game over")
                    exit(0)

        for doshman in self.doshmans:
            if arcade.check_for_collision(doshman, self.my_jet):
                self.my_jet.sound()
                arcade.draw_text('GAME OVER', self.w//2-200, self.h//2, arcade.color.ORANGE, DEFAULT_FONT_SIZE //2, width=400, align='center')
                print("Game Over")
                exit(0)

        self.my_jet.move()
        arcade.draw_text('Score: %i'%self.my_jet.Score, self.w-130, 10, arcade.color.RED, DEFAULT_FONT_SIZE //2, width=200, align='left')

    
        for doshman in self.doshmans:  
            doshman.move()

window = Game()

arcade.run()