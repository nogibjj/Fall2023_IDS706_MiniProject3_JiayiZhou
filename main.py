"""Main function goes here"""
import polars as pl
import matplotlib.pyplot as plt


def describe_file(input1):
    """define a function read a file"""
    df1 = pl.read_csv(input1)
    summary_statistics = df1.describe()
    return summary_statistics


def plot_file(input1):
    """define a function plot relationship in a dataframe"""
    df1 = pl.read_csv(input1)
    plt.scatter(df1["year"], df1["gwar"])
    plt.title("Start year of season vs Goose Wins Above Replacement")
    plt.xlabel("Start year of season")
    plt.ylabel("Goose Wins Above Replacement")
    plt.show()
    # Save the plot as a figure
    plt.savefig("plant_capacity_factor.png")
