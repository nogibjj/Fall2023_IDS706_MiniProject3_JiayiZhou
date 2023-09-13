"""
Test Cases
"""
import polars as pl
from main import read_file, describe_file, plot_file


def test_read():
    """test function for read"""
    df1 = read_file(
        "https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv"
    )
    assert isinstance(df1, pl.DataFrame), "Fail to read the csv file"


def test_describe():
    """test function for describe dataframe"""
    # read a csv file by url
    df1 = describe_file(
        "https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv"
    )
    assert df1[["describe", "year"]][4, 1] == 1921.0
    assert df1[["describe", "ppf"]][0, 1] == 30962.0
    assert df1[["describe", "ppf"]][4, 1] == 88.0


def test_plot():
    """test function for plot"""
    plot_file(
        "https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv"
    )
    assert True, "Plot generation successed"


def test_main():
    """test main function"""
    test_read()
    test_describe()
    test_plot()


if __name__ == "__main__":
    test_main()
