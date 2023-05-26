import pygame
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
alto = 1040
ancho = 480

# Colores
negro = (0, 0, 0)
blanco = (255, 255, 255)
rojo = (255, 0, 0)

# Creación de la ventana del juego
screen = pygame.display.set_mode((alto, ancho))
pygame.display.set_caption("Juego Serpiente")

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Tamaño y velocidad de la serpiente
tamañoBloque = 20
velocidad = 5


# Función para dibujar la serpiente en la pantalla
def dibujarSerpiete(tamañoBloque, serpienteLista):
    for x in serpienteLista:
        pygame.draw.rect(screen, negro, [x[0], x[1], tamañoBloque, tamañoBloque])


# Función principal del juego
def game_loop():
    game_over = False
    game_exit = False

    # Posición inicial de la serpiente
    x = alto / 2
    y = ancho / 2

    # Cambios en la posición de la serpiente
    cambiox = 0
    cambioy = 0

    # Lista para almacenar las partes de la serpiente
    serpienteLista = []
    serpienteLongitud = 1

    # Posición aleatoria de la comida
    comidaX = (
        round(random.randrange(0, alto - tamañoBloque) / tamañoBloque) * tamañoBloque
    )
    comidaY = (
        round(random.randrange(0, ancho - tamañoBloque) / tamañoBloque) * tamañoBloque
    )

    while not game_exit:
        while game_over:
            screen.fill(blanco)
            # Mensaje de "Game Over" y puntuación
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render(
                "Game Over" " presiona C para seguir jugando", True, rojo
            )
            screen.blit(message, [alto / 6, ancho / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                        game_exit = True
                    if event.key == pygame.K_c:
                        game_loop()

        # Control de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cambiox = -tamañoBloque
                    cambioy = 0
                elif event.key == pygame.K_RIGHT:
                    cambiox = tamañoBloque
                    cambioy = 0
                elif event.key == pygame.K_UP:
                    cambioy = -tamañoBloque
                    cambiox = 0
                elif event.key == pygame.K_DOWN:
                    cambioy = tamañoBloque
                    cambiox = 0

        # Actualizar posición de la serpiente
        x += cambiox
        y += cambioy

        # Lógica del juego
        if x >= alto or x < 0 or y < 0:
            game_over = True

        # Actualizar posición de la serpiente
        x += cambiox
        y += cambioy

        screen.fill(blanco)
        pygame.draw.rect(screen, rojo, [comidaX, comidaY, tamañoBloque, tamañoBloque])
        serpienteCuerpo = []
        serpienteCuerpo.append(x)
        serpienteCuerpo.append(y)
        serpienteLista.append(serpienteCuerpo)

        if len(serpienteLista) > serpienteLongitud:
            del serpienteLista[0]

        for segment in serpienteLista[:-1]:
            if segment == serpienteCuerpo:
                game_over = True

        dibujarSerpiete(tamañoBloque, serpienteLista)

        pygame.display.update()

        if x == comidaX and y == comidaY:
            comidaX = (
                round(random.randrange(0, alto - tamañoBloque) / tamañoBloque)
                * tamañoBloque
            )
            comidaY = (
                round(random.randrange(0, ancho - tamañoBloque) / tamañoBloque)
                * tamañoBloque
            )
            serpienteLongitud += 1

        clock.tick(velocidad)

    pygame.quit()


# Iniciar el juego
game_loop()
