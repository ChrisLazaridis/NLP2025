# Natural Language Processing Summer 2025 Assignment

![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![Poetry](https://img.shields.io/badge/poetry-managed-brightgreen)

**Authors:** Christos Lazaridis, Athanasios Kalogeropoulos, Michalis Nikiforakis

---

## Overview

This repository contains the coding portion of the Summer 2025 Natural Language Processing (NLP) assignment, which focuses on addressing ambiguity in text.

---

## Repository Structure

├── Naive/           Deterministic automata and basic NLP techniques
├── ML/              LSTM-based encoder-decoder (Seq2Seq) implementations
│   ├── try1/        First ML approach (models and preprocessing)
│   └── try2/        Second ML approach (models and preprocessing)
├── Lib/             Library-based approach with pre-trained models
├── poetry.toml      Poetry configuration
└── poetry.lock      Locked dependencies for reproducibility
- **Naive/**  
  Contains two attempts at reconstructing selected sentences using deterministic automatons and rule-based NLP techniques.

- **ML/**  
  Includes two LSTM-based Seq2Seq systems: one in each subdirectory (`model1/` and `model2/`). Each contains training and evaluation CSV files.

- **Lib/**  
  Leverages pre-trained models and external pipelines to reconstruct entire texts in a more flexible manner.

---

## Dataset

The input dataset for the second ML model is hosted on Kaggle:  
**EnronSense Ambiguity Dataset**  
https://www.kaggle.com/datasets/christoslazaridis/enronsent-ambiguity
**HuggingFace Repository**
https://huggingface.co/RagerGr/NLP2025-Ambiguity
---

## Prerequisites

- **Python** 3.10
- **Poetry/Conda** for dependency management

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
2. **Install dependencies**
  ```bash
   poetry install
3. **Run setup.py**
