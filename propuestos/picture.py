from colors import *

class Picture:
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        if color not in inverter:
            return color
        return inverter[color]

    def verticalMirror(self):
        """ Devuelve el espejo vertical de la imagen """
        vertical = []
        for value in self.img:
            vertical.append(value[::-1])
        return Picture(vertical)

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        horizontal = self.img[::-1]
        return Picture(horizontal)

    def negative(self):
        """ Devuelve un negativo de la imagen """
        negative = []
        for value in self.img:
            invertedColor = "".join([self._invColor(c) for c in value])
            negative.append(invertedColor)
        return Picture(negative)

    def join(self, p):
        """ Devuelve una nueva figura poniendo la figura del argumento 
            al lado derecho de la figura actual """
        joined = []
        for i in range(len(self.img)):
            joined.append(self.img[i]+p.img[i])
        return Picture(joined)
