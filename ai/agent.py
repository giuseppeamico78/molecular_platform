# agent.py
# "Mente" della piattaforma: orchestration dei tool

from . import tools_viewer, tools_analysis, tools_docking, tools_db

class MolecularAgent:
    """
    Orchestratore semplice che chiama i vari tool.
    In futuro: integrazione con LLM.
    """
    def __init__(self):
        pass

    def describe_structure(self, mol_obj):
        return tools_analysis.describe_molecule(mol_obj)

    def run_docking_workflow(self, receptor, ligand):
        return tools_docking.docking_pipeline(receptor, ligand)

    def fetch_from_db(self, source, identifier):
        return tools_db.fetch_from_source(source, identifier)
