# rmsd.py
# RMSD strutturale tra due insiemi di coordinate

import math

def rmsd(coords1, coords2):
    """
    Calcola l'RMSD tra due liste di coordinate:
    coords = [(x,y,z), ...]
    """
    if len(coords1) != len(coords2):
        raise ValueError("Le due liste devono avere lo stesso numero di atomi.")

    n = len(coords1)
    s = 0.0

    for (x1,y1,z1), (x2,y2,z2) in zip(coords1, coords2):
        s += (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2

    return math.sqrt(s / n)
