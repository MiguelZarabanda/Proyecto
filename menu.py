import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Configurar colores
black = (0, 0, 0)
white = (255, 255, 255)
brown = (139, 69, 19)

# Cargar la imagen de fondo
bg_image = pygame.image.load('yes.jpg')
bg_image = pygame.transform.scale(bg_image, (screen_width, screen_height))

# Clase para los botones
class Button:
   def __init__(self, color, x, y, width, height, text=''):
       self.color = color
       self.x = x
       self.y = y
       self.width = width
       self.height = height
       self.text = text

   def draw(self, screen, outline=None):
       if outline:
           pygame.draw.rect(screen, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
       pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
       if self.text != '':
           font = pygame.font.SysFont('comicsans', 30)
           text = font.render(self.text, 1, (0, 0, 0))
           screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

   def is_over(self, pos):
       if self.x < pos[0] < self.x + self.width:
           if self.y < pos[1] < self.y + self.height:
               return True
       return False

# Crear botones para los juegos y niveles de dificultad
ahorcado_button = Button(brown, 100, 100, 200, 50, 'Ahorcado')
buscaminas_button = Button(brown, 500, 100, 200, 50, 'Buscaminas')
facil_button = Button(brown, 100, 300, 200, 50, 'Facil')
medio_button = Button(brown, 300, 300, 200, 50, 'Medio')
dificil_button = Button(brown, 500, 300, 200, 50, 'Dificil')
play_button = Button(brown, 300, 100, 200, 50, 'Play')

# Implementar los juegos de Ahorcado y Buscaminas
def juego_ahorcado(dificultad):
   # Aquí va el código para iniciar el juego de Ahorcado
   print(f"Iniciando Ahorcado en nivel {dificultad}...")
   pass

def juego_buscaminas(dificultad):
   # Aquí va el código para iniciar el juego de Buscaminas
   print(f"Iniciando Buscaminas en nivel {dificultad}...")
   pass

# Bucle principal para manejar eventos y actualizar pantalla
def game_loop():
   while True:
       for event in pygame.event.get():
           pos = pygame.mouse.get_pos()
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           if event.type == pygame.MOUSEBUTTONDOWN:
               if ahorcado_button.is_over(pos):
                  if facil_button.is_over(pos):
                      juego_ahorcado('facil')
                  elif medio_button.is_over(pos):
                      juego_ahorcado('medio')
                  elif dificil_button.is_over(pos):
                      juego_ahorcado('dificil')
               if buscaminas_button.is_over(pos):
                  if facil_button.is_over(pos):
                      juego_buscaminas('facil')
                  elif medio_button.is_over(pos):
                      juego_buscaminas('medio')
                  elif dificil_button.is_over(pos):
                      juego_buscaminas('dificil')
               if play_button.is_over(pos):
                  # Aquí puedes agregar el código para cambiar a la ventana de juego
                  pass

       screen.blit(bg_image, (0, 0))
       ahorcado_button.draw(screen)
       buscaminas_button.draw(screen)
       facil_button.draw(screen)
       medio_button.draw(screen)
       dificil_button.draw(screen)
       play_button.draw(screen)
       pygame.display.update()

game_loop()