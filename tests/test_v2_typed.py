import pandas as pd
import pytest

import swedish_cities_v2_typed as sc


def pandas_load(csv_file):
    df = pd.read_csv(csv_file, names=("city", "year")).set_index("city")
    return df.year.to_dict()


def test_load(test_data):
    data = sc.load_data(test_data)
    assert {"Gothenburg", "Malmö", "Skanör med Falsterbo"} == set(data.keys())
    assert data["Malmö"] == 1250


def test_should_be_filtered():
    assert sc.should_be_filtered("year > 1500", 1501) is True
    assert sc.should_be_filtered("year > 1500", 1500) is False
    assert sc.should_be_filtered("year >= 1500", 1500) is True


def test_filter_data(test_data):
    data = pandas_load(test_data)
    cities = sc.filter_data(data, ["year < 1500"])
    assert all(data[city] < 1500 for city in cities)


def test_print(test_data, capsys):
    """Tests the print_data function"""
    data = pandas_load(test_data)
    sc.print_data(data)
    out, err = capsys.readouterr()
    assert "was established in" in out


@pytest.mark.parametrize("args", [("year >= 1500", "year < 1600"), ("year < 1300",)])
def test_main(capsys, args):
    sc.main(args)
    out, err = capsys.readouterr()
    assert "was established in" in out
