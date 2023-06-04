# Melsy Melany Huamaní Vargas
# Pw2 - Laboratorio 04

from interpreter import draw
from chessPictures import *

squares1 = square.up(square.negative())
squares2 = square.negative().up(square)

finalSquares = squares1.join(squares2)

draw(finalSquares.verticalRepeat(2).horizontalRepeat(4))
