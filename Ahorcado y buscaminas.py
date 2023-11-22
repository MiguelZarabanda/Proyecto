from tkinter import *
from tkinten import messagebox
import random 
import time
import pygame


def Datos (val):
  Espacios = []
  for i in range(tamaño)
    Espacios.append([val] * tamaño)
  return Espacios
def Tableroran():
  icono = []
  minas = 0
  for x in range(tamaño):
    for y in range (altura):
      if minas < NMINES:
        icons.append(#minas, verde) # no tengo idea 
          minas += 1
      else: 
        icons.append(#square, white? #no tengo idea 

  random.shuffle(icons) 
  tablero = []
  for x in range (tamaño)
  columna = []
  for y in range (altura)
    colum.append(icon[0])
    del icons[0]
  tablero.append(columna)
  
/////////////////////////////////////////////////////////////////////////////////////////
  def __init__(self, Altura, tamaño)
    self.ancho = int(input("Numero entre 4 a 20 :"))
    while self.ancho < 4 or self.size > 20:
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
/////////////////////////////////////////////////////////////////////




bomb = 0
bomb1 = 0
bomb2 = 0
bomb3 = 0 
bombo4 = 0

def Bombran ():
bomb = random.randrange():
bomb1 = random.randrange():
bomb2 = ramdom.randrange():
bomb3 = ramdom.randrange():
bombo4 = ramdom.randrange():

print("las bombas se ubican en estos lugares")
print(bomb)
print(bomb1)
print(bomb2)
print(bomb3)
print(bomb4)
def casillas  ():
  
def banderas ():
  global bandera
  bandera = True 
banderaImg=PhotoImage(file="img/bandera.png")
banderaImgSlot=PhotoImage(file="img/banderaSlot.png")
def ponerbandera():

  if bandera and banderasbomba>0:
    banderasbomba = banderasbomba-1
    contadorBanderas.config(text="Banderas disponibles: " + str(banderasDisponibles))
    Botones[Espacio].config(image=banderaImgSlot, width=64, height=65)
    print("La bandera se puso en")
    print (Espacio)
    bandera = False
    #contador y poner
contadorBanderas=Label(frame, text="Banderas disponibles: " + str(banderasbomba), font=("Arial 15"))
contadorBanderas.grid(column=6, row=0, columnspan=5)
Teclaband=Button(frame, text=" ", image=banderaImg, command=lambda:presionarBandera())
Teclaband.grid(column=5, row=0)
    

  
