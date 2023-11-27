from tkinter import *
from tkinten import messagebox
import random 
import time
import pygame

class game:
  def __init__(self, Altura, tamaño)
    self.ancho = int(input("Numero entre 4 a 20 :"))
    while self.ancho < 4 or self.ancho > 20:
        print("La cuadricula debe ser mayor que 4 y menor que 20\n")
        self.ancho = int(input("Ingrese el tamaño de la cuadricula, debe ser mayor que 4:"))
  self.grosor = 400//self.ancho   
# se ponen mas cosas pero no se exactamente cuales


#pygame, pues segun el proyecto del rosario esto es necesario por pygame
  self.fuente = pygame.font.SysFont('newyorkitalicttf', self.width, True)     #Numeros
  self.temp = pygame.font.SysFont('newyorkitalicttf', 20, True)               #Tiempo
  self.msg = pygame.font.SysFont('newyorkitalicttf', 30, True)                #Mensaje de victoria y derrota
  self.p_ancho = ancho
  self.p_alto = alto
  self.ventana = pygame.display.set_mode((self.p_ancho, self.p_alto))         #Ventana y dimensiones
  pygame.display.set_caption("Buscaminas")    
  self.centro = self.ventana.get_rect().center                                #Centro de la ventana
  mina = pygame.image.load("Mina.png")               
  self.mina = pygame.transform.scale(mina, (self.width , self.width))         #Imagen de la mina
  bandera = pygame.image.load("Bandera.png")
  self.bandera = pygame.transform.scale(bandera, (self.width, self.width))    #Imagen de la bandera
  pygame.mixer.init()                                                                     
  
  #buscaminas
  self.coord = {}                                                             #Diccionario con coordenadas y color del cuadro
  self.Nbanderas = 0                                                          #Contador de banderas bien colocadas
  self.Fbanderas = 0                                                 #Banderas que tiene el jugador
  self.Mbanderas = 0                                                       #Banderas maximas que puede tener el jugador
  self.estado = {}                                                            #Diccionario con coordenadas y valores booleanos que indican la presencia de banderas
  self.est = True                                                             #Indica con un booleano si se esta en juego o no                                                               
  self.coordenadas = []                                                        #Lista de coordenadas del tablero
  self.di_coordenadas()                                                      
  self.minas_d = {}                                                           #Diccionario que indica si hay minas o no en una coorenada
  self.ColocarMinas()                                                         
  self.minasA_dt = {}                                                         #Diccionario con el valor del nimero de minas aledañas a un cuadro
  self.ContarCuadros()  
# Faltan cosas pq pues estas son las variables y no tengo idea de cuantas variables vamos a poner XD
def Cuadricula(self):
  x = self.centro[0] - (self.ancho * (self.grosor + 5) / 2)
  y = self.centro[1] - (self.ancho * (self.grosor +5) / 2)
  for i in range (self.ancho):
    self.coord[(x,y)] = self.coord.get((x,y),(192, 192, 192))
    self.estado[(x,y)] = False 
    self.coordenadas.append((x,y))
    x += self.grosor + 5
  x -= (self.grosor + 5) * self.ancho
  y += self.grosor + 5
#cuadro XD
def Mostrarcuad(self):
  for i in range self.coordenadas:
    color = self.coord.get(i)
    x = i[0]
    y = i[1]
    pygame.draw.polygon(self.ventana, (224, 224, 224), [(x + self., y),(x + self.grosor + 2.5, y - 2.5),  (x - 2.5, y - 2.5), (x - 2.5, y + self.grosor + 2.5), (x, y + self.grosor), (x, y)])                                                        #Borde superior e izquierdo de cada cuadro
    pygame.draw.polygon(self.ventana, (96, 96, 96), [(x, y + self.grosor), (x - 2.5, y + self.grosor + 2.5), (x + self.grosor + 2.5, y + self.grosor + 2.5), (x + self.grosor + 2.5, y - 2.5), (x + self.grosor, y), (x + self.grosor, y + self.grosor)])       #Borde inferior y derecho de cada cuadro
    pygame.draw.rect(self.ventana, (color), (x, y, self.grosor, self.grosor))    
#mostrar
def Colocarminas(self):
  self.minas_d = {}
  self.banderas_restantes = 0
  self.banderas_max = 0
  for i in self.coordenadas:
    self.minas_d[i] = self.minas_d.get(i, False)
  rng = random.random()
  while self.banderas_restantes < len (self.minas_d) // 5:
    M = rng.randrange (0, len(self.coordenadas))
    if self.minas_d.get(self.coordenadas[M] == False:
       self.minas_d[self.coordenadas[M]] = True
       self.banderas_restantes +=1
       self.banderas_max +=1
#minas
def seguro (self, pos):
  for i in self.coord:
    if pos[0] >= i[0] and pos[0] <= i[0] + self.grosor and pos[1] >= i[1] and pos[1] <= i[1] + self.grosor:
      while self.minasA_dt[i] != 0:
        self.Colocarminas()
        self.ContarCuadros()
      return 1
  return 0
#no perder
def ContarCuadros(self):
  self.minasA_dt = {}
  counter = 0
  for i in self.minas_d
    minasC = 0
    y = self.coordenadas[counter]
    if self.minas_d[i] == True:
      self.minasA_dt[i] = True
    else: 
      if (y[0] + self.grosor + 5 ,y[1]) in self.minas_d:
        if self.minas_d[(y[0] + self.grosor + 5 ,y[1])] == True:
          minasC += 1
      if (y[0] + self.grosor + 5 ,y[1] + self.grosor + 5 ) in self.minas_d:            
        if self.minas_d[(y[0] + self.grosor + 5 ,y[1] + self.grosor + 5 )] == True:
          minasC += 1
      if (y[0],y[1] + self.grosor + 5 ) in self.minas_d:                              
        if self.minas_d[(y[0],y[1] + self.grosor + 5 )] == True:
          minasC += 1
      if (y[0] - self.grosor - 5 ,y[1] + self.grosor + 5 ) in self.minas_d:             
        if self.minas_d[(y[0] - self.grosor - 5 ,y[1] + self.grosor + 5 )] == True:
          minasC += 1
      if (y[0] - self.grosor - 5 ,y[1]) in self.minas_d:                              
        if self.minas_d[(y[0] - self.grosor - 5 ,y[1])] == True:
          minasC += 1
      if (y[0] - self.grosor - 5 ,y[1] - self.grosor - 5 ) in self.minas_d:             
        if self.minas_d[(y[0] - self.grosor - 5 ,y[1] - self.grosor - 5 )] == True:
          minasC += 1
      if (y[0],y[1] - self.grosor - 5 ) in self.minas_d:                               
        if self.minas_d[(y[0],y[1] - self.grosor - 5 )] == True:
          minasC += 1
      if (y[0] + self.grosor + 5 ,y[1] - self.grosor - 5 ) in self.minas_d:             
        if self.minas_d[(y[0] + self.grosor + 5 ,y[1] - self.grosor - 5 )] == True:
          minasC += 1 
      self.minasA_dt[i] = self.minasA_dt.get(i, minasC)
    counter += 1
    #minas alrededor
def descubrir(self, i):
  val = self.minasA_dt.get(i)
  pos = [i[0] + (self.grosor // 5), i[1]]
  self.coord[i] = (96,96,96)
  self.Mostrarcuad()
  stringgggggggggggggg

def Poner_QuitarBand(self,pos):
  for i in self.coord:
      if pos[0] >= i[0] and pos[0] <= i[0] + self.grosor and pos[1] >= i[1] and pos[1] <= i[1] + self.grosor:
        pos = [i[0],i[1]]
        if self.estado[i] == False:
          if self.Fbanderas != 0:
            if i in self.coordenadas:
              self.coordenadas.remove(i)
              self.ventana.blit(self.bandera, pos)
              self.Fbanderas -=1
              self.estado [i] = True
            if self.minasA_dt[i] == True:
              self.Nbanderas +=1
            break
      else: 
        self.coordenadas.append(i)
        self.Fbanderas +=1
        self.estado[i] = False
        if str(self.minasA_dt[i]) == "True":
          self.Nbanderas -=1
        break
#banderas
  def ejecucion(self,pos):
    for i in self.coord:
      if pos[0] >= i[0] and pos[0] <= i[0] + self.grosor and pos[1] >= i[1] and pos[1] <=i[1] + self.grosor:
        if self.estado[i]  != True:
          if self.minas_d[i] == True:
            pos = [i[0], i[1]]
            self.ventana.blit(self.mina,pos)
            pygame.mixer.music.play()
            self.est = False
          else:
            self.descubrir(i)
             if self.minasA_dt[i] == 0:
              self.minasaA_dt[i] = "0"
              
              if (i[0] + self.grosor + 5 , i[1]) in self.minasA_dt:
                                a = self.minasA_dt[(i[0] + self.grosor + 5 , i[1])]
                                self.descubrir((i[0] + self.grosor + 5 , i[1]))
                                if a == 0:
                                    self.ejecucion((i[0] + self.grosor + 5 , i[1]))                      #Si el valor de la casilla es 0 repite la ejecucion con esa casilla
                            if (i[0] + self.grosor + 5 ,i[1] + self.grosor + 5 ) in self.minas_d:
                                a = self.minasA_dt[(i[0] + self.grosor + 5 ,i[1] + self.grosor + 5 )]
                                self.descubrir((i[0] + self.grosor + 5 ,i[1] + self.grosor + 5 ))
                                if a == 0:
                                    self.ejecucion((i[0] + self.grosor + 5 ,i[1] + self.grosor + 5 ))     #Si el valor de la casilla es 0 repite la ejecucion con esa casilla     
                            if (i[0], i[1] + self.grosor + 5 ) in self.minasA_dt:
                                a = self.minasA_dt[(i[0], i[1] + self.grosor + 5 )]
                                self.descubrir((i[0], i[1] + self.grosor + 5 ))
                                if a == 0:
                                    self.ejecucion((i[0], i[1] + self.grosor + 5 ))                      #Si el valor de la casilla es 0 repite la ejecucion con esa casilla
                            if (i[0] - self.grosor - 5 ,i[1] + self.grosor + 5 ) in self.minas_d:
                                a = self.minasA_dt[(i[0] - self.grosor - 5 ,i[1] + self.grosor + 5 )]
                                self.descubrir((i[0] - self.grosor - 5 ,i[1] + self.grosor + 5 ))
                                if a == 0:
                                    self.ejecucion((i[0] - self.grosor - 5 ,i[1] + self.grosor + 5 ))     #Si el valor de la casilla es 0 repite la ejecucion con esa casilla
                            if (i[0] - self.grosor - 5 , i[1]) in self.minasA_dt:
                                a = self.minasA_dt[(i[0] - self.grosor - 5 , i[1])]
                                self.descubrir((i[0] - self.grosor - 5 , i[1]))
                                if a == 0:
                                    self.ejecucion((i[0] - self.grosor - 5 , i[1]))                      #Si el valor de la casilla es 0 repite la ejecucion con esa casilla
                            if (i[0] - self.grosor - 5 ,i[1] - self.grosor - 5 ) in self.minas_d:
                                a = self.minasA_dt[(i[0] - self.grosor - 5 ,i[1] - self.grosor - 5 )]
                                self.descubrir((i[0] - self.grosor - 5 ,i[1] - self.grosor - 5 ))
                                if a == 0:
                                    self.ejecucion((i[0] - self.grosor - 5 ,i[1] - self.grosor - 5 ))     #Si el valor de la casilla es 0 repite la ejecucion con esa casilla   
                            if (i[0], i[1] - self.grosor - 5 ) in self.minasA_dt:
                                a = self.minasA_dt[(i[0], i[1] - self.grosor - 5 )]
                                self.descubrir((i[0], i[1] - self.grosor - 5 ))
                                if a == 0:
                                    self.ejecucion((i[0], i[1] - self.grosor - 5 ))                      #Si el valor de la casilla es 0 repite la ejecucion con esa casilla
                            if (i[0] + self.grosor + 5 ,i[1] - self.grosor - 5 ) in self.minas_d:
                                a = self.minasA_dt[(i[0] + self.grosor + 5 ,i[1] - self.grosor - 5 )]
                                self.descubrir((i[0] + self.grosor + 5 ,i[1] - self.grosor - 5 ))
                                if a == 0:
                                    self.ejecucion((i[0] + self.grosor + 5 ,i[1] - self.grosor - 5 ))     #Si el valor de la casilla es 0 repite la ejecucion con esa casilla
        break
        
def Tiempo(self, t1)
    pos =(self.centro[0] - 200, self.centro[1] + (self.grosor + 5) * (self.ancho/2) +15
    t2 = time.perf_counter()
    t = str(int(t2-t1))
    t = self.temp.render("Tiempo : {0} sec".format(t), 1, (255,255,0))
    pygame.draw.rect(self.ventana, (0,0,0), (pos[0], pos[1], 200, self.grosor))
    self.ventana.blit(t, (pos))
def Respuestas(self):
  for i in self.minas_d:
      if self.minas_d[i] == True and self.estado[i] == False:
          pos = [i[0], i[1]]
          self.ventana.blit(self.mina, pos)
      if self.estado[i] == True and self.minas_d[i] == False:
        pygame.draw.line(self.ventana, (0,0,0), (i[0], i[1]), (i[0] + self.grosor, i[1] + self.grosor), (5))
        pygame.draw.line(self.ventana, (0,0,0), (i[0] + self.grosor, i[1]), (i[0], i[1] + self.grosor), (5))
/////////////////////////////////////////////////////////////////////




    

  
