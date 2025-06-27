import pygame as py 
import configuracion as config

class Ball:

    def __init__(self, velocidad_x, velocidad_y, tamaño, pantalla,
                  posicion_x, posicion_y, S_alto, S_ancho, 
                    ):
        self.velocidad_x = velocidad_x
        self.velocidad_y = velocidad_y
        
        self.tamaño = tamaño

        self.pantalla = pantalla
        self.S_alto = S_alto
        self.S_ancho = S_ancho

        self.posicion_x = posicion_x
        self.posicion_y = posicion_y

        self.direcion = -1
        self.isMoving = True



    def dibjuar(self):     #screen           #color     
        py.draw.circle(self.pantalla,(172,216,230), (self.posicion_x, self.posicion_y), self.tamaño, self.tamaño)



    def mover(self):
        if self.isMoving != True: 
            return 
        

        self.posicion_x += self.velocidad_x * self.direcion
        self.posicion_y += self.velocidad_y




    
    def colision(self):

        # si tocas el borde de pantalla 
        if self.posicion_y >= self.S_alto or self.posicion_y <= 0:
            self.velocidad_y *= -1



    def reset(self):
        self.posicion_x = config.ancho /2 
        self.posicion_y = config.alto / 2
        self.direcion *=-1







    def actulizar(self):
        self.dibjuar()
        self.colision()
        self.mover()

