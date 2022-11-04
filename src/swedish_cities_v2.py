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


def should_be_filtered(cond, year):
    result = eval(cond, {"year": year})
    return result


def filter_data(all_cities, conditions):
    """Filter data based on the year."""
    cities = None
    for cond in conditions:
        cities_filtered = {
            city for city, year in all_cities.items() if should_be_filtered(cond, year)
        }
        if not cities:
            cities = cities_filtered
        else:
            # NOTE: set intersection == boolean "AND" operation
            cities = cities.intersection(cities_filtered)

    return cities


def print_data(cities):
    for city, year in cities.items():
        print(city, "was established in", year)


def main(argv=None):
    data = load_data("data.csv")

    # NOTE: New filter feature
    conditions = argv or sys.argv[1:]
    cities_filtered = filter_data(data, conditions)
    if len(cities_filtered):
        data = {city: data[city] for city in cities_filtered}

    print_data(data)


if __name__ == "__main__":
    main()
