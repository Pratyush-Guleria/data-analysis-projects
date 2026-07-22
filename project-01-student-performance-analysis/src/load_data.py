import pandas as pd
import sys
try:
    # Load the dataset
    df = pd.read_csv('data/students.csv')
    print("✅ File loaded Successfully")

except FileNotFoundError as e:

    print("❌ Sorry File not found plz try again")
    print(f"🔍 System Error Details: {e}")
    sys.exit(1)     # (1) means error 

# Custom Functions
def heading():      # Created a function because we are gonna this block of code frequently
    print("="*50)

def end_heading():
    print("-"*50 +"\n")

# =====================================================================
# 1. VIEWING THE FIRST 5 ROWS
# =====================================================================
heading()
print("📌 FIRST 5 ROWS OF THE DATASET")
heading()

print(df.head())

end_heading()


# =====================================================================
# 2. DATASET DIMENSIONS (ROWS & COLUMNS)
# =====================================================================
heading()
print("📊 DATASET DIMENSIONS")
heading()

print(f"Total Number of Rows    : {len(df)}")
print(f"Total Number of Columns : {len(df.columns)}")

end_heading()


# =====================================================================
# 3. COLUMN NAMES LISTING
# =====================================================================
heading()
print("📋 ALL COLUMN NAMES")
heading()

# Loop through column names with a serial number starting from 1
for count, col in enumerate(df.columns, start=1):   
    print(f"  {count}. {col}")

end_heading()


# =====================================================================
# 4. DATA TYPES CHECKING
# =====================================================================
heading()
print("⚙️ DATA TYPE OF EVERY COLUMN")
heading()

print(df.dtypes)

end_heading()


# =====================================================================
# 5. MISSING VALUES ANALYSIS
# =====================================================================
heading()
print("🔍 MISSING VALUES IN EACH COLUMN")
heading()

# Unpack key-value pairs to print each column name and its total missing values
for col_name, missing_count in df.isnull().sum().items():     
    print(f"  ➤ {col_name:<25} : {missing_count} missing values")

end_heading()


# =====================================================================
# 6. TOTAL MISSING VALUES IN DATASET
# =====================================================================
heading()
print("🔍 TOTAL MISSING VALUES IN DATASET")
heading()

print(f"Total Missing Values : {df.isna().sum().sum()}")

end_heading()


# =====================================================================
# 7. DUPLICATE ROWS IN DATASET
# =====================================================================
heading()
print("🔍 DUPLICATE ROWS IN DATASET")
heading()

print(f"Number of Duplicate Rows : {df.duplicated().sum()}")

end_heading()


# =====================================================================
# 8. NUMERICAL COLUMNS 
# =====================================================================
heading()
print("🔍 NUMERICAL COLUMNS")
heading()

print(f"Numerical Columns : {df.select_dtypes(include='number').columns.tolist()}")

end_heading()


# =====================================================================
# 9. CATEGORICAL COLUMNS
# =====================================================================
heading()
print("🔍 CATEGORICAL COLUMNS")
heading()

print(f"Categorical Columns : {df.select_dtypes(include=['string', 'object']).columns.tolist()}")

end_heading()


# =====================================================================
# 10. SUMMARY STATISTICS OF NUMERICAL COLUMNS
# =====================================================================
heading()
print("📊 SUMMARY STATISTICS OF NUMERICAL COLUMNS")
heading()

print(f"Summary Statistics (NUMERICAL COLUMNS) : {df.select_dtypes(include=['number']).describe()}")    # Describle helps to find mean, max, min

end_heading()


# =====================================================================
# 11. MEMORY USAGE BY DATASET
# =====================================================================
heading()
print("💻 MEMORY USAGE BY DATASET")
end_heading()
                                                           # deep = True helps to find exact memory 
print(f"Memory Usage : {df.memory_usage(deep=True).sum()/1024:.2f} KB") # sum helps to add memory usage of all columns
                                                                        # :.2f means just show 2 number after decimal 
end_heading()

# =====================================================================
# 12. GENDER DISTRIBUTION
# =====================================================================
heading()
print("👦🏻👧🏻 GENDER DISTRIBUTION")
heading()

for gender, count in df['gender'].value_counts().items():
    print(f" ➤ {gender:<10} : {count}")

end_heading()


# =====================================================================
# 13. LUNCH DISTRIBUTION
# =====================================================================
heading()
print("🍱 LUNCH DISTRIBUTION")
heading()

for lunch, count in df['lunch'].value_counts().items():
    print(f" ➤ {lunch:<15} : {count} students")

end_heading()


# =====================================================================
# 14. TEST PREPARATION
# =====================================================================
heading()
print("📝 TEST PREPARATION")
heading()

for test, count in df['test preparation course'].value_counts().items():
    print(f" ➤ {test:<15} : {count} students")

end_heading()


# =====================================================================
# 15. RACE / ETHNICITY GROUP 
# =====================================================================
heading()
print("🔍 RACE / ETHNICITY GROUP")
heading()

for group, count in df['race/ethnicity'].value_counts().items():
    print(f" ➤ {group:<15} : {count} students")

end_heading()


# =====================================================================
# 16. PARENT EDUCATION
# =====================================================================
heading()
print("📚 Parent Education")
heading()

for parents_edu, count in df["parental level of education"].value_counts().items():
    print(f" ➤ {parents_edu:<15} : {count} parents")

end_heading()


# =====================================================================
# 17. AVERAGE MATH SCORE
# =====================================================================
heading()
print("🧮 AVERAGE MATH SCORE")
heading()

avg_math_score = df["math score"].mean()        # Created variable because mean can't be used in for loop, mean only give 1 value so for loop will throw an error 
print(f"Average Math Score : {avg_math_score:.2f} Marks")

end_heading()


# =====================================================================
# 18. AVERAGE READING SCORE
# =====================================================================
heading()
print("📖 AVERAGE READING SCORE")
heading()

avg_reading_score = df['reading score'].mean()
print(f"Average Reading Score : {avg_reading_score:.2f} Minutes")

end_heading()


# =====================================================================
# 19. AVERAGE WRITING SCORE
# ===================================================================== 
heading()
print("✍️ AVERAGE WRITING SCORE")
heading()

avg_writing_score = df["writing score"].mean()
print(f"Average Writing Score : {avg_writing_score:.2f} minutes")

end_heading()


# =====================================================================
# 20. HIGHEST MATH SCORE WITH STUDENTS NAME
# =====================================================================
heading()
print("📈 HIGHEST MATH SCORE WITH STUDENT NAME")
heading()

highest_math_score = df["math score"].max()
max_student_row = df[df["math score"] == highest_math_score]

print(f"Highest math score : {highest_math_score}")
print("Students Having Highest Math Score :")
print(max_student_row)


# =====================================================================
# 21. LOWEST MATH SCORE WITH STUDENTS NAME
# =====================================================================
heading()
print("📉 LOWEST MATH SCORE WITH STUDENTS NAME")
heading()

lowest_math_score = df["math score"].min()
low_student_row = df[df["math score"] == lowest_math_score]

print(f"Lowest math score : {lowest_math_score}")
print("Students Having Lowest Math Score :")
print(low_student_row)

end_heading()


# =====================================================================
# 22. TOP 10 STUDENTS BASED ON MATH SCORE
# =====================================================================
heading()
print("🔝 TOP 10 STUDENTS BASED ON MATH SCORE")
heading()

top_10_stu = df.nlargest(10, 'math score')
print(top_10_stu)

end_heading()


# =====================================================================
# 23. BOTTOM 10 STUDENTS BASED ON MATH SCORE
# =====================================================================
heading()
print("⬇️ BOTTOM 10 STUDENTS BASED ON MATH SCORE")
heading()

bottom_10_stu = df.nsmallest(10, "math score")
print(bottom_10_stu)

end_heading()


# =====================================================================
# 24. AVERAGE MATH SCORE OF MALE AND FEMALE
# =====================================================================
heading()
print("📊 AVERAGE MATH SCORE OF MALE AND FEMALE")
heading()

math_avg_by_gender = df.groupby("gender")["math score"].mean() # General syntax: df.groupby('category_column')['numeric_column'].aggregation_function()

for gender, avg_score in math_avg_by_gender.items():
    print(f" ➤ {gender:<15} : {avg_score:.2f} marks")

end_heading()