#pong de yo
#25/6/2025
import configuracion as config
import pygame as py
import ballClass
import playerClass




def comenzar():
    global pantalla, pelota , player_1, player_2, players, fuente
    fuente = py.font.Font(None, 56)

    pantalla = py.display.set_mode((config.ancho, config.alto))
    py.display.set_caption("pong") 


    player_1 = playerClass.Player(8, config.alto /2, config.ancho, config.alto, 0,  pantalla)
    player_2 = playerClass.Player(config.ancho - 15, config.alto /2, config.ancho, config.alto, 0, pantalla )
    players = {player_1, player_2}

    pelota = ballClass.Ball(5,5, config.tamaño_de_pelota, pantalla, config.pelota_x, config.peolota_y, config.alto, config.ancho )





def colisiones():
    
        #P1
    if pelota.posicion_x <= player_1.posicion_x + player_1.ancho:
        if player_1.posicion_y <= pelota.posicion_y <= player_1.posicion_y + player_1.alto:
            pelota.direcion *= -1
        else:
            config.P2_score += 1
            pelota.reset()
          
        #P2
    if pelota.posicion_x + pelota.tamaño >= player_2.posicion_x:
        if player_2.posicion_y <= pelota.posicion_y <= player_2.posicion_y + player_2.alto:
            pelota.direcion *= -1
        else:
            config.P1_score += 1
            pelota.reset()
            





def dibjuar_texto():
    texto = fuente.render(f"{config.P1_score}   |   {config.P2_score}", True, (255, 255, 255))
    pantalla.blit(texto, (config.ancho // 2 - texto.get_width() // 2, 20))  # centro superior









def actulizar():
    dibjuar_texto()
    colisiones()
    player_1.actulizar()
    player_2.actulizar()
    pelota.actulizar()



#**************************
#entrada del program
#****************************
py.init() #need for text or computer get angwy
comenzar()
while True:
    config.reloj.tick(60)
    for evento in py.event.get():
        if evento.type == py.QUIT:
            py.quit()

        
    #*****************************************************
        #******************Movimentio del jugadores****
    #**********************************************

        if evento.type == py.KEYDOWN:
            if evento.key ==  py.K_w:
                player_1.direcion = -1
            elif evento.key == py.K_s:
                player_1.direcion = 1
            if evento.key ==  py.K_UP:
                player_2.direcion = -1
            elif evento.key == py.K_DOWN:
                player_2.direcion = 1
         


        if evento.type == py.KEYUP:
            if evento.key in [py.K_w, py.K_s]:
                player_1.direcion = 0
            if evento.key in [py.K_UP, py.K_DOWN]:
                player_2.direcion = 0






    actulizar()
    py.display.flip()
    pantalla.fill(config.color_fondo)

 