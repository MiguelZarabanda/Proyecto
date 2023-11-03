import random
import csv
from tkinter import *

raiz = Tk()
raiz.title("Ahorcado")
raiz.config(width=1000, height=600, bg="blue", relief="groove", bd=10)
JuegoFrame = Frame(raiz)
JuegoFrame.config(width=1000, height=600, relief="sunken", bd=15)
JuegoFrame.grid_propagate(False)
JuegoFrame.pack()

Label(JuegoFrame,text="Introduce una letra", font=("Verdana",24)).grid(row=0, column=0, padx=10, pady=10)
Letra = Entry(JuegoFrame, width=1, font=("Verdana", 24)).grid(row=0, column=1, padx=10, pady=10)


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
"""
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
"""

raiz.mainloop()