import pygame
from src.ship import Ship
from src.settings import Settings


def test_ship_move_right():
    pygame.init() # Inicializa o Pygame para evitar erros relacionados a superfícies e fontes

    screen = pygame.display.set_mode((800, 600)) # Cria uma janela de teste
    settings = Settings() # Cria uma instância de Settings para passar para a Ship

    ship = Ship(screen, settings) # Cria uma instância da Ship

    
    x_inicial = ship.x # Armazena a posição inicial da nave

    # Ação
    ship.moving_right = True # Define a flag de movimento para a direita
    ship.update() # Atualiza a posição da nave

    # Verificação
    assert ship.x > x_inicial # Verifica se a posição x da nave aumentou, indicando que ela se moveu para a direita