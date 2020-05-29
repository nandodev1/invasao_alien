class Settings:
    def __init__(self):
        """Classe para armazenar configurações
            da invasão alienigena"""
        self.screen_width = 1024
        self.scren_height = 740
        self.bg_color = (150,150,150)
        """configuração da espaçonave"""
        self.ship_speed_factor = 2.5

        """Configuração dos misséis"""

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
