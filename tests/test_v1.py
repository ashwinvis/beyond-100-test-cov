import pandas as pd

import swedish_cities_v1 as sc


def pandas_load(csv_file):
    df = pd.read_csv("data.csv", names=("city", "year")).set_index("city")
    return df.year.to_dict()


def test_load(test_data):
    data = sc.load_data(test_data)
    assert {"Gothenburg", "Malmö", "Skanör med Falsterbo"} == set(data.keys())
    assert data["Malmö"] == 1250


def test_print(test_data, capsys):
    """Tests the print_data function"""
    data = pandas_load(test_data)
    sc.print_data(data)
    out, err = capsys.readouterr()
    assert "was established in" in out


def test_main(capsys):
    sc.main()
    out, err = capsys.readouterr()
    assert "was established in" in out
