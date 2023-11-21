from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPainter, QPixmap
from PySide6.QtWidgets import QFrame

class Gui(QFrame):
    def __init__(self, agent) -> None:
        super(Gui, self).__init__()
        self.agent = agent
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        mar_image = QImage("mar.jpg")
        painter.drawImage(0, 0, mar_image)
        for fish in self.agent.fish_list:
            # Cargar la imagen del pez
            fish_image = QImage("fish.png")
            
            # Escalar la imagen al tamaño del pez
            fish_image = fish_image.scaled(fish.size, fish.size//2)

            # Dibujar la imagen del pez en lugar del rectángulo
            painter.drawImage(fish.x, fish.y, fish_image)

