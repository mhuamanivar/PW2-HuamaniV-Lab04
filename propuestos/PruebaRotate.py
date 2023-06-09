# Melsy Melany Huamaní Vargas
# Pw2 - Laboratorio 04

from interpreter import draw
from chessPictures import *

wSquare = square
bSquare = square.negative()

wPawns = wSquare.under(pawn).join(bSquare.under(pawn)).horizontalRepeat(4)
bPawns = wPawns.negative()

wPieces = bSquare.under(rock).join(wSquare.under(knight)).join(bSquare.under(bishop)).join(wSquare.under(queen)).join(bSquare.under(king)).join(wSquare.under(bishop)).join(bSquare.under(knight)).join(wSquare.under(rock))
bPieces = wPieces.negative()

squares1 = bSquare.up(wSquare)
squares2 = wSquare.up(bSquare)

finalSquares = squares1.join(squares2).verticalRepeat(2).horizontalRepeat(4)

tabla = wPieces.up(wPawns.up(finalSquares.up(bPawns.up(bPieces))))

draw(tabla.rotate())
