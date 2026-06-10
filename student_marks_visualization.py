import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": ["Aisha", "Rahul", "Priya", "Rohan", "Ananya"],
    "Marks": [85, 72, 91, 78, 88]
}

df = pd.DataFrame(data)

plt.bar(df["Student"], df["Marks"])

plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()