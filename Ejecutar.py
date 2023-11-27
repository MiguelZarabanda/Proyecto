import pygame 
import time 
import definicion as Df

pygame.init()
x = 0
game = DF.game(700,600)
t1 = time.perf_counter()
juega = True
pos_arriba = (juego.centro[0] - 75, juego.centro[1] - (juego.grosor + 5) * (juego.ancho/2) - 40)
pos_abajo = (juego.centro[0], juego.centro[1] + (juego.grosor + 5) * (juego.ancho/2) + 15)
run = True
while run:
  game.Mostrarcuad()                                                                   
    event = pygame.event.poll()                                                                                     #Lee los eventos
    if event.type == pygame.QUIT:   
        run = False                                                                                                 #Termina el ciclo
    if event.type == pygame.MOUSEBUTTONDOWN and juega:  
        pos = event.dict['pos']                                                                                     #Lee la posicion del mouse
        if event.button == 1:   
            if x == 0:  
                x = juego.safe(pos)                                                                                 #Ejecuta el metodo safe, si se ejecuta adecuadamente retorna 1 y no se vuelve a hacer
            game.ejecucion(pos)
        if event.button == 3:
            juego.Poner(pos)
  
