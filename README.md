# Natural Language Processing Summer 2025 Assignment

![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![Poetry](https://img.shields.io/badge/poetry-managed-brightgreen)

**Authors:** Christos Lazaridis, Athanasios Kalogeropoulos, Michalis Nikiforakis

---

## Overview

This repository contains the coding portion of the Summer 2025 Natural Language Processing (NLP) assignment, which focuses on addressing ambiguity in text.

---

## Repository Structure
```
├── Naive/           Deterministic automata and basic NLP techniques
├── ML/              LSTM-based encoder-decoder (Seq2Seq) implementations
│   ├── try1/        First ML approach (models and preprocessing)
│   └── try2/        Second ML approach (models and preprocessing)
├── external_pipelines/             Library-based approach with pre-trained models
├── evaluatiom/                  Evaluation of all approaches
├── Masking/                     The non mandatory Masking Research on Greek Text (only reproducable through kaggle)
├── Papers/                      The papers for the two exercises
├── poetry.toml      Poetry configuration
└── poetry.lock      Locked dependencies for reproducibility
```
- **Naive/**  
  Contains two attempts at reconstructing selected sentences using deterministic automatons and rule-based NLP techniques.

- **ML/**  
  Includes two LSTM-based Seq2Seq systems: one in each subdirectory (`model1/` and `model2/`). Each contains training and evaluation CSV files.

- **external_pipelines/**  
  Leverages pre-trained models and external pipelines to reconstruct entire texts in a more flexible manner.
- **Report**
  Detailed report with our metholodogy and findings lies in [Report](https://github.com/ChrisLazaridis/NLP2025/blob/main/Papers/NLP2025Mandatory.pdf)
  The report of the Greek Masking exercise with it's detailed results lies in [Report](https://github.com/ChrisLazaridis/NLP2025/blob/main/Papers/NLP2025Optional.pdf)

---

## Dataset

The input dataset for the second ML model is hosted on Kaggle:  
**EnronSense Ambiguity Dataset**  
https://www.kaggle.com/datasets/christoslazaridis/enronsent-ambiguity
**HuggingFace Repository**
https://huggingface.co/RagerGr/NLP2025-Ambiguity

---

## Prerequisites

- **Python** 3.12
- **Poetry/Conda** for dependency management

---

## Installation
1. **Create a new conda environment on `python12` using
```bash
conda create -n <env-name> python=3.12 -y
```

2. **Clone the repository**
   ```bash
   git clone https://github.com/ChrisLazaridis/NLP2025.git
   cd NLP2025
3. **Install dependencies**
  inside the `conda` environment
  ```bash
   pip install poetry
   poetry install --no-root
```
3. **Run setup.py**
