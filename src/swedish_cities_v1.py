import csv
import sys


def load_data(filename):
    data = {}
    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            city, year = row
            data[city] = int(year)

    return data


def print_data(cities):
    for city, year in cities.items():
        print(city, "was established in", year)


def main():
    data = load_data("data.csv")
    print_data(data)


if __name__ == "__main__":
    main()
