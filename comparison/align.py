# align.py
# Allineamento strutturale (scheletro, per estensioni future)

def superpose_structures(coords_ref, coords_mobile):
    """
    Placeholder per superposizione strutturale.
    Per ora ritorna semplicemente le stesse coordinate.
    In futuro: Kabsch / SVD per allineamento ottimale.
    """
    if len(coords_ref) != len(coords_mobile):
        raise ValueError("Le due strutture devono avere lo stesso numero di atomi.")
    return coords_mobile
