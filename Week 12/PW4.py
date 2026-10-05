import numpy as np
import pandas as pd

# 2D NumPy Matrix (5x3) untuk 5 orang pelajar dan 3 eksperimen
scores = np.array([
    [78, 85, 90],
    [65, 70, 75],
    [88, 92, 85],
    [55, 60, 58],
    [92, 95, 98]
])

print("----- Original Scores Matrix (5x3) -----")
print(scores)

# Matrix Manipulation
# Scalar addition: Tambah 5 standardization points
standardized_scores = scores + 5
print("\n----- Standardized Scores (+5 Points) -----")
print(standardized_scores)

# Slicing: Ambil subset skor 3 pelajar teratas
top_3_students = standardized_scores[:3]
print("\n----- Top 3 Students (Slicing) -----")
print(top_3_students)

# NumPy Mathematical Functions
exp_mean = np.mean(standardized_scores, axis=0)
student_total = np.sum(standardized_scores, axis=1)
highest_score = np.max(standardized_scores)
lowest_score = np.min(standardized_scores)

print("\n----- Statistical Analysis -----")
print("Mean per Experiment (Exp 1, 2, 3):", exp_mean)
print("Total Score per Student (1 to 5):", student_total)
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)

# Comparative Analysis Report (Tabulated Format guna DataFrame)
report_df = pd.DataFrame(
    standardized_scores,
    columns=['Exp 1', 'Exp 2', 'Exp 3'],
    index=['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5']
)
report_df['Total_Score'] = student_total

print("\n----- Comparative Analysis Report -----")
print(report_df)
