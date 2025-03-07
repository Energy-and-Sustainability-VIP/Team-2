import pandas as pd

df = pd.read_csv("AssignmentOne/Watts, 3-Ph total.csv")

max_row = df.loc[df["meter_reading"].idxmax()]
min_row = df.loc[df["meter_reading"].idxmax()]
average_value = df["meter_reading"].mean()

print("Max Meter Reading Row:\n", max_row, "\n")
print("Min Meter Reading Row:\n", min_row, "\n")
print(f"Average Meter Reading: {average_value:.2f}\n")

df["kilowatts"] = df["meter_reading"] / 1000
df["kWh"] = df["kilowatts"] * 0.25
df.to_csv("Isaac's Folder/AssignmentOne.csv", index = False)