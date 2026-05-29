# scoring.py
# Funzioni di scoring e analisi pose di docking

import math

def rmsd(coords1, coords2):
    """
    Calcola l'RMSD tra due liste di coordinate:
    coords = [(x,y,z), (x,y,z), ...]
    """
    if len(coords1) != len(coords2):
        raise ValueError("Le due liste devono avere lo stesso numero di atomi.")

    n = len(coords1)
    s = 0.0

    for (x1,y1,z1), (x2,y2,z2) in zip(coords1, coords2):
        s += (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2

    return math.sqrt(s / n)


def rank_by_energy(energies):
    """
    Ordina le energie dal valore più basso (migliore) al più alto.
    Ritorna gli indici ordinati.
    """
    return sorted(range(len(energies)), key=lambda i: energies[i])


def normalize_energies(energies):
    """
    Normalizza le energie tra 0 e 1.
    """
    if not energies:
        return []

    min_e = min(energies)
    max_e = max(energies)

    if max_e == min_e:
        return [0.0 for _ in energies]

    return [(e - min_e) / (max_e - min_e) for e in energies]
