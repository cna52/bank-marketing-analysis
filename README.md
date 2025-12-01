# bank-marketing-analysis

Team: *Ravdeep Aulakh, Camille Ng*

This repo contains a clean, modular pipeline for **Data Preprocessing** and **Exploratory Data Analysis (EDA)**
on the Bank Marketing dataset (Kaggle). It is organized for easy grading and reproducibility.


## Repo Structure

```
project-root/
│
├── data/
│ └── bank.csv
│
├── notebooks/
│ ├── 01_data_preprocessing.ipynb
│ ├── 02_eda.ipynb
│ ├── EDA_Preprocessing.ipynb
│ ├── elliptic_envelope_outlier_detection.ipynb
│ ├── final_project.ipynb
│ ├── grid_search_hyperparameter_tuning.ipynb
│ ├── hierarchical_cluster_analysis.ipynb
│ ├── isolation_forest_outlier_detection.ipynb
│ ├── kmeans_cluster_analysis.ipynb
│ ├── lasso_regression_feature_selection.ipynb
│ ├── random_forest_classification.ipynb
│ ├── rfe_feature_selection.ipynb
│ └── svm_classification.ipynb
│
├── src/
│ ├── preprocessing.py
│ └── visualization.py
│ 
├── .gitignore
├── README.md
│
└── requirements.txt
```

## Setup & Execution
1. **Create a virtual environment (recommended)**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add data**
   - [Bank Marketing Dataset](https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset)
   - Download `bank.csv` and place it at: `data/bank.csv`

4. **Run the preprocessing and EDA notebook**
   - Open Jupyter: `jupyter notebook`
   - Run: `notebooks/EDA_Preprocessing.ipynb`
   - It will create `data/bank_cleaned.csv`

5. **Run the Full Project Analysis**
   - Open Jupyter: `jupyter notebook`
   - Run: `final_project.ipynb`
   - All the Analysis and results will be self contained in this file along with a report for each major section