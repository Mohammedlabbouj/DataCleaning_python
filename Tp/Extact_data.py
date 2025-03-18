# %%
import pandas as pd

# Load the Excel file
file_path = "D:\\master2\\powerBI\\MLAIM_PBI_2025\\Seance 3\\Exercice Transpose, Pivot, Unpivot\\Power-Query.xlsx"

# Read the specific sheets
query3 = pd.read_excel(file_path, sheet_name="Query3")
result3 = pd.read_excel(file_path, sheet_name="Result3")
query4 = pd.read_excel(file_path, sheet_name="Query4")
result4 = pd.read_excel(file_path, sheet_name="Result4")

result3.to_excel(
    "D:\\master2\\powerBI\\MLAIM_PBI_2025\\Seance 3\\Exercice Transpose, Pivot, Unpivot\\result3.xlsx"
)
# for i in range(len(query3)):
#     print(query3.iloc[i].values)
# print(result3.values)  # Show first few rows of Result3
# # Display Query3 and Result3
# print("=== QUERY 3 ===")
# print(query3.head())  # Show first few rows of Query3
# print("\n=== RESULT 3 ===")
# print(result3.head())  # Show first few rows of Result3a

# # Display Query4 and Result4
# print("\n=== QUERY 4 ===")
# print(query4.head())  # Show first few rows of Query4
# print("\n=== RESULT 4 ===")
# print(result4.head())  # Show first few rows of Result4
# %%
