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
```
## 🧠 Tasks Overview

### 🔸 Node Classification

Predict the topic or research area of a **Paper** or **Author** using graph structure and related attributes. Example tasks include:
- Classifying papers into topics based on citation networks.
- Predicting an author's expertise based on their co-authorship network.

### 🔸 Link Prediction

Predict future **collaborations** or **citation links** between entities using supervised or unsupervised link prediction models. Example use cases:
- Forecasting future co-authorship.
- Suggesting relevant citations for a given paper.
- Recommending suitable journals for paper submission.

---

## 📊 Evaluation Metrics

### Node Classification:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score**

### Link Prediction:
- **AUC-ROC**
- **Precision@K**
- **Recall@K**

---

## 📘 Dataset Information

The dataset consists of the following CSV files:

- `authors.csv`: Author ID, Name, URL
- `journal.csv`: Journal Name, Publisher
- `paper.csv`: Paper ID, DOI, Title, Year, URL, Citation Count, Field of Study, Volume, Date
- `topic.csv`: Topic ID, Name, URL
- `paper_journal.csv`: Paper ID, Journal Name, Publisher
- `paper_topic.csv`: Paper ID, Topic ID
- `paper_reference.csv`: Paper ID, Referenced Paper ID

This dataset is derived from bibliographic research and is cited as follows:

BibTeX:
```bibtex
@article{10.1162/qss_a_00163,
  author = {Rothenberger, Liane and Pasta, Muhammad Qasim and Mayerhoffer, Daniel},
  title = {Mapping and impact assessment of phenomenon-oriented research fields: The example of migration research},
  journal = {Quantitative Science Studies},
  volume = {2},
  number = {4},
  pages = {1466-1485},
  year = {2021},
  doi = {10.1162/qss_a_00163}
}


