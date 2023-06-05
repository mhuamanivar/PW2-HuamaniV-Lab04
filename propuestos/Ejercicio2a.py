# Melsy Melany Huamaní Vargas
# Pw2 - Laboratorio 04

from interpreter import draw
from chessPictures import *

wKnight = knight
bKnight = knight.negative()

firstKnights = wKnight.join(bKnight)
secondKnights = bKnight.join(wKnight)

draw(secondKnights.up(firstKnights))
