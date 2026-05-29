# ligand_compare.py
# Confronto semplice tra ligandi (placeholder)

def compare_ligand_properties(props1: dict, props2: dict):
    """
    Confronta proprietà base di due ligandi:
    - formula
    - peso molecolare
    Ritorna un dizionario con le differenze.
    """
    result = {
        "formula_1": props1.get("formula"),
        "formula_2": props2.get("formula"),
        "mw_1": props1.get("molecular_weight"),
        "mw_2": props2.get("molecular_weight"),
    }

    if result["mw_1"] is not None and result["mw_2"] is not None:
        result["delta_mw"] = result["mw_2"] - result["mw_1"]
    else:
        result["delta_mw"] = None

    return result
