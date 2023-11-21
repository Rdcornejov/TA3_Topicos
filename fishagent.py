import random
from globals import Global
from pade.core.agent import Agent
from PySide6.QtGui import QColor

class FishAgent(Agent):
    def __init__(self, aid):
        super(FishAgent, self).__init__(aid=aid, debug=False)
        self.x = random.randint(1, 100)
        self.y = random.randint(1, 100)
        self.color = QColor(random.randint(0, 0xffffff))
        self.size = random.randint(5, 30)
        self.speed = 10 * 25 / self.size
        self.status = -1

    def updateStatus(self):
        if self.y < 200:
            self.status = 1
            if self.x > 300 :
                self.status = 4
        elif self.y > 500:
            self.status = 2
            if self.x < 30:
                self.status = 3
        else:
            if self.x < 30:
                self.status = 3
            else:
                self.status = 4

    def swim(self):
        if self.status == 1:
            self.x += self.speed
        elif self.status == 2:
            self.x -= self.speed
        elif self.status == 3:
            self.y -= self.speed
        elif self.status == 4:
            self.y += self.speed



