import matplotlib.pyplot as plt
import pandas as pd

# 1. Excel File Load Karein
file_name = "Student_Placement_Dashboard_Practice.xlsx"

try:
  df = pd.read_excel(file_name)
  print("--- Dataset Overview ---")
  print(df.head())
  print("\n--- Dataset Summary ---")
  print(df.info())
  print("\n--- Summary Statistics ---")
  print(df.describe())

except FileNotFoundError:
  print(f"Error: {file_name} file nahi mili. Path check karein.")

# 2. Basic Analysis (Aap apne columns ke name ke hisab se modify kar sakte hain)
# Example: Placement status distribution
if "PlacementStatus" in df.columns:
  status_counts = df["PlacementStatus"].value_counts()
  print("\n--- Placement Counts ---")
  print(status_counts)

  # Chart Visualisation
  plt.figure(figsize=(6, 4))
  status_counts.plot(kind="bar", color=["skyblue", "orange"])
  plt.title("Student Placement Status")
  plt.xlabel("Status")
  plt.ylabel("Number of Students")
  plt.tight_layout()
  plt.savefig("placement_summary.png")
  print("\nChart 'placement_summary.png' ke naam se save ho gaya hai.")