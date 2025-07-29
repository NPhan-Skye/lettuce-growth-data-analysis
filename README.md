# 🥬 Lettuce Growth Days Analysis – Python Portfolio Project
> A hands-on Python project analyzing environmental factors affecting lettuce growth, using real-world agricultural data.

This repository demonstrates practical Python data analysis using a real-world dataset: the **Lettuce Growth Days** dataset sourced from [Kaggle](https://www.kaggle.com/). Originally designed for spreadsheet-based tasks as part of the Google Data Analytics Certificate, this project replicates and extends those objectives using Python. It includes a complete data pipeline—from cleaning and transformation to statistical analysis and visualization.

---

## Dataset Overview

- **Name**: Lettuce Growth Days  
- **Source**: [Kaggle - Lettuce Growth Days](https://www.kaggle.com/datasets/jurijsruko/lettuce)  
- **Timeframe**: August 3, 2023 – September 19, 2023  
- **Key Columns**: `Plant_ID`, `Date`, `Temperature (°C)`, `Humidity (%)`, `pH Level`, `TDS Value (ppm)`, `Growth Days`.

---

## SMART Questions Addressed

This project explores five SMART (Specific, Measurable, Actionable, Relevant, Time-Bound) questions:

| SMART Element       | Example Question                                                                |
|---------------------|---------------------------------------------------------------------------------|
| **Specific**        | Is there a connection between humidity and temperature?                         |
| **Measurable**      | What is the average growth over one week?                                       |
| **Action-Oriented** | Does increasing TDS speed up the growth of lettuce?                             |
| **Relevant**        | Which environmental factors are most related to plant growth?                   |
| **Time-Bound**      | What is the time range covered in this dataset?                                 |

---

## What This Code Does

| Feature                | Description |
|------------------------|-------------|
| **Data Cleaning**      | Handles inconsistent entries and removes irrelevant/redundant columns |
| **Descriptive Stats**  | Computes mean, median, min, max, and quartiles |
| **Feature Engineering**| Adds Fahrenheit temperature and Growth Weeks |
| **Correlation Analysis** | Measures and visualizes relationships between variables and plant growth |
| **Data Visualization** | Uses Matplotlib & Seaborn to create visual insights like heatmaps |
| **Exporting**          | Saves cleaned data and outputs for further use |

---

## Files in This Repository

| File                          | Description |
|-------------------------------|-------------|
| `analyze_lettuce.py`          | Main script that performs all analysis and visualization |
| `download_lettuce.py`         | Script to simulate data loading |
| `lettuce_dataset.csv`         | Original dataset from Kaggle |
| `lettuce_dataset_updated.csv` | Enhanced version with calculated features |
| `lettuce_cleaned.csv`         | Final cleaned dataset used for analysis |
| `lettuce_heatmap.png`         | Correlation heatmap image generated from the analysis |
| `unseen_data.csv`             | Optional external dataset for testing or additional exploration |

---

## License

The **Lettuce Growth Days** dataset is publicly available on [Kaggle](https://www.kaggle.com/) under the **Apache 2.0 License**.  
All rights and credit go to the original dataset creator.  
→ [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

---

## Author

Developed by **Skye (Ngan Phan)** as part of a professional portfolio for the **Google Data Analytics Professional Certificate**.

