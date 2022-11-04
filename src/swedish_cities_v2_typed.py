import csv
import sys
from typing import Iterable, Mapping, MutableMapping, Optional, Set


def load_data(filename: str) -> MutableMapping[str, int]:
    data = {}
    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            city, year = row
            data[city] = int(year)

    return data


def should_be_filtered(cond: str, year: int) -> bool:
    result = eval(cond, {"year": year})
    return result


def filter_data(all_cities: Mapping[str, int], conditions: Iterable[str]) -> Set[str]:
    """Filter data based on the year."""
    cities = None
    # FIXME:
    # cities: Set[str] = set()
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


def print_data(cities: Mapping[str, int]):
    for city, year in cities.items():
        print(city, "was established in", year)


def main(argv: Optional[Iterable[str]] = None):
    data = load_data("data.csv")

    # NOTE: New filter feature
    conditions = argv or sys.argv[1:]
    cities_filtered = filter_data(data, conditions)
    if len(cities_filtered):
        data = {city: data[city] for city in cities_filtered}

    print_data(data)


if __name__ == "__main__":
    main()
