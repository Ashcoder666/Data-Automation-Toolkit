# 📊 Data Automation Toolkit

A beginner-friendly **data cleaning and automation toolkit** built with Python.  
This project uses real-world datasets (Titanic, Netflix, and Superstore) to demonstrate how to **clean, transform, and export data** in multiple formats (CSV, JSON, Excel).  

---

## 🚀 Features
- Handle missing/null values (drop, fill, interpolate).
- Normalize text (case formatting, remove duplicates).
- Convert column types (dates, numbers, categorical).
- Perform filtering, sorting, and aggregations.
- Create derived columns (e.g., profit margin, categories).
- Import/export datasets to **CSV, JSON, Excel**.
- Command-line utility to clean datasets with a single command.


---

## 📊 Datasets Used
- **[Titanic Dataset](https://www.kaggle.com/c/titanic/data)** → survival analysis & missing data.
- **[Netflix Movies & TV Shows](https://www.kaggle.com/shivamb/netflix-shows)** → text cleaning & JSON export.
- **[Superstore Sales Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)** → Excel operations.
- **Messy CSVs (self-generated)** → practice handling nulls & inconsistencies.

---

## ⚡ Installation
Clone this repo and install dependencies:
```bash
git clone https://github.com/your-username/data-automation-toolkit.git
cd data-automation-toolkit
pip install -r requirements.txt
🛠 Usage
1️⃣ Run from CLI

python clean_data.py data/titanic.csv --export json
Options:

--export csv → save as CSV

--export json → save as JSON

--export excel → save as Excel

2️⃣ Use in Jupyter Notebook

import pandas as pd
from utils.clean_utils import clean_dataframe
from utils.file_utils import export_data

df = pd.read_csv("data/netflix.csv")
df_clean = clean_dataframe(df)
export_data(df_clean, "output/netflix_clean.json", "json")
📦 Requirements
Python 3.9+

Pandas

OpenPyXL

Jupyter Notebook

Install via:


pip install -r requirements.txt
📸 Example Output
Name	Age	Survived
Jack Dawson	20	0
Rose DeWitt	19	1
Thomas Andrews	39	0

Cleaned Titanic dataset sample (missing ages handled, casing normalized).

🔮 Roadmap
Add automated data profiling report (using pandas-profiling).

Extend CLI to support multiple datasets at once.

Add visualization utilities for summary statistics.

🤝 Contributing
Contributions are welcome!

Fork the repo

Create a feature branch (git checkout -b feature-new)

Commit changes (git commit -m 'Add new feature')

Push to branch & open a Pull Request

📜 License
This project is licensed under the MIT License.

