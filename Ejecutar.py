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
            juego.Poner_QuitarBand(pos)
  msg_banderas = game.temp.render("Banderas: {0}" .format(game.Fbanderas), 1, (255,255,0))
  pygaame.draw.rect(game.ventana, (0,0,0), (pos_abajo[0] + 100, pos_abajo[1], game.grosor * 20, 30))
  game.ventana.blit(msg_banderas, (pos_abajo[0] + 100,pos_abajo[1]))
  
  if game.Nbanderas == game.Mbanderas:
      msg = game.msg.render("victoria", 1, (255,255, 0))
      pygame.draw.rect(juego.ventana, (0,0,0), (pos_arriba[0], pos_arriba[1], game.grosor * 10,30))
      game.ventana.blit(msg, pos_arriba)
      game.Respuesta()
      pygame.display.update()
      juega = False
  elif not game.est:
    msg = game.msg.render("Perdiste", 1, (255,255,0))
    pygame.draw.rect(juego.ventana, (0,0,0), (pos_arriba[0], pos_arriba[1], game.grosor * 10, 30))
    game.Respuesta()
    pygame.display.update()
    juega = False
  else:
    juego.Tiempo(t1)
    pygame.display.update()
pygame.quit()    
    

