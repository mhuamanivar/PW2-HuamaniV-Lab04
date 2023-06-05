# Melsy Melany Huamaní Vargas
# Pw2 - Laboratorio 04

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

    def up(self, p):
        """ Devuelve una nueva figura poniendo la figura recibida como argumento
            encima de la figura actual """
        newFigure = p.img[:]
        for value in self.img:
            newFigure.append(value)
        return Picture(newFigure)

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura p sobre la
            figura actual """
        filas = range(len(self.img))
        columnas = range(len(self.img[0]))

        newFigure = []
        for i in filas:
            string = ""
            for j in columnas:
                if (self.img[i][j] != p.img[i][j] and p.img[i][j] != " "):
                    string += p.img[i][j]
                else:
                    string += self.img[i][j]
            newFigure.append(string)
        return Picture(newFigure)
    
    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual al costado
            la cantidad de veces que indique el valor de n """
        newFigure = []
        for value in self.img:
            newFigure.append(value*n)
        return Picture(newFigure)

    def verticalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual debajo,
            la cantidad de veces que indique el valor de n """
        newFigure = self.img[:] * n
        return Picture(newFigure)
    
    #Extra
    def rotate(self):
        """Devuelve una figura rotada en 90 grados """
        filas = range(len(self.img))
        columnas = range(len(self.img[0]))

        newFigure = []
        for i in filas:
            string = ""
            for j in columnas:
                string += self.img[j][-i]
            newFigure.append(string)
        return Picture(newFigure)
