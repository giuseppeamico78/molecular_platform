from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import di TUTTI i router API
from .pdb_api import router as pdb_router
from .pdbe_api import router as pdbe_router
from .pubchem_api import router as pubchem_router
from .chembl_api import router as chembl_router
from .alphafold_api import router as alphafold_router
from .uniprot_api import router as uniprot_router
from .swissmodel_api import router as swissmodel_router
from .pubmed_api import router as pubmed_router
from .sciencedirect_api import router as sciencedirect_router
from .nature_api import router as nature_router
from .crossref_api import router as crossref_router   # ⭐ NUOVO


app = FastAPI(
    title="Molecular Platform API",
    description="Backend modulare per integrazione database molecolari e articoli scientifici",
    version="1.0.0"
)

# ---------------------------------------------------------
# CORS (per frontend React / JS)
# ---------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------
# REGISTRAZIONE DI TUTTI I ROUTER
# ---------------------------------------------------------

app.include_router(pdb_router, prefix="/pdb")
app.include_router(pdbe_router, prefix="/pdbe")
app.include_router(pubchem_router, prefix="/pubchem")
app.include_router(chembl_router, prefix="/chembl")
app.include_router(alphafold_router, prefix="/alphafold")
app.include_router(uniprot_router, prefix="/uniprot")
app.include_router(swissmodel_router, prefix="/swissmodel")

# Literature
app.include_router(pubmed_router, prefix="/pubmed")
app.include_router(sciencedirect_router, prefix="/sciencedirect")
app.include_router(nature_router, prefix="/nature")
app.include_router(crossref_router, prefix="/crossref")   # ⭐ NUOVO FALLBACK UNIVERSALE

# ---------------------------------------------------------
# ROOT
# ---------------------------------------------------------
@app.get("/")
def root():
    return {"message": "Molecular Platform API is running"}
