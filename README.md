# Big Data Processing with MapReduce and Spark

This repository contains implementations for two big data processing problems using Python's mrjob library for MapReduce and PySpark for distributed data processing.

## Project Overview

This project demonstrates distributed data processing techniques through two main problems:
- **Problem I**: Statistical analysis of income data using MapReduce (mrjob)
- **Problem II**: Analysis of world cities population data using PySpark

## Repository Structure

```
.
├── p1/                          # Problem I: MapReduce implementations
│   ├── bigdata_p1.ipynb        # Jupyter notebook with all mrjob implementations
│   ├── trial_incomes.csv       # Small dataset (1,000 records) for testing
│   └── test_incomes.zip        # Large dataset (1M+ records) for production
│
├── p2/                          # Problem II: PySpark implementations
│   ├── bigdata_p2 (2).ipynb    # Jupyter notebook with PySpark solutions
│   ├── Install_And_Test_Spark.ipynb  # Spark installation guide and demos
│   └── worldcitiespop.zip      # World cities population dataset
│
├── report/                      # MapReduce Python programs (standalone)
│   ├── total_incomes.py        # Calculate sum of all incomes
│   ├── mean.py                 # Calculate mean income
│   ├── generalized_mean.py     # Calculate generalized mean (p-norm)
│   ├── maximum.py              # Find maximum income
│   ├── minimum.py              # Find minimum income
│   └── standard_deviation.py   # Calculate standard deviation
│
├── report.pdf                   # Final report with results
├── report.docx                  # Report (Word format)
└── FinalExam.pdf               # Assignment description
```

## Problem I: MapReduce Income Analysis

### Objective
Calculate statistical metrics on income datasets using MapReduce pattern with Python's mrjob library.

### Datasets
- **trial_incomes.csv**: 1,000 income records (for development/testing)
- **test_incomes.csv**: 1,000,000+ income records (for large-scale testing)

### Implementations

Six separate MapReduce programs calculate different statistics:

#### 1. Total Incomes (`total_incomes.py`)
Calculates the sum of all incomes in the dataset.

**Formula**: `Total = Σxi`

**Results**:
- Trial: 63,168
- Test: 210,015,551,664

#### 2. Mean (`mean.py`)
Calculates the arithmetic mean of all incomes.

**Formula**: `μ = (1/n) × Σxi`

**Results**:
- Trial: 63.168
- Test: 21,001.56

#### 3. Generalized Mean (`generalized_mean.py`)
Calculates the generalized mean (power mean) with order p=2.

**Formula**: `Mp = ((1/n) × Σ(xi^p))^(1/p)`

**Results** (p=2):
- Trial: 665.86
- Test: 52,883,028.36

#### 4. Maximum (`maximum.py`)
Finds the highest income value in the dataset.

**Results**:
- Trial: 13,473
- Test: 164,016,448,792

#### 5. Minimum (`minimum.py`)
Finds the lowest income value in the dataset.

**Results**:
- Trial: 1
- Test: 1

#### 6. Standard Deviation (`standard_deviation.py`)
Calculates the population standard deviation.

**Formula**: `σ = sqrt(Σ(xi - μ)² / n)`

**Results**:
- Trial: 662.85
- Test: 52,883,024.19

### Usage

Each program can be run independently using mrjob:

```bash
# Install mrjob
pip install mrjob

# Run on trial dataset
python report/total_incomes.py p1/trial_incomes.csv

# Run on test dataset (requires extraction of zip file)
unzip p1/test_incomes.zip
python report/total_incomes.py test_incomes.csv
```

## Problem II: Sparkifying World Cities

### Objective
Analyze world cities population data using PySpark with efficient transformations (limited to 4 shufflable operations).

### Dataset
**worldcitiespop.txt**: Contains city-level population data with columns:
- Country code
- City name
- Region
- Population
- Latitude/Longitude

### Implemented Tasks

1. **Data Cleaning**: Filter rows with valid population data
2. **Statistics**: Calculate min, max, sum, and average of city populations
3. **Histogram**: Generate frequency histogram with logarithmic bins
4. **Top-K Cities**: Find 10 most populous cities
5. **Population Percentage**: Calculate % of total population by top K cities
6. **Regional Analysis**: Total population by region
7. **Country Filtering**: Countries with total population > threshold
8. **Country Averages**: Average population per country (with threshold)
9. **Above-Average Cities**: Cities exceeding their country's average
10. **Deduplication**: Remove duplicate cities (e.g., Delhi/New Delhi)

### Expected Results (After Deduplication)

**Statistics**:
- Count: 37,774 cities
- Mean: 56,685.35
- Standard Deviation: 335,272.73
- Max: 31,480,498
- Min: 7.0

**Histogram** (logarithmic bins):
```
[(0, 4), (1, 65), (2, 1324), (3, 14545), (4, 18456), (5, 3107), (6, 264), (7, 9)]
```

**Top 10 Cities**:
1. Tokyo, Japan - 31,480,498
2. Shanghai, China - 14,608,512
3. Bombay, India - 12,692,717
4. Karachi, Pakistan - 11,627,378
5. Delhi, India - 10,928,270
6. Manila, Philippines - 10,443,877
7. Moscow, Russia - 10,381,288
8. Seoul, South Korea - 10,323,448
9. São Paulo, Brazil - 10,021,437
10. Istanbul, Turkey - 9,797,536

### Usage

Run the PySpark notebook on Google Colab:

```python
# The notebook includes Spark installation
# All tasks are implemented using PySpark RDD transformations
# Limited to 4 shufflable operations per task
```

## Technical Details

### MapReduce Pattern
Each mrjob program follows the standard MapReduce pattern:
- **Mapper**: Emits key-value pairs from input data
- **Reducer**: Aggregates values by key to produce final results

### PySpark Constraints
Solutions must use at most 4 shufflable transformations:
- `reduceByKey`, `groupByKey`, `combineByKey`
- `sortByKey`, `join`, `leftOuterJoin`, `rightOuterJoin`
- `intersection`, `cogroup`, `groupWith`
- `distinct`, `repartition`, `coalesce`

## Requirements

### Python Packages
```bash
pip install mrjob
pip install pyspark
pip install pandas  # For validation
```

### Environment
- Python 3.x
- Jupyter Notebook or Google Colab (for .ipynb files)
- Sufficient memory for large datasets (test_incomes: ~7MB, worldcitiespop: ~40MB)

## Running the Code

### For MapReduce Programs

```bash
# Navigate to report directory
cd report

# Run any statistical calculation
python total_incomes.py ../p1/trial_incomes.csv
python mean.py ../p1/trial_incomes.csv
python standard_deviation.py ../p1/trial_incomes.csv
```

### For Spark Programs

1. Open `p2/bigdata_p2 (2).ipynb` in Google Colab
2. Run cells sequentially
3. Spark installation is included in the notebook
4. Results are displayed inline

## Results Validation

The implementation includes validation by comparing MapReduce results with pandas calculations to ensure correctness. All results match expected values within floating-point precision.

## Documentation

- **FinalExam.pdf**: Complete assignment specification
- **report.pdf**: Detailed report with outputs and analysis
- **report.docx**: Report in Word format

## Key Learnings

1. **Distributed Computing**: MapReduce enables processing of large datasets that don't fit in memory
2. **Scalability**: Both solutions scale from 1K to 1M+ records
3. **Optimization**: PySpark shuffle constraints force efficient algorithm design
4. **Data Quality**: Handling missing values and duplicates in real-world datasets

## Author

Big Data Final Exam Project - MapReduce and Spark Implementations

## License

Academic project for educational purposes.
