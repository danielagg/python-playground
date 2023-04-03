# import matplotlib.pyplot as plot
import pandas as pd
import numpy as np

data1 = {
    "X": [78, 85, 96, 80, 86],
    "Y": [84, 94, 89, 83, 86],
    "Z": [86, 97, 96, 72, 83],
}
data2 = pd.DataFrame(data1)


exam_data = {
    "name": [
        "Anastasia",
        "Dima",
        "Katherine",
        "James",
        "Emily",
        "Michael",
        "Matthew",
        "Laura",
        "Kevin",
        "Jonas",
    ],
    "score": [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    "attempts": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    "qualify": ["yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes"],
}

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
data3 = pd.DataFrame(exam_data, labels)

print(data3.loc[:, ["attempts", "name", "qualify", "score"]])

# select rows 0:2, as in 0th and 1st, and columns 0, 1, 2
print(data3.iloc[0:2, [0, 1, 2]])

print(data3.iloc[0:2])  # same as .head(2), rows 0, 1


print(data3.loc[:, ["attempts"]])  # all rows, 'attempts' column
print(data3["attempts"])  # all rows, 'attempts' column
print(data3[["name", "attempts"]])  # all rows, two columns --> now we do neet [[]]
