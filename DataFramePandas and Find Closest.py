import pandas as pd
import numpy as np
data1 = {
    "Name": ["Asadur", "Anirban", "Munshi"],
    "Roll": [131, 161, 165],
    "Marks": [50, 45, 55]
}
data2 = {
    "Name": ["Ankur", "Sayan", "Rohit"],
    "Roll": [68, 78, 65],
    "Attendance": [6, 10, 20]
}
student_df = pd.DataFrame(data1)
student_df2 = pd.DataFrame(data2)
merge = pd.merge(student_df, student_df2, on=["Name", "Roll"], how="outer")
print("Merged DataFrame:")
print(merge)

numbers = [10, 220, 600, 300, 400]
target = 26
arr = np.array(numbers)
closest = arr[np.abs(arr - target).argmin()]
print("\nClosest number is:", closest)
