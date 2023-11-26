import random
import csv
import pygame
import sys

pygame.init()

Inicio = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Juego del Ahorcado")
FPS = 60
clock = pygame.time.Clock()
Dificultad = random.randint(1,3)
TipoPalabra = random.randint(1,7)
Iniciar = 0

#Fuentes

Fuente1 = pygame.font.SysFont("Monocraft", 80)
Fuente2 = pygame.font.SysFont("Monocraft", 40)
Fuente3 = pygame.font.SysFont("Monocraft", 20)
Fuente4 = pygame.font.SysFont("Monocraft", 60)

#Palabras

Label1 = Fuente1.render("Ahorcado", 1, (0, 0, 0))
Label2 = Fuente2.render("Dificultad", 1, (0, 0, 0))
Label3 = Fuente2.render("Palabras", 1, (0, 0, 0))

#Imagenes

IMGFacil = pygame.image.load("Facil.png")
IMGMedio = pygame.image.load("Medio.png")
IMGDificil = pygame.image.load("Dificil.png")
IMGFacilSelect = pygame.image.load("FacilSelect.png")
IMGMedioSelect = pygame.image.load("MedioSelect.png")
IMGDificilSelect = pygame.image.load("DificilSelect.png")

#Marcos

Marco = pygame.image.load("Marco.png")
MarcoG = pygame.image.load("MarcoG.png")
MarcoSelect=pygame.image.load("MarcoSelect.png")

#Fondo

Fondo = pygame.image.load("Fondo.png")
Fondo = pygame.transform.scale(Fondo, (1000, 600))

#Dificultad

Jugar = pygame.Rect(0+(1000-150)/2, 500, 150, 50)
Facil = pygame.Rect(110+(166-130)/2, 200, 130, 50)
Medio = pygame.Rect(110+(166-130)/2, 300, 130, 50)
Dificil = pygame.Rect(110+(166-130)/2, 400, 130, 50)

#Palabras

Deportes = pygame.Rect(450+(166-130)/2, 200, 130, 50)
Frutas  = pygame.Rect(616+(166-130)/2, 200, 130, 50)
Paises = pygame.Rect(783+(166-130)/2, 200, 130, 50)
Ciudades = pygame.Rect(450+(166-130)/2, 300, 130, 50)
Colores = pygame.Rect(616+(166-130)/2, 300, 130, 50)
Animales = pygame.Rect(783+(166-130)/2, 300, 130, 50)
Verbos = pygame.Rect(450+(500-130)/2, 400, 130, 50)

while True:
    clock.tick(FPS)   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            if Facil.collidepoint(pygame.mouse.get_pos()):
                Dificultad = 1
            if Medio.collidepoint(pygame.mouse.get_pos()):
                Dificultad = 2
            if Dificil.collidepoint(pygame.mouse.get_pos()):
                Dificultad = 3
            if Deportes.collidepoint(pygame.mouse.get_pos()):
                TipoPalabra = 1
            if Frutas.collidepoint(pygame.mouse.get_pos()):
                TipoPalabra = 2
            if Paises.collidepoint(pygame.mouse.get_pos()):
                TipoPalabra = 3
            if Ciudades.collidepoint(pygame.mouse.get_pos()):
                TipoPalabra = 4
            if Colores.collidepoint(pygame.mouse.get_pos()):
                TipoPalabra = 5
            if Animales.collidepoint(pygame.mouse.get_pos()):
                TipoPalabra = 6
            if Verbos.collidepoint(pygame.mouse.get_pos()):
                TipoPalabra = 7
            if Jugar.collidepoint(pygame.mouse.get_pos()):
                Iniciar = 1
       
    Inicio.fill([0, 170, 230])
    Inicio.blit(Fondo, (0, 0))
    Inicio.blit(Label1, (0+(1000-Label1.get_width())/2, 25))
    Inicio.blit(Label2, (0+(500-Label2.get_width())/2, 130))
    Inicio.blit(Label3, (450+(500-Label3.get_width())/2, 130))

    if Jugar.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(Inicio, (57, 143, 17), Jugar, 0)
    else:
        pygame.draw.rect(Inicio, (72, 245, 66), Jugar, 0)
    texto1 = Fuente3.render("Jugar", True, (0, 0, 0))   
    Inicio.blit(texto1, ((0+(1000-150)/2)+(Jugar.width-texto1.get_width())/2, 
                        500+(Jugar.height-texto1.get_height())/2))
    Inicio.blit(MarcoG, (0+(1000-150)/2, 500, 150, 50))

    if Facil.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(Inicio, (83, 191, 33), Facil, 0)
    else:
        pygame.draw.rect(Inicio, (139, 245, 118), Facil, 0)
    texto2 = Fuente3.render("Facil", True, (0, 0, 0))
    Inicio.blit(texto2, ((110+(166-130)/2)+(Facil.width-texto2.get_width())/2, 
                        200+(Facil.height-texto2.get_height())/2))
    Inicio.blit(IMGFacil, (300, 190))
    Inicio.blit(Marco, (110+(166-130)/2, 200))

    if Medio.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(Inicio, (184, 184, 44), Medio, 0)
    else:
        pygame.draw.rect(Inicio, (239, 252, 58), Medio, 0)
    texto3 = Fuente3.render("Medio", True, (0, 0, 0))
    Inicio.blit(texto3, ((110+(166-130)/2)+(Medio.width-texto3.get_width())/2, 
                        300+(Medio.height-texto3.get_height())/2))
    Inicio.blit(IMGMedio, (300, 290))
    Inicio.blit(Marco, (110+(166-130)/2, 300))

    if Dificil.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(Inicio, (145, 12, 12), Dificil, 0)
    else:
        pygame.draw.rect(Inicio, (252, 50, 50), Dificil, 0)
    texto4 = Fuente3.render("Dificil", True, (0, 0, 0))
    Inicio.blit(texto4, ((110+(166-130)/2)+(Dificil.width-texto4.get_width())/2, 
                        400+(Dificil.height-texto4.get_height())/2))
    Inicio.blit(IMGDificil, (300, 390))
    Inicio.blit(Marco, (110+(166-130)/2, 400))

    if Deportes.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(Inicio, (181, 125, 47), Deportes, 0)
    else:
        pygame.draw.rect(Inicio, (255, 177, 69), Deportes, 0)
    texto5 = Fuente3.render("Deportes", True, (0, 0, 0))
    Inicio.blit(texto5, ((450+(166-130)/2)+(Deportes.width-texto5.get_width())/2, 
                        200+(Deportes.height-texto5.get_height())/2))
    Inicio.blit(Marco, (450+(166-130)/2, 200))

    if Frutas.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(Inicio, (181, 125, 47), Frutas, 0)
    else:
        pygame.draw.rect(Inicio, (255, 177, 69), Frutas, 0)
    texto6 = Fuente3.render("Frutas", True, (0, 0, 0))
    Inicio.blit(texto6, ((616+(166-130)/2)+(Frutas.width-texto6.get_width())/2, 
                        200+(Frutas.height-texto6.get_height())/2))
    Inicio.blit(Marco, (616+(166-130)/2, 200))

    if Paises.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(Inicio, (181, 125, 47), Paises, 0)
    else:
        pygame.draw.rect(Inicio, (255, 177, 69), Paises, 0)
    texto7 = Fuente3.render("Paises", True, (0, 0, 0))
    Inicio.blit(texto7, ((783+(166-130)/2)+(Paises.width-texto7.get_width())/2, 
                        200+(Paises.height-texto7.get_height())/2))
    Inicio.blit(Marco, (783+(166-130)/2, 200))

    if Ciudades.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(Inicio, (181, 125, 47), Ciudades, 0)
    else:
        pygame.draw.rect(Inicio, (255, 177, 69), Ciudades, 0)
    texto8 = Fuente3.render("Ciudades", True, (0, 0, 0))
    Inicio.blit(texto8, ((450+(166-130)/2)+(Ciudades.width-texto8.get_width())/2, 
                        300+(Ciudades.height-texto8.get_height())/2))
    Inicio.blit(Marco, (450+(166-130)/2, 300))

    if Colores.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(Inicio, (181, 125, 47), Colores, 0)
    else:
        pygame.draw.rect(Inicio, (255, 177, 69), Colores, 0)
    texto9 = Fuente3.render("Colores", True, (0, 0, 0))
    Inicio.blit(texto9, ((616+(166-130)/2)+(Colores.width-texto9.get_width())/2, 
                        300+(Colores.height-texto9.get_height())/2))
    Inicio.blit(Marco, (616+(166-130)/2, 300))

    if Animales.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(Inicio, (181, 125, 47), Animales, 0)
    else:
        pygame.draw.rect(Inicio, (255, 177, 69), Animales, 0)
    texto10 = Fuente3.render("Animales", True, (0, 0, 0))
    Inicio.blit(texto10, ((783+(166-130)/2)+(Animales.width-texto10.get_width())/2, 
                        300+(Animales.height-texto10.get_height())/2))
    Inicio.blit(Marco, (783+(166-130)/2, 300))

    if Verbos.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(Inicio, (181, 125, 47), Verbos, 0)
    else:
        pygame.draw.rect(Inicio, (255, 177, 69), Verbos, 0)
    texto11 = Fuente3.render("Verbos", True, (0, 0, 0))
    Inicio.blit(texto11, ((450+(500-130)/2)+(Verbos.width-texto11.get_width())/2, 
                        400+(Verbos.height-texto11.get_height())/2))
    Inicio.blit(Marco, (450+(500-130)/2, 400))

    if Dificultad == 1:
        Inicio.blit(IMGFacilSelect, (299, 189))
        Inicio.blit(MarcoSelect, (109+(166-130)/2, 199))
    elif Dificultad ==2:
        Inicio.blit(IMGMedioSelect, (299, 289))
        Inicio.blit(MarcoSelect, (109+(166-130)/2, 299))
    elif Dificultad == 3:
        Inicio.blit(IMGDificilSelect, (299, 389))
        Inicio.blit(MarcoSelect, (109+(166-130)/2, 399))

    if TipoPalabra == 1:
        Inicio.blit(MarcoSelect, (449+(166-130)/2, 199))
    elif TipoPalabra == 2:
        Inicio.blit(MarcoSelect, (615+(166-130)/2, 199))
    elif TipoPalabra == 3:
        Inicio.blit(MarcoSelect, (782+(166-130)/2, 199))
    elif TipoPalabra == 4:
        Inicio.blit(MarcoSelect, (449+(166-130)/2, 299))
    elif TipoPalabra == 5:
        Inicio.blit(MarcoSelect, (615+(166-130)/2, 299))
    elif TipoPalabra == 6:
        Inicio.blit(MarcoSelect, (782+(166-130)/2, 299))
    elif TipoPalabra == 7:
        Inicio.blit(MarcoSelect, (615+(166-130)/2, 399))

    pygame.display.flip()
    
    if Iniciar == 1:
        pygame.init()
        size = (1200, 635)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Juego del Ahorcado")
        FPS = 60
        clock = pygame.time.Clock()
        Ahorcado = 0
        MarcoP = pygame.image.load("MarcoP.png")

        #Fondos

        Fondo1 = pygame.image.load("Fondo1.png")
        Fondo1 = pygame.transform.scale(Fondo1, (1200, 635))

        #Fuentes

        Fuente = pygame.font.SysFont("Monocraft", 80)

        #Palabras

        Label = Fuente.render("Ahorcado", 1, (0, 0, 0))
        texto12 = Fuente4.render("Deportes", True, (0, 0, 0))
        texto13 = Fuente4.render("Frutas", True, (0, 0, 0))
        texto14 = Fuente4.render("Paises", True, (0, 0, 0))
        texto15 = Fuente4.render("Ciudades", True, (0, 0, 0))
        texto16 = Fuente4.render("Colores", True, (0, 0, 0))
        texto17 = Fuente4.render("Animales", True, (0, 0, 0))
        texto18 = Fuente4.render("Verbos", True, (0, 0, 0))

        #Variables de Botones

        Radio = 23
        GAP = 20
        Letras = []
        Letras1 = []
        Letras2 = []
        iniciox = round((1630 -(Radio * 2 + GAP) * 9) / 2)
        inicioy = 400
        A = 65
        for i in range(26):
            x = iniciox + GAP * 3 + ((Radio * 2 + GAP) * (i % 9))
            y = inicioy + ((i // 9) * (GAP + Radio * 2))
            Letras.append((x, y, 50, 50))
            Letras1.append(chr(A + i))
            Letras2.append([x, y])

        #Imagenes

        imagenes = []
        for i in range(8):
            imagenes.append	(pygame.image.load("Ahorcado" + str(i) + ".png"))

        def Dibujar():
            X = 0
            Inicio.blit(Fondo1, (0, 0))
            screen.blit(imagenes[Ahorcado], (30, 100))
            screen.blit(Label, (400, 15))
            
            #Botones

            for letra in Letras:
                ltr = A
                pygame.draw.rect(screen, (255, 255, 255), letra)
                screen.blit(MarcoP, (letra))
                texto = Fuente2.render(Letras1[X], 0,(0, 0, 0))
                screen.blit(texto, (Letras2[X][0]+(50 - texto.get_width())/2, Letras2[X][1] + (50 - texto.get_height())/2))
                X += 1

            if Dificultad==1:
                Inicio.blit(IMGFacil, (300, 22))
            elif Dificultad == 2:
                Inicio.blit(IMGMedio, (300, 22))
            elif Dificultad == 3:
                Inicio.blit(IMGDificil, (300, 22))

            if TipoPalabra == 1:
                Inicio.blit(texto12, (710, 120))
            elif TipoPalabra == 2:
                Inicio.blit(texto13, (750, 120))
            elif TipoPalabra == 3:
                Inicio.blit(texto14, (750, 120))
            elif TipoPalabra == 4:
                Inicio.blit(texto15, (730, 120))
            elif TipoPalabra == 5:
                Inicio.blit(texto16, (750, 120))
            elif TipoPalabra == 6:
                Inicio.blit(texto17, (710, 120))
            elif TipoPalabra == 7:
                Inicio.blit(texto18, (750, 120))

            pygame.display.update()

        while True:
            clock.tick(FPS)   
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    print(pos)
            
            Dibujar()
                        
            pygame.display.flip()


            

def TipoPalabra(Archivo, Valor):
    Tipo = []
    for i in Archivo:
        if Valor == 1 and i[0] != "" and i[0] != "Deportes":
            Tipo.append(i[0])
        elif Valor == 2 and i[1] != "" and i[1] != "Frutas":
            Tipo.append(i[1])
        elif Valor == 3 and i[2] != "" and i[2] != "Paises":
            Tipo.append(i[2])
        elif Valor == 4 and i[3] != "" and i[3] != "Ciudades":
            Tipo.append(i[3])
        elif Valor == 5 and i[4] != "" and i[4] != "Colores":
            Tipo.append(i[4])
        elif Valor == 6 and i[5] != "" and i[5] != "Animales":
            Tipo.append(i[5])
        elif Valor == 7 and i[6] != "" and i[6] != "Verbos":
            Tipo.append(i[6])
    return Tipo

def Dificultad(Tipo, Valor):
    Dificultad=[]
    for i in Tipo:
        lista=list(i)
        Tam = len(lista)
        if Tam <= 5 and Valor == 1:
            Dificultad.append(i)
        elif Tam >= 6 and Tam <= 7 and Valor == 2:
            Dificultad.append(i)
        elif Tam >= 8 and Valor == 3:
            Dificultad.append(i)
    return Dificultad

def Palabra(Lista):
    Palabras = Lista
    Random = random.choice(Palabras)
    return Random

def Tablero(Palabra, Adivinadas):
    Tablero=""
    for letra in Palabra:
        if letra in Adivinadas:
            Tablero+=letra
        else:
            Tablero+="_"
    print(Tablero)

def Intentos(Dif):
    if Dif == 1:
        Intentos = 5
    elif Dif == 2:
       Intentos = 6
    elif Dif == 3:
     Intentos = 7
    return Intentos

'''
with open("Palabras.csv", "r") as File:
    Difi=3
    csv_reader = csv.reader(File)
    Tipo = TipoPalabra(csv_reader, 3)
    Dif = Dificultad(Tipo, 3)
    Pal = (Palabra(Dif)).lower()
    LetrasAdivinadas=[]
    Inte=Intentos(Difi)
    while Inte > 0:
        Tablero(Pal, LetrasAdivinadas)
        letra=input("Introduzca una letra: ").lower()
        if letra in LetrasAdivinadas:
            print("Ya has introducido esta letra.")
            continue
        if letra in Pal:
            LetrasAdivinadas.append(letra)
            if set(LetrasAdivinadas)==set(Pal):
                print("Has ganado, Felicidades.")
                break
        else: 
            Inte-=1
            print(f"Letra incorrecta, {Inte} intentos")
    if Inte==0:
        print("Has perdido")

    print(Pal)
'''