import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Results.csv")

plt.scatter(data.Diff, data.DocumentType)
# plt.xticks(rotation=45)
plt.show()

# we want to minimize this:
def loss_function(w, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].x
        y = points.iloc[i].y
        total_error += (y - (w * x + b)) ** 2
    total_error / float(len(points))


# L corresponds to alfa, the learning rate
def gradiant_descent(w_now, b_now, points, L):
    w_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].x
        y = points.iloc[i].y

        w_gradient += -(2 / n) * x * (y - (w_now * x + b_now))
        b_gradient += -(2 / n) * (y - (w_now * x + b_now))

    w = w_now - w_gradient * L
    b = b_now - b_gradient * L

    return w, b


w = 0
b = 0
L = 0.0001  # learning rate
epochs = 300  # number of iterations

for i in range(epochs):
    if i % 50 == 0:
        print(f"Epoch: {i}")

    w, b = gradiant_descent(w, b, data, L)

print(w, b)
plt.scatter(data.x, data.y, color="black")
plt.plot(list(range(30, 80)), [w * x + b for x in range(30, 80)], color="red")
plt.show()
