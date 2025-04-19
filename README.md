# GDS-Bibliographic-GraphML-Project

This project explores the application of **graph-based machine learning** techniques on a bibliographic dataset for two main tasks: **Node Classification** and **Link Prediction**. The dataset is extracted from bibliographic records, and the graph is constructed and analyzed using **Neo4j** and **Python-based ML frameworks**.

---

## 🚀 Project Overview

- **Domain**: Bibliographic Data Analysis
- **Frameworks Used**: Neo4j, NetworkX, Scikit-learn, PyTorch Geometric (optional)
- **Languages**: Python, Cypher
- **Tasks**:
  - Node Classification: Classify papers/authors using graph structure
  - Link Prediction: Predict future collaborations or citations

---

## 📂 Repository Structure

```bash
GDS-Bibliographic-GraphML-Project/
├── data/
│   ├── raw/                # Original CSV files
│   └── processed/          # Cleaned and merged files
│
├── src/
│   ├── preprocessing/      # Data cleaning and transformation scripts
│   ├── graph_construction/ # Graph model creation and Neo4j loading
│   ├── node_classification/ # ML models for node classification
│   ├── link_prediction/    # ML models for link prediction
│   └── utils/              # Shared helper functions
│
├── notebooks/              # EDA & Cypher query notebooks
│
├── results/                # Evaluation metrics, plots, and outputs
│
├── report/                 # Final project report in IEEE format
│
├── requirements.txt        # Python dependencies
├── README.md               # Project overview and setup (this file)
└── .gitignore              # Ignored files for Git
