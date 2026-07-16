# Transcriptomic-Data_Analysis

# RNA-seq Analysis of Human Immune Cell Subsets Across Diseases

> A complete RNA-seq analysis workflow using publicly available GEO data, covering metadata exploration, quality control, exploratory data analysis, dimensionality reduction, differential expression analysis, and biological interpretation.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.x-orange)
![NumPy](https://img.shields.io/badge/NumPy-1.x-blue)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-green)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-blueviolet)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-PCA-yellow)

---

# Project Overview

RNA sequencing (RNA-seq) is a powerful technique for studying genome-wide gene expression and identifying molecular differences between biological conditions.

This project demonstrates a complete RNA-seq analysis pipeline using a publicly available dataset from the NCBI Gene Expression Omnibus (GEO). The workflow includes:

- Data loading and preprocessing
- Metadata parsing and cleaning
- Exploratory data analysis
- Quality control
- PCA and clustering
- Differential gene expression analysis
- Biological interpretation

The goal is to reproduce the early stages of a real-world bioinformatics workflow while following reproducible research practices.

---

# Dataset

**Source**

NCBI Gene Expression Omnibus (GEO)

**Accession**

GSE60424

**Title**

Next generation sequencing of human immune cell subsets across diseases

Dataset includes RNA-seq profiles from multiple immune cell populations collected from patients with:

- Healthy Controls
- Multiple Sclerosis (Pre-treatment)
- Multiple Sclerosis (Post-treatment)
- Type 1 Diabetes
- Sepsis
- Amyotrophic Lateral Sclerosis (ALS)

The study contains RNA-seq expression profiles from:

- Whole Blood
- CD4 T Cells
- CD8 T Cells
- B Cells
- NK Cells
- Monocytes
- Neutrophils

---

# Objectives

- Explore RNA-seq count data
- Parse and organize GEO metadata
- Investigate sample distribution across diseases and immune cell types
- Perform quality control
- Visualize sample relationships using PCA
- Identify differentially expressed genes between selected biological conditions
- Generate publication-quality figures

---

# Project Structure

```text
rna-seq-mini/

├── data/
│   ├── raw/
│   ├── processed/
│   └── metadata/
│
├── notebooks/
│   ├── 01_Data_Loading.ipynb
│   ├── 02_Metadata_Exploration.ipynb
│   ├── 03_Preprocessing_QC.ipynb
│   ├── 04_PCA_and_Clustering.ipynb
│   ├── 05_Differential_Expression.ipynb
│   ├── 06_Functional_Analysis.ipynb
│   └── 07_Report.ipynb
│
├── scripts/
│
├── figures/
│
├── results/
│
├── requirements.txt
│
└── README.md
```

---

# Analysis Workflow

```text
          GEO Dataset
               │
               ▼
     Load Expression Matrix
               │
               ▼
       Parse Sample Metadata
               │
               ▼
      Metadata Exploration
               │
               ▼
        Quality Control
               │
               ▼
      Low Count Filtering
               │
               ▼
      Log2 Transformation
               │
               ▼
      Principal Component Analysis
               │
               ▼
      Sample Clustering
               │
               ▼
 Differential Expression Analysis
               │
               ▼
    Volcano Plot & Heatmap
               │
               ▼
 Functional Interpretation
```

---

# Metadata Explored

The metadata extracted from the GEO Series Matrix include:

- Sample ID
- GEO Accession
- Cell Type
- Disease Status
- Age
- Gender
- Donor ID
- Race
- Smoking Status
- Collection Date

These metadata are used to identify biologically meaningful comparisons while avoiding confounding variables.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SciPy
- Jupyter Notebook

Future additions:

- DESeq2
- GSEApy
- Scanpy
- Biopython

---

# Results

The project generates:

- Metadata summary tables
- Disease distribution plots
- Cell type distribution plots
- Expression distributions
- PCA plots
- Correlation heatmaps
- Hierarchical clustering
- Volcano plots
- Heatmaps of differentially expressed genes
- Functional enrichment analysis

---

# Learning Outcomes

Through this project I learned to:

- Work with public RNA-seq datasets from GEO
- Parse complex GEO metadata
- Organize RNA-seq projects using reproducible folder structures
- Perform quality control on RNA-seq count data
- Explore transcriptomic datasets using PCA and clustering
- Prepare data for differential expression analysis
- Build publication-ready visualizations
- Follow reproducible bioinformatics workflows

---

# Future Improvements

- Differential expression using DESeq2
- Batch effect correction
- Gene Ontology enrichment
- KEGG pathway analysis
- Interactive dashboards
- Workflow automation using Snakemake

---

# Citation

If you use this dataset, please cite:

Linsley PS, Speake C, Whalen E, et al.

**Copy number loss of the interferon gene cluster in melanomas is linked to reduced T cell infiltrate and poor patient prognosis.**

PLoS ONE (2014)

Dataset:
GEO Accession: GSE60424

---

# License

This project is released under the MIT License.

---

# Author

**Antara Shaw**

Bioinformatics | Computational Biology | Cancer Genomics

GitHub: https://github.com/antara-1505

LinkedIn: *https://www.linkedin.com/in/antara-shaw-480384224/*
