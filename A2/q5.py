import pandas as pd
import math


def calculate_distance(arr1, arr2):
    n = min(len(arr1), len(arr2))
    distance = 0
    for i in range(0, n):
        distance += (arr1[i] - arr2[i]) ** 2
    return math.sqrt(distance)


excel_data = pd.read_excel("Q5_data.xlsx")
data = excel_data.to_numpy()

k = int(input())

min_distances = []
for i in range(k):
    min_distances.append([0.0, 0.0, 0.0])

for i in range(0, k):
    age = data[i][0]
    loan = data[i][1]
    l = [age, loan]
    min_distances[i][0] = calculate_distance(l, [37, 142])
    min_distances[i][1] = data[i][2]
    min_distances[i][2] = data[i][3]

for i in data:
    age = i[0]
    loan = i[1]
    hpi = i[2]
    bhk = i[3]
    l1 = [age, loan]
    l2 = [37, 142]
    current_distance = calculate_distance(l1, l2)
    print(l1, current_distance)
    index = 0
    maxVal = 0
    for j in range(0, k):
        if min_distances[j][0] > maxVal:
            maxVal = min_distances[j][0]
            index = j

    if current_distance < maxVal:
        min_distances[index][0] = current_distance
        min_distances[index][1] = hpi
        min_distances[index][2] = bhk

print(min_distances)
