import pygame
from pygame.locals import *
from button import *
from text import *
from menu import *
from play import *


class Letters:
    def __init__(self, game):
        self.game = game
        width = game.width
        height = game.height
        x_width = (width-210)/11.5
       

        self.a_but = Button(x_width,height-175, 50,50, (192,192,192), False,self.game)
        self.a_text = Text('a', x_width+5, height-180, 50, BLACK)

        self.b_but = Button(x_width*2,height-175, 50,50, (192,192,192), False,self.game)
        self.b_text = Text('b', (x_width*2)+5, height-180, 50, BLACK)

        self.c_but = Button(x_width*3, height-175, 50,50, (192,192,192), False,self.game)
        self.c_text = Text('c', (x_width*3)+5, height-180, 50, BLACK)

        self.d_but = Button(x_width*4, height-175, 50,50, (192,192,192), False,self.game)
        self.d_text = Text('d', (x_width*4)+5, height-180, 50, BLACK)

        self.e_but = Button(x_width*5, height-175, 50,50, (192,192,192), False,self.game)
        self.e_text = Text('e', (x_width*5)+5, height-180, 50, BLACK)

        self.f_but = Button(x_width*6, height-175, 50,50, (192,192,192), False,self.game)
        self.f_text = Text('f', (x_width*6)+5, height-180, 50, BLACK)

        self.g_but = Button(x_width*7, height-175, 50,50, (192,192,192), False,self.game)
        self.g_text = Text('g', (x_width*7)+5, height-180,50, BLACK)

        self.h_but = Button(x_width*8, height-175, 50,50, (192,192,192), False,self.game)
        self.h_text = Text('h', (x_width*8)+5, height-180,50, BLACK)

        self.i_but = Button(x_width*9, height-175, 50,50, (192,192,192), False,self.game)
        self.i_text = Text('i', (x_width*9)+5, height-180,50, BLACK)

        self.j_but = Button(x_width*10,height-175, 50,50, (192,192,192), False,self.game)
        self.j_text = Text('j', (x_width*10)+5, height-180,50, BLACK)

        self.k_but = Button(x_width*11,height-175, 50,50, (192,192,192), False,self.game)
        self.k_text = Text('k', (x_width*11)+5, height-180,50, BLACK)

        self.l_but = Button(x_width*12,height-175, 50,50, (192,192,192), False,self.game)
        self.l_text = Text('l', (x_width*12)+5, height-180,50, BLACK)

        self.m_but = Button(x_width*13,height-175, 50,50, (192,192,192), False,self.game)
        self.m_text = Text('m', (x_width*13)+5, height-180,50, BLACK)


        self.n_but = Button(x_width,   height-100, 50,50, (192,192,192), False,self.game)
        self.n_text = Text('n', (x_width)+5, height-105,50, BLACK)

        self.o_but = Button(x_width*2, height-100, 50,50, (192,192,192), False,self.game)
        self.o_text = Text('o', (x_width*2)+5, height-105,50, BLACK)

        self.p_but = Button(x_width*3, height-100, 50,50, (192,192,192), False,self.game)
        self.p_text = Text('p', (x_width*3)+5, height-105,50, BLACK)

        self.q_but = Button(x_width*4, height-100, 50,50, (192,192,192), False,self.game)
        self.q_text = Text('q', (x_width*4)+5, height-105,50, BLACK)

        self.r_but = Button(x_width*5, height-100, 50,50, (192,192,192), False,self.game)
        self.r_text = Text('r', (x_width*5)+5, height-105,50, BLACK)

        self.s_but = Button(x_width*6, height-100, 50,50, (192,192,192), False,self.game)
        self.s_text = Text('s', (x_width*6)+5, height-105,50, BLACK)

        self.t_but = Button(x_width*7, height-100, 50,50, (192,192,192), False,self.game)
        self.t_text = Text('t', (x_width*7)+5, height-105,50, BLACK)

        self.u_but = Button(x_width*8, height-100, 50,50, (192,192,192), False,self.game)
        self.u_text = Text('u', (x_width*8)+5, height-105, 50, BLACK)

        self.v_but = Button(x_width*9, height-100, 50,50, (192,192,192), False,self.game)
        self.v_text = Text('v',(x_width*9)+5, height-105, 50, BLACK)

        self.w_but = Button(x_width*10,height-100, 50,50, (192,192,192), False,self.game)
        self.w_text = Text('w', (x_width*10)+5, height-105,50, BLACK)

        self.x_but = Button(x_width*11,height-100, 50,50, (192,192,192), False,self.game)
        self.x_text = Text('x', (x_width*11)+5, height-105,50, BLACK)

        self.y_but = Button(x_width*12,height-100, 50,50, (192,192,192), False,self.game)
        self.y_text = Text('y', (x_width*12)+5, height-105, 50, BLACK)

        self.z_but = Button(x_width*13,height-100, 50,50, WHITE, False,self.game)
        self.z_text = Text('z', (x_width*13)+5, height-105,50, BLACK)

        self.z1_but = Button(200,200, 50,50, WHITE, False,self.game)

        self.buttons = [
            self.a_but,self.b_but,self.c_but,self.d_but, self.e_but,self.f_but,self.g_but,self.h_but,self.i_but,self.j_but,self.k_but,self.l_but,self.m_but,
            self.n_but,self.o_but,self.p_but,self.q_but, self.r_but,self.s_but,self.t_but,self.u_but,self.v_but,self.w_but,self.x_but,self.y_but,self.z_but
        ]

        self.text = [
            self.a_text,self.b_text,self.c_text,self.d_text, self.e_text,self.f_text,self.g_text,self.h_text,self.i_text,self.j_text,self.k_text,self.l_text,self.m_text,
            self.n_text,self.o_text,self.p_text,self.q_text, self.r_text,self.s_text,self.t_text,self.u_text,self.v_text,self.w_text,self.x_text,self.y_text,self.z_text
        ]

        self.alpha =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    def draw_screen(self):
        for i in self.buttons:
            i.draw(self.game.screen)
        for j in self.text:
            j.draw(self.game.screen)

    def catch_actions(self, event, mx, my):
        self.z1_but.draw(self.game.screen)
            
                


             
            