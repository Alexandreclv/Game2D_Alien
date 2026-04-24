from alien import Alien

class FastAlien(Alien):
    """Alienígena mais rápido."""

    def update(self):
        self.x += (self.settings.alien_speed * 2) * self.settings.fleet_direction # Move o alienígena para a direita ou esquerda com base na direção da frota, mas 50% mais rápido que os alienígenas normais
        self.rect.x = self.x # Atualiza a posição do rect do alienígena com base na nova coordenada x   