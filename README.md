# Ozon Dataset Project

## Overview
This project automates the process of collecting, downloading, and merging category-based datasets from Ozon.

## Workflow

### 1. Get Links by Category into CSV
- Collect category links from Ozon and save them into a CSV file (e.g., `ozon_links.csv`).
- Each row contains a category label and its corresponding URL.

### 2. Download Dataset by Category
- For each link in the CSV, the script opens the link, clicks the Download button, and saves the resulting dataset (usually as an `.xlsx` file).
- Downloaded files are named according to their category label for easy identification.

### 3. Merge All Datasets into One
- All downloaded `.xlsx` files are merged into a single dataset using the provided merge script.
- The script removes unnecessary header rows, keeps only the relevant column names, adds a `Category` column, and exports the final merged dataset as a CSV file.

## Usage

1. **Collect Links**
   - Prepare `ozon_links.csv` with columns: `Label;URL`.

2. **Download Datasets**
   - Run the download script to fetch and save all category datasets.

3. **Merge Datasets**
   - Run `merge_brands_year.py` to combine all `.xlsx` files in the `brands_year` folder into `merged_brands_year.csv`.
