import csv
import numpy as np
import matplotlib.pyplot as plt


def write_and_read_txt(filename, numbers):
    with open(filename, "w") as file:
        for number in numbers:
            file.write(str(number) + "\n")

    result = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                result.append(int(line))

    return result


def write_and_read_csv(filename, data):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    result = []
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            result.append([int(value) for value in row])

    return result


def read_array_from_file(filename):
    return np.loadtxt(filename)


def plot_data(numbers):
    plt.figure(figsize=(8, 5))
    plt.plot(numbers)
    plt.title("Line Plot")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()


def density_plot(data):
    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=10, edgecolor="black", density=True)
    plt.title("Density Plot")
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.grid(True)
    plt.show()