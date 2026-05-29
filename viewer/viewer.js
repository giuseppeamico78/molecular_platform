// viewer.js
// Viewer 3D con layout moderno e header con logo globale

export class MolecularViewer {
    constructor(containerId, options = {}) {
        this.containerId = containerId;
        this.options = options;

        // Inizializza layout
        this.initLayout();

        // Inizializza NGL
        this.stage = new NGL.Stage(this.viewerArea.id, {
            backgroundColor: options.theme === "dark" ? "black" : "white"
        });

        window.addEventListener("resize", () => {
            this.stage.handleResize();
        });
    }

    initLayout() {
        const container = document.getElementById(this.containerId);
        container.innerHTML = "";

        // HEADER
        const header = document.createElement("div");
        header.className = "viewer-header";

        const logo = document.createElement("img");
        logo.src = "/assets/logo.svg";
        logo.className = "viewer-logo";

        const title = document.createElement("div");
        title.className = "viewer-title";
        title.innerText = this.options.title || "Molecular Viewer";

        header.appendChild(logo);
        header.appendChild(title);

        // MAIN AREA
        const main = document.createElement("div");
        main.className = "viewer-main";

        // VIEWER AREA
        this.viewerArea = document.createElement("div");
        this.viewerArea.id = `${this.containerId}-3d`;
        this.viewerArea.className = "viewer-3d";

        // SIDEBAR (opzionale)
        this.sidebar = document.createElement("div");
        this.sidebar.className = "viewer-sidebar";
        this.sidebar.innerHTML = "<p>Ready.</p>";

        main.appendChild(this.viewerArea);
        main.appendChild(this.sidebar);

        container.appendChild(header);
        container.appendChild(main);
    }

    loadMoleculeFromString(pdbString, type = "protein") {
        const blob = new Blob([pdbString], { type: "text/plain" });
        const file = new File([blob], "structure.pdb");

        return this.stage.loadFile(file, { ext: "pdb" }).then(component => {
            this.component = component;
            this.applyStyle(type);
            this.stage.autoView();
        });
    }

    applyStyle(type) {
        if (!this.component) return;

        this.component.removeAllRepresentations();

        const styles = {
            protein: () => this.component.addRepresentation("cartoon", { colorScheme: "sstruc" }),
            ligand: () => this.component.addRepresentation("ball+stick", { colorScheme: "element" }),
            dna: () => this.component.addRepresentation("cartoon", { colorScheme: "nucleic" }),
            rna: () => this.component.addRepresentation("cartoon", { colorScheme: "nucleic" }),
            complex: () => {
                this.component.addRepresentation("cartoon", { colorScheme: "sstruc" });
                this.component.addRepresentation("ball+stick", { sele: "hetero", colorScheme: "element" });
            }
        };

        (styles[type] || styles["protein"])();
    }

    highlight(selection) {
        if (!this.component) return;

        this.component.addRepresentation("ball+stick", {
            sele: selection,
            color: "yellow",
            scale: 2.0
        });
    }

    setSidebarText(text) {
        this.sidebar.innerHTML = `<p>${text}</p>`;
    }

    reset() {
        if (this.component) {
            this.component.removeAllRepresentations();
            this.stage.removeComponent(this.component);
            this.component = null;
        }
    }
}
