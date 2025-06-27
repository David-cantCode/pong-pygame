import pygame as py

class Player:
    def __init__(self, posicion_x, posicion_y, S_ancho, S_alto, direcion, pantalla, ):
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.velocidad = 5
        

        self.ancho = 10 
        self.alto = 70
        
        
        self.S_ancho = S_ancho
        self.S_alto = S_alto

        self.pantalla = pantalla

        self.direcion = direcion



    def mover(self):
        nueva_pos = self.posicion_y + self.velocidad * self.direcion

        # Mantener al jugador dentro de la pantalla
        if 0 <= nueva_pos <= self.S_alto - self.alto:
            self.posicion_y = nueva_pos



    def dibjuar(self):
        py.draw.rect(self.pantalla,(255,255,255), (self.posicion_x, self.posicion_y, self.ancho, self.alto))


    def actulizar(self):
        self.mover()
        self.dibjuar()





        