# Melsy Melany Huamaní Vargas
# Pw2 - Laboratorio 04

from interpreter import draw
from chessPictures import *

squares1 = square.negative().up(square)
squares2 = square.up(square.negative())

finalSquares = squares1.join(squares2)

draw(finalSquares.verticalRepeat(2).horizontalRepeat(4))
