# tools_docking.py
# Pipeline di docking ad alto livello

from ..docking.prepare_receptor import prepare_receptor
from ..docking.prepare_ligand import prepare_ligand
from ..docking.vina_wrapper import run_vina

def docking_pipeline(receptor_pdb: str, ligand_block: str,
                     center=(0,0,0), size=(20,20,20)):
    """
    Pipeline logica (per ora senza Vina reale):
    1. prepara recettore
    2. prepara ligando
    3. chiama run_vina (placeholder)
    """
    rec_prep = prepare_receptor(receptor_pdb)
    lig_prep = prepare_ligand(ligand_block)

    # In futuro: conversione in PDBQT
    result = run_vina("receptor.pdbqt", "ligand.pdbqt",
                      center=center, size=size)

    return {
        "receptor_prepared": rec_prep,
        "ligand_prepared": lig_prep,
        "docking_result": result,
    }
