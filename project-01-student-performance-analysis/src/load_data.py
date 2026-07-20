import pandas as pd

# Load the dataset
df = pd.read_csv('data/students.csv')

# =====================================================================
# 1. VIEWING THE FIRST 5 ROWS
# =====================================================================
print("\n" + "="*50)
print("📌 1. FIRST 5 ROWS OF THE DATASET")
print("="*50)
print(df.head())
print("-" * 50 + "\n")


# =====================================================================
# 2. DATASET DIMENSIONS (ROWS & COLUMNS)
# =====================================================================
print("="*50)
print("📊 2. DATASET DIMENSIONS")
print("="*50)
print(f"Total Number of Rows    : {len(df)}")
print(f"Total Number of Columns : {len(df.columns)}")
print("-" * 50 + "\n")


# =====================================================================
# 3. COLUMN NAMES LISTING
# =====================================================================
print("="*50)
print("📋 3. ALL COLUMN NAMES")
print("="*50)
# Loop through column names with a serial number starting from 1
for count, col in enumerate(df.columns, start=1):   
    print(f"  {count}. {col}")
print("-" * 50 + "\n")


# =====================================================================
# 4. DATA TYPES CHECKING
# =====================================================================
print("="*50)
print("⚙️ 4. DATA TYPE OF EVERY COLUMN")
print("="*50)
print(df.dtypes)
print("-" * 50 + "\n")


# =====================================================================
# 5. MISSING VALUES ANALYSIS
# =====================================================================
print("="*50)
print("🔍 5. MISSING VALUES IN EACH COLUMN")
print("="*50)
# Unpack key-value pairs to print each column name and its total missing values
for col_name, missing_count in df.isnull().sum().items():     
    print(f"  ➤ {col_name:<25} : {missing_count} missing values")
print("="*50 + "\n")


# =====================================================================
# 6. TOTAL MISSING VALUES IN DATASET
# =====================================================================
print("="*50)
print("🔍 6. TOTAL MISSING VALUES IN DATASET")
print("="*50)
print(f"Total Missing Values : {df.isna().sum().sum()}")
print("-"*50 + "\n")


# =====================================================================
# 7. DUPLICATE ROWS IN DATASET
# =====================================================================
print("="*50)
print("🔍 7. DUPLICATE ROWS IN DATASET")
print("="*50)
print(f"Number of Duplicate Rows : {df.duplicated().sum()}")
print("-"*50 +"\n")


# =====================================================================
# 8. NUMERICAL COLUMNS 
# =====================================================================
print("="*50)
print("🔍 8. NUMERICAL COLUMNS")
print("="*50)
print(f"Numerical Columns : {df.select_dtypes(include='number').columns.tolist()}")
print("-"*50 +"\n")


# =====================================================================
# 9. CATEGORICAL COLUMNS
# =====================================================================
print("="*50)
print("🔍 9. CATEGORICAL COLUMNS")
print("="*50)
print(f"Categorical Columns : {df.select_dtypes(include=['string', 'object']).columns.tolist()}")
print("-"*50 +"\n")


# =====================================================================
# 10. SUMMARY STATISTICS OF NUMERICAL COLUMNS
# =====================================================================
print("="*50)
print("📊 10. SUMMARY STATISTICS OF NUMERICAL COLUMNS")
print("="*50)
print(f"Summary Statistics (NUMERICAL COLUMNS) : {df.select_dtypes(include=['number']).describe()}")    # Describle helps to find mean, max, min
print("-"*50 +"\n")


# =====================================================================
# 11. MEMORY USAGE BY DATASET
# =====================================================================
print("="*50)
print("💻 11. MEMORY USAGE BY DATASET")
print("="*50)                                                           # deep = True helps to find exact memory 
print(f"Memory Usage : {df.memory_usage(deep=True).sum()/1024:.2f} KB") # sum helps to add memory usage of all columns
print("-"*50 +"\n")                                                     # :.2f means just show 2 number after decimal 


# =====================================================================
# 12. GENDER DISTRIBUTION
# =====================================================================
print("="*50)
print("👦🏻👧🏻 12. GENDER DISTRIBUTION")
print("="*50)

for gender, count in df['gender'].value_counts().items():
    print(f" ➤ {gender:<10} : {count}")
print("-"*50 + "\n")


# =====================================================================
# 13. LUNCH DISTRIBUTION
# =====================================================================
print("="*50)
print("🍱 13. LUNCH DISTRIBUTION")
print("="*50)

for lunch, count in df['lunch'].value_counts().items():
    print(f" ➤ {lunch:<15} : {count} students")
print("-"*50 + "\n")


# =====================================================================
# 14. TEST PREPARATION
# =====================================================================
print("="*50)
print("📝 14. TEST PREPARATION")
print("="*50)

for test, count in df['test preparation course'].value_counts().items():
    print(f" ➤ {test:<15} : {count} students")
print("-"*50 +"\n")


# =====================================================================
# 15. RACE / ETHNICITY GROUP 
# =====================================================================
print("="*50)
print("🔍 15. RACE / ETHNICITY GROUP")
print("="*50)

for group, count in df['race/ethnicity'].value_counts().items():
    print(f" ➤ {group:<15} : {count} students")
print("="*50 +"\n")


# =====================================================================
# 16. PARENT EDUCATION
# =====================================================================
print("="*50)
print("📚 16. Parent Education")
print("="*50)

for parents_edu, count in df["parental level of education"].value_counts().items():
    print(f" ➤ {parents_edu:<15} : {count} parents")
print("="*50 +"\n")