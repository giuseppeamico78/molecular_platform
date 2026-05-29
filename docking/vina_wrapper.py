# vina_wrapper.py
# Wrapper per AutoDock Vina (struttura base, senza esecuzione reale)

import os

class VinaDockingResult:
    """
    Risultato del docking:
    - pose (lista di PDBQT o PDB)
    - energie (lista di float)
    """
    def __init__(self, poses=None, energies=None):
        self.poses = poses or []
        self.energies = energies or []

    def __repr__(self):
        return f"<VinaDockingResult: {len(self.poses)} poses>"


def run_vina(receptor_pdbqt: str, ligand_pdbqt: str,
             center=(0,0,0), size=(20,20,20),
             exhaustiveness=8, num_modes=9):
    """
    Wrapper base per AutoDock Vina.
    Per ora NON esegue il docking reale.
    Ritorna un oggetto VinaDockingResult vuoto.
    """

    # Validazione parametri
    if not receptor_pdbqt or not ligand_pdbqt:
        raise ValueError("Receptor e ligand devono essere in formato PDBQT.")

    if not isinstance(center, tuple) or len(center) != 3:
        raise ValueError("center deve essere una tupla (x, y, z).")

    if not isinstance(size, tuple) or len(size) != 3:
        raise ValueError("size deve essere una tupla (sx, sy, sz).")

    # Placeholder: docking non ancora implementato
    return VinaDockingResult(poses=[], energies=[])
