"""
Exercise 33 — CSV Files

Task:
    Read a CSV file and compute:
        - Number of rows
        - Average of a numeric column
"""

import csv

def read_ages(filename):
    ages = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ages.append(int(row["age"]))
    return ages

def main():
    ages = read_ages("data.csv")
    print("Rows:", len(ages))
    print("Average age:", sum(ages) / len(ages))

if __name__ == "__main__":
    main()
