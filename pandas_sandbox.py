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
data3 = data3.loc[:, ["attempts", "name", "qualify", "score"]]

print(data3)
