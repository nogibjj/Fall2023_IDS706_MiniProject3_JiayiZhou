"""
Test Cases
"""
from main import describe_file
from main import plot_file


def test_read():
    """test function"""
    #read a csv file by url
    df1 = describe_file("egrid2016.csv")[0]
    assert df1["SEQPLT16"]["mean"] == 4855.0
    assert df1["SEQPLT16"]["count"] == 9709.0
    assert df1["CAPFAC"]["count"] == 8038.0
    plot_file("https://www.dropbox.com/s/x2awp0e9znsyub7/egrid2016.csv?dl=1")

if __name__ == "__main__":
    test_read()
