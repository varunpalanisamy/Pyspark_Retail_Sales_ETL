
# Pyspark Retail Sales ETL

## Project Description
This project is a Pyspark-based ETL pipeline to analyze retail sales data. The project performs data ingestion, transformation, aggregation, and visualization. The processed data is stored in Azure Data Lake.

## Features
- ETL pipeline using Pyspark
- Data aggregation and analysis
- Visualizations of retail sales trends
- Data export to Azure Data Lake Storage Gen2

## Directory Structure
```
Pyspark-Retail-Sales-ETL/
├── data/                      # Data files
├── src/                       # Source code for ETL and visualization
├── notebooks/                 # Exploratory notebooks (optional)
├── config/                    # Configuration files
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
└── LICENSE                    # License file
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/varunpalanisamy/Pyspark-Retail-Sales-ETL.git
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the ETL script using the following command:

   ```
   spark-submit --packages org.apache.hadoop:hadoop-azure:3.3.1,com.microsoft.azure:azure-storage:7.0.0 src/product_sales_etl/product_sales_etl.py
   ```
2. Run the visualization script:
   ```
   python src/visualization/visualization.py
   ```

## Output
The transformed data is exported to Azure Data Lake and visualized using Matplotlib.
