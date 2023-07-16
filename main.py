# Hello! This is my first Machine Learning project. It's a simple fan-made replica of the program that Love Solutions company from the series How I Met Your Mother uses. You can e-mail me at contact@alphard.tk if you want your name to be added to the list, with the age and interests. Hope you enjoy!
import pandas as pd
from math import sqrt
import csv
sex = input("Are you a [w]oman or [m]an?")
dir_men = "men.csv"
dir_women = "women.csv"
wdir = r""
if(sex.lower()=="w"):
    data = pd.read_csv(dir_men)
    wdir = dir_women
elif(sex.lower()=="m"):
    data = pd.read_csv(dir_women)
    wdir = dir_men
new_value = []
topfive = []
print("In the next steps, your age and interests will be asked. For age, you have to type your age. For the each interest you'll be asked, you must rate your level of interest from 1 to 100.")
k = 5
characteristics = len(data.columns) - 1
distances = {}
for i in data.columns[0 : characteristics]:
    new_value.append(float(input(f"Type your {i}.")))
for index, row in data.iterrows():
    distance = 0

    if(new_value[0] < 18 and row[0] > 17):
        continue
    if(new_value[0] > 17 and row[0] < 17):
        continue
# We are avoiding matching an adult with a minor
    for val in range(characteristics):
        distance += (row[data.columns[val]]-new_value[val])**2
    distance = sqrt(distance)
    distances[distance] = index
keys = list(distances.keys())
keys.sort()
print(keys)
topfive = [distances[keys[i]] for i in range(5)]
print(topfive)
results = []
for j in topfive:
    result = data.iloc[j]
    results.append(result["name"])
print(results)
with open(wdir, "w") as f:
    writer = csv.writer(f)
    writer.writerow(new_value)
