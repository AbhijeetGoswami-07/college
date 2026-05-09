import pandas as pd

# Read the text file into a DataFrame
file_name = input()
df = pd.read_csv(file_name, sep="\s+", names=["Name", "Age", "Grade"])

print("First five rows:")
print(df.head())

average_age = round(df["Age"].mean(), 2)
print(f"Average age: {average_age}")

filtered_students = df[df["Grade"] <= "B"]
print("Students with a grade up to B")
print(filtered_students)

