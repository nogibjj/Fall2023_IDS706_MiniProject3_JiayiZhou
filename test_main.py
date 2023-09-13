"""
Test Cases
"""
from main import describe_file
from main import plot_file


def test_read():
    """test function"""
    # read a csv file by url
    df1 = describe_file(
        "https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv"
    )
    assert df1[["describe", "year"]][4, 1] == 1921.0
    assert df1[["describe", "ppf"]][0, 1] == 30962.0
    assert df1[["describe", "ppf"]][4, 1] == 88.0
    plot_file(
        "https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv"
    )


if __name__ == "__main__":
    test_read()
