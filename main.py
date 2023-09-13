"""Main function goes here"""
import polars as pl
import matplotlib.pyplot as plt


def read_file(input1):
    """Read a file"""
    df1 = pl.read_csv(input1)
    return df1


def describe_file(input1):
    """Describe the data frame"""
    df1 = pl.read_csv(input1)
    summary_statistics = df1.describe()
    return summary_statistics


def plot_file(input1):
    """Plot relationship in a dataframe"""
    df1 = pl.read_csv(input1)
    plt.scatter(df1["year"], df1["gwar"])
    plt.title("Start year of season vs Goose Wins Above Replacement")
    plt.xlabel("Start year of season")
    plt.ylabel("Goose Wins Above Replacement")
    # Save the plot as a figure
    plt.savefig("plant_capacity_factor.png")


def main():
    """Main function to run the functions"""
    data1 = "https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv"
    # read dataset
    df1 = read_file(data1)
    print(df1)

    # compute summary statistics
    df2 = describe_file(data1)
    print(df2)

    # generate plot
    plot_file(data1)


if __name__ == "__main__":
    main()
