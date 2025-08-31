# Collatz Proof Companion — Automaton Visualization

This repository provides the **interactive automaton visualization** that accompanies the proof paper:

**Idriss Elyamani (2025).  
_A Multi-Domain, Mechanistic Model of the Collatz Dynamic_**

The project contains both the **interactive web demo** (viewable via GitHub Pages) and the **data generation pipeline** used to construct the automaton graphs.

---

## 🔗 Live Demo


The visualization allows you to explore **k-bit Collatz automata**, showing states, classifications, and transition edges derived from the True Explicit Collatz Formula.

---

## 📂 Repository Structure

├── README.md # Project documentation (this file)
├── index.html # Main interactive visualization page (for GitHub Pages)
├── graph_data.js # Precomputed automaton data for k = 2,...,12
├── generate_graph_data.py # Python script to regenerate the graph data



---

## ⚙️ Usage

### 1. Interactive Visualization
Simply open **index.html** in any modern browser (or use the GitHub Pages link above).  
You can zoom, pan, and click states to inspect automaton properties.

### 2. Regenerating Graph Data
To reproduce or extend the dataset:

```bash
python generate_graph_data.py
This will:

Generate automaton nodes & edges for k = 2,...,12

Save results into graph_data.js for direct use by the visualization

📖 Mathematical Background
The automaton encodes the Collatz dynamics modulo 2^k.
Each state S_j is classified as:

Contractive: convergent states (j ≡ 1 mod 4)

Transitional: special states (j ≡ 3 mod 4)

Highest: maximal state (j = 2^k - 1)

Unknown: edge cases

Transition edges correspond to the successor function:

𝑓
(
𝑛
)
=
3
𝑛
+
1
2
𝑣
2
(
3
𝑛
+
1
)
f(n)= 
2 
v 
2
​
 (3n+1)
 
3n+1
​
 
projected onto the space of k-bit residue classes.

🛠️ Technology Stack
Python 3 → generates automaton graph data

JavaScript (JSON export) → serves precomputed data

HTML + JS (Cytoscape.js / D3.js) → interactive visualization frontend



mathematica

Idriss Elyamani (2025).
A Multi-Domain, Mechanistic Model of the Collatz Dynamic.
Supplementary Interactive Visualization: GitHub Repository.
📬 Contact
For questions, collaborations, or further details:
Idriss Elyamani — GitHub Profile


---

✨ This README is **polished, formal, self-contained**.  
It explains the project, provides live demo access, reproducibility instructions, background, and citation
