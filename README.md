# bank-marketing-analysis

Team: *Ravdeep Aulakh, Camille Ng*

This repo contains a clean, modular pipeline for **Data Preprocessing** and **Exploratory Data Analysis (EDA)**
on the Bank Marketing dataset (Kaggle). It is organized for easy grading and reproducibility.


## Repo Structure

```
cmpt459-project/
├── data/
│   └── bank.csv
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   └── 02_eda.ipynb
├── src/
│   ├── preprocessing.py
│   └── visualization.py
├── README.md
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

4. **Run the preprocessing notebook**
   - Open Jupyter: `jupyter notebook`
   - Run: `notebooks/01_data_preprocessing.ipynb`
   - It will create `data/bank_cleaned.csv`

5. **Run the EDA notebook**
   - Run: `notebooks/02_eda.ipynb` to generate plots and quick insights.