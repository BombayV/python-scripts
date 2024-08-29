import os

folder: str = "./photos"
files: list = os.listdir(folder)
arr: list = []

for file in files:
    arr.append(file)

with open("output.txt", "w") as f:
    f.write(str(arr))